# File: S (Python 2.4)

import copy
from direct.gui.DirectGui import *
from direct.task.Task import Task
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from pirates.uberdog.DistributedInventoryBase import DistributedInventoryBase
from pirates.piratesgui import LootPopupPanel
from pirates.ship import ShipGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import GuiTray
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui import AnchorButton
from pirates.piratesgui import GuiButton
from pirates.piratesgui import StatusEffectsPanel
from pirates.piratesgui import PiratesGuiGlobals
from pirates.ship import ShipMeter
from pirates.piratesgui.ShipArmorGui import ShipArmorGui
from pirates.piratesgui.BoardingPermissionPanel import BoardingPermissionPanel
from pirates.battle import EnemyGlobals
from pirates.piratesgui.BorderFrame import BorderFrame
from pirates.audio import SoundGlobals
import random
from pirates.ship import HighSeasGlobals
from pirates.piratesgui import MessageGlobals

class ShipStatusDisplay(GuiTray.GuiTray):

    def __init__(self, parent, shipId, **kw):
        optiondefs = (('relief', None, None), ('pos', (-0.029999999999999999, 0, -0.55000000000000004), None), ('shipId', shipId, None), ('shipName', ('', 0), self.applyShipName), ('shipClass', '', self.applyShipClass), ('shipHp', (0, 0), self.applyShipHp), ('shipSp', (0, 0), self.applyShipSp), ('shipCargo', (0, 0), self.applyShipCargo), ('oldCargo', 0, None), ('shipCrew', (0, 0), self.applyShipCrew), ('oldCrew', 0, None), ('ownShip', 0, None))
        self.defineoptions(kw, optiondefs)
        GuiTray.GuiTray.__init__(self, parent, 0.5, 0.5)
        self.invReq = None
        self.timer = None
        self.anchorButton = None
        self.lootPanel = None
        self.prevChange = 0
        self.statusEffectsPanel = None
        self.skillEffects = { }
        self.durationTask = None
        self.armorGui = None
        self.permissionButton = None
        self.permissionLabel = None
        self.permissionPanel = None
        self.loadGUI()
        self.accept('setName-%s' % self['shipId'], self.setShipName)
        self.accept('setShipClass-%s' % self['shipId'], self.setShipClass)
        self.accept('setShipHp-%s' % self['shipId'], self.setShipHp)
        self.accept('setShipSp-%s' % self['shipId'], self.setShipSp)
        self.accept('setShipCargo-%s' % self['shipId'], self.setShipCargo)
        self.accept('setShipCrew-%s' % self['shipId'], self.setShipCrew)
        self.accept('setShipSpeed-%s' % self['shipId'], self.setShipSpeed)
        self.initialiseoptions(ShipStatusDisplay)


    def destroy(self):
        self.ignoreAll()
        taskMgr.remove('doThreatMessageQueue')
        if self.invReq:
            DistributedInventoryBase.cancelGetInventory(self.invReq)
            self.invReq = None

        if self.statusEffectsPanel:
            self.statusEffectsPanel.destroy()
            self.statusEffectsPanel = None

        if self.openPortLabel:
            self.openPortLabel.destroy()
            self.openPortLabel = None

        if self.anchorButton:
            self.anchorButton.destroy()
            self.anchorButton = None

        self.hpMeterDownIval.pause()
        self.hpMeterUpGreenIval.pause()
        self.hpMeterUpRedIval.pause()
        self.hpMeterUpYellowIval.pause()
        del self.hpMeterDownIval
        del self.hpMeterUpGreenIval
        del self.hpMeterUpRedIval
        del self.hpMeterUpYellowIval
        self.timer = None
        self.anchorButton = None
        GuiTray.GuiTray.destroy(self)
        self.destroyBoardingPermissionPanel()


    def loadGUI(self):
        shipcard = loader.loadModel('models/gui/ship_battle')
        self.nameBox = DirectFrame(parent = self, relief = None, pos = (0.058000000000000003, 0, -0.0064999999999999997), text = PLocalizer.ShipName, text_align = TextNode.ALeft, text_scale = 0.044999999999999998, text_pos = (0, -0.01), text_fg = PiratesGuiGlobals.TextFG1, text_wordwrap = 15, text_shadow = (0, 0, 0, 1), textMayChange = 1, text_font = PiratesGlobals.getInterfaceFont())
        tex = shipcard.find('**/ship_battle_speed_bar*')
        self.hpFrame = DirectFrame(parent = self, pos = (0.46500000000000002, 0, 0.14000000000000001), relief = None, image = tex, image_scale = (0.29999999999999999, 1, 0.59999999999999998))
        self.hpMeter = DirectWaitBar(parent = self.hpFrame, relief = DGG.RAISED, range = 100, value = 100, borderWidth = (0.002, 0.002), frameColor = (0, 0, 0, 1), barColor = (0.10000000000000001, 0.69999999999999996, 0.10000000000000001, 1), frameSize = (-0.27000000000000002, 0.13100000000000001, -0.01, 0.01), pos = (0.069000000000000006, 0, 0.0), text = PLocalizer.Hull, text_scale = PiratesGuiGlobals.TextScaleLarge * 0.75, text_align = TextNode.ALeft, text_pos = (0.16, -0.012), text_fg = PiratesGuiGlobals.TextFG1, text_shadow = (0, 0, 0, 1), text_font = PiratesGlobals.getInterfaceFont())
        self.hpMeterChange = DirectFrame(parent = self.hpFrame, relief = DGG.FLAT, borderWidth = (0.0040000000000000001, 0.0040000000000000001), frameColor = (1.0, 0.0, 0.0, 1.0), sortOrder = 0)
        self.hpMeterChange.setBin('gui-fixed', 0)
        self.hpMeterChange.hide()
        self.hpMeterDownIval = Sequence(Func(self.hpMeterChange.show), Wait(0.10000000000000001), LerpColorInterval(self.hpMeterChange, 0.5, color = VBase4(0.69999999999999996, 0.10000000000000001, 0.10000000000000001, 1.0), blendType = 'easeOut'), LerpColorInterval(self.hpMeterChange, 0.25, color = VBase4(0.0, 0.0, 0.0, 1.0), blendType = 'easeOut'), Func(self.hpMeterChange.hide))
        self.hpMeterUpGreenIval = Sequence(Func(self.hpMeterChange.show), Wait(0.10000000000000001), LerpColorInterval(self.hpMeterChange, 0.75, color = VBase4(0.10000000000000001, 0.69999999999999996, 0.10000000000000001, 1.0)), Func(self.hpMeterChange.hide))
        self.hpMeterUpRedIval = Sequence(Func(self.hpMeterChange.show), Wait(0.10000000000000001), LerpColorInterval(self.hpMeterChange, 0.75, color = VBase4(1.0, 0.0, 0.0, 1.0)), Func(self.hpMeterChange.hide))
        self.hpMeterUpYellowIval = Sequence(Func(self.hpMeterChange.show), Wait(0.10000000000000001), LerpColorInterval(self.hpMeterChange, 0.75, color = VBase4(1.0, 1.0, 0.10000000000000001, 1.0)), Func(self.hpMeterChange.hide))
        self.spFrame = DirectFrame(parent = self, pos = (0.45500000000000002, 0, 0.115), relief = None, image = tex, image_scale = (0.29999999999999999, 1, 0.52000000000000002))
        speedArrow = loader.loadModel('models/gui/toplevel_gui').find('**/generic_arrow')
        self.speedMeter = DirectWaitBar(parent = self.spFrame, relief = DGG.RAISED, range = 100, value = 100, borderWidth = (0.002, 0.002), frameColor = (0, 0, 0, 1), barColor = (0.69999999999999996, 0.69999999999999996, 0.10000000000000001, 1), frameSize = (-0.27000000000000002, 0.13200000000000001, -0.0080000000000000002, 0.0080000000000000002), pos = (0.069000000000000006, 0, 0.0), text = PLocalizer.Speed, text_scale = PiratesGuiGlobals.TextScaleLarge * 0.75, text_align = TextNode.ALeft, text_pos = (0.16, -0.0080000000000000002), text_fg = PiratesGuiGlobals.TextFG1, text_shadow = (0, 0, 0, 1), text_font = PiratesGlobals.getInterfaceFont(), geom = speedArrow, geom_pos = (-0.25, 0, -0.01), geom_hpr = (0, 0, 90), geom_scale = (0.40000000000000002, 0.40000000000000002, 0.25))
        self.knotSpeed = DirectFrame(parent = self.spFrame, relief = None, state = DGG.DISABLED, pos = (-0.095000000000000001, 0, -0.055), text = PLocalizer.Knots % 0, text_align = TextNode.ACenter, text_scale = 0.040000000000000001, text_pos = (0.10000000000000001, -0.01), text_fg = PiratesGuiGlobals.TextFG1, text_wordwrap = 15, text_shadow = (0, 0, 0, 1), textMayChange = 1, text_font = PiratesGlobals.getInterfaceFont())
        circlecard = loader.loadModel('models/textureCards/skillIcons')
        base1 = circlecard.find('**/base')
        base2 = circlecard.find('**/base_over')
        base3 = circlecard.find('**/base_down')
        self.cargoMeter = GuiButton.GuiButton(parent = self, frameSize = (-0.045312499999999999, 0.045312499999999999, -0.045312499999999999, 0.045312499999999999), pos = (0.33000000000000002, 0, 0.20999999999999999), helpText = PLocalizer.CargoIconHelp, helpPos = (0.053999999999999999, 0, -0.10000000000000001), helpOpaque = 1, command = self.toggleCargo, image = (base1, base3, base2), image_scale = 0.10000000000000001, scale = 0.90000000000000002, relief = None)
        tex = loader.loadModel('models/gui/toplevel_gui').find('**/icon_crate')
        self.cargoLabel = DirectLabel(parent = self.cargoMeter, relief = None, state = DGG.DISABLED, image = tex, image_scale = 0.050000000000000003, image_color = (1, 1, 1, 0.80000000000000004), text = '0/0', text_scale = 0.044999999999999998, text_align = TextNode.ACenter, text_pos = (0.0044999999999999997, -0.025000000000000001), text_fg = PiratesGuiGlobals.TextFG1, text_shadow = (0, 0, 0, 1), text_font = PiratesGlobals.getInterfaceFont())
        self.crewMeter = GuiButton.GuiButton(parent = self, relief = None, frameSize = (-0.045312499999999999, 0.045312499999999999, -0.045312499999999999, 0.045312499999999999), pos = (0.46000000000000002, 0, 0.20999999999999999), helpText = PLocalizer.CrewIconHelp, helpPos = (-0.050000000000000003, 0, -0.10000000000000001), helpOpaque = 1, image = base1, image_scale = 0.10000000000000001, scale = 0.90000000000000002)
        icons = loader.loadModel('models/textureCards/icons')
        tex = icons.find('**/icon_stickman')
        self.crewLabel = DirectLabel(parent = self.crewMeter, relief = None, state = DGG.DISABLED, image = tex, image_scale = 0.080000000000000002, image_color = (1, 1, 1, 0.80000000000000004), text = '0/0', text_scale = 0.044999999999999998, text_align = TextNode.ACenter, text_pos = (0.0044999999999999997, -0.025000000000000001), text_fg = PiratesGuiGlobals.TextFG1, text_shadow = (0, 0, 0, 1), text_font = PiratesGlobals.getInterfaceFont())
        self.crewLabel.setTransparency(1, 1)
        gui = loader.loadModel('models/gui/avatar_chooser_rope')
        self.openPortLabel = DirectLabel(parent = base.a2dTopRight, relief = None, image = gui.find('**/avatar_c_A_middle'), image_scale = 0.29999999999999999, pos = (-0.23000000000000001, 0, -0.5), state = DGG.DISABLED, text = '', text_scale = 0.040000000000000001, text_align = TextNode.ACenter, text_pos = (0.0, -0.01), text_fg = PiratesGuiGlobals.TextFG2, text_shadow = (0, 0, 0, 1), text_font = PiratesGlobals.getPirateBoldOutlineFont())
        self.openPortLabel.hide()
        self.setupPermissionUI()
        self.statusEffectsPanel = StatusEffectsPanel.StatusEffectsPanel(parent = self, pos = (0.29999999999999999, 0, 0.29999999999999999))
        self.statusEffectsPanel.iconScale = 0.65000000000000002
        self.armorGui = ShipArmorGui(self, pos = (0.14999999999999999, 0.14999999999999999, 0.14999999999999999))
        self.threatFrame = DirectFrame(parent = self, pos = (0.14999999999999999, 0, 0.155), relief = None, image = None, image_scale = 0.13500000000000001)
        self.accept('LocalAvatar_Ship_ThreatLevel_Update', self.setThreatLevel)
        self.accept('LocalAvatar_Ship_OpenPort_Update', self.setOpenPort)
        self.accept('settingLocalShip', self.handleLocalShipSet)
        self.accept('settingLocalShipId', self.handleLocalShipSet)
        self.handleLocalShipSet(quiet = 1)


    def handleLocalShipSet(self, quiet = 1):
        if localAvatar.ship:
            self.setThreatLevel(localAvatar.ship.getThreatLevel(), quiet)
            self.setOpenPort(localAvatar.ship.getOpenPort(), None, quiet)
        else:
            self.setThreatLevel(0, quiet)
            self.setOpenPort(None, None, quiet)


    def setOpenPort(self, portId, oldPortId, quiet = 0):
        openPortUID = EnemyGlobals.OPEN_PORT_DICT.get(portId, '')
        openPortName = PLocalizer.OpenPortNames.get(openPortUID)
        oldPortUID = EnemyGlobals.OPEN_PORT_DICT.get(oldPortId, '')
        oldPortName = PLocalizer.OpenPortNames.get(oldPortUID)
        if openPortName:
            self.openPortLabel.show()
            self.openPortLabel['text'] = PLocalizer.OpenPortMessage % openPortName
            if not quiet:
                if oldPortId:
                    oldPortMessage = HighSeasGlobals.getPortClosedMessage(oldPortUID)
                    openPortMessage = HighSeasGlobals.getPortOpenMessage(openPortUID)
                    messageText = oldPortMessage[0] + openPortMessage[0]
                    messageSoundList = [
                        oldPortMessage[1],
                        openPortMessage[1]]
                    base.localAvatar.guiMgr.queueInstructionMessage(messageText, messageSoundList, messageCategory = MessageGlobals.MSG_CAT_TELL_PORT)
                else:
                    allPortMessage = HighSeasGlobals.getInitPortMessage()
                    openPortMessage = HighSeasGlobals.getPortOpenMessage(openPortUID)
                    messageText = allPortMessage[0] + openPortMessage[0]
                    messageSoundList = [
                        allPortMessage[1],
                        openPortMessage[1]]
                    base.localAvatar.guiMgr.queueInstructionMessage(messageText, messageSoundList, messageCategory = MessageGlobals.MSG_CAT_TELL_PORT)

            self.disableAnchorButton()
        else:
            self.openPortLabel.hide()
            self.hideWrongPort()


    def hideWrongPort(self):
        base.localAvatar.guiMgr.unlockInstructionMessage(self)


    def tellWrongPort(self):
        taskMgr.remove('hideWrongPortText')
        openPortName = ''
        if localAvatar.ship:
            portIndex = localAvatar.ship.getOpenPort()
            openPortUID = EnemyGlobals.OPEN_PORT_DICT.get(portIndex, '')
            openPortName = PLocalizer.OpenPortNames.get(openPortUID, '')

        if openPortName:
            localPortUID = ''
            if localAvatar.getPort():
                localPortDO = base.cr.doId2do.get(localAvatar.getPort())
                if localPortDO:
                    localPortUID = localPortDO.uniqueId


            if localPortUID in EnemyGlobals.NON_WILD_ISLANDS:
                wrongIslandMessage = HighSeasGlobals.getWrongIslandMessage()
                messageText1 = wrongIslandMessage[0]
                messageSound1 = wrongIslandMessage[1]
            else:
                wildIslandMessage = HighSeasGlobals.getWildIslandMessage()
                messageText1 = wildIslandMessage[0]
                messageSound1 = wildIslandMessage[1]
            openPortMessage = HighSeasGlobals.getPortOpenMessage(openPortUID)
            messageText2 = openPortMessage[0]
            messageSound2 = openPortMessage[1]
            messageText = messageText1 + messageText2
            base.localAvatar.guiMgr.lockInstructionMessage(self, messageText, [
                messageSound1,
                messageSound2], messageCategory = MessageGlobals.MSG_CAT_NO_PORT)
        else:
            base.localAvatar.guiMgr.lockInstructionMessage(self, PLocalizer.WrongIslandNoPort, messageCategory = MessageGlobals.MSG_CAT_NO_PORT)


    def setThreatLevel(self, threatLevel, quiet = 0):
        if localAvatar.ship and localAvatar.ship.getSiegeTeam():
            quiet = 0
            threatLevel = 0

        threatCard = loader.loadModel('models/gui/ship_threat_icons')
        threatImage = None
        threatIconName = EnemyGlobals.THREAT_ICON_DICT.get(threatLevel)
        if threatIconName:
            threatImage = threatCard.find('**/%s*' % threatIconName)

        self.threatFrame['image'] = threatImage
        self.threatFrame['image_scale'] = 0.13500000000000001
        threatDescription = HighSeasGlobals.getThreatLevelDescription(threatLevel, 0)
        if threatDescription and not quiet:
            base.localAvatar.guiMgr.queueInstructionMessageFront(threatDescription[0], threatDescription[1], threatImage, 1.0, messageCategory = MessageGlobals.MSG_CAT_THREAT_LEVEL)



    def setupPermissionUI(self):
        if not self.permissionButton:
            if self['ownShip']:
                text = PLocalizer.PermIconHelpOwn
            else:
                text = PLocalizer.PermIconHelp
            circlecard = loader.loadModel('models/textureCards/skillIcons')
            base1 = circlecard.find('**/base')
            base2 = circlecard.find('**/base_over')
            base3 = circlecard.find('**/base_down')
            self.permissionButton = GuiButton.GuiButton(parent = self, relief = None, state = DGG.NORMAL, frameSize = (-0.045312499999999999, 0.045312499999999999, -0.045312499999999999, 0.045312499999999999), pos = (0.58999999999999997, 0, 0.20999999999999999), helpText = text, helpPos = (-0.17999999999999999, 0, -0.10000000000000001), helpOpaque = 1, image = (base1, base3, base2), image_scale = 0.10000000000000001, command = self.handlePermissionButton, scale = 0.90000000000000002)
            tex = loader.loadModel('models/gui/toplevel_gui').find('**/gui_boarding')
            self.permissionLabel = DirectLabel(parent = self.permissionButton, relief = None, state = DGG.DISABLED, image = tex, image_scale = 0.14999999999999999, image_color = (1, 1, 1, 0.80000000000000004))
            self.permissionLabel.setTransparency(1, 1)



    def handlePermissionButton(self):
        if self.permissionPanel:
            if self.permissionPanel.isHidden():
                self.showPermissionPanel()
            else:
                self.hidePermissionPanel()
        else:
            self.showPermissionPanel()


    def showPermissionButton(self):
        if self.permissionButton:
            self.permissionButton.show()



    def hidePermissionButton(self):
        if self.permissionButton:
            self.permissionButton.hide()



    def createBoardingPermissionPanel(self):
        if not self.permissionPanel:
            self.permissionPanel = BoardingPermissionPanel(self, ownShip = self['ownShip'], command = self.hidePermissionPanel)
            self.permissionPanel.hide()



    def destroyBoardingPermissionPanel(self):
        if self.permissionPanel:
            self.permissionPanel.destroy()
            self.permissionPanel = None



    def hidePermissionPanel(self):
        if self.permissionPanel:
            self.permissionPanel.hide()



    def showPermissionPanel(self):
        if not self.permissionPanel:
            self.createBoardingPermissionPanel()

        self.permissionPanel.show()


    def loadLootPanel(self):
        if self.lootPanel:
            return None

        self.lootPanel = LootPopupPanel.LootPopupPanel()
        self.lootPanel.reparentTo(self)
        self.lootPanel.setPos(0.050000000000000003, 0, 0)
        self.lootPanel.hide()


    def applyShipName(self):
        self.setShipName(*self['shipName'])


    def applyShipClass(self):
        self.setShipClass(self['shipClass'])


    def applyShipHp(self):
        self.setShipHp(*self['shipHp'])


    def applyShipSp(self):
        self.setShipSp(*self['shipSp'])


    def applyShipCargo(self):
        self.setShipCargo(*self['shipCargo'])


    def applyShipCrew(self):
        self.setShipCrew(*self['shipCrew'])


    def setShipName(self, name, team):
        if (name, team) != self['shipName']:
            self['shipName'] = (name, team)
            return None

        self.nameBox['text'] = name
        if team == PiratesGlobals.PLAYER_TEAM:
            self.nameBox['text_fg'] = PiratesGlobals.PLAYER_NAMETAG
        elif team == PiratesGlobals.NAVY_TEAM:
            self.nameBox['text_fg'] = PiratesGlobals.NAVY_NAMETAG
        elif team == PiratesGlobals.UNDEAD_TEAM:
            self.nameBox['text_fg'] = PiratesGlobals.UNDEAD_NAMETAG
        elif team == PiratesGlobals.FRENCH_UNDEAD_TEAM:
            self.nameBox['text_fg'] = PiratesGlobals.FRENCH_NAMETAG
        elif team == PiratesGlobals.SPANISH_UNDEAD_TEAM:
            self.nameBox['text_fg'] = PiratesGlobals.SPANISH_NAMETAG



    def setShipClass(self, shipClass):
        if shipClass != self['shipClass']:
            self['shipClass'] = shipClass
            return None



    def setShipHp(self, hp, maxHp):
        if (hp, maxHp) != self['shipHp']:
            self['shipHp'] = (hp, maxHp)
            return None

        if hp < 0:
            hp = 0
        elif hp > maxHp:
            hp = maxHp

        if not maxHp:
            return None

        hpFraction = float(hp) / float(maxHp)
        if hpFraction >= 0.5:
            barColor = (0.10000000000000001, 0.69999999999999996, 0.10000000000000001, 1)
        elif hpFraction >= 0.25:
            barColor = (1.0, 1.0, 0.10000000000000001, 1)
        else:
            barColor = (1.0, 0.0, 0.0, 1)
        self.hpMeter['barColor'] = barColor
        prevRange = self.hpMeter['range']
        prevValue = self.hpMeter['value']
        self.hpMeter['range'] = maxHp
        self.hpMeter['value'] = hp
        if self.hpMeterDownIval.isPlaying():
            currentTime = self.hpMeterDownIval.getT()
        elif self.hpMeterUpGreenIval.isPlaying():
            currentTime = self.hpMeterUpGreenIval.getT()
        elif self.hpMeterUpRedIval.isPlaying():
            currentTime = self.hpMeterUpRedIval.getT()
        elif self.hpMeterUpYellowIval.isPlaying():
            currentTime = self.hpMeterUpYellowIval.getT()
        else:
            currentTime = None
        if currentTime is not None:
            if currentTime < 0.5:
                prevValue = prevValue + self.prevChange


        if prevValue > hp:
            self.hpMeterChange.setColor(1.0, 0.0, 0.0, 1.0)
            self.prevChange = float(prevValue - hp)
            change = float(prevValue - hp)
            valueScale = float(hp) / float(maxHp)
            changeScale = float(change) / float(maxHp)
            frameRight = float(changeScale * 0.39900000000000002)
            frameLeft = float(valueScale * 0.39900000000000002)
            frameX = frameLeft - 0.001
            self.hpMeterChange.setPos(frameX - 0.19950000000000001, 0.0, 0.0)
            self.hpMeterChange['frameSize'] = (0.0, frameRight, -0.010999999999999999, 0.0080000000000000002)
            if currentTime is None:
                self.hpMeterDownIval.start()
                return None

            if currentTime >= 0.5:
                self.hpMeterDownIval.start()
            else:
                self.hpMeterDownIval.start(startT = currentTime)
        elif prevValue < hp:
            self.hpMeterChange.setColor(0.0, 0.0, 0.0, 1.0)
            change = float(hp - prevValue)
            valueScale = float(hp) / float(maxHp)
            changeScale = float(change) / float(maxHp)
            frameRight = float(changeScale * 0.39900000000000002)
            frameLeft = float(valueScale * 0.39900000000000002)
            if frameLeft < 0.025000000000000001:
                return None

            frameX = frameLeft - frameRight
            self.hpMeterChange.setPos(frameX - 0.19450000000000001, 0.0, 0.0)
            if frameLeft > 0.39900000000000002:
                diff = frameLeft - 0.39900000000000002
                frameRight = float(frameRight - diff)

            self.hpMeterChange['frameSize'] = (0.0, frameRight, -0.010999999999999999, 0.0080000000000000002)
            if hpFraction >= 0.5:
                self.hpMeterUpGreenIval.start()
            elif hpFraction >= 0.25:
                self.hpMeterUpYellowIval.start()
            else:
                self.hpMeterUpRedIval.start()



    def setShipSp(self, sp, maxSp):
        if (sp, maxSp) != self['shipSp']:
            self['shipSp'] = (sp, maxSp)
            return None

        self.speedMeter['range'] = maxSp
        self.speedMeter['value'] = sp


    def setShipCargo(self, cargo, maxCargo):
        if (cargo, maxCargo) != self['shipCargo']:
            self['shipCargo'] = (cargo, maxCargo)
            return None

        if self['oldCargo'] != cargo:
            self['oldCargo'] = cargo
            self.cargoLabel['text'] = '%s/%s' % (len(cargo), maxCargo)
            if len(cargo) >= maxCargo:
                self.cargoLabel['text_fg'] = (1, 0, 0, 1)
            elif len(cargo) >= int(maxCargo * 0.75):
                self.cargoLabel['text_fg'] = (1, 0.80000000000000004, 0, 1)
            else:
                self.cargoLabel['text_fg'] = (1, 1, 1, 1)
            scaleAnim = self.cargoMeter.scaleInterval(0.5, Point3(0.90000000000000002), startScale = Point3(1.5), blendType = 'easeIn')
            scaleAnim.start()
            if self.lootPanel and not self.lootPanel.isHidden():
                self.lootPanel.showLoot(cargo)




    def setShipCrew(self, crew, maxCrew):
        if (crew, maxCrew) != self['shipCrew']:
            self['shipCrew'] = (crew, maxCrew)
            return None

        if self['oldCrew'] != crew:
            self['oldCrew'] = crew
            if self['oldCrew'] == 0:
                return None

            self.crewLabel['text'] = '%s/%s' % (len(crew), maxCrew)
            if len(crew) >= maxCrew:
                self.crewLabel['text_fg'] = (1, 0, 0, 1)
            else:
                self.crewLabel['text_fg'] = (1, 1, 1, 1)
            scaleAnim = self.crewMeter.scaleInterval(0.5, VBase3(0.90000000000000002), startScale = VBase3(1.5), blendType = 'easeIn')
            scaleAnim.start()



    def setShipSpeed(self, speed, maxSpeed):
        self.knotSpeed['text'] = PLocalizer.Knots % abs(int(speed * 0.20999999999999999))
        minP = -0.25
        maxP = 0.125
        percent = min(1.0, max(0.0, float(speed) / float(maxSpeed)))
        newP = (maxP - minP) * percent + minP
        self.speedMeter['geom_pos'] = (newP, 0, -0.01)


    def toggleCargo(self):
        self.loadLootPanel()
        if self.lootPanel.isHidden():
            self.lootPanel.showLoot(self['oldCargo'])
        else:
            self.lootPanel.hide()


    def updateStatusEffects(self, effects):
        effectIdList = effects.keys()
        for effectKeyId in effectIdList:
            (effectId, attackerId, duration, timeLeft, ts, buffs) = effects[effectKeyId]
            if effectKeyId not in self.skillEffects.keys():
                self.statusEffectsPanel.addStatusEffect(effectId, duration, timeLeft, ts, attackerId)
                continue
            self.statusEffectsPanel.updateStatusEffect(effectId, duration, timeLeft, ts, attackerId)

        for effectKeyId in self.skillEffects.keys():
            if effectKeyId not in effectIdList:
                buff = self.skillEffects.get(effectKeyId)
                if buff:
                    effectId = buff[0]
                    attackerId = buff[1]
                    self.statusEffectsPanel.removeStatusEffect(effectId, attackerId)


        self.skillEffects = copy.copy(effects)
        if self.skillEffects:
            self.addDurationTask()
        else:
            self.removeDurationTask()


    def addDurationTask(self):
        if not self.durationTask:
            self.durationTask = taskMgr.add(self.updateDurationTask, self.taskName('updateStatusPanelTask'))



    def removeDurationTask(self):
        if self.durationTask:
            taskMgr.remove(self.taskName('updateStatusPanelTask'))
            self.durationTask = None



    def updateDurationTask(self, task):
        if len(self.skillEffects) > 0:
            if self.statusEffectsPanel:
                self.statusEffectsPanel.updateDurations()

            return Task.cont
        else:
            self.durationTask = None
            return Task.done


    def enableAnchorButton(self):
        if not self.anchorButton:
            self.anchorButton = AnchorButton.AnchorButton(parent = base.a2dBottomCenter, helpText = PLocalizer.AnchorButtonHelp, image_scale = 0.17999999999999999, pos = (0, 0, 0.34000000000000002), scale = 1.2, command = self.handleAnchorButton)

        self.anchorButton.show()


    def disableAnchorButton(self):
        if self.anchorButton:
            self.anchorButton.hide()



    def handleAnchorButton(self):
        self.disableAnchorButton()
        base.cr.doId2do[self['shipId']].requestDropAnchor()


    def setArmorStatus(self, location, status):
        self.armorGui.setArmorStatus(location, status)


    def setAllowFriends(self, allow):
        if self.permissionPanel:
            self.permissionPanel.setAllowFriends(allow)



    def setAllowCrew(self, allow):
        if self.permissionPanel:
            self.permissionPanel.setAllowCrew(allow)



    def setAllowGuild(self, allow):
        if self.permissionPanel:
            self.permissionPanel.setAllowGuild(allow)



    def setAllowPublic(self, allow):
        if self.permissionPanel:
            self.permissionPanel.setAllowPublic(allow)
