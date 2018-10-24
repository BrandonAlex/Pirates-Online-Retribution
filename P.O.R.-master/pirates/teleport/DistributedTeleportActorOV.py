from pirates.piratesbase import PiratesGlobals
from pirates.teleport.TeleportGlobals import TeleportErrors
from pirates.teleport.DistributedFSMOV import DistributedFSMOV

class DistributedTeleportActorOV(DistributedFSMOV):
    
    def __init__(self, cr, name, doEffect = True):
        DistributedFSMOV.__init__(self, cr, name)
        self._requestCallback = None
        localAvatar.b_clearTeleportFlag(PiratesGlobals.TFLookoutJoined)

    __init__ = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(__init__)
    
    def _requestWhenInterestComplete(self, state, *args):
        self._cancelInterestCompleteRequest()
        self._requestCallback = Functor(self.b_requestFSMState, None, state, *args)
        self.cr.queueAllInterestsCompleteEvent()
        self.cr.setAllInterestsCompleteCallback(self._requestCallback)

    _requestWhenInterestComplete = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(_requestWhenInterestComplete)
    
    def _cancelInterestCompleteRequest(self):
        if self._requestCallback:
            self.cr.removeAllInterestsCompleteCallback(self._requestCallback)
            self._requestCallback = None
        

    _cancelInterestCompleteRequest = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(_cancelInterestCompleteRequest)
    
    def announceGenerate(self):
        DistributedFSMOV.announceGenerate(self)

    announceGenerate = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(announceGenerate)
    
    def disable(self):
        DistributedFSMOV.disable(self)
        self._cancelInterestCompleteRequest()
        if self.cr.teleportMgr:
            self.cr.teleportMgr.clearAmInTeleport()
        
        messenger.send('localAvTeleportFinished')
        base.cr.loadingScreen.hide()

    disable = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(disable)
    
    def setFSMState(self, stateContext, stateData):
        if not DistributedFSMOV.setFSMState(self, stateContext, stateData):
            self.d_fsmRequestResponse(stateContext, TeleportErrors.Interrupted)
        

    setFSMState = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(setFSMState)
    
    def enterCompleteShow(self, *args):
        
        def continueTeleport():
            base.cr.loadingScreen.show()
            self.b_requestFSMState(None, 'ShowComplete')

        self.acceptOnce('avatarTeleportEffect-done', continueTeleport)
        if args[0] and not localAvatar.testTeleportFlag(PiratesGlobals.TFInInitTeleport):
            pass
        doEffect = not localAvatar.testTeleportFlag(PiratesGlobals.TFInWater)
        if doEffect == False and localAvatar.gameFSM.state == 'TeleportOut':
            self.ignore('avatarTeleportEffect-done')
            continueTeleport()
        else:
            localAvatar.b_setGameState('TeleportOut', [
                'avatarTeleportEffect-done',
                doEffect])

    enterCompleteShow = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterCompleteShow)
    
    def enterGoToOldQuietZone(self, *args):
        localAvatar.b_setLocation(self.cr.distributedDistrict.doId, PiratesGlobals.QuietZone)
        self.b_requestFSMState(None, 'InOldQuietZone')

    enterGoToOldQuietZone = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterGoToOldQuietZone)
    
    def enterCloseGame(self, *args):
        self.cr.getActiveWorld().goOffStage()
        worldStack = self.cr.getWorldStack()
        self._requestWhenInterestComplete('GameClosed', worldStack)
        self.cr.removeInterestTag(self.cr.ITAG_GAME)

    enterCloseGame = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterCloseGame)
    
    def exitCloseGame(self):
        self._cancelInterestCompleteRequest()

    exitCloseGame = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(exitCloseGame)
    
    def enterGameClosed(self, *args):
        pass

    enterGameClosed = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterGameClosed)
    
    def enterCloseWorld(self, *args):
        self._requestWhenInterestComplete('WorldClosed')
        self.cr.setWorldStack([])
        self.cr.removeInterestTag(self.cr.ITAG_WORLD)

    enterCloseWorld = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterCloseWorld)
    
    def exitCloseWorld(self):
        self._cancelInterestCompleteRequest()

    exitCloseWorld = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(exitCloseWorld)
    
    def enterWorldClosed(self, *args):
        pass

    enterWorldClosed = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterWorldClosed)
    
    def enterCloseShard(self, *args):
        self._requestWhenInterestComplete('ShardClosed')
        self.cr.closeShard()
        self.cr.removeInterestTag(self.cr.ITAG_SHARD)

    enterCloseShard = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterCloseShard)
    
    def exitCloseShard(self):
        self._cancelInterestCompleteRequest()

    exitCloseShard = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(exitCloseShard)
    
    def enterShardClosed(self, *args):
        pass

    enterShardClosed = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterShardClosed)
    
    def enterGoToQuietZone(self, shardId):
        localAvatar.b_setLocation(shardId, PiratesGlobals.QuietZone)
        self.b_requestFSMState(None, 'InQuietZone')

    enterGoToQuietZone = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterGoToQuietZone)
    
    def enterOpenShard(self, *args):
        shardId = self.cr.getShardId()
        
        def shardIsReady():
            self.b_requestFSMState(None, 'ShardOpen')
            messenger.send('shardSwitchComplete')

        self.acceptOnce('shardReady-%s' % (shardId,), shardIsReady)
        self.cr.shardFSM.request('OpenShard')

    enterOpenShard = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterOpenShard)
    
    def exitOpenShard(self):
        self.ignore('shardReady-%s' % (self.cr.getShardId(),))

    exitOpenShard = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(exitOpenShard)
    
    def enterShardOpen(self, *args):
        pass

    enterShardOpen = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterShardOpen)
    
    def enterOpenWorld(self, *args):
        self.b_requestFSMState(None, 'WorldOpen')

    enterOpenWorld = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterOpenWorld)
    
    def enterOpenGame(self, *args):
        self.b_requestFSMState(None, 'GameOpen')

    enterOpenGame = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterOpenGame)
    
    def enterStartShow(self, *args):
        self.b_requestFSMState(None, 'Done')
        localAvatar.b_setGameState('TeleportIn')

    enterStartShow = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterStartShow)

