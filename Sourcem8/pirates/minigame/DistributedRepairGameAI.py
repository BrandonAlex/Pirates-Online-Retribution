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

    def requestMincroGame(self, game):
        self.game = game

    def reportMincroGameProgress(self, todo0, todo1, todo2):
        pass

    def reportMincroGameScore(self, todo0, todo1):
        pass

    def requestMincroGameResponse(self, todo0, todo1):
        print "requestMincroGameResponse %s %s" % (todo0, todo1)
        return ACCEPT | ACCEPT_SEND_UPDATE

    def setMincroGameProgress(self, progress):
        self.progress = progress

    def getMincroGameProgress(self):
        return self.progress

    def setGoldBonus(self, goldBonus):
        self.goldBonus = goldBonus

    def posControlledByIsland(self):
        return False
