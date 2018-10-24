from panda3d.core import Datagram
from direct.showbase.DirectObject import DirectObject
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.FSM import FSM

from otp.distributed import OtpDoGlobals

from pirates.uberdog.ClientServicesManagerUD import RemoteAccountDB

class BanFSM(FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('BanFSM')
    BanUrl = config.GetString('ban-base-url', 'http://api.piratesonline.co/ban/')
    DoActualBan = config.GetBool('ban-do-ban', True)
    
    def __init__(self, mgr):
        FSM.__init__(self, 'BanFSM')
        self.mgr = mgr
        
    def enterStart(self, bannerId, avId, accountId, duration, banReason):
        self.bannerId = bannerId
        self.avId = avId
        self.accountId = accountId
        self.duration = duration
        self.banReason = banReason
        
        self.demand('RetrieveBanner')
        
    def enterRetrieveBanner(self):
        self.mgr.air.dbInterface.queryObject(self.mgr.air.dbId, self.bannerId, self.__handleRetrieveBanner)

    def __handleRetrieveBanner(self, dclass, fields):
        if dclass != self.mgr.air.dclassesByName['DistributedPlayerPirateUD']:
            self.demand('Error', 'Banner object was not found in the database!')
            return

        self.bannerName = fields['setName'][0]
        self.banner = '%s (%s)' % (self.bannerName, self.bannerId)
        self.demand('RetrieveAccount')
        
    def enterRetrieveAccount(self):
        self.mgr.air.dbInterface.queryObject(self.mgr.air.dbId, self.accountId, self.__handleRetrieveAccount)

    def __handleRetrieveAccount(self, dclass, fields):
        if dclass != self.mgr.air.dclassesByName['AccountUD']:
            self.demand('Error', 'Banner object was not found in the database!')
            return
        
        self.targetUsername = fields['ACCOUNT_ID']
        self.demand('Ban')
        
    def enterBan(self):
        if not self.DoActualBan:
            self.mgr.callback(self, True, None)
            self.demand('Off')
            return

        (success, error), res = RemoteAccountDB.post(self.mgr.air, self.BanUrl,
                                                     username=self.targetUsername,
                                                     duration=self.duration,
                                                     reason=self.banReason,
                                                     banner=self.banner)
        if success:
            success = res['success']
            error = res.get('error')
        
        self.mgr.callback(self, success, error)
    
    def enterError(self, error):
        self.mgr.callback(self, False, error)

class BanManagerUD(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('BanManagerUD')

    def __init__(self, air):
        self.air = air
        self.accept('BANMGR_ban', self.banUD)

    def banUD(self, bannerId, avId, accountId, duration, banReason):
        BanFSM(self).demand('Start', bannerId, avId, accountId, duration, banReason)
        
    def callback(self, fsm, success, error):            
        if not success:
            # Better notify the banner
            avId = self.air.csm.GetPuppetConnectionChannel(fsm.bannerId)
            msg = 'Failed to ban %s: %s' % (fsm.targetUsername, error)
            self.air.systemMessage('BanManagerUD: ERROR: %s' % msg, avId)
            self.notify.warning(msg)
            return

        dg = PyDatagram()
        dg.addServerHeader(self.air.csm.GetPuppetConnectionChannel(fsm.avId), self.air.ourChannel, CLIENTAGENT_EJECT)
        dg.addUint16(152)
        dg.addString(fsm.targetUsername)
        self.air.send(dg)

        msg = '%s banned %s for %s hours: %s' % (fsm.banner, fsm.targetUsername, fsm.duration, fsm.banReason)
        self.notify.info(msg)
        self.air.writeServerEvent('banned', fsm.accountId, username=fsm.targetUsername,
                                  moreInfo=msg)

        self.air.systemMessage(msg, OtpDoGlobals.OTP_STAFF_CHANNEL)
