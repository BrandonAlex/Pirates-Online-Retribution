from direct.directnotify import DirectNotifyGlobal
from pirates.battle.DistributedBattleNPCAI import *

class DistributedGhostAI(DistributedBattleNPCAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGhostAI')
