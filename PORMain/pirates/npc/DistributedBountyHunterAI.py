from direct.directnotify import DirectNotifyGlobal
from pirates.battle.DistributedBattleNPCAI import *

class DistributedBountyHunterAI(DistributedBattleNPCAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBountyHunterAI')
