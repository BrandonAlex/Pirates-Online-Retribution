from direct.distributed.DistributedObjectAI import DistributedObjectAI
from DistributedRepairGameBase import *

'''
dclass DistributedRepairGame : DistributedObject {
  start(uint8(0-5));
  stop();
  requestMincroGame(uint8(0-5)) airecv clsend;
  requestMincroGameResponse(bool, uint8);
  reportMincroGameProgress(uint8(0-5), int8, uint8) clsend airecv;
  setMincroGameProgress(uint8(0-5), int8);
  setAllMincroGameProgress(int8 []);
  setAvIds2CurrentGameList(uint8(0-5) [0-5], uint32 [0-5]);
  reportMincroGameScore(uint8(0-5), uint32) clsend airecv;
  cycleComplete(uint8, uint32 [0-5], uint16 [0-5], uint32);
  shipDamaged(bool, uint8);
  setGoldBonus(uint32) broadcast;
};
'''

class DistributedRepairGameAI(DistributedObjectAI, DistributedRepairGameBase):
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        DistributedRepairGameBase.__init__(self)
        self.difficulty = 0

    def setDifficulty(self, difficulty):
        self.difficulty = difficulty
    
    def getDifficulty(self):
        return self.difficulty
    
    def requestMincroGame(self, gameIndex):
        avId = self.air.getAvatarIdFromSender()
        success = False
        if self.location == ON_LAND:
            success = gameIndex < len(GAME_ORDER[ON_LAND])
   
        elif self.location == AT_SEA:
            success = gameIndex < len(GAME_ORDER[AT_SEA])
 
        self.sendUpdateToAvatarId(avId, 'requestMincroGameResponse', [success, self.difficulty])

    def reportMincroGameProgress(self, todo0, todo1, todo2):
        pass

    def reportMincroGameScore(self, todo0, todo1):
        pass

    def requestMincroGameResponse(self, success, difficulty):
        self.notify.info('mincroGameResponse: %s' % success)
        self.sendUpdate('requestMincroGameResponse', [success, difficulty])

    def setMincroGameProgress(self, progress):
        self.progress = progress

    def getMincroGameProgress(self):
        return self.progress

    def setGoldBonus(self, goldBonus):
        self.goldBonus = goldBonus

    def posControlledByIsland(self):
        return False
