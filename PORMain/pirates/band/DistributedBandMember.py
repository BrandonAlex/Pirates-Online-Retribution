from direct.distributed.DistributedObject import DistributedObject
from pirates.band import BandConstance
from direct.directnotify.DirectNotifyGlobal import directNotify
from pirates.piratesbase import PLocalizer
from pirates.pirate.PAvatarHandle import PAvatarHandle
from otp.speedchat import SCDecoders
from pirates.speedchat import PSCDecoders
from pirates.piratesbase import PiratesGlobals
from otp.otpgui import OTPDialog

class DistributedBandMember(DistributedObject, PAvatarHandle):
    notify = directNotify.newCategory('BandMember')
    allBandmembers = { }
    band_map = { }
    ShipMessageDelay = 10

    def areSameCrew(cls, doId1, doId2):
        bm1 = cls.getBandMember(doId1)
        bm2 = cls.getBandMember(doId2)
        if bm1 and bm2:
            return bm1.bandId == bm2.bandId

    areSameCrew = classmethod(areSameCrew)

    def getBandMember(cls, doId):
        return cls.allBandmembers.get(doId)

    getBandMember = classmethod(getBandMember)

    def getBandSet(cls, doId):
        bm = cls.getBandMember(doId)
        if bm:
            return cls.band_map.get(bm.bandId, set())
        else:
            return set()

    getBandSet = classmethod(getBandSet)

    def getBandSetLocalAvatar(cls):
        return cls.getBandSet(localAvatar.doId)

    getBandSetLocalAvatar = classmethod(getBandSetLocalAvatar)

    def getLeaderNameLocalAvatar(cls):
        b_set = cls.getBandSetLocalAvatar()
        print '----------------------------'
        for b in b_set:
            print '----------------------------%s-%s' % (b.isManager, b.name)
            if b.isManager:
                return b.name
                continue

        print '---------------------------- Return None'

    getLeaderNameLocalAvatar = classmethod(getLeaderNameLocalAvatar)

    def IsAvatarHeadOfBand(cls, doId):
        br = cls.getBandMember(doId)
        if br:
            if not br.isManager:
                pass
            return br.isTempManager
        else:
            return 0

    IsAvatarHeadOfBand = classmethod(IsAvatarHeadOfBand)

    def IsLocalAvatarHeadOfBand(cls):
        return cls.IsAvatarHeadOfBand(base.cr.localAvatarDoId)

    IsLocalAvatarHeadOfBand = classmethod(IsLocalAvatarHeadOfBand)

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.avatarId = 0
        self.name = ''
        self.maxHp = 1
        self.hp = 0
        self.bandId = None
        self.shipId = None
        self.inPvp = 0
        self.inParlorGame = 0
        self.disconnect = 0
        self.isManager = 0
        self.isTempManager = 0
        self.shipInfo = [
            0,
            '',
            0,
            []]
        self.whiteListEnabled = base.config.GetBool('whitelist-chat-enabled', 1)
        self.TC = None
        self.shipMessageDoLater = None

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        messenger.send(BandConstance.BandMembershipChange, [
            self,
            0])
        messenger.send('CrewChange')

    def disable(self):
        if self.bandId:
            self.band_map[self.bandId].remove(self)
            if len(self.band_map[self.bandId]) <= 0:
                del self.band_map[self.bandId]

        if self.avatarId != 0 and self.avatarId in self.allBandmembers:
            del self.allBandmembers[self.avatarId]

        if self.shipMessageDoLater:
            taskMgr.remove(self.shipMessageDoLater)
            self.shipMessageDoLater = None

        messenger.send(BandConstance.BandMembershipChange, [
            self,
            1])
        messenger.send('CrewChange')
        DistributedObject.disable(self)

    def delete(self):
        self.avatarId = None
        DistributedObject.delete(self)

    def setAvatarId(self, avatarId):
        if self.avatarId != 0:
            del self.allBandmembers[avatarId]

        self.avatarId = avatarId
        self.allBandmembers[avatarId] = self

    def setName(self, name):
        self.name = name
        if self.isGenerated():
            messenger.send(BandConstance.BandMemberNameChange, [
                self,
                self.name])

    def setHp(self, hp):
        self.hp = hp
        if self.isGenerated():
            messenger.send(BandConstance.BandMemberHpChange, [
                self,
                self.hp,
                self.maxHp])

    def setMaxHp(self, maxHp):
        self.maxHp = maxHp
        if self.isGenerated():
            messenger.send(BandConstance.BandMemberHpChange, [
                self,
                self.hp,
                self.maxHp])

    def setBandId(self, manager, id):
        if self.bandId:
            self.band_map[self.bandId].remove(self)
            if len(self.band_map[self.bandId]) <= 0:
                del self.band_map[self.bandId]

        self.bandId = (manager, id)
        if self.bandId:
            self.band_map.setdefault(self.bandId, set()).add(self)

    def getBandId(self):
        return self.bandId

    def setPvp(self, value):
        self.inPvp = value
        messenger.send(BandConstance.BandMemberPVPChange, [
            self,
            value,
            self.avatarId])

    def setParlor(self, value):
        self.inParlorGame = value
        messenger.send(BandConstance.BandMemberParlorChange, [
            self,
            value,
            self.avatarId])

    def setDisconnect(self, value):
        self.disconnect = value
        if not self.inPvp:
            messenger.send(BandConstance.BandMemberOnlineChange, [
                self,
                value,
                self.avatarId])

    def setIsManager(self, flag):
        self.isManager = flag
        if self.isGenerated():
            messenger.send(BandConstance.BandMemberManagerChange, [
                self,
                flag])

    def setIsTempManager(self, flag):
        self.isTempManager = flag
        if self.isGenerated():
            messenger.send(BandConstance.BandMemberManagerChange, [
                self,
                flag])

    def setShipInfo(self, shipId, shipName, shipClass, mastInfo):
        self.shipInfo = [
            shipId,
            shipName,
            shipClass,
            mastInfo]
        if self.isGenerated:
            messenger.send(BandConstance.BandMemberShipChange, [
                self,
                shipId])

    def getShipInfo(self):
        return self.shipInfo

    def setShipHasSpace(self, hasSpace):
        self.shipHasSpace = hasSpace
        if self.isGenerated:
            messenger.send(BandConstance.BandMemberShipChange, [
                self,
                self.shipInfo[0]])

    def getShipHasSpace(self):
        if self.shipInfo[0] and self.shipHasSpace and localAvatar.getInventory():
            pass
        return self.shipInfo[0] in localAvatar.getInventory().getShipDoIdList()

    def setTalk(self, fromAV, avatarName, chat, mods, flags):
        (message, scrubbed) = localAvatar.scrubTalk(chat, mods)
        base.talkAssistant.receivePartyTalk(fromAV, avatarName, message)

    def setSpeedChat(self, senderId, msgIndex):
        if not self.cr.avatarFriendsManager.checkIgnored(self.avatarId):
            displayMess = '%s %s %s' % (self.name, PLocalizer.CrewPrefix, SCDecoders.decodeSCStaticTextMsg(msgIndex))
            message = SCDecoders.decodeSCStaticTextMsg(msgIndex)
            if message:
                base.talkAssistant.receivePartyMessage(senderId, self.name, message)

    def setSCQuestChat(self, senderId, questInt, msgType, taskNum):
        if not self.cr.avatarFriendsManager.checkIgnored(self.avatarId):
            displayMess = '%s %s %s' % (self.name, PLocalizer.CrewPrefix, PSCDecoders.decodeSCQuestMsgInt(questInt, msgType, taskNum))
            message = PSCDecoders.decodeSCQuestMsgInt(questInt, msgType, taskNum)
            base.talkAssistant.receivePartyMessage(senderId, self.name, message)

    def getName(self):
        return self.name

    def setMessage(self, fromAvatarId, message):
        if self.avatarId != fromAvatarId:
            print message

    def setShipDeployMessage(self, fromAvatarId, shipId, shipName, locationName, siege):
        self.shipId = shipId
        if self.avatarId != localAvatar.doId:
            self.shipMessageDoLater = taskMgr.doMethodLater(self.ShipMessageDelay, self.showShipDeployMessage, 'showShipDeployMessage', extraArgs = [
                shipName,
                locationName,
                siege])

    def showShipDeployMessage(self, shipName, locationName, siege):
        self.shipMessageDoLater = None
        if hasattr(base, 'localAvatar'):
            if siege:
                message = PLocalizer.OtherPrivShipIsBeingDeployed % (self.name, shipName, locationName)
            else:
                message = PLocalizer.OtherShipIsBeingDeployed % (self.name, shipName, locationName)
            localAvatar.guiMgr.messageStack.addModalTextMessage(message, seconds = 8, buttonStyle = OTPDialog.TwoChoice, yesCallback = self._DistributedBandMember__handleGotoShip, icon = ('ship', None))

    def removeShipDeployMessage(self, shipId):
        if self.shipId and self.shipId == shipId:
            if self.shipMessageDoLater:
                taskMgr.remove(self.shipMessageDoLater)
                self.shipMessageDoLater = None

            localAvatar.guiMgr.messageStack.removeShipMessage()
            self.shipId = None

    def setCrewHUDUpdate(self, numberOfNearByCrew, memberIcon):
        if self.avatarId != localAvatar.getDoId():
            localAvatar.guiMgr.crewHUD.updateActionIcons(self.avatarId, memberIcon[0], memberIcon[1], memberIcon[2])
        else:
            localAvatar.guiMgr.crewHUD.updateCrewNearBy(numberOfNearByCrew)

    def _DistributedBandMember__handleGotoShip(self):
        base.cr.teleportMgr.queryAvatarForTeleport(self.avatarId)

    def isOnline(self):
        return True

    def isUnderstandable(self):
        return True

    def sendTeleportQuery(self, sendToId, localBandMgrId, localBandId, localGuildId, localShardId):
        self.d_teleportQuery(localAvatar.doId, localGuildId, localShardId)

    def d_teleportQuery(self, localAvId, localGuildId, localShardId):
        self.sendUpdate('teleportQuery', [
            localAvId,
            localGuildId,
            localShardId])

    def sendTeleportResponse(self, available, shardId, instanceDoId, areaDoId, sendToId = None):
        self.d_teleportResponse(available, shardId, instanceDoId, areaDoId, sendToId)

    def d_teleportResponse(self, available, shardId, instanceDoId, areaDoId, sendToId):
        self.sendUpdate('teleportResponse', [
            localAvatar.doId,
            available,
            shardId,
            instanceDoId,
            areaDoId])

    def setLocation(self, parentId, zoneId, teleport = 0):
        if parentId != base.cr.PirateBandManager.doId:
            self.notify.warning('DistributedBandMember.setLocation : Parent ID does not match! parentId = %s, zoneId = %s' % (parentId, zoneId))
            printStack()

        DistributedObject.setLocation(self, parentId, zoneId)
