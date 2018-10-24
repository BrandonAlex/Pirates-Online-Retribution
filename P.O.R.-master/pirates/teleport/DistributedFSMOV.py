from direct.distributed.DistributedObjectOV import DistributedObjectOV
from pirates.teleport.DistributedFSMBase import DistributedFSMBase

class DistributedFSMOV(DistributedObjectOV, DistributedFSMBase):
    
    def __init__(self, air, name = 'DistributedFSMOV'):
        DistributedFSMBase.__init__(self, name)
        DistributedObjectOV.__init__(self, air)
        self._DistributedFSMOV__requestContext = 0
        self._requests = { }
        self.obj = None

    __init__ = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(__init__)
    
    def __repr__(self):
        return '%s (%s)' % (DistributedFSMBase.__repr__(self), self.doId)

    
    def getObj(self):
        if not self.obj:
            self.obj = self.cr.getDo(self.doId)
        
        return self.obj

    
    def _incrementRequestContext(self):
        self._DistributedFSMOV__requestContext += 1
        if self._DistributedFSMOV__requestContext == 256:
            self._DistributedFSMOV__requestContext = 1
        
        return self._DistributedFSMOV__requestContext

    _incrementRequestContext = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(_incrementRequestContext)
    
    def fsmRequestResponse(self, requestContext, reason):
        (state, args, callback) = self._requests.pop(requestContext, ('', (), None))
        if callback:
            callback(reason, state, *args)
        

    fsmRequestResponse = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(fsmRequestResponse)
    
    def d_fsmRequestResponse(self, requestContext, reason):
        self.sendUpdate('fsmRequestResponse', [
            requestContext,
            reason])

    d_fsmRequestResponse = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(d_fsmRequestResponse)
    
    def b_requestFSMState(self, callback, state, *args):
        if callback:
            requestContext = self._incrementRequestContext()
            self._requests[requestContext] = (state, args, callback)
        else:
            requestContext = 0
        self.d_requestFSMState(requestContext, state, *args)

    b_requestFSMState = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(b_requestFSMState)
    
    def d_requestFSMState(self, requestContext, state, *args):
        self.sendUpdate('requestFSMState', [
            requestContext,
            [
                (state,) + args]])

    d_requestFSMState = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(d_requestFSMState)
    
    def setFSMState(self, stateContext, stateData):
        stateData = stateData[0]
        state = stateData[0]
        args = stateData[1:]
        return self.request(state, *args)

    setFSMState = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(setFSMState)

