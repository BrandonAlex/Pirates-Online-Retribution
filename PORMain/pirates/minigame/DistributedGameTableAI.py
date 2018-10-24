from direct.directnotify import DirectNotifyGlobal
from pirates.distributed import DistributedInteractiveAI

class DistributedGameTableAI(DistributedInteractiveAI.DistributedInteractiveAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGameTableAI')

    def __init__(self, air):
        DistributedInteractiveAI.__init__(self, air)

    def handleInteraction(self):
        return ACCEPT # gonna return it as accept, will need to have checks soon

    def requestSeat(self, todo0, todo1):
        pass
