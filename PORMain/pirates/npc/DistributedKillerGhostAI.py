from direct.directnotify import DirectNotifyGlobal
from pirates.battle.DistributedBattleNPCAI import *

class DistributedKillerGhostAI(DistributedBattleNPCAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKillerGhostAI')
