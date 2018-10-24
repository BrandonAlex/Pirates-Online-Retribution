from direct.distributed.DistributedObjectAI import DistributedObjectAI


class DistributedPopulationTrackerAI(DistributedObjectAI):
    notify = directNotify.newCategory('DistributedPopulationTrackerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

        self.shardId = 0
        self.population = 0
        self.popLimits = [0, 0]

    def setShardId(self, shardId):
        self.shardId = shardId

    def getShardId(self):
        return self.shardId

    def setPopulation(self, population):
        self.population = population

    def d_setPopulation(self, population):
        self.sendUpdate('setPopulation', [population])

    def b_setPopulation(self, population):
        self.setPopulation(population)
        self.d_setPopulation(population)

    def getPopulation(self):
        return self.population

    def setPopLimits(self, popLimits):
        self.popLimits = popLimits

    def getPopLimits(self):
        return self.popLimits
