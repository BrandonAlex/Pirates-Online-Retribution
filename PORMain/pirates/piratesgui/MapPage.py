from panda3d.core import NodePath, Plane, Point3, TextNode, Vec3
# File: M (Python 2.4)

from direct.gui.DirectGui import *
from pirates.piratesbase import PLocalizer, PiratesGlobals
from pirates.piratesgui import InventoryPage, BorderFrame, ShardPanel, PiratesGuiGlobals, GuiButton
from pirates.map.WorldMap import WorldMap

class MapPage(InventoryPage.InventoryPage):

    def __init__(self):
        InventoryPage.InventoryPage.__init__(self)
        self.initialiseoptions(MapPage)
        self.shardPanel = None
        self.worldMap = None
        self.gear = None
        self.portOfCall = ''
        self.portOfCallLabel = None
        self.portOfCallButton = None
        self.minimapButton = None
        self.createPortOfCall()
        self.createWorldMap()
        self.createFrontOrnament()
        self.createShardPanel()
        self.createButtons()
        self.hide()


    def destroy(self):
        InventoryPage.InventoryPage.destroy(self)
        self.shardPanel = None
        self.gear = None
        self.worldMap = None
        self.portOfCallLabel = None
        self.portOfCallButton = None
        self.minimapButton = None


    def show(self, *args, **kwargs):
        super(self.__class__, self).show(*args, **kwargs)
        self.worldMap.enable()
        self.worldMap.show()


    def slideOpenCallback(self):
        self.worldMap.resetArcBall()
        self.worldMap.rotateAvatarToCenter()


    def hide(self, *args, **kwargs):
        super(self.__class__, self).hide(*args, **kwargs)
        self.worldMap.disable()
        self.worldMap.hide()


    def slideCloseCallback(self):
        self.shardPanel.hideIfShown()


    def createPortOfCall(self):
        if self.portOfCallLabel:
            self.portOfCallLabel.destroy()

        if self.portOfCallButton:
            self.portOfCallButton.destroy()

        compassGui = loader.loadModel('models/gui/compass_gui')
        topGui = loader.loadModel('models/gui/toplevel_gui')
        teleportIcon = topGui.find('**/treasure_w_b_slot_empty').copyTo(NodePath(''))
        compassGui.find('**/compass_icon_objective_green').copyTo(teleportIcon)
        teleportIcon.flattenStrong()
        self.portOfCallLabel = DirectLabel(parent = self, text = '', text_align = TextNode.ALeft, text_font = PiratesGlobals.getPirateOutlineFont(), text_scale = 0.0448, text_fg = PiratesGuiGlobals.TextFG2, textMayChange = 1, pos = (0.489, 0, 0.0725))
        self.portOfCallButton = GuiButton.GuiButton(parent = self, pos = (0.38, 0, 0.085), scale = 0.848, text = PLocalizer.Return, text_pos = (0.033, -0.014), text_scale = 0.0448, textMayChange = 1, image3_color = (0.800000, 0.800000, 0.800000, 1), geom = teleportIcon, geom_pos = (-0.065, 0, 0), geom_scale = 0.200, command = self.handlePortOfCall)


    def createFrontOrnament(self):
        geom = loader.loadModel('models/gui/gui_map_window')
        geom.reparentTo(self)
        geom.setPos(0.540000, 0, 0.72498)
        geom.setScale(0.320)
        geom.flattenStrong()


    def createButtons(self):
        if not base.config.GetBool('want-momentary-minimap', 0):
            guiMain = loader.loadModel('models/gui/gui_main')
            btImages = (guiMain.find('**/minimap_button'), guiMain.find('**/minimap_button'), guiMain.find('**/minimap_button_over'), guiMain.find('**/minimap_button'))
            self.minimapButton = GuiButton.GuiButton(parent = self, image = btImages, selectedImage = btImages, pos = (0.9, 0, 1.15), scale = 1.5, hotkeys = [
                'f8'], hotkeyLabel = 'F8', command = self.handleMinimapButton)
            self.minimapButton.hotkeyLabel.setPos(-0.050000, 0.0, -0.050000)
            self.minimapButton.hotkeyLabel.setScale(0.75)
        else:
            self.minimapButton = None


    def createWorldMap(self):
        self.worldMap = WorldMap(parent = self, state = DGG.NORMAL, pos = (0.550000, 0, 0.62), scale = 0.46)
        if __dev__ and 0:

            def changeMouseMode():
                self.worldMap.mapBall.rMode += 1
                self.worldMap.mapBall.rMode %= 2
                self.mouseModeLabel['text'] = `self.worldMap.mapBall.rMode`

            self.mouseModeButton = DirectButton(parent = self, text = 'MouseMode', scale = 0.065, pos = (0.25, 0, 0.089), command = changeMouseMode)
            self.mouseModeLabel = DirectLabel(parent = self, scale = 0.074, pos = (0.5, 0, 0.0864), text = `self.worldMap.mapBall.rMode`, text_fg = (1, 1, 1, 1), textMayChange = 1)



    def createShardPanel(self):
        if self.shardPanel:
            self.shardPanel.destroy()
            self.clearClipPlane()

        if self.gear:
            self.gear.detachNode()

        gui = loader.loadModel('models/gui/gui_map_window_drawer')
        gui.reparentTo(self)
        gui.setPos(0.550000, 0, 0.72498)
        gui.setScale(0.320)
        self.gear = gui.find('**/gear')
        self.gear.wrtReparentTo(self)
        gui.detachNode()
        self.shardPanel = ShardPanel.ShardPanel(parent = self, relief = None, gear = self.gear)
        self.setScissor(Point3(-2, 0, -2), Point3(2.0, 0, 1.35))
        if __dev__ and 0:

            def showShardList():
                self.shardPanel.show()
                self.shardButton['text'] = 'Hide Shards'
                self.shardButton['command'] = hideShardList


            def hideShardList():
                self.shardPanel.hide()
                self.shardButton['text'] = 'Show Shards'
                self.shardButton['command'] = showShardList

            self.shardButton = DirectButton(parent = self, text = 'Show Shards', scale = 0.065, pos = (0.75, 0, 0.089), command = showShardList, textMayChange = 1)



    def handleMinimapButton(self, *args):
        localAvatar.guiMgr.nextMinimap()


    def updateTeleportIsland(self, teleportToken, amt):
        self.worldMap.updateTeleportIsland(teleportToken)


    def setReturnIsland(self, islandUid):
        self.worldMap.setReturnIsland(islandUid)
        self.setPortOfCall(islandUid)


    def setCurrentIsland(self, islandUid):
        self.worldMap.setCurrentIsland(islandUid)


    def setPortOfCall(self, islandUid):
        self.portOfCall = islandUid
        self.worldMap.setPortOfCall(self.portOfCall)
        if self.portOfCall:
            self.portOfCallLabel.show()
            self.portOfCallButton.show()
            islandName = PLocalizer.LocationNames.get(islandUid)
            if islandName:
                self.portOfCallLabel['text'] = '%s %s' % (PLocalizer.WordTo, islandName)
            else:
                self.portOfCallLabel['text'] = '%s %s' % (PLocalizer.WordTo, 'Unknown Island')
        else:
            self.portOfCallLabel.hide()
            self.portOfCallButton.hide()
            self.portOfCallLabel['text'] = ''


    def handlePortOfCall(self):
        if self.portOfCall:
            base.cr.teleportMgr.requestTeleportToIsland(self.portOfCall)

    def addQuestDart(self, questId, worldPos):
        return self.worldMap.addQuestDart(questId, worldPos)


    def updateQuestDart(self, questId, worldPos):
        return self.worldMap.updateQuestDart(questId, worldPos)


    def removeQuestDart(self, questId):
        return self.worldMap.removeQuestDart(questId)


    def addLocalAvDart(self, worldPos = Vec3(0)):
        return self.worldMap.addLocalAvDart(worldPos)


    def updateLocalAvDart(self, worldPos):
        return self.worldMap.updateLocalAvDart(worldPos)


    def addIsland(self, name, islandUid, modelPath, pos, h):
        return self.worldMap.addIsland(name, islandUid, modelPath, pos, h)


    def updateIsland(self, name, worldPos = None, rotation = None):
        return self.worldMap.updateIsland(name, worldPos, rotation)


    def removeIsland(self, name):
        return self.worldMap.removeIsland(name)


    def addOceanArea(self, name, areaUid, pos1, pos2):
        self.worldMap.addOceanArea(name, areaUid, pos1, pos2)


    def addShip(self, shipInfo, worldPos):
        self.worldMap.addShip(shipInfo, worldPos)


    def removeShip(self, shipDoId):
        self.worldMap.removeShip(shipDoId)


    def addFleet(self, fleetObj):
        self.worldMap.addFleet(fleetObj)


    def removeFleet(self, fleetObj):
        self.worldMap.removeFleet(fleetObj)


    def addPath(self, pathInfo):
        self.worldMap.addPath(pathInfo)


    def removePath(self, pathInfo):
        self.worldMap.removePath(pathInfo)
