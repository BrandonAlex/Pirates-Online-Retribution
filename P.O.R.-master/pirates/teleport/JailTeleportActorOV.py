from pirates.teleport.DistributedTeleportActorOV import DistributedTeleportActorOV

class JailTeleportActorOV(DistributedTeleportActorOV):
    
    def __init__(self, cr, doEffect = True):
        DistributedTeleportActorOV.__init__(self, cr, 'JailTeleportActorOV', doEffect = doEffect)

    __init__ = report(types = [
        'args'], dConfigParam = [
        'dteleport'])(__init__)

