from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedNodeAI import DistributedNodeAI

from pirates.world.DistributedLocatableObjectAI import DistributedLocatableObjectAI

IGNORE = 0
REJECT = 1
ACCEPT = 2
ACCEPT_SET_AV = 4
ACCEPT_SEND_UPDATE = 8

class DistributedInteractiveAI(DistributedLocatableObjectAI, DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInteractiveAI')
    REJECT_IF_BUSY = True

    def __init__(self, air):
        DistributedLocatableObjectAI.__init__(self, air)
        DistributedNodeAI.__init__(self, air)
        self.avId = 0
        self.uniqueId = ''

    def setUniqueId(self, uid):
        self.uid = uid

    def getUniqueId(self):
        return self.uid

    def requestInteraction(self, avId, interactType, instant):
        if avId != self.air.getAvatarIdFromSender():
            self.air.writeServerEvent('suspicious', avId, 'tried to requestInteraction as someone else!')
            return

        if avId not in self.air.doId2do:
            self.air.writeServerEvent('suspicious', avId, 'tried to requestInteraction but not in shard!')
            return

        if self.avId and self.REJECT_IF_BUSY:
            self.sendUpdateToAvatarId(avId, 'rejectInteraction', [])
            return

        self.notify.debug('%d requested interaction.' % avId)

        result = self.handleInteract(avId, interactType, instant)
        if result & ACCEPT:
            if result & ACCEPT_SET_AV:
                self.setAvatar(avId)

            if result & ACCEPT_SEND_UPDATE:
                self.sendUpdateToAvatarId(avId, 'acceptInteraction', [])

        elif result & REJECT:
            self.sendUpdateToAvatarId(avId, 'rejectInteraction', [])

    def handleInteract(self, avId, interactType, instant):
        ''' Must be overwritten by subclasses '''
        return REJECT

    def d_offerOptions(self, optionsId, statusCodes):
        self.sendUpdateToAvatarId(self.avId, 'offerOptions', [optionIds, statusCodes])

    def selectOption(self, optionId):
        ''' Must be overwritten by subclasses '''
        pass

    def setAvatar(self, avId):
        self.ignore(self.air.getAvatarExitEvent(self.avId))
        self.avId = avId
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.setAvatar, [0])
        self.sendUpdate('setUserId', [self.avId])

    def requestExit(self):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.avId:
            self.air.writeServerEvent('suspicious', avId, 'tried to requestExit as someone else!')
            return

        self.doExit()

    def doExit(self):
        self.setAvatar(0)

    def demandExit(self):
        self.requestExit()

    def offerOptions(self, optionIds, statusCodes):
        self.optionIds = optionIds
        self.statusCodes = statusCodes

    def selectOption(self, optionId):
        self.optionId = optionId

    def d_selectOption(self, optionId):
        self.sendUpdate('selectOption', [optionId])

    def b_selectOption(self, optionId):
        self.selectOption(optionId)
        self.d_selectOption(optionId)

    def posControlledByIsland(self):
        return True

    @staticmethod
    def makeFromObjectKey(cls, air, objKey, data):
        obj = cls(air)
        obj.setUniqueId(objKey)
        obj.setPos(data.get('Pos', 0))
        obj.setHpr(data.get('Hpr', 0))
        return obj
