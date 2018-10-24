from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal


class DistributedTravelAgent(DistributedObjectGlobal):
    notify = directNotify.newCategory('DistributedTravelAgent')

    def sendRequestInitLoc(self, desiredShard):
        self.sendUpdate('requestInitLoc', [desiredShard])

    def requestInitLocResponse(self, shardAllowed, desiredShard):
        print 'Shard %s is %s' % (desiredShard, shardAllowed)
        if shardAllowed:
            self.cr.playingGameLocReceived(desiredShard, 2000)
