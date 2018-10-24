from direct.distributed.DistributedCartesianGridAI import DistributedCartesianGridAI
from direct.distributed.GridParent import GridParent
from direct.directnotify import DirectNotifyGlobal
from pirates.world.DistributedGameAreaAI import DistributedGameAreaAI
import WorldGlobals

# World
from DistributedInteriorDoorAI import DistributedInteriorDoorAI

class DistributedGAInteriorAI(DistributedGameAreaAI, DistributedCartesianGridAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGAInteriorAI')

    def __init__(self, air, extDoor):
        DistributedGameAreaAI.__init__(self, air, '')

        cellWidth = WorldGlobals.ISLAND_TM_CELL_SIZE
        gridSize = WorldGlobals.GAME_AREA_INTERIOR_GRID_SIZE
        gridRadius = WorldGlobals.GAME_AREA_INTERIOR_GRID_RADIUS
        zoneId = WorldGlobals.GAME_AREA_INTERIOR_STARTING_ZONE

        DistributedCartesianGridAI.__init__(self, air, zoneId, gridSize, gridRadius, cellWidth)

        self.extDoor = extDoor
        self.intDoors = []

    def setBuildingInterior(self, buildingInterior):
        self.buildingInterior = buildingInterior

    def getBuildingInterior(self):
        return self.buildingInterior

    def createObject(self, objType, parent, objKey, object):
        genObj = None

        if objType == 'Island Game Area' and not self.buildingInterior:
            self.b_setUniqueId(objKey)
            self.sendUpdate('setModelPath', [object['Visual']['Model']])

        elif objType == 'Building Interior':
            if not self.getUniqueId():
                self.b_setUniqueId(objKey)
                self.sendUpdate('setModelPath', [object['Visual']['Model']])

        elif objType == 'Door Locator Node':
            genObj = self.createIntDoor(objKey, object)

        else:
            genObj = DistributedGameAreaAI.createObject(self, objType, parent, objKey, object)

        return genObj

    def createIntDoor(self, objKey, object):
        intDoor = DistributedInteriorDoorAI.makeFromObjectKey(self.air, objKey,
                                         object, self.extDoor.getBuildingUid())
        intDoor.setOtherDoorId(self.extDoor.doId)
        self.generateChild(intDoor)
        self.intDoors.append(intDoor)
        return intDoor

    def generateChild(self, obj, zoneId = None):
        if zoneId is None:
            if self.buildingInterior:
                zoneId = 2709

            else:
                zoneId = self.getZoneFromXYZ(obj.getPos())

        obj.interior = self
        obj.generateWithRequiredAndId(self.air.allocateChannel(), self.doId, zoneId)
        if obj.posControlledByIsland(): # This method must be defined in your AI
            if not self.buildingInterior:
                cell = GridParent.getCellOrigin(self, zoneId)
                pos = obj.getPos()
                obj.reparentTo(cell)
                obj.setPos(self, pos)
            obj.sendUpdate('setPos', obj.getPos())
            obj.sendUpdate('setHpr', obj.getHpr())
