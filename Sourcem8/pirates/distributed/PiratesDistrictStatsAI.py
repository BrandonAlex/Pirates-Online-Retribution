from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class PiratesDistrictStatsAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("PiratesDistrictStatsAI")
    districtId = 0
    avatarCount = 0
    newAvatarCount = 0

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        # We want to handle shard status queries so that a ShardStatusReceiver
        # being created after we're generated will know where we're at:
        self.air.netMessenger.accept('queryShardStatus', self, self.handleShardStatusQuery)

    def handleShardStatusQuery(self):
        # Send a shard status update containing our population:
        status = {'population': self.avatarCount}
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, status])

    def setPiratesDistrictId(self, districtId):
        self.districtId = districtId

    def getPiratesDistrictId(self):
        return self.districtId

    def d_setPiratesDistrictId(self, districtId):
        self.sendUpdate('setPiratesDistrictId', [districtId])

    def b_setPiratesDistrictId(self, districtId):
        self.d_setPiratesDistrictId(districtId)
        self.setPiratesDistrictId(districtId)

    def setAvatarCount(self, avCount):
        self.avatarCount = avCount

    def getAvatarCount(self):
        return self.avatarCount

    def d_setAvatarCount(self, avCount):
        self.sendUpdate('setAvatarCount', [avCount])

    def b_setAvatarCount(self, avCount):
        self.d_setAvatarCount(avCount)
        self.setAvatarCount(avCount)

    def setNewAvatarCount(self, newAvCount):
        self.newAvatarCount = newAvCount

    def getNewAvatarCount(self):
        return self.newAvatarCount

    def d_setNewAvatarCount(self, newAvCount):
        self.sendUpdate('setNewAvatarCount', [newAvCount])

    def b_setNewAvatarCount(self, newAvCount):
        self.d_setNewAvatarCount(newAvCount)
        self.setNewAvatarCount(newAvCount)
