from direct.directnotify import DirectNotifyGlobal
from pirates.battle.DistributedBattleNPCAI import *

class DistributedBossGhostAI(DistributedBattleNPCAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBossGhostAI')
