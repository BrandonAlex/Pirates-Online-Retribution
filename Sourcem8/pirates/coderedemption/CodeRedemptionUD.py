from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify

class CodeRedemptionUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('CodeRedemptionUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

    def sendCodeForRedemption(self, code, userName, accountId):
        # todo: gotta have this written to accept codes. For now, let's reject the code.
        return REJECT
