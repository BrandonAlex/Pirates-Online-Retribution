from pirates.piratesbase import PiratesGlobals
from pirates.teleport.DoorTeleportActorOV import DoorTeleportActorOV

class InteriorDoorTeleportActorOV(DoorTeleportActorOV):
    
    def __init__(self, cr, name = 'InteriorDoorTeleportActorOV'):
        DoorTeleportActorOV.__init__(self, cr, name)
        self.doorRequest = None

    __init__ = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(__init__)
    
    def disable(self):
        if self.doorRequest:
            base.cr.relatedObjectMgr.abortRequest(self.doorRequest)
            self.doorRequest = None
        
        DoorTeleportActorOV.disable(self)

    
    def enterOpenGame(self, areaDoId, doorId):
        self.areaDoId = areaDoId
        self.doorId = doorId
        world = self.cr.getDo(self.worldDoId)
        world.goOnStage()
        area = self.cr.getDo(areaDoId)
        area.goOnStage()
        
        def doorArrived(door):
            doorLocator = door.getDoorLocator()
            localAvatar.reparentTo(doorLocator)
            localAvatar.setPosHpr(0, 10, 0, 0, 0, 0)
            localAvatar.wrtReparentTo(area)
            localAvatar.setP(0)
            localAvatar.setR(0)
            localAvatar.setScale(1)
            area.parentObjectToArea(localAvatar)
            area.handleEnterGameArea(None)
            localAvatar.enableGridInterest()
            area.manageChild(localAvatar)
            self._requestWhenInterestComplete('GameOpen')

        
        def doorNotArrived(doIdList):
            self.notify.error('InteriorDoorTeleportActorOV.enterOpenGame: door %s never arrived in area %s' % (self.doorId, area.uniqueId))

        self.doorRequest = base.cr.relatedObjectMgr.requestObjects([
            self.doorId], eachCallback = doorArrived, timeout = 60, timeoutCallback = doorNotArrived)

    enterOpenGame = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterOpenGame)
    
    def enterStartShow(self, *args):
        DoorTeleportActorOV.enterStartShow(self, *args)
        door = self.cr.getDo(self.doorId)
        messenger.send('fadeInInteriorDoor', [
            door.getBuildingUid()])
        base.cr.loadingScreen.hide()

    enterStartShow = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterStartShow)

