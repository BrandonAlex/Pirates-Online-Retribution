from direct.distributed.DistributedObjectAI import *
from direct.directnotify import DirectNotifyGlobal
from pirates.distributed.DistributedInteractiveAI import *

class DistributedSearchableContainerAI(DistributedInteractiveAI, DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSearchableContainerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        DistributedInteractiveAI.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def setSearchTime(self, searchTime):
        self.searchTime = searchTime

    def getSearchTime(self):
        return self.searchTime

    def setType(self, searchType):
        self.type = searchType

    def getType(self):
        return self.type

    def setVisZone(self, visZone):
        self.visZone = visZone

    def getVisZone(self):
        return ''

    def setContainerColor(self, color1, color2, color3, color4):
        self.color = [color1, color2, color3, color4]

    def getContainerColor(self):
        return [0,0,0,0]

    def setSphereScale(self, sphereScale):
        self.sphereScale = sphereScale

    def getSphereScale(self):
        return self.sphereScale

    def handleInteract(self, avId, interactType, instant):
        # TO DO: If av has a quest to search, allow them
        return REJECT

    @classmethod
    def makeFromObjectKey(cls, air, objKey, data):
        obj = DistributedInteractiveAI.makeFromObjectKey(cls, air, objKey, data)
        obj.setSearchTime(int(float(data['searchTime'])))
        obj.setType(data['type'])
        obj.setSphereScale(int(float(data['Aggro Radius'])))
        return obj
