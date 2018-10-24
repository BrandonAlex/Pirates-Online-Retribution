from direct.directnotify import DirectNotifyGlobal
from pirates.distributed.DistributedInteractiveAI import *

class DistributedHolidayObjectAI(DistributedInteractiveAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedHolidayObjectAI')

    def __init__(self, air):
        DistributedInteractiveAI.__init__(self, air)

    def setInteractRadius(self, radius):
        self.radius = radius

    def setInteractMode(self, mode):
        self.mode = mode

    def getInteractRadius(self):
        return 0

    def getInteractMode(self):
        return 0

    @classmethod
    def makeFromObjectKey(cls, air, objKey, data):
        obj = DistributedInteractiveAI.makeFromObjectKey(cls, air, objKey, data)
        return obj
