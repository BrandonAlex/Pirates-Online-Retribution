from pirates.teleport.DistributedTeleportActorOV import DistributedTeleportActorOV

class InstanceTeleportActorOV(DistributedTeleportActorOV):
    
    def __init__(self, cr, name = 'InstanceTeleportActorOV', doEffect = True):
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
    
    def enterOpenGame(self, areaDoId, spawnPt):
        self.areaDoId = areaDoId
        self.spawnPt = spawnPt
        world = self.cr.getDo(self.worldDoId)
        if not world:
            self.notify.warning('enterOpenGame: world %s not found, probably got removed already' % self.worldDoId)
            self.sendUpdate('clientAbort')
            return None
        
        world.goOnStage()
        area = self.cr.getDo(areaDoId)
        area.goOnStage()
        self._requestWhenInterestComplete('GameOpen')
        localAvatar.reparentTo(area)
        localAvatar.setPosHpr(area, *self.spawnPt)
        area.parentObjectToArea(localAvatar)
        localAvatar.enableGridInterest()
        area.manageChild(localAvatar)
        localAvatar.sendCurrentPosition()

    enterOpenGame = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterOpenGame)
    
    def exitOpenGame(self):
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

