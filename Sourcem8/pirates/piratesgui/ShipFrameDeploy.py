# File: S (Python 2.4)

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui.ShipFrameSelect import ShipFrameSelect
from pirates.piratesgui.ShipSnapshot import ShipSnapshot
from pirates.ship import ShipGlobals
from pirates.piratesbase import Freebooter

class ShipFrameDeploy(ShipFrameSelect):

    def __init__(self, parent, **kw):
        optiondefs = (('avatarName', '', None),)
        self.defineoptions(kw, optiondefs)
        ShipFrameSelect.__init__(self, parent)
        self.initialiseoptions(ShipFrameDeploy)


    def enableStats(self, shipName = '', shipClass = 0, mastInfo = [], hp = 0, sp = 0, cargo = 0, crew = 0, time = 0):
        hullInfo = ShipGlobals.getShipConfig(shipClass)
        self.shipClass = shipClass
        self.snapShot = ShipSnapshot(self, None, self['siegeTeam'], shipName, shipClass, mastInfo, hp, hullInfo['hp'], sp, hullInfo['sp'], cargo, hullInfo['maxCargo'], crew, hullInfo['maxCrew'], time, pos = self['snapShotPos'])
        typeStr = self['avatarName']
        if self['shipType'] is ShipFrameSelect.STBand:
            self.button['text'] = PLocalizer.BoardShip
        elif self['shipType'] is ShipFrameSelect.STGuild:
            self.button['text'] = PLocalizer.BoardShip
        elif self['shipType'] is ShipFrameSelect.STFriend:
            self.button['text'] = PLocalizer.BoardShip
        elif self['shipType'] is ShipFrameSelect.STPublic:
            self.button['text'] = PLocalizer.BoardShip
        else:
            typeStr = ''
        stateStr = PLocalizer.ShipAtSea
        if hp <= 0:
            self.button['state'] = DGG.DISABLED
            stateStr = 'red%s' % (PLocalizer.ShipSunk,)
            self['shipColorScale'] = VBase4(0.80000000000000004, 0.29999999999999999, 0.29999999999999999, 1)
        elif crew >= hullInfo['maxCrew']:
            self.button['state'] = DGG.DISABLED
            stateStr = 'red%s' % (PLocalizer.ShipFull,)
            self['shipColorScale'] = VBase4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1)
        else:
            self.button['state'] = DGG.NORMAL
        if typeStr:
            self.typeLabel['text'] = 'smallCaps(%s)' % typeStr



    def enableStatsOV(self, shipOV):
        self.snapShot = ShipSnapshot(self, shipOV, self['siegeTeam'], pos = self['snapShotPos'])
        typeStr = ''
        if self['siegeTeam']:
            hp = shipOV.maxHp
            sp = shipOV.maxSp
        else:
            hp = shipOV.Hp
            sp = shipOV.Sp
        if hp <= 0:
            self.button['state'] = DGG.DISABLED
            self.button['text'] = PLocalizer.DeployShip
            stateStr = 'Ired%s' % PLocalizer.ShipSunk
            self['shipColorScale'] = VBase4(1, 0.40000000000000002, 0.40000000000000002, 1)
            self.button['image3_color'] = VBase4(*PiratesGuiGlobals.ButtonColor3[2])
            self.button['geom3_color'] = VBase4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002)
            self.button['text3_color'] = VBase4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002)
            self.button['helpText'] = PLocalizer.ShipSunk
        elif len(shipOV.crew) >= shipOV.maxCrew:
            self.button['state'] = DGG.DISABLED
            self.button['text'] = PLocalizer.BoardShip
            self.button['helpText'] = PLocalizer.ShipFull
            stateStr = 'red%s' % (PLocalizer.ShipFull,)
            self['shipColorScale'] = VBase4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1)
        elif localAvatar.getActiveShipId() and shipOV.doId != localAvatar.getActiveShipId():
            self.button['state'] = DGG.DISABLED
            self.button['text'] = PLocalizer.DeployShip
            self.button['helpText'] = PLocalizer.OtherShipOut
            stateStr = 'Ired%s' % PLocalizer.OtherShipOut
            self['shipColorScale'] = VBase4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1)
        elif shipOV.state in 'Off':
            self.button['state'] = DGG.NORMAL
            self.button['text'] = PLocalizer.DeployShip
            stateStr = PLocalizer.ShipInBottle
            self.button['helpText'] = PLocalizer.ShipInBottle
        else:
            self.button['state'] = DGG.NORMAL
            self.button['text'] = PLocalizer.BoardShip
            stateStr = PLocalizer.ShipAtSea
            self.button['helpText'] = PLocalizer.ShipAtSea
        if not Freebooter.getPaidStatus(base.localAvatar.getDoId()) and shipOV.shipClass != ShipGlobals.INTERCEPTORL1 and shipOV.shipClass != ShipGlobals.MERCHANTL1:
            self.button['command'] = base.localAvatar.guiMgr.showNonPayer
            self.button['extraArgs'] = [
                'Restricted_ShipFrame_Deploy',
                3]
            self.button['text'] = PLocalizer.Locked
            subgui = loader.loadModel('models/gui/toplevel_gui')
            if subgui:
                self.button['geom'] = subgui.find('**/pir_t_gui_gen_key_subscriber')
                self.button['geom_scale'] = 0.14999999999999999
                self.button['geom_color'] = Vec4(0.69999999999999996, 0.69999999999999996, 0.69999999999999996, 1.0)
                subgui.remove_node()


        if typeStr:
            self.typeLabel['text'] = 'smallCaps(%s)' % typeStr



    def addCrewMemberName(self, name):
        if name not in self.snapShot['crewNames']:
            self.snapShot['crewNames'] += [
                name]
