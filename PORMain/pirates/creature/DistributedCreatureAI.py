from direct.directnotify import DirectNotifyGlobal
from pirates.battle.DistributedBattleNPCAI import *

class DistributedCreatureAI(DistributedBattleNPCAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCreatureAI')
    avatarType = AvatarTypes.Creature
    isGhost = 0
    ghostColor = 0
    hasGhostPowers = 0

    def __init__(self, air):
        DistributedBattleNPCAI.__init__(self, air)

    def setIsGhost(self, isGhost):
        self.isGhost = isGhost

    def getIsGhost(self):
        return self.isGhost

    def setGhostColor(self, ghostColor):
        self.ghostColor = ghostColor

    def getGhostColor(self):
        return self.ghostColor

    def setHasGhostPowers(self, hasGhostPowers):
        self.hasGhostPowers = hasGhostPowers

    def getHasGhostPowers(self):
        return self.hasGhostPowers