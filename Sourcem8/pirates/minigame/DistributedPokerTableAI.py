from direct.directnotify import DirectNotifyGlobal
from pirates.distributed import DistributedInteractiveAI
import DistributedGameTableAI

class DistributedPokerTableAI(DistributedGameTableAI.DistributedGameTableAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPokerTableAI')

    def __init__(self, air):
        DistributedInteractiveAI.__init__(self, air)

    def handleInteraction(self):
        return ACCEPT #gonna return it as accept, will need to have checks soon
