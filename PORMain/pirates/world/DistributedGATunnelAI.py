# STUB

from direct.directnotify import DirectNotifyGlobal
from pirates.world.DistributedGAConnectorAI import DistributedGAConnectorAI

class DistributedGATunnelAI(DistributedGAConnectorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGATunnelAI')

    def __init__(self, air):
        DistributedGAConnectorAI.__init__(self, air)

    # sendLeaveTunnelDone() airecv clsend


