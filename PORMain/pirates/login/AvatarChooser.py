from panda3d.core import DocumentSpec, HTTPClient, NodePath, Point3, Ramfile, TPHigh, TPLow, TextNode, Vec3, Vec4, invert
import math
import time
import os
import random
import sys
from direct.gui.DirectGui import *
from direct.task.Task import Task
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
from direct.fsm.StateData import StateData
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.gui import DirectGuiGlobals
from direct.interval.IntervalGlobal import *
from direct.showbase.PythonUtil import quickProfile
from otp.otpgui import OTPDialog
from otp.otpbase import OTPGlobals
from pirates.audio import SoundGlobals
from pirates.piratesgui.GameOptions import GameOptions
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui import PDialog
from pirates.piratesgui.BorderFrame import BorderFrame
from pirates.piratesgui.ShardPanel import ShardPanel
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import TimeOfDayManager
from pirates.piratesbase import TODGlobals
from pirates.pirate import Pirate
from pirates.seapatch.SeaPatch import SeaPatch
from pirates.seapatch.Reflection import Reflection
from pirates.makeapirate import NameGUI
from pirates.pirate import Human, DynamicHuman
from pirates.pirate import HumanDNA
from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx

APPROVED = 1
DENIED = 2

class AvatarChooser(DirectObject, StateData):
    notify = directNotify.newCategory('AvatarChooser')

    def __init__(self, parentFSM, doneEvent):
        StateData.__init__(self, doneEvent)
        self.choice = (0, 0)
        self.gameOptions = None
        self.av = None
        self.deleteConfirmDialog = None
        self.shareConfirmDialog = None
        self.notQueueCompleteDialog = None
        self.notifications = { }
        self.subFrames = { }
        self.subAvButtons = { }
        self.handleDialogOnScreen = 0
        self.subIds = base.cr.avList.keys()
        self.subIds.sort()
        self.currentSubIndex = 0
        self.currentSubId = 0
        self.httpClient = None
        self.loginTask = None
        self.loginStatusRequest = None
        self.queueTask = None
        self.queueRequest = None
        self.queueComplete = False
        self.lastMousePos = (0, 0)
        base.avc = self
        self.forceQueueStr = ''
        self.finalizeConfirmDialog = None
        self.deniedConfirmDialog = None
        base.loadingScreen.tick(tickNumber = 150)

    def enter(self):
        taskMgr.setupTaskChain('phasePost', threadPriority = TPHigh)
        if self.isLoaded == 0:
            self.load()

        base.disableMouse()
        self.quitButton.show()
        self.scene.reparentTo(render)
        camera.reparentTo(render)
        camera.setPosHpr(-29.0187, 37.0125, 24.75, 4.09, 1.0, 0.0)
        self.showSub(0)
        if self.ship:
            taskMgr.add(self.__shipRockTask, 'avatarChooserShipRockTask')

        base.transitions.fadeScreen(1)
        base.transitions.fadeIn(3)
        base.graphicsEngine.renderFrame()
        base.graphicsEngine.renderFrame()
        base.cr.loadingScreen.hide()
        globalClock.tick()
        base.graphicsEngine.renderFrame()
        base.playSfx(self.oceanSfx, looping = 1, volume = 0.60)
        base.musicMgr.request(SoundGlobals.MUSIC_AVATAR_CHOOSER, volume = 0.4, priority = -2)
        self.accept('mouse1', self._startMouseReadTask)
        self.accept('mouse1-up', self._stopMouseReadTask)
        self.accept('mouse3', self._startMouseReadTask)
        self.accept('mouse3-up', self._stopMouseReadTask)
        if not self.disableOptions:
            self.accept('f7', self.__handleOptions)

        self.__allPhasesComplete()
        self._startLoginStatusTask()
        base.options.savePossibleWorking(base.options)

    def exit(self):
        if self.isLoaded == 0:
            return None

        base.musicMgr.requestFadeOut(SoundGlobals.MUSIC_AVATAR_CHOOSER)
        self.oceanSfx.stop()
        if self.deleteConfirmDialog:
            self.deleteConfirmDialog.destroy()
            self.deleteConfirmDialog = None

        if self.shareConfirmDialog:
            self.shareConfirmDialog.destroy()
            self.shareConfirmDialog = None

        self.avatarListFrame.hide()
        self.highlightFrame.hide()
        self.quitFrame.hide()
        self.renameButton.hide()
        self.scene.detachNode()
        if self.ship:
            taskMgr.remove('avatarChooserShipRockTask')

        self.ignore('mouse1')
        self.ignore('mouse1-up')
        self.ignore('mouse3')
        self.ignore('mouse3-up')
        self.ignore('f7')
        self._stopMouseReadTask()
        self._stopQueueTask()
        base.options.saveWorking()
        self.ignoreAll()
        if hasattr(self, 'fadeInterval'):
            self.fadeInterval.pause()
            del self.fadeInterval

        if hasattr(self, 'fadeFrame'):
            self.fadeFrame.destroy()

        taskMgr.setupTaskChain('phasePost', threadPriority = TPLow)

    def load(self):
        if self.isLoaded == 1:
            return None

        self.disableOptions = base.config.GetBool('disable-pirates-options', False)
        base.musicMgr.load(SoundGlobals.MUSIC_AVATAR_CHOOSER)
        self.model = loader.loadModel('models/gui/avatar_chooser_rope')
        charGui = loader.loadModel('models/gui/char_gui')
        self.oceanSfx = loadSfx(SoundGlobals.SFX_FX_OCEAN_LOOP)
        self.exclam = charGui.find('**/chargui_exclamation_mark')
        self.scene = NodePath('AvatarChooserScene')
        self.todManager = TimeOfDayManager.TimeOfDayManager()
        self.todManager.request('EnvironmentTOD')
        
        if config.GetBool('want-spooky-avatarchooser', False):
            self.todManager.switchJollyMoon(True)
            self.todManager.setEnvironment(TODGlobals.ENV_CURSED_NIGHT, { })
        else:
            self.todManager.setEnvironment(TODGlobals.ENV_DEFAULT, {})

        self.todManager.doEndTimeOfDay()
        self.todManager.skyGroup.setSunTrueAngle(Vec3(260, 0, 15))
        self.todManager.skyGroup.setSunLock(1)
        self.todManager.skyGroup.dirLightSun.node().setColor(Vec4(0.9, 0.7, 0.8, 1))

        pier = loader.loadModel('models/islands/pier_port_royal_2deck')
        pier.setPosHpr(-222.23, 360.08, 15.06, 251.57, 0.0, 0.0)
        pier.flattenStrong()
        pier.reparentTo(self.scene)
        pier2 = loader.loadModel('models/islands/pier_port_royal_1deck')
        pier2.setPosHpr(-35.0, 83.27, 19.26, 274.09, 0.0, 0.0)
        pier2.setScale(0.4, 0.3, 0.4)
        pier2.flattenStrong()
        pier2.reparentTo(self.scene)
        self.water = SeaPatch(render, Reflection.getGlobalReflection(), todMgr = self.todManager)
        self.water.loadSeaPatchFile('out.spf')
        self.water.updateWater(2)
        self.water.ignore('grid-detail-changed')
        self.ship = None
        from pirates.ship import ShipGlobals
        
        if config.GetBool('want-spooky-avatarchooser', False):
            self.ship = base.shipFactory.getShip(ShipGlobals.P_SKEL_PHANTOM)
            self.ship.playStormEffect()
        else:
            self.ship = base.shipFactory.getShip(ShipGlobals.INTERCEPTORL1)

        self.ship.modelRoot.setPosHpr(140.86, 538.97, -3.62, -133.04, 0.0, 0.0)
        self.ship.modelRoot.reparentTo(self.scene)
        self.shipRoot = self.ship.modelRoot
        self.ship.playIdle()
        lodNode = self.ship.lod.node()
        self.ship.lod.node().forceSwitch(0)

        self.avatarListFrame = DirectFrame(parent = base.a2dTopLeft, relief = None)
        self.ropeFrame = DirectFrame(parent = self.avatarListFrame, relief = None, image = self.model.find('**/avatar_c_A_rope'), image_scale = 0.36, pos = (0, 0, -0.015))
        self.subFrame = BorderFrame(parent = self.avatarListFrame, frameSize = (-0.25, 0.25, -0.04, 0.09), borderScale = 0.2, pos = (0, 0, -0.16), modelName = 'general_frame_f')
        triangleGui = loader.loadModel('models/gui/triangle')
        self.subLabel = DirectLabel(parent = self.subFrame, relief = None, text = '', text_scale = 0.05, text_fg = (1, 0.9, 0.7, 0.9), text_pos = (0, 0.015), textMayChange = 1)
        if base.config.GetBool('allow-linked-accounts', 0):
            self.nextSubButton = DirectButton(parent = self.subFrame, relief = None, image = (triangleGui.find('**/triangle'), triangleGui.find('**/triangle_down'), triangleGui.find('**/triangle_over')), pos = (0.31, 0, 0.025), scale = 0.08, command = self.changeSub, extraArgs = [
                1])
            self.prevSubButton = DirectButton(parent = self.subFrame, relief = None, image = (triangleGui.find('**/triangle'), triangleGui.find('**/triangle_down'), triangleGui.find('**/triangle_over')), hpr = (0, 0, 180), pos = (-0.31, 0, 0.025), scale = 0.08, command = self.changeSub, extraArgs = [
                -1])

        self.__createAvatarButtons()
        self.ropeFrame.reparentTo(self.avatarListFrame)
        self.subFrame.reparentTo(self.avatarListFrame)
        self.versionLabel = DirectLabel(parent = base.a2dTopRight, relief = None, text_scale = 0.04, text_fg = (1, 1, 1, 0.5), text = '%s\n%s' % (base.cr.getServerVersion(), base.win.getPipe().getInterfaceName()), text_align = TextNode.ARight, pos = (-0.05, 0, -0.05))
        self.highlightFrame = DirectFrame(parent = base.a2dBottomCenter, relief = None, image = self.model.find('**/avatar_c_B_frame'), image_scale = 0.37, pos = (0, 0, 0.25), scale = 0.9)
        self.highlightFrame.hide()
        if base.config.GetBool('allow-linked-accounts', 0):
            self.shareButton = DirectButton(parent = self.highlightFrame, relief = None, text_scale = 0.045, text_fg = (1, 0.9, 0.7, 0.9), text_shadow = PiratesGuiGlobals.TextShadow, text = ('', '', PLocalizer.AvatarChooserShared, ''), image = (self.model.find('**/avatar_c_B_unlock'), self.model.find('**/avatar_c_B_unlock'), self.model.find('**/avatar_c_B_unlock_over')), image_scale = 0.37, text_pos = (0, -0.1), pos = (-0.51, 0, -0.08), scale = 1.3, command = self.__handleShare)

        self.playButton = DirectButton(parent = self.highlightFrame, relief = None, text_scale = 0.05, text_fg = (0.7, 0.7, 0.7, 0.7), text_shadow = PiratesGuiGlobals.TextShadow, text = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserLoading, image = (self.model.find('**/avatar_c_B_bottom'), self.model.find('**/avatar_c_B_bottom'), self.model.find('**/avatar_c_B_bottom_over')), image_scale = 0.37, text_pos = (0, -0.015), pos = (0, 0, -0.08), scale = 1.7, color = (0.7, 0.7, 0.7, 0.7), state = DGG.DISABLED, command = self.__handlePlay)
        if not self.queueComplete:
            self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserInQueue
        else:
            self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserPlay
            self.playButton.setColor(1, 1, 1, 1)
            self.playButton['text_fg'] = (1.0, 0.9, 0.7, 0.9)
        self.accept('enter', self.__handleEnter)
        self.accept('arrow_up', self.__handleArrowUp)
        self.accept('arrow_down', self.__handleArrowDown)
        self.deleteButton = DirectButton(parent = self.highlightFrame, relief = None, text_scale = 0.045, text_fg = (1, 0.9, 0.7, 0.9), text_shadow = PiratesGuiGlobals.TextShadow, text = ('', '', PLocalizer.AvatarChooserDelete, ''), image = (self.model.find('**/avatar_c_B_delete'), self.model.find('**/avatar_c_B_delete'), self.model.find('**/avatar_c_B_delete_over')), image_scale = 0.37, text_pos = (0, -0.1), pos = (0.51, 0, -0.08), scale = 1.3, command = self.__handleDelete)
        self.quitFrame = DirectFrame(parent = base.a2dBottomRight, relief = None, image = self.model.find('**/avatar_c_C_back'), image_scale = 0.37, pos = (-0.4, 0, 0.21), scale = 0.9)
        self.quitFrameForeground = DirectFrame(parent = self.quitFrame, relief = None, image = self.model.find('**/avatar_c_C_frame'), image_scale = 0.37, pos = (0, 0, 0))
        if self.disableOptions:
            optionsState = DGG.DISABLED
        else:
            optionsState = DGG.NORMAL

        self.optionsButton = DirectButton(parent = self.quitFrame, relief = None, text_scale = 0.05, text_fg = (1, 0.9, 0.7, 0.9), text_shadow = PiratesGuiGlobals.TextShadow, text = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserOptions, image = (self.model.find('**/avatar_c_C_box'), self.model.find('**/avatar_c_C_box'), self.model.find('**/avatar_c_C_box_over')), image_scale = 0.37, text_pos = (0, -0.015), pos = (0, 0, 0.075), command = self.__handleOptions, state = optionsState)
        if self.disableOptions:
            self.optionsButton.setColorScale(Vec4(0.7, 0.7, 0.7, 0.7))

        self.quitButton = DirectButton(parent = self.quitFrame, relief = None, text_scale = 0.05, text_fg = (1, 0.9, 0.7, 0.9), text_shadow = PiratesGuiGlobals.TextShadow, text = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserQuit, image = (self.model.find('**/avatar_c_C_box'), self.model.find('**/avatar_c_C_box'), self.model.find('**/avatar_c_C_box_over')), image_scale = 0.37, text_pos = (0, -0.015), pos = (0, 0, -0.075), command = self.__handleQuit)
        self.renameButton = DirectButton(parent = base.a2dTopRight, relief = None, text_scale = 0.05, text_fg = (1, 0.9, 0.7, 0.9), text_shadow = PiratesGuiGlobals.TextShadow, text = '\x01smallCaps\x01%s\x02' % 'rename', image = (self.model.find('**/avatar_c_C_box'), self.model.find('**/avatar_c_C_box'), self.model.find('**/avatar_c_C_box_over')), image_scale = 0.37, text_pos = (0, -0.015), pos = (-0.3, 0, -0.2), command = self.__handleRename)

        def shardSelected(shardId):
            base.cr.defaultShard = shardId

        self.shardPanel = ShardPanel(base.a2dBottomLeft, gear = NodePath('gear'), inverted = True, relief = None, scale = 0.85, hpr = Vec3(0, 0, 180), pos = Vec3(0.42, 0, 0.02), uppos = Vec3(0.42, 0, 0.02), downpos = Vec3(0.42, 0, 0.6), shardSelected = shardSelected, buttonFont = PiratesGlobals.getInterfaceFont())
        self.shardPanel.setScissor(self.highlightFrame, Point3(-20, 0, -0.18), Point3(20, 0, 1.0))
        self.shardPanelBottom = loader.loadModel('models/gui/general_frame_bottom')
        self.shardPanelBottom.setPos(0.42, 0, 0.095)
        self.shardPanelBottom.setScale(0.273)
        self.shardPanelBottom.reparentTo(base.a2dBottomLeft)
        self.logo = loader.loadModel('models/gui/potcLogo')
        self.logo.reparentTo(self.avatarListFrame)
        self.logo.setPos(0, 0, 0.1)
        self.logo.setScale(0.66)
        charGui.remove_node()

    def __createAvatarButtons(self):
        subCard = loader.loadModel('models/gui/toplevel_gui')
        for subFrame in self.subFrames.values():
            subFrame.destroy()

        for buttonList in self.subAvButtons.values():
            for button in buttonList:
                button.destroy()

        self.subFrames = { }
        self.subAvButtons = { }
        i = 0
        for (subId, avData) in base.cr.avList.items():
            subFrame = DirectFrame(parent = self.avatarListFrame, relief = None, pos = (0, 0, -0.3))
            self.subFrames[subId] = subFrame
            avatarButtons = []
            self.subAvButtons[subId] = avatarButtons
            spacing = -0.1
            for (av, slot) in zip(avData, range(len(avData))):
                x = 0.0
                imageColor = Vec4(1, 1, 1, 1)
                textScale = 0.045
                textFg = (1, 0.9, 0.7, 0.9)
                if slot == 0:
                    z = -0.08
                    textPos = (0, -0.02)
                    image = (self.model.find('**/avatar_c_A_top'), self.model.find('**/avatar_c_A_top'), self.model.find('**/avatar_c_A_top_over'), self.model.find('**/avatar_c_A_top'))
                elif slot == len(avData) - 1:
                    z = slot * spacing - 0.125
                    textPos = (0, 0.033)
                    image = (self.model.find('**/avatar_c_A_bottom'), self.model.find('**/avatar_c_A_bottom'), self.model.find('**/avatar_c_A_bottom_over'), self.model.find('**/avatar_c_A_bottom'))
                else:
                    z = slot * spacing - 0.08
                    textPos = (0, -0.015)
                    image = (self.model.find('**/avatar_c_A_middle'), self.model.find('**/avatar_c_A_middle'), self.model.find('**/avatar_c_A_middle_over'), self.model.find('**/avatar_c_A_middle'))
                if av == OTPGlobals.AvatarSlotAvailable:
                    text = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserCreate
                    command = self.__handleCreate
                    state = DGG.NORMAL
                elif av == OTPGlobals.AvatarPendingCreate:
                    text = PLocalizer.AvatarChooserUnderConstruction
                    command = None
                    state = DGG.DISABLED
                    imageColor = Vec4(0.7, 0.7, 0.7, 1)
                elif av == OTPGlobals.AvatarSlotUnavailable:
                    text = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserCreate
                    command = self.__handleCreate
                    state = DGG.NORMAL
                else:
                    avName = av.dna.getDNAName()
                    text = avName
                    command = self.__handleHighlight
                    state = DGG.NORMAL
                dib = DirectButton(relief = None, parent = subFrame, state = state, text_fg = textFg, text_scale = textScale, text_shadow = PiratesGuiGlobals.TextShadow, text = text, image = image, image_color = imageColor, image_scale = 0.37, text_pos = textPos, pos = (x, 0, z), command = command, extraArgs = [
                    subId,
                    slot])
                avatarButtons.append(dib)

            i += 1

        subCard.remove_node()
        self.isLoaded = 1
        if self.queueComplete == False:
            self.__deactivateCreateButtons()

    def unload(self):
        if self.isLoaded == 0:
            return None

        loader.unloadSfx(self.oceanSfx)
        del self.oceanSfx
        loader.unloadModel(self.model)
        self.model.remove_node()
        del self.model
        self.todManager.skyGroup.setSunLock(0)
        self.logo.remove_node()
        if self.av:
            self.av.delete()
            del self.av

        if self.ship:
            self.ship.destroy()
            self.ship = None
            taskMgr.remove('avatarChooserShipRockTask')
            self.shipRoot = None

        self.water.delete()
        del self.water
        self.scene.remove_node()
        del self.scene
        self.todManager.disable()
        self.todManager.delete()
        del self.todManager
        cleanupDialog('globalDialog')
        for subFrame in self.subFrames.values():
            subFrame.destroy()

        for buttonList in self.subAvButtons.values():
            for button in buttonList:
                button.destroy()

        del self.subFrames
        del self.subAvButtons
        self.avatarListFrame.destroy()
        self.highlightFrame.destroy()
        self.quitFrame.destroy()
        self.renameButton.destroy()

        if self.gameOptions is not None:
            base.options = self.gameOptions.options
            self.gameOptions.destroy()
            del self.gameOptions

        self.versionLabel.destroy()
        del self.versionLabel
        self.shardPanel.destroy()
        del self.shardPanel
        self.shardPanelBottom.remove_node()
        self.ignoreAll()
        self.isLoaded = 0
        if self.finalizeConfirmDialog:
            self.finalizeConfirmDialog.destroy()
            self.finalizeConfirmDialog = None

        if self.deniedConfirmDialog:
            self.deniedConfirmDialog.destroy()
            self.deniedConfirmDialog = None

    def getChoice(self):
        return self.choice

    def __showHighlightedAvatar(self):
        self.notify.debugCall()
        (subId, slot) = self.choice
        potAv = base.cr.avList[subId][slot]
        if self.av:
            self.av.cleanupHuman()
            self.av.delete()

        if self.deleteConfirmDialog:
            self.deleteConfirmDialog.destroy()
            self.deleteConfirmDialog = None

        if self.shareConfirmDialog:
            self.shareConfirmDialog.destroy()
            self.shareConfirmDialog = None

        self.av = DynamicHuman.DynamicHuman()
        self.av.setDNAString(potAv.dna.makeNetString())
        self.av.loadHuman(self.av.style.gender)
        self.av.setPosHpr(-29.69, 46.35, 22.05, 180.0, 0.0, 0.0)
        self.av.reparentTo(self.scene)
        self.av.loop('idle')
        self.av.useLOD(2000)
        self.highlightFrame.show()
        if base.config.GetBool('allow-linked-accounts', 0):
            if potAv.shared:
                self.shareButton['image'] = (self.model.find('**/avatar_c_B_unlock'), self.model.find('**/avatar_c_B_unlock'), self.model.find('**/avatar_c_B_unlock_over'))
                self.shareButton['text'] = ('', '', PLocalizer.AvatarChooserLocked, '')
            else:
                self.shareButton['image'] = (self.model.find('**/avatar_c_B_lock'), self.model.find('**/avatar_c_B_lock'), self.model.find('**/avatar_c_B_lock_over'))
                self.shareButton['text'] = ('', '', PLocalizer.AvatarChooserShared, '')

        if not (potAv.online):
            if potAv.creator or not base.config.GetBool('allow-linked-accounts', 0):
                self.deleteButton['state'] = DGG.NORMAL
                if base.config.GetBool('allow-linked-accounts', 0):
                    self.shareButton['state'] = DGG.NORMAL

            else:
                self.deleteButton['state'] = DGG.DISABLED
                if base.config.GetBool('allow-linked-accounts', 0):
                    self.shareButton['state'] = DGG.DISABLED

        if potAv.online:
            self.playButton['text'] = PLocalizer.AvatarChooserAlreadyOnline
            self.playButton['state'] = DGG.DISABLED
        elif potAv.shared and potAv.creator or not base.config.GetBool('allow-linked-accounts', 0):
            if not self.queueComplete:
                self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserInQueue
            else:
                self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserPlay
            self.playButton['state'] = DGG.NORMAL
        else:
            self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserLockedByOwner
            self.playButton['state'] = DGG.DISABLED
        self.renameButton.hide()
        if potAv.wishState == 'APPROVED':
            self.blockInput()
            self.finalizeConfirmDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserNameAccepted, style = OTPDialog.Acknowledge, command = self.__handleFinalize)
        elif potAv.wishState == 'DENIED' or potAv.wishState == 'OPEN':
            if self.notifications.get(slot, 0):
                self.blockInput()
                if not self.handleDialogOnScreen:
                    self.notify.info('deniedConfirmDialog on screen')
                    self.deniedConfirmDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserPleaseRename, style = OTPDialog.Acknowledge, command = self.__handleDenied)

                self.handleDialogOnScreen = 1

            self.renameButton.show()

        if not (potAv.lastLogout) or int(time.time() / 60) - potAv.lastLogout > 60:
            potAv.defaultShard = 0
            base.cr.avPlayedRecently = False
        else:
            base.cr.avPlayedRecently = True
        if base.cr.defaultShard == 0:
            self.shardPanel['preferredShard'] = potAv.defaultShard

    def __hideHighlightedAvatar(self):
        if self.av:
            self.av.delete()
            self.av = None

        self.highlightFrame.hide()
        self.renameButton.hide()

    def __handleRename(self):
        self.enterNameMode()

    def __handleHighlight(self, subId, slot):
        self.choice = (subId, slot)
        for button in self.subAvButtons[subId]:
            if button['text'] == PLocalizer.AvatarChooserSlotUnavailable:
                button['text_fg'] = (0.5, 0.5, 0.5, 1)
                continue
            button['text_fg'] = (1, 0.9, 0.7, 0.9)

        self.subAvButtons[subId][slot]['text_fg'] = (1, 1, 1, 1)
        self.__showHighlightedAvatar()

    def __rotateHighlightedAvatar(self, val):
        if self.av:
            self.av.setH(val)

    def __handleArrowUp(self):
        if self.gameOptions is not None and not self.gameOptions.isHidden():
            return None

        sub = self.choice[0]
        slot = self.choice[1]
        initialSlot = slot
        if not sub:
            return None

        numButtons = len(self.subAvButtons[sub])
        av = False
        for index in xrange(0, numButtons - 1):
            if base.cr.avList.get(sub)[index] not in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
                av = True
                break
                continue

        if not av:
            return None

        if slot == 0:
            slot = numButtons - 1
        else:
            slot = slot - 1
        while base.cr.avList.get(sub)[slot] in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
            if slot > 0:
                slot = slot - 1
                continue
            slot = numButtons - 1
        if self.subAvButtons[sub][slot]['state'] == DGG.NORMAL and initialSlot != slot:
            self.__handleHighlight(sub, slot)

    def __handleArrowDown(self):
        if self.gameOptions is not None and not self.gameOptions.isHidden():
            return None

        sub = self.choice[0]
        slot = self.choice[1]
        initialSlot = slot
        if not sub:
            return None

        numButtons = len(self.subAvButtons[sub])
        av = False
        for index in xrange(0, numButtons - 1):
            if base.cr.avList.get(sub)[index] not in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
                av = True
                break
                continue

        if not av:
            return None

        if slot == numButtons - 1:
            slot = 0
        else:
            slot = slot + 1
        while base.cr.avList.get(sub)[slot] in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
            if slot < numButtons - 1:
                slot = slot + 1
                continue
            slot = 0
        if self.subAvButtons[sub][slot]['state'] == DGG.NORMAL and initialSlot != slot:
            self.__handleHighlight(sub, slot)

    def __handleCreate(self, subId, slot):
        self.choice = (subId, slot)
        self.__avatarSlotResponse(*self.choice)
        self.blockInput()

    def __rejectAvatarSlot(self, reasonId, subId, slot):
        self.notify.warning('rejectAvatarSlot: %s' % reasonId)
        self.allowInput()

    def __avatarSlotResponse(self, subId, slot):
        self.doneStatus = {
            'mode': 'create' }
        base.transitions.fadeOut(finishIval = Func(messenger.send, self.doneEvent, [
            self.doneStatus]))
        base.loadingScreen.showTarget(jail = True)
        base.loadingScreen.show()

    def __handleShare(self):
        if self.shareConfirmDialog:
            self.shareConfirmDialog.destroy()

        (subId, slot) = self.choice
        potAv = base.cr.avList[subId][slot]
        name = potAv.dna.getDNAName()
        self.blockInput()
        if potAv.shared:
            self.shareConfirmDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserConfirmLock % name, style = OTPDialog.TwoChoice, command = self.__handleShareConfirmation)
        else:
            self.shareConfirmDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserConfirmShare % name, style = OTPDialog.TwoChoice, command = self.__handleShareConfirmation)

    def __shareAvatarResponse(self, avatarId, subId, shared):
        base.cr.cleanupWaitingForDatabase()
        self.ignore('rejectShareAvatar')
        self.ignore('shareAvatarResponse')
        (subId, slot) = self.choice
        potAv = base.cr.avList[subId][slot]
        potAv.shared = shared
        if potAv.shared:
            self.shareButton['image'] = (self.model.find('**/avatar_c_B_unlock'), self.model.find('**/avatar_c_B_unlock'), self.model.find('**/avatar_c_B_unlock_over'))
            self.shareButton['text'] = ('', '', PLocalizer.AvatarChooserLocked, '')
        else:
            self.shareButton['image'] = (self.model.find('**/avatar_c_B_lock'), self.model.find('**/avatar_c_B_lock'), self.model.find('**/avatar_c_B_lock_over'))
            self.shareButton['text'] = ('', '', PLocalizer.AvatarChooserShared, '')
        self.allowInput()

    def __rejectShareAvatar(self, reasonId):
        self.notify.warning('rejectShareAvatar: %s' % reasonId)
        base.cr.cleanupWaitingForDatabase()
        self.ignore('rejectShareAvatar')
        self.ignore('shareAvatarResponse')
        self.allowInput()

    def __handleEnter(self):
        if self.playButton['state'] == DGG.NORMAL:
            self.__handlePlay()

    def __handlePlay(self):
        if not self.queueComplete:
            if not self.notQueueCompleteDialog:
                self.notQueueCompleteDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserQueued, style = OTPDialog.Acknowledge, command = self.__handleNotQueueComplete)

            self.notQueueCompleteDialog.show()
            return None

        if (0, 0) == self.choice:
            self.__handleCreate(self.currentSubId, 0)
            return None

        (subId, slot) = self.choice
        potAv = base.cr.avList[subId][slot]
        base.emoteGender = base.cr.avList[subId][slot].dna.gender
        if potAv in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
            return None

        self.notify.info('AvatarChooser: wants to play slot: %s avId: %s subId: %s' % (slot, potAv.id, subId))
        self.accept('rejectPlayAvatar', self.__rejectPlayAvatar)
        self.accept('playAvatarResponse', self.__playAvatarResponse)
        winInfo = base.win.getProperties()
        x = winInfo.getXSize()
        y = winInfo.getYSize()
        ratio = float(x) / y
        self.fadeFrame = DirectFrame(parent = aspect2dp, frameSize = (-1.0 * ratio, 1.0 * ratio, -1.0, 1.0))
        self.fadeFrame.setTransparency(1)
        self.fadeInterval = Sequence(Func(self.blockInput), Func(self.fadeFrame.show), LerpColorScaleInterval(self.fadeFrame, 0.3, Vec4(0.0, 0.0, 0.0, 1.0), Vec4(0.0, 0.0, 0.0, 0.0), blendType = 'easeInOut'), Func(base.transitions.fadeOut, t = 0), Func(base.cr.loginFSM.request, 'waitForSetAvatarResponse', [potAv]))
        base.emoteGender = potAv.dna.gender
        self.fadeInterval.start()

    def __rejectPlayAvatar(self, reasonId, avatarId):
        self.notify.warning('rejectPlayAvatar: %s' % reasonId)
        self.ignore('rejectPlayAvatar')
        self.ignore('playAvatarResponse')
        base.cr.cleanupWaitingForDatabase()
        self.rejectPlayAvatarDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserRejectPlayAvatar, style = OTPDialog.Acknowledge, command = self.__handleRejectPlayAvatar)

    def __handleRejectPlayAvatar(self, value):
        base.cr.loginFSM.request('shutdown')

    def __playAvatarResponse(self, avatarId, subId):
        (subId, slot) = self.choice
        self.notify.info('AvatarChooser: acquired avatar slot: %s avId: %s subId: %s' % (slot, avatarId, subId))
        self.ignore('rejectPlayAvatar')
        self.ignore('playAvatarResponse')
        base.cr.cleanupWaitingForDatabase()
        self.doneStatus = {
            'mode': 'chose' }
        messenger.send(self.doneEvent, [
            self.doneStatus])

    def __activatePlayButton(self):
        if not self.queueComplete:
            self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserInQueue
            return None

        self.playButton['state'] = DGG.NORMAL
        self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserPlay
        self.playButton.setColor(1, 1, 1, 1)
        self.playButton['text_fg'] = (1.0, 0.9, 0.7, 0.9)

    def __activateCreateButtons(self):
        if not self.queueComplete:
            return None

        for (currSubId, currSubVal) in base.cr.avList.items():
            for currIdx in xrange(len(currSubVal)):
                if currSubVal[currIdx] == OTPGlobals.AvatarSlotAvailable:
                    button = self.subAvButtons[currSubId][currIdx]
                    button.setColorScale(1, 1, 1, 1)
                    button['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserCreate
                else:
                    button = self.subAvButtons[currSubId][currIdx]
                    button.setColorScale(1, 1, 1, 1)
                    button['text'] = '\x01smallCaps\x01%s\x02' % currSubVal[currIdx].name

    def __deactivatePlayButton(self):
        self.playButton['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserInQueue
        self.playButton.setColor(0.7, 0.7, 0.7, 0.7)
        self.playButton['text_fg'] = (0.7, 0.7, 0.7, 0.7)

    def __deactivateCreateButtons(self):
        for (currSubId, currSubVal) in base.cr.avList.items():
            for currIdx in xrange(len(currSubVal)):
                if currSubVal[currIdx] == OTPGlobals.AvatarSlotAvailable:
                    button = self.subAvButtons[currSubId][currIdx]
                    button.setColorScale(0.7, 0.7, 0.7, 0.7)
                    button['text'] = '\x01smallCaps\x01%s\x02' % PLocalizer.AvatarChooserInQueue
                    continue

    def __allPhasesComplete(self):
        self.__activatePlayButton()
        self.__activateCreateButtons()

    def _startLoginStatusTask(self):
        if __dev__ or launcher.getValue('IS_DEV'):
            disableQueueDefault = 1
        else:
            disableQueueDefault = 0
        if config.GetBool('disable-server-queueing', disableQueueDefault):
            self._setQueueComplete()
            return None

        self.httpClient = HTTPClient()
        import urllib2 as urllib2
        proxies = urllib2.getproxies()
        if proxies and proxies.get('http'):
            self.notify.info('queuing proxy found')
            self.httpClient.setProxySpec(proxies.get('http'))
        else:
            self.notify.info('queuing proxy is none')
        loginTokenKey = config.GetString('queueing-token-1', 'SESSION_TOKEN')
        self.notify.info('using queueing token 1 of %s' % loginTokenKey)
        self.loginToken = launcher.getValue(loginTokenKey, None)
        self.queueComplete = False
        self.queueStatus = launcher.getValue('LOGIN_ACTION', None)
        if self.queueStatus and self.queueStatus == 'PLAY':
            self._setQueueComplete()
            return None

        self.queueFreqSeconds = launcher.getValue('QUEUE_FREQ_SECONDS', None)
        self.queueUrl = launcher.getValue('QUEUE_URL', None)
        if self.loginToken is not None and self.queueStatus == 'QUEUE' and self.queueFreqSeconds is not None and self.queueUrl is not None:
            self.queueFreqSeconds = int(self.queueFreqSeconds)
            self._startQueueTask()
            return None

        self.loginStatusRequest = None
        self.loginStatusTask = taskMgr.add(self._checkLoginStatus, 'AvatarChooser-CheckLoginStatus')
        self.loginStatusTask.delayTime = 0.1

    def _checkLoginStatus(self, task):
        if not self.loginStatusRequest:
            loginStatusUrl = launcher.getValue('WEB_PAGE_LOGIN_RPC', 'Our domain') + '?'
            if self.loginToken:
                loginStatusUrl += 'login_token=%s' % (self.loginToken,)
            elif __dev__ or launcher.getValue('IS_DEV'):
                testLogin = config.GetString('queueing-login', 'xx')
                testPass = config.GetString('queueing-pass', 'xx')
                loginStatusUrl += 'username=%s&password=%s' % (testLogin, testPass)
                if config.GetBool('server-queueing-force', 0):
                    self.forceQueueStr = '&wannaqueue=1'

                loginStatusUrl += self.forceQueueStr

            loginStatusUrl += '&fromGame=1'
            self.notify.info('Checking login status at: %s' % (loginStatusUrl,))
            self.statusRF = Ramfile()
            self.loginStatusRequest = self.httpClient.makeChannel(False)
            self.loginStatusRequest.beginGetDocument(DocumentSpec(loginStatusUrl))
            self.loginStatusRequest.downloadToRam(self.statusRF)

        if self.loginStatusRequest.run():
            return task.again

        requestData = ''
        if self.loginStatusRequest.isValid():
            requestData = self.statusRF.getData()
            self.statusRF = None
        else:
            self.notify.info('LoginStatus check failed: %s' % (self.loginStatusRequest.getStatusString(),))
            self.loginStatusRequest = None
            return task.again
        results = { }
        for line in requestData.split('\n'):
            pair = line.split('=', 1)
            if len(pair) == 2:
                results[pair[0].strip()] = pair[1].strip()
                continue

        self.queueStatus = results.get('LOGIN_ACTION', None)
        if self.queueStatus == 'PLAY':
            self._setQueueComplete()
            return task.done

        if self.queueStatus != 'QUEUE':
            self.notify.warning('Received invalid LOGIN_ACTION: %s' % (self.queueStatus,))
            sys.exit(1)

        loginTokenKey = config.GetString('queueing-token-2', 'SESSION_TOKEN')
        self.notify.info('using queueing token 2 of %s' % loginTokenKey)
        self.loginToken = results.get(loginTokenKey, self.loginToken)
        self.queueFreqSeconds = int(results.get('QUEUE_FREQ_SECONDS', '10'))
        self.queueUrl = results.get('QUEUE_URL', None)
        if not (self.loginToken) or not (self.queueUrl):
            self.notify.warning('No login token or queueUrl, trying again:')
            self.loginStatusRequest = None
            return task.again

        if config.GetBool('server-queueing-force', 0):
            self.notify.info('forcing queue')
            self.forceQueueStr = '&wannaqueue=1'

            def clearForceQueue(task = None):
                if self.forceQueueStr:
                    self.notify.info('clearing force queue')
                    self.forceQueueStr = ''
                else:
                    self.notify.info('setting force queue')
                    self.forceQueueStr = '&wannaqueue=1'
                    self._setQueueNotComplete()

            self.accept('f1', clearForceQueue)
        else:
            self.forceQueueStr = ''
        self._startQueueTask()
        return task.done

    def _stopLoginStatusTask(self):
        self._stopQueueTask()
        self.httpClient = None
        self.loginStatusRequest = None
        if self.loginStatusTask:
            taskMgr.remove(self.loginStatusTask)
            self.loginStatusTask = None

    def _startQueueTask(self):
        self.notify.info('Checking queue status...')
        self.queueRequest = None
        self.queueTask = taskMgr.add(self._checkQueue, 'AvatarChooser-CheckQueue')

    def _checkQueue(self, task):
        if not self.queueRequest:
            self.notify.info('Checking queue status at: %s' % (self.queueUrl + self.forceQueueStr,))
            self.queueRequest = self.httpClient.makeChannel(False)
            self.queueRequest.beginGetDocument(DocumentSpec(self.queueUrl + self.forceQueueStr))
            self.statusRF = Ramfile()
            self.queueRequest.downloadToRam(self.statusRF)
            task.delayTime = 0.1

        if self.queueRequest.run():
            return task.again

        requestData = ''
        if self.queueRequest.isValid():
            self.notify.info('CheckQueue download complete')
            requestData = self.statusRF.getData()
            self.statusRF = None
        else:
            self.notify.info('CheckQueue check failed: %s' % (self.loginStatusRequest.getStatusString(),))
            self.queueRequest = None
            return task.again
        task.delayTime = self.queueFreqSeconds
        results = { }
        for line in requestData.split('\n'):
            pair = line.split('=', 1)
            if len(pair) == 2:
                results[pair[0].strip()] = pair[1].strip()
                continue

        userError = results.get('USER_ERROR', None)
        if userError:
            self.notify.warning('Received USER_ERROR: %s fetching queue status' % (userError,))
            sys.exit(1)

        self.queueStatus = results.get('QUEUE_ACTION', None)
        if self.queueStatus == 'PLAY':
            self._setQueueComplete()
            return task.done

        if self.queueStatus != 'QUEUE':
            self.notify.warning('Received invalid QUEUE_ACTION: %s' % (self.queueStatus,))
            sys.exit(1)

        self.notify.info('Queue not ready.  Next check in %s seconds...' % (self.queueFreqSeconds,))
        self.queueRequest = None
        return task.again

    def _setQueueComplete(self):
        self.notify.info('Queueing is complete!')
        self.queueTask = None
        self.queueComplete = True
        self.__activatePlayButton()
        self.__activateCreateButtons()

    def _setQueueNotComplete(self):
        self.notify.info('Queueing is not complete!')
        self.queueComplete = False
        self.__deactivatePlayButton()
        self.__deactivateCreateButtons()
        if not taskMgr.hasTaskNamed('AvatarChooser-CheckQueue'):
            self._startQueueTask()

    def _stopQueueTask(self):
        self.queueRequest = None
        if self.queueTask:
            taskMgr.remove(self.queueTask)
            self.queueTask = None

    def __handleDelete(self):
        if self.deleteConfirmDialog:
            self.deleteConfirmDialog.destroy()

        (subId, slot) = self.choice
        potAv = base.cr.avList[subId][slot]
        name = potAv.name
        self.blockInput()
        self.deleteConfirmDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserConfirmDelete % name, style = OTPDialog.YesNo, command = self.__handleDeleteConfirmation)

    def __handleDeleteConfirmation(self, value):
        self.deleteConfirmDialog.destroy()
        self.deleteConfirmDialog = None
        if value == DGG.DIALOG_OK:
            (subId, slot) = self.choice
            potAv = base.cr.avList[subId][slot]
            self.notify.info('AvatarChooser: request delete slot: %s avId: %s subId: %s' % (slot, potAv.id, subId))
            self.accept('avDeleted', self.__removeAvatarResponse)
            base.cr.csm.sendDeleteAvatar(potAv.id)
            self.blockInput()
        else:
            self.allowInput()

    def __handleShareConfirmation(self, value):
        self.shareConfirmDialog.destroy()
        self.shareConfirmDialog = None
        if value == DGG.DIALOG_OK:
            (subId, slot) = self.choice
            potAv = base.cr.avList[subId][slot]
            self.notify.info('AvatarChooser: request share slot: %s avId: %s subId: %s' % (slot, potAv.id, subId))
            self.accept('rejectShareAvatar', self.__rejectShareAvatar)
            self.accept('shareAvatarResponse', self.__shareAvatarResponse)
            if potAv.shared:
                wantShared = 0
            else:
                wantShared = 1
            base.cr.waitForDatabaseTimeout(requestName = 'WaitForShareAvatarResponse')
            self.blockInput()
        else:
            self.allowInput()

    def __removeAvatarResponse(self, avatarId, subId):
        self.ignore('avDeleted')
        base.cr.cleanupWaitingForDatabase()
        base.cr.loginFSM.request('waitForAvatarList')

    def updateAvatarList(self):
        self.__hideHighlightedAvatar()
        self.__createAvatarButtons()
        self.subIds = base.cr.avList.keys()
        self.subIds.sort()
        if self.currentSubId not in self.subIds:
            self.notify.warning('subId %s is no longer in family: %s' % (self.currentSubIndex, self.subIds))
            self.currentSubIndex = 0

        self.showSub(self.currentSubIndex)
        subAvs = base.cr.avList[self.currentSubId]
        if len(subAvs) > 0 and subAvs[0] not in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
            self.__handleHighlight(self.currentSubId, 0)

        if not self.handleDialogOnScreen:
            self.allowInput()

    def __handleOptions(self):
        width = 1.8
        height = 1.6
        x = -width / 2
        y = -height / 2
        self.currentSubId = self.subIds[self.currentSubIndex]
        self.gameOptions = GameOptions('Game Options', x, y, width, height, base.options, chooser = self)
        self.gameOptions.show()
        self.avatarListFrame.hide()

    def __handleQuit(self):
        from pirates.piratesgui.MainMenuConfirm import MainMenuConfirm
        self.areYouSureMenu = MainMenuConfirm("quit")

    def __handleLogoutWithoutConfirm(self):
        base.cr.loginFSM.request('login')

    def __shipRockTask(self, task):
        h = self.shipRoot.getH()
        p = 1.5 * math.sin(task.time * 0.9)
        r = 1.5 * math.cos(task.time * 1.1) + 1.5 * math.cos(task.time * 1.8)
        self.shipRoot.setHpr(h, p, r)
        return Task.cont

    def blockInput(self):
        color = Vec4(0.7, 0.7, 0.7, 0.7)
        for subButtons in self.subAvButtons.values():
            for button in subButtons:
                button['state'] = DGG.DISABLED
                button.setColorScale(color)

        self.renameButton['state'] = DGG.DISABLED
        self.renameButton.setColorScale(color)
        self.quitButton['state'] = DGG.DISABLED
        self.quitButton.setColorScale(color)
        self.playButton['state'] = DGG.DISABLED
        self.playButton.setColorScale(color)
        if base.config.GetBool('allow-linked-accounts', 0):
            self.shareButton['state'] = DGG.DISABLED
            self.shareButton.setColorScale(color)

        self.deleteButton['state'] = DGG.DISABLED
        self.deleteButton.setColorScale(color)
        self.optionsButton['state'] = DGG.DISABLED
        self.optionsButton.setColorScale(color)
        if base.config.GetBool('allow-linked-accounts', 0):
            self.nextSubButton['state'] = DGG.DISABLED
            self.nextSubButton.setColorScale(color)
            self.prevSubButton['state'] = DGG.DISABLED
            self.prevSubButton.setColorScale(color)

    def allowInput(self):
        for subButtons in self.subAvButtons.values():
            for button in subButtons:
                if button['text']:
                    button['state'] = DGG.NORMAL
                else:
                    button['state'] = DGG.DISABLED
                button.clearColorScale()

        self.renameButton['state'] = DGG.NORMAL
        self.renameButton.clearColorScale()
        self.quitButton['state'] = DGG.NORMAL
        self.quitButton.clearColorScale()

        self.playButton['state'] = DGG.NORMAL
        self.playButton.clearColorScale()
        if base.config.GetBool('allow-linked-accounts', 0):
            self.shareButton['state'] = DGG.NORMAL
            self.shareButton.clearColorScale()

        self.deleteButton['state'] = DGG.NORMAL
        self.deleteButton.clearColorScale()
        if not self.disableOptions:
            self.optionsButton['state'] = DGG.NORMAL
            self.optionsButton.clearColorScale()

        if base.config.GetBool('allow-linked-accounts', 0):
            self.nextSubButton['state'] = DGG.NORMAL
            self.nextSubButton.clearColorScale()
            self.prevSubButton['state'] = DGG.NORMAL
            self.prevSubButton.clearColorScale()

        if self.choice == (0, 0):
            potAv = None
        else:
            (subId, slot) = self.choice
            potAv = base.cr.avList[subId][slot]
        if potAv and potAv not in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
            if not (potAv.online):
                if potAv.creator or not base.config.GetBool('allow-linked-accounts', 0):
                    self.deleteButton['state'] = DGG.NORMAL
                    if base.config.GetBool('allow-linked-accounts', 0):
                        self.shareButton['state'] = DGG.NORMAL

                else:
                    self.deleteButton['state'] = DGG.DISABLED
                    if base.config.GetBool('allow-linked-accounts', 0):
                        self.shareButton['state'] = DGG.DISABLED

            if potAv.online:
                self.playButton['state'] = DGG.DISABLED
            elif potAv.shared and potAv.creator or not base.config.GetBool('allow-linked-accounts', 0):
                self.playButton['state'] = DGG.NORMAL
            else:
                self.playButton['state'] = DGG.DISABLED

        if self.queueComplete == False:
            self.__deactivatePlayButton()
            self.__deactivateCreateButtons()

    def __handleFinalize(self, value):
        (subId, slot) = self.choice
        self.notifications[slot].remove_node()
        del self.notifications[slot]
        self.finalizeConfirmDialog.destroy()
        self.finalizeConfirmDialog = None
        potAv = base.cr.avList[subId][slot]
        base.cr.csm.sendAcknowledgeName(potAv.id)
        potAv.name = potAv.wishName
        potAv.wishState = 'CLOSED'
        avButton = self.subAvButtons[subId][slot]
        avButton['text'] = potAv.name
        potAv.dna.setName(potAv.wishName)
        self.allowInput()

    def __handleNotQueueComplete(self, value):
        self.notQueueCompleteDialog.destroy()
        self.notQueueCompleteDialog = None
        self.allowInput()

    def __handleDenied(self, value):
        (subId, slot) = self.choice
        self.notifications[slot].remove_node()
        del self.notifications[slot]
        self.deniedConfirmDialog.destroy()
        self.deniedConfirmDialog = None
        self.handleDialogOnScreen = 0
        potAv = base.cr.avList[subId][slot]
        if potAv.wishState == 'DENIED':
            base.cr.csm.sendAcknowledgeName(potAv.id)
        self.allowInput()

    def enterNameMode(self):
        (subId, slot) = self.choice
        self.quitFrame.setColorScale(Vec4(1, 1, 1, 0))
        self.highlightFrame.setColorScale(Vec4(1, 1, 1, 0))
        self.avatarListFrame.setColorScale(Vec4(1, 1, 1, 0))
        base.camera.setX(-26)
        self.subFrame.hide()
        av = base.cr.avList[subId][slot]
        self.accept('q', self.exitNameMode)
        self.accept('NameGUIFinished', self.exitNameMode)
        self.renameButton.hide()
        self.nameGui = NameGUI.NameGUI(main = av, independent = True)
        self.nameGui.enter()

    def exitNameMode(self, value=0, name=None):
        def newList():
            base.cr.loginFSM.request('waitForAvatarList')
            if hasattr(self, 'sendingDialog'):
                self.sendingDialog.destroy()

        if name:
            base.cr.csm.sendNewName(value, name)
            self.sendingDialog = PDialog.PDialog(text = PLocalizer.AvatarChooserNewName)
            self.blockInput()
            self.acceptOnce('newNameResp', newList)

        else:
            newList()
            self.renameButton.show()
        self.nameGui.unload()
        del self.nameGui
        self.ignore('q')
        self.ignore('NameGUIFinished')
        self.quitFrame.setColorScale(Vec4(1, 1, 1, 1))
        self.highlightFrame.setColorScale(Vec4(1, 1, 1, 1))
        self.avatarListFrame.setColorScale(Vec4(1, 1, 1, 1))
        base.camera.setX(-29)
        self.subFrame.show()

    def placeNotification(self, slot, pos, style):
        notification = self.exclam.copyTo(self.avatarListFrame)
        self.notifications[slot] = notification
        notification.setPos(pos[0], pos[1], pos[2])
        notification.setScale(0.14)
        notification.setR(25)

    def changeSub(self, delta):
        self.showSub(self.currentSubIndex + delta)

    def showSub(self, index):
        if self.subIds[self.currentSubIndex]:
            numAvs = len(self.subAvButtons[self.subIds[self.currentSubIndex]])
            for slot in xrange(0, numAvs):
                if self.notifications.get(slot, 0):
                    self.notifications[slot].remove_node()
                    del self.notifications[slot]
                    continue

        self.currentSubIndex = index
        numSubs = len(self.subIds)
        if self.currentSubIndex <= 0:
            self.currentSubIndex = 0
            if base.config.GetBool('allow-linked-accounts', 0):
                self.prevSubButton.hide()

        elif base.config.GetBool('allow-linked-accounts', 0):
            self.prevSubButton.show()

        if self.currentSubIndex >= numSubs - 1:
            self.currentSubIndex = numSubs - 1
            if base.config.GetBool('allow-linked-accounts', 0):
                self.nextSubButton.hide()

        elif base.config.GetBool('allow-linked-accounts', 0):
            self.nextSubButton.show()

        self.currentSubId = self.subIds[self.currentSubIndex]
        subName = base.cr.csm.username
        subLabelText = '\x01white\x01%s\x02' % subName
        self.subLabel['text'] = subLabelText
        for frame in self.subFrames.values():
            frame.hide()

        self.subFrames[self.currentSubId].show()
        anyAvatars = False
        for avList in base.cr.avList.values():
            for av in avList:
                if av not in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
                    anyAvatars = True
                    break
                    continue

            if anyAvatars:
                break
                continue

        avList = base.cr.avList[self.currentSubId]
        for avIdx in xrange(0, len(avList)):
            if avList[avIdx] not in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
                if avList[avIdx].wishState == 'APPROVED':
                    self.placeNotification(avIdx, (0.32, 0, -0.37 - avIdx * 0.095), APPROVED)
                elif avList[avIdx].wishState in ('DENIED', 'OPEN'):
                    self.placeNotification(avIdx, (0.32, 0, -0.37 - avIdx * 0.095), DENIED)

        if anyAvatars:
            self.avatarListFrame.reparentTo(base.a2dTopLeft)
            self.avatarListFrame.setPosHprScale(0.42, 0, -0.3, 0, 0, 0, 1, 1, 1)
        else:
            self.avatarListFrame.reparentTo(base.a2dTopCenter)
            self.avatarListFrame.setPosHprScale(0, 0, -0.3, 0, 0, 0, 1.1, 1.1, 1.1)
            self.renameButton.hide()
            self.shardPanel.hide()
            self.shardPanelBottom.hide()
        subAvs = base.cr.avList[self.currentSubId]
        if len(subAvs) > 0 and subAvs[0] not in (OTPGlobals.AvatarSlotUnavailable, OTPGlobals.AvatarSlotAvailable, OTPGlobals.AvatarPendingCreate):
            self.__handleHighlight(self.currentSubId, 0)
        else:
            self.__hideHighlightedAvatar()

    def _stopMouseReadTask(self):
        taskMgr.remove('AvatarChooser-MouseRead')

    def _startMouseReadTask(self):
        self._stopMouseReadTask()
        mouseData = base.win.getPointer(0)
        self.lastMousePos = (mouseData.getX(), mouseData.getY())
        taskMgr.add(self._mouseReadTask, 'AvatarChooser-MouseRead')

    def _mouseReadTask(self, task):
        if not base.mouseWatcherNode.hasMouse():
            pass
        winSize = (base.win.getXSize(), base.win.getYSize())
        mouseData = base.win.getPointer(0)
        if mouseData.getX() > winSize[0] or mouseData.getY() > winSize[1]:
            pass
        dx = mouseData.getX() - self.lastMousePos[0]
        mouseData = base.win.getPointer(0)
        self.lastMousePos = (mouseData.getX(), mouseData.getY())
        if self.av:
            value = self.av.getH()
            value = (value + dx * 0.7) % 360
            self.__rotateHighlightedAvatar(value)

        return Task.cont
