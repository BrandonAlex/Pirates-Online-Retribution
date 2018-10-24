from panda3d.core import NodePath
from pirates.instance import DistributedInstanceBase

class DistributedTeleportZone(DistributedInstanceBase.DistributedInstanceBase, NodePath):

    def __init__(self, cr):
        DistributedInstanceBase.DistributedInstanceBase.__init__(self, cr)


    def getInstanceNodePath(self):
        return self
