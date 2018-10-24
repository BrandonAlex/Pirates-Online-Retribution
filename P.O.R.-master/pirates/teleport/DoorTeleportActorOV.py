from pirates.piratesbase import PiratesGlobals
from pirates.teleport.AreaTeleportActorOV import AreaTeleportActorOV

class DoorTeleportActorOV(AreaTeleportActorOV):
    
    def __init__(self, cr, name = 'DoorTeleportActorOV'):
        AreaTeleportActorOV.__init__(self, cr, name)

    __init__ = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(__init__)
    
    def enterCompleteShow(self, *args):
        base.cr.loadingScreen.show()
        self.b_requestFSMState(None, 'ShowComplete')

    enterCompleteShow = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(enterCompleteShow)

