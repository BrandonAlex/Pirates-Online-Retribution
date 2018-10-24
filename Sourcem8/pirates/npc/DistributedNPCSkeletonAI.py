from direct.directnotify.DirectNotifyGlobal import directNotify
from pirates.battle.DistributedBattleNPCAI import DistributedBattleNPCAI

class DistributedNPCSkeletonAI(DistributedBattleNPCAI):
    notify = directNotify.newCategory('DistributedNPCSkeletonAI')

    def __init__(self, air):
        DistributedBattleNPCAI.__init__(self, air)

    def disable(self):
        DistributedBattleNPCAI.disable(self)

    def delete(self):
        DistributedBattleNPCAI.delete(self)

    def generate(self):
        DistributedBattleNPCAI.generate(self)

    def announceGenerate(self):
        DistributedBattleNPCAI.announceGenerate(self)

    @classmethod
    def makeFromObjectKey(cls, air, objKey, data):
        obj = DistributedBattleNPCAI.makeFromObjectKey(air, objKey, data)
        return obj
