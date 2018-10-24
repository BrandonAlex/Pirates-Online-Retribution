from direct.directnotify import DirectNotifyGlobal

from pirates.economy.DistributedShopKeeperAI import DistributedShopKeeperAI
from pirates.battle.DistributedBattleNPCAI import *
from pirates.piratesbase import PiratesGlobals

class DistributedNPCTownfolkAI(DistributedBattleNPCAI, DistributedShopKeeperAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedNPCTownfolkAI')

    def __init__(self, spawner):
        DistributedBattleNPCAI.__init__(self, spawner)
        DistributedShopKeeperAI.__init__(self, self.air)
        self.customModel = ''
        self.shopId = 0
        self.helpId = 0
        self.isGhost = 0
        self.ghostColor = 0
        self.hasGhostPowers = 0

    def getDNAId(self):
        if self.customModel:
            return self.customModel
        return self.getUniqueId()

    def setShopId(self, shopId):
        self.shopId = shopId

    def getShopId(self):
        return self.shopId

    def setHelpId(self, helpId):
        self.helpId = helpId

    def getHelpId(self):
        return self.helpId

    def setIsGhost(self, isGhost):
        self.isGhost = isGhost

    def getIsGhost(self):
        return self.isGhost

    def setGhostColor(self, ghostColor):
        self.ghostColor = ghostColor

    def getGhostColor(self):
        return self.ghostColor

    def setHasGhostPowers(self, hasGhostPowers):
        self.hasGhostPowers = hasGhostPowers

    def getHasGhostPowers(self):
        return self.hasGhostPowers

    # requestMusic(uint32) airecv clsend
    # playMusic(uint32) broadcast
    # levelUpCutlass(uint32) airecv clsend
    # setQuestRewardsEarned(uint32, uint32, uint32 [])
    # setInInvasion(bool) broadcast ram
    # setViewedPotionInstructions() airecv clsend
    # setZombie(bool) broadcast ram
    # setMovie(string, uint32) broadcast ram
    # triggerInteractShow(uint32)
    # offerOptions(int8)
    # startTutorial(uint8)
    # swordTutorialPt1(uint32) airecv clsend
    # pistolTutorialPt1(uint32) airecv clsend
    # shipTutorialPt1(uint32, ItemNameHolder) airecv clsend

    def handleInteract(self, avId, interactType, instant):
        if interactType == PiratesGlobals.INTERACT_TYPE_FRIENDLY:
            return REJECT

        return DistributedBattleNPCAI.handleInteract(self, avId, interactType, instant)

    @staticmethod
    def makeFromObjectKey(cls, spawner, uid, data):
        if cls is None:
            cls = DistributedNPCTownfolkAI
        avType = getattr(AvatarTypes, data['Category'])
        obj = DistributedBattleNPCAI.makeFromObjectKey(cls, spawner, uid, avType, data)

        helpId = data.get('HelpID', 'NONE')
        if helpId and helpId.isdigit():
            obj.setHelpId(int(helpId))

        shopId = data.get('ShopID', 'PORT_ROYAL_DEFAULTS')
        shopId = getattr(PiratesGlobals, shopId, None)
        if shopId is not None:
            obj.setShopId(shopId)
        # TO DO: Uncomment to make cast NPCs work (currently, it crashes the client)
        if 'CustomModel' in data and '/' in data['CustomModel']:
            obj.customModel = data['CustomModel']

        return obj
