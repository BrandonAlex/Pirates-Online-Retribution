from direct.distributed import DistributedObjectUD

class DistributedTeleportZoneUD(DistributedObjectUD.DistributedObjectUD):

    def ___init___(self, air):
        DistributedObjectUD.DistributedObjectUD.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectUD.DistributedObjectUD.announceGenerate(self)

    def generate(self):
        DistributedObjectUD.DistributedObjectUD.generate(self)

    def delete(self):
        DistributedObjectUD.DistributedObjectUD.delete(self)

    def disable(self):
        DistributedObjectUD.DistributedObjectUD.disable(self)
