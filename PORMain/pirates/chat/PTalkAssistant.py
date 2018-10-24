from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPGlobals, OTPLocalizer
from otp.chat.ChatGlobals import *
from otp.chat.TalkGlobals import *
from otp.chat.TalkAssistant import TalkAssistant
from pirates.speedchat import PSCDecoders
from pirates.piratesbase import PLocalizer

class PTalkAssistant(TalkAssistant):
    notify = DirectNotifyGlobal.directNotify.newCategory('PTalkAssistant')

    def __init__(self):
        TalkAssistant.__init__(self)
        self.SCDecoder = PSCDecoders

    def checkShipPVPTypedChat(self):
        return hasattr(localAvatar.ship, 'getSiegeTeam') and localAvatar.ship.getSiegeTeam() is not None

    def receivePartyTalk(self, avId, name, message):
        # TODO: Chat Log
        pass

    def receiveSystemMessage(self, message):
        base.localAvatar.guiMgr.messageStack.addTextMessage(message, seconds = 20, priority = 0, color = (0.5, 0, 0, 1), icon = ('admin', ''))
        TalkAssistant.receiveSystemMessage(self, message)

    def receivePartyMessage(self, avId, name, message):
        # TODO: Chat Log
        pass

    def receiveShipPVPMessage(self, fromAv, avatarName, teamName, message, scrubbed = 0):
        # TODO: Chat Log
        pass

    def sendPartyTalk(self, message):
        if base.localAvatar.bandMember:
            localAvatar.bandMember.sendTalk(0, '', message, 0, 0)

    def sendShipPVPCrewTalk(self, message):
        if self.checkShipPVPTypedChat():
            base.cr.distributedDistrict.siegeManager.sendTalk(message)

    def sendSCQuestChat(self, msgType, questInt, taskNum):
        messenger.send(SCQuestEvent)
        messenger.send('chatUpdateSCQuest', [questInt, msgType, taskNum])

    def sendPartySpeedChat(self, type, msgIndex):
        if base.localAvatar.bandMember:
            localAvatar.bandMember.b_setSpeedChat(msgIndex)

    def sendPartySCQuestChat(self, msgType, questInt, taskNum):
        if base.localAvatar.bandMember:
            localAvatar.bandMember.b_setSCQuestChat(questInt, msgType, taskNum)

    def sendGuildSCQuestChat(self, msgType, questInt, taskNum):
        if base.localAvatar.guildId:
            base.cr.guildManager.sendSCQuest(questInt, msgType, taskNum)

    def sendShipPVPCrewSpeedChat(self, type, msgIndex):
        if self.checkShipPVPTypedChat():
            base.cr.distributedDistrict.siegeManager.sendSC(msgIndex)

    def sendShipPVPCrewSCQuestChat(self, msgType, questInt, taskNum):
        if self.checkShipPVPTypedChat():
            base.cr.distributedDistrict.siegeManager.sendSCQuest(msgType, questInt, taskNum)

    def sendAvatarWhisperQuestSpeedChat(self, questInt, msgType, taskNum, receiverId):
        base.localAvatar.whisperSCQuestTo(questInt, msgType, taskNum, receiverId)
        message = PSCDecoders.decodeSCQuestMsgInt(questInt, msgType, taskNum)
        
        # TODO: Chat Log
        pass

    def receiveCannonDefenseMessage(self, avId, name, message):
        # TODO: Chat Log
        pass
