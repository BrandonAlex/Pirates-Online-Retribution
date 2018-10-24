from pirates.teleport.DistributedTeleportActorOV import DistributedTeleportActorOV
from pirates.cutscene import CutsceneData

class TutorialTeleportActorOV(DistributedTeleportActorOV):
    
    def __init__(self, cr, name = 'TutorialTeleportActorOV', doEffect = True):
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
    
    def exitOpenWorld(self):
        self._cancelInterestCompleteRequest()

    exitOpenWorld = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(exitOpenWorld)
    
    def enterOpenGame(self, tutorialDoId, areaDoId, spawnPt):
        self.tutorialDoId = tutorialDoId
        self.areaDoId = areaDoId
        self.spawnPt = spawnPt
        world = self.cr.getDo(self.worldDoId)
        world.goOnStage()
        if localAvatar.style.getTutorial() == 0:
            tutorial = self.cr.getDo(self.tutorialDoId)
            tutorial.preloadCutscene(CutsceneData.PRELOADED_CUTSCENE_STAGE1)
        
        area = self.cr.getDo(areaDoId)
        area.goOnStage()
        self._requestWhenInterestComplete('GameOpen')
        area = self.cr.getDo(self.areaDoId)
        localAvatar.reparentTo(area)
        localAvatar.setPosHpr(area, *self.spawnPt)
        area.parentObjectToArea(localAvatar)
        localAvatar.enableGridInterest()
        area.manageChild(localAvatar)

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
        self._requestWhenInterestComplete('Done')

    enterStartShow = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterStartShow)

