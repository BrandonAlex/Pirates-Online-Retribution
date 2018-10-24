from direct.directnotify.DirectNotifyGlobal import *

# Base
from pirates.piratesbase import PiratesGlobals

# World
from DistributedBuildingDoorAI import DistributedBuildingDoorAI
from DistributedJailInteriorAI import DistributedJailInteriorAI
from DistributedGAInteriorAI import DistributedGAInteriorAI
from WorldCreatorBase import WorldCreatorBase
import WorldGlobals

class InteriorFlags:
    FORT = 1
    JAIL = 2
    # Next id is 4 (powers of 2)
    # Thought I'd say it since TTR had a similar flag thing
    # and Joey added 3, messing a lot of stuff

class WorldCreatorAI(WorldCreatorBase):
    notify = directNotify.newCategory('WorldCreatorAI')

    def __init__(self, air):
        WorldCreatorBase.__init__(self, air)
        self.air = self.repository
        self.fileDicts = {}

        self.__loadingInterior = False

    def createObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj=False, fileName=None, actualParentObj=None):
        objType = WorldCreatorBase.createObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj, fileName=fileName)
        if not objType:
            return

        newObj = None
        genObj = None
        objectCat = ''

        if dynamic:
            objectCat = self.findObjectCategory(objType)

        if self.__loadingInterior:
            actualParentObj = parent.getPythonTag('npTag-gameArea')

        if objType == 'Region':
            self.air.mainWorld.oceanGrid.registerIslandData(object['Objects'])

        elif objType == 'Island':
            il = self.air.mainWorld.oceanGrid.createIsland(objKey)
            actualParentObj = il

        elif actualParentObj:
            genObj = actualParentObj.createObject(objType, parent, objKey, object)

        if genObj:
            if 'Objects' in object:
                newObj = genObj

        return (newObj, actualParentObj)

    def createBuilding(self, parent, objKey, object):
        interiorFile = object['File']

        if not (interiorFile and 'Objects' in object):
            return

        flags = 0
        if 'Fort' in interiorFile:
            flags |= InteriorFlags.FORT

        elif 'Jail' in interiorFile:
            flags |= InteriorFlags.JAIL

        extDoor = None

        object['key'] = objKey
        for key, obj in object['Objects'].items():
            if obj['Type'] == 'Door Locator Node':
                extDoor = DistributedBuildingDoorAI.makeFromObjectKey(self.air, key, obj, object)
                break

        else:
            self.notify.warning('%s defines interior, but has no exterior door!' % objKey)
            return

        parent.generateChild(extDoor)
        interior = self.loadInterior(interiorFile, parent.getParentObj(), extDoor, flags)
        extDoor.b_setInteriorId(interior.doId, interior.getUniqueId(), interior.parentId, interior.zoneId)

        return extDoor

    def loadInterior(self, interiorFile, parent, extDoor, flags):
        if flags & InteriorFlags.JAIL:
            interior = DistributedJailInteriorAI(self.air, extDoor)

        else:
            interior = DistributedGAInteriorAI(self.air, extDoor)

        interior.setBuildingInterior(~flags & InteriorFlags.FORT)
        zoneId = PiratesGlobals.InteriorDoorZone << 16 | extDoor.doId & 0xFFFF
        parent.generateChild(interior, zoneId)

        self.__loadingInterior = True
        self.__loadInteriorFileAndAdditionalData(interiorFile, interior)
        self.__loadingInterior = False

        if not interior.intDoors:
            self.notify.warning('Interior %s defines no door, forcing generate...' % interiorFile)
            interior.createIntDoor('int%d.fakedoor' % interior.doId, {})

        return interior

    def __loadInteriorFileAndAdditionalData(self, filename, interior):
        ret = self.loadObjectsFromFile(filename, interior, True)[0]
        additionalData = []
        for obj in ret['Objects'].values():
            additionalData.extend(obj.get('AdditionalData', []))

        for additional in additionalData:
            self.__loadInteriorFileAndAdditionalData(additional, interior)
