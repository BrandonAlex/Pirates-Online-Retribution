
from direct.distributed.PyDatagram import *

from otp.ai.TimeManagerAI import TimeManagerAI
from otp.distributed.OtpDoGlobals import *
from otp.ai.MagicWordManagerAI import MagicWordManagerAI
from otp.ai.BanManagerAI import BanManagerAI

from pirates.distributed.PiratesInternalRepository import PiratesInternalRepository
from pirates.instance.DistributedMainWorldAI import DistributedMainWorldAI
from pirates.distributed.DistrictManagerAI import DistrictManagerAI
from pirates.ai.NewsManagerAI import NewsManagerAI

from pirates.world.WorldCreatorAI import WorldCreatorAI
from pirates.piratesbase.DistributedTimeOfDayManagerAI import DistributedTimeOfDayManagerAI
from pirates.piratesbase.DistributedGameStatManagerAI import DistributedGameStatManagerAI
from pirates.instance.DistributedTeleportMgrAI import DistributedTeleportMgrAI
from pirates.distributed.TargetManagerAI import TargetManagerAI
from pirates.battle.BattleManagerAI import BattleManagerAI

class PiratesAIRepository(PiratesInternalRepository):
    def __init__(self, baseChannel, stateServerChannel, districtName):
        PiratesInternalRepository.__init__(
            self, baseChannel, stateServerChannel, dcSuffix='AI')

        self.districtName = districtName
        self.districtManager = None
        self.uid2do = {}

        self.notify.setInfo(True)

    def createManagers(self):
        self.timeManager = TimeManagerAI(self)
        self.timeManager.generateWithRequired(2)

        self.newsManager = NewsManagerAI(self)
        self.newsManager.generateWithRequired(2)

        self.todManager = DistributedTimeOfDayManagerAI(self)
        self.todManager.generateWithRequired(2)

        self.tpMgr = DistributedTeleportMgrAI(self)
        self.tpMgr.generateWithRequired(2)

        self.targetMgr = TargetManagerAI(self)
        self.targetMgr.generateWithRequired(2)

        self.gameStatManager = DistributedGameStatManagerAI(self)
        self.gameStatManager.generateWithRequired(2)

        self.magicWordManager = MagicWordManagerAI(self)
        self.magicWordManager.generateWithRequired(2)

        self.banMgr = BanManagerAI(self)
        self.battleMgr = BattleManagerAI(self)

    def createMainWorld(self):
        self.worldCreator = WorldCreatorAI(self)

        self.mainWorld = DistributedMainWorldAI(self)
        self.mainWorld.generateWithRequired(2)

        self.worldCreator.makeMainWorld(self.districtManager.district.mainWorld)

    def handleConnected(self):
        PiratesInternalRepository.handleConnected(self)

        self.districtId = self.allocateChannel()
        self.notify.info('Creating PiratesDistrictAI(%d)...' % self.districtId)

        self.districtManager = DistrictManagerAI(self)
        self.districtManager.generateDistrict()

        self.notify.info('Claiming ownership of channel ID: %d...' % self.districtId)
        self.claimOwnership(self.districtId)

        self.notify.info('Creating managers...')
        self.createManagers()

        self.notify.info('Creating the main world...')
        self.createMainWorld()

        self.notify.info('Making district available...')
        self.districtManager.openDistrict()
        self.notify.info('Done.')
        messenger.send('startShardActivity')

        from pirates.battle.DistributedEnemySpawnerAI import DistributedEnemySpawnerAI
        DistributedEnemySpawnerAI.printMissingTypes()
        self.accept('pirate-inventory-activate', self.__inventoryActivate)
    
    def __inventoryActivate(self, ownerId, invId):
        owner = self.doId2do.get(ownerId)
        
        if owner:
            owner.b_setInventoryId(invId)
        else:
            self.acceptOnce('generate-%d' % ownerId, lambda av: av.b_setInventoryId(invId))

    def getTrackClsends(self):
        return False

    def incrementPopulation(self):
        self.districtManager.district.b_setAvatarCount(self.districtManager.district.getAvatarCount() + 1)

    def decrementPopulation(self):
        self.districtManager.district.b_setAvatarCount(self.districtManager.district.getAvatarCount() - 1)
