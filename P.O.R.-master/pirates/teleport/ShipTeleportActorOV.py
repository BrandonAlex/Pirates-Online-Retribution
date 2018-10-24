from pirates.teleport.DistributedTeleportActorOV import DistributedTeleportActorOV
from pirates.piratesbase import PiratesGlobals

class ShipTeleportActorOV(DistributedTeleportActorOV):
    
    def __init__(self, cr, name = 'ShipTeleportActorOV', doEffect = True):
        DistributedTeleportActorOV.__init__(self, cr, name, doEffect = doEffect)

    __init__ = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(__init__)
    
    def enterOpenWorld(self, worldLocations, worldDoId):
        self.worldDoId = worldDoId
        self._requestWhenInterestComplete('WorldOpen')
        self.cr.setWorldStack(worldLocations, event = 'WorldOpen')

    enterOpenWorld = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterOpenWorld)
    
    def enterOpenGame(self, shipParentId, shipZoneId, shipDoId):
        self.shipDoId = shipDoId
        world = self.cr.getDo(self.worldDoId)
        world.goOnStage()
        self.cr.relatedObjectMgr.requestObjects((self.shipDoId,), allCallback = self.shipInterestReady, timeout = 30, timeoutCallback = self.shipTimedOut)
        self.oceanInterest = self.cr.addTaggedInterest(shipParentId, shipZoneId, self.cr.ITAG_GAME, 'ocean')

    enterOpenGame = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterOpenGame)
    
    def shipTimedOut(self, doIds):
        self.sendUpdate('clientAbort')

    shipTimedOut = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(shipTimedOut)
    
    def shipInterestReady(self, shipList):
        ship = shipList[0]
        self.cr.queueAllInterestsCompleteEvent()
        self.cr.setAllInterestsCompleteCallback(self.shipZoneComplete)

    shipInterestReady = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(shipInterestReady)
    
    def shipZoneComplete(self):
        if self.getCurrentOrNextState() != 'OpenGame':
            return None
        
        if self.cr == None:
            return None
        
        ship = self.cr.getDo(self.shipDoId)
        if ship:
            self._requestWhenInterestComplete('GameOpen')
            ship.placeLocalAvatar(localAvatar)
            localAvatar.b_setLocation(ship.getDoId(), PiratesGlobals.ShipZoneOnDeck)
            localAvatar.sendCurrentPosition()
            self.cr.removeTaggedInterest(self.oceanInterest)
            self.oceanInterest = None
        

    shipZoneComplete = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(shipZoneComplete)
    
    def exitOpenGame(self):
        self.cr.removeTaggedInterest(self.oceanInterest)
        self.oceanInterest = None
        self._cancelInterestCompleteRequest()

    exitOpenGame = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(exitOpenGame)
    
    def enterStartShow(self, *args):
        self.cr.loadingScreen.hide()
        base.transitions.fadeIn()
        localAvatar.b_setGameState('LandRoam')
        self.b_requestFSMState(None, 'Done')

    enterStartShow = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterStartShow)

