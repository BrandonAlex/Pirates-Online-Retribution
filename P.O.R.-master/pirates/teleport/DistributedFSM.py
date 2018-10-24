from direct.distributed.DistributedObject import DistributedObject
from pirates.teleport.DistributedFSMBase import DistributedFSMBase

class DistributedFSM(DistributedObject, DistributedFSMBase):
    
    def __init__(self, cr, name):
        DistributedFSMBase.__init__(self, name)
        DistributedObject.__init__(self, cr)

    
    def setFSMState(self, stateContext, stateData):
        stateData = stateData[0]
        state = stateData[0]
        args = stateData[1:]
        result = self.request(state, *args)

    setFSMState = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(setFSMState)

