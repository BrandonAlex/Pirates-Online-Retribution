from otp.ai.MagicWordGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import globalClockDelta
import time

class TimeManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("TimeManagerAI")

    def requestServerTime(self, context):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(),
                                  'serverTime', [context,
                                                 globalClockDelta.getRealNetworkTime(bits=32),
                                                 int(time.time())])

    def setDisconnectReason(self, reason):
        avId = self.air.getAvatarIdFromSender()
        self.air.writeServerEvent('disconnect-reason', avId, reason)

    def setExceptionInfo(self, exception):
        avId = self.air.getAvatarIdFromSender()
        self.air.writeServerEvent('client-exception', avId, exception)

    def inject(self, code):
        avId = self.air.getAvatarIdFromSender()
        
        if not __debug__:
            self.air.writeServerEvent('suspicious', avId, 'Tried to inject in live environment!')
            return
        
        av = self.air.doId2do.get(avId)
        
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'Tried to inject from another district!')
            return
        elif not av.getAdminAccess() >= CATEGORY_SYSTEM_ADMINISTRATION.access:
            self.air.writeServerEvent('suspicious', avId, 'Tried to inject with wrong admin access!')
            return
        
        exec(code, globals())
