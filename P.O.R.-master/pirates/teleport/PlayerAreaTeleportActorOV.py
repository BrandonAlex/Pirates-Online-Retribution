from pirates.piratesbase import PiratesGlobals
from pirates.teleport.AreaTeleportActorOV import AreaTeleportActorOV

class PlayerAreaTeleportActorOV(AreaTeleportActorOV):
    
    def __init__(self, cr, name = 'PlayerAreaTeleportActorOV'):
        AreaTeleportActorOV.__init__(self, cr, name)

    __init__ = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(__init__)

