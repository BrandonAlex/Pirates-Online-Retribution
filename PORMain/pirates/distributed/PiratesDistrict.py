from panda3d.core import NodePath
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from otp.distributed.DistributedDistrict import DistributedDistrict
from pirates.world import WorldGlobals
from pirates.world import WorldCreator
from pirates.piratesbase import PiratesGlobals

class PiratesDistrict(DistributedDistrict, NodePath):
    notify = DirectNotifyGlobal.directNotify.newCategory('PiratesDistrict')

    def __init__(self, cr):
        DistributedDistrict.__init__(self, cr)
        NodePath.__init__(self, render.attachNewNode('District-%s' % id(self)))
        self.mainWorldFile = None
        self.islands = { }
        self.shardType = 0

    def announceGenerate(self):
        DistributedDistrict.announceGenerate(self)
        self.worldCreator = base.worldCreator
        self.worldCreator.district = self
        if self.shardType == PiratesGlobals.SHARD_MAIN:
            self.worldCreator.makeMainWorld(self.mainWorldFile)
            self.worldCreator.registerFileObject(self.mainWorldFile)

    def setShardType(self, shardType):
        self.shardType = shardType

    def setMainWorld(self, world):
        self.mainWorldFile = world

    def delete(self):
        DistributedDistrict.delete(self)
        if self.worldCreator:
            self.worldCreator.destroy()

    def setAvatarCount(self, avatarCount):
        self.avatarCount = avatarCount
        messenger.send('PiratesDistrict-updateAvCounts', sentArgs = [
            self.doId,
            self.name,
            self.avatarCount,
            self.newAvatarCount])

    def getAvatarCount(self):
        return self.avatarCount

    def setNewAvatarCount(self, newAvatarCount):
        self.newAvatarCount = newAvatarCount

    def getNewAvatarCount(self):
        return self.newAvatarCount

    def setStats(self, avatarCount, newAvatarCount):
        self.setAvatarCount(avatarCount)
        self.setNewAvatarCount(newAvatarCount)

    def getName(self):
        return self.name

    def getUniqueId(self):
        pass
