from panda3d.core import VBase4
from pirates.ship.DistributedSimpleShip import DistributedSimpleShip, MinimapShip

class DistributedBlackPearlSimpleShip(DistributedSimpleShip):

    def __init__(self, cr):
        DistributedSimpleShip.__init__(self, cr)


    def checkAbleDropAnchor(self):
        if self.shipStatusDisplay:
            self.shipStatusDisplay.disableAnchorButton()



    def handleChildArrive(self, child, zoneId):
        DistributedSimpleShip.handleChildArrive(self, child, zoneId)
        if child.isLocal():
            localAvatar.guiMgr.radarGui.zoomFSM.setLevels([
                1000])
            mapObj = self.getMinimapObject()
            if mapObj:
                mapObj.setAsLocalAvShip(child.getCrewShipId() == self.doId)




    def loadShipStatusDisplay(self):
        DistributedSimpleShip.loadShipStatusDisplay(self)
        self.shipStatusDisplay.hidePermissionButton()


    def getMinimapObject(self):
        if not (self.minimapObj) and not self.isDisabled():
            self.minimapObj = MinimapBlackPearlShip(self)

        return self.minimapObj



class MinimapBlackPearlShip(MinimapShip):
    DEFAULT_COLOR = VBase4(0.1, 0.5, 1.0, 0.7)

    def updateOnMap(self, map):
        MinimapShip.updateOnMap(self, map)
        if self.isLocalAvShip:
            map.updateRadarTransform(self.worldNode)
