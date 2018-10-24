from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
from pirates.battle import CannonGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui.ReputationMeter import ReputationMeter
from pirates.battle import CannonGlobals
from pirates.battle import WeaponGlobals
import random
import math

class CannonGUI(DirectFrame):
    
    def __init__(self, cannon):
        gui = loader.loadModel('models/gui/toplevel_gui')
        shipGui = loader.loadModel('models/gui/ship_battle')
        card = loader.loadModel('models/textureCards/skillIcons')
        weaponIcons = loader.loadModel('models/gui/gui_icons_weapon')
        DirectFrame.__init__(self, parent = base.a2dBottomCenter, relief = None, pos = (0, 0, 0.34999999999999998), scale = 0.59999999999999998)
        self.initialiseoptions(CannonGUI)
        self.cannon = cannon
        self.reloadIval = None
        self.skillTray = localAvatar.guiMgr.combatTray.skillTray
        self.volleyLabel = DirectLabel(parent = self, relief = None, pos = (0, 0, 0.080000000000000002), text = '0', text_align = TextNode.ACenter, text_scale = 0.080000000000000002, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, sortOrder = 2)
        self.volleyLabel.setTransparency(1)
        self.reloadBar = DirectWaitBar(parent = self, relief = None, image = shipGui.find('**/ship_battle_speed_bar*'), image_pos = (0.25, 0, 0.02), image_scale = (0.37, 1.0, 1.0), borderWidth = (0, 0), range = 1, value = 1, frameColor = (0.050000000000000003, 0.34999999999999998, 0.050000000000000003, 1), barColor = (0.25, 0.10000000000000001, 1.0, 1), pos = (-0.25, 0, -0.10000000000000001), frameSize = (0, 0.5, 0, 0.040000000000000001), text = '', text_fg = (0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 1), text_pos = (0.070000000000000007, 0.01, 0.0), text_scale = 0.029999999999999999, sortOrder = 2)
        self.reloadBar.setTransparency(1)
        self.ammoImage = DirectFrame(parent = self, relief = None, image = card.find('**/base'), image_scale = 0.25, image_pos = (0.10000000000000001, 0, 0.050000000000000003), geom = card.find('**/pir_t_gui_amo_cannonBalls'), geom_scale = 0.25, geom_pos = (0.10000000000000001, 0, 0.050000000000000003), pos = (-0.10000000000000001, 0, 0.050000000000000003), frameSize = (0, 0.20000000000000001, 0, 0.20000000000000001), sortOrder = 1)
        self.ammoImage.setTransparency(1)
        self.exitCannon = DirectButton(parent = base.a2dBottomRight, relief = None, pos = (-0.39000000000000001, 0, 0.089999999999999997), scale = 0.5, text = PLocalizer.lExit, text_pos = (0, -0.14999999999999999), text_scale = 0.080000000000000002, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getPirateBoldOutlineFont(), image = weaponIcons.find('**/pir_t_ico_can_single'), image_pos = (0, 0, 0), image_scale = 0.17999999999999999, geom = (gui.find('**/pir_t_gui_but_circle_slash'), gui.find('**/pir_t_gui_but_circle_slash'), gui.find('**/pir_t_gui_but_circle_slash_over')), geom_pos = (0, 0, 0), geom_scale = 1, geom_hpr = (0, 0, 90), geom_color = (1.0, 0.5, 0.5, 1), sortOrder = 2, command = self.handleExitCannon)
        self.hideTonic()
        self.hideWeapon()
        gui.removeNode()
        card.removeNode()
        weaponIcons.removeNode()

    
    def setAmmoId(self, ammoSkillId):
        if self.skillTray.traySkillMap:
            if ammoSkillId in self.skillTray.traySkillMap:
                for i in xrange(len(self.skillTray.tray)):
                    if self.skillTray.traySkillMap[i] == ammoSkillId:
                        if self.skillTray.origMap[i][1]:
                            self.skillTray.tray[i + 1].toggleButton(True)
                        
                    self.skillTray.origMap[i][1]
                    if self.skillTray.origMap[i][1]:
                        self.skillTray.tray[i + 1].toggleButton(False)
                        continue
                
            
        

    
    def setVolley(self, volleyCount):
        self.volleyLabel['text'] = '%d' % (volleyCount,)

    
    def setAmmoLeft(self, count, maxCount):
        pass

    
    def hideCannonControls(self):
        self.skillTray.hide()
        self.volleyLabel.hide()
        self.reloadBar.hide()
        self.ammoImage.hide()

    
    def showCannonControls(self):
        self.skillTray.show()
        self.volleyLabel.show()
        self.reloadBar.show()
        self.ammoImage.show()

    
    def resetGui(self):
        pass

    
    def hideTonic(self):
        base.localAvatar.guiMgr.combatTray.tonicButton.hide()

    
    def hideWeapon(self):
        base.localAvatar.guiMgr.combatTray.find('**/InventoryUICombatTrayGrid*').hide()

    
    def handleExitCannon(self):
        self.cannon.requestExit()

    
    def updateReload(self, val, volley):
        self.reloadBar['value'] = val
        if val >= 1:
            self.reloadBar['text'] = ''
            self.reloadBar['barColor'] = (0.050000000000000003, 0.57999999999999996, 0.69999999999999996, 1)
            return None
        else:
            self.reloadBar['text'] = PLocalizer.Reloading
        if volley:
            self.reloadBar['barColor'] = (0.93000000000000005, 0.97999999999999998, 0.34999999999999998, 1)
        else:
            self.reloadBar['barColor'] = (0.90000000000000002, 0.0, 0.0, 1)

    
    def startReload(self, time, volley, elapsedTime = 0, doneCallback = None):
        self.stopReload()
        self.reloadIval = Sequence(LerpFunctionInterval(self._CannonGUI__updateReloadBar, time), Func(self._CannonGUI__reloadDone))
        if doneCallback:
            self.reloadIval.append(Func(doneCallback))
        
        self.reloadBar['text'] = PLocalizer.Reloading
        if volley:
            self.reloadBar['barColor'] = (0.93000000000000005, 0.97999999999999998, 0.34999999999999998, 1)
        else:
            self.reloadBar['barColor'] = (0.90000000000000002, 0.0, 0.0, 1)
        self.reloadIval.start(elapsedTime)

    
    def _CannonGUI__updateReloadBar(self, val):
        self.reloadBar['value'] = val

    
    def _CannonGUI__reloadDone(self):
        self.reloadBar['text'] = ''
        self.reloadBar['barColor'] = (0.25, 1.0, 0.10000000000000001, 1)

    
    def stopReload(self):
        if self.reloadIval:
            self.reloadIval.pause()
            self.reloadIval = None
        

    
    def destroy(self):
        self.stopReload()
        del self.cannon
        self.volleyLabel.destroy()
        del self.volleyLabel
        del self.ammoImage
        self.exitCannon.destroy()
        del self.exitCannon
        del self.reloadBar
        DirectFrame.destroy(self)


