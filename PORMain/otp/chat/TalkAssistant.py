from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPGlobals, OTPLocalizer
from otp.speedchat import SCDecoders
from otp.chat.TalkGlobals import *
from otp.chat.ChatGlobals import *

ThoughtPrefix = '.'

class TalkAssistant(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TalkAssistant')

    def __init__(self):
        self.lastWhisper = None
        self.SCDecoder = SCDecoders

    def delete(self):
        self.ignoreAll()

    def start(self):
        pass

    def stop(self):
        pass

    def getCompleteTextFromRecent(self, numLines, startPoint = 0):
        return ''

    def getAllCompleteText(self):
        return []

    def findName(self, id):
        info = base.cr.identifyAvatar(id)
        return info.getName() if info else ''

    def isThought(self, message):
        return message is not None and len(message) <= 1 and ThoughtPrefix in message

    def removeThoughtPrefix(self, message):
        if self.isThought(message):
            return message[len(ThoughtPrefix):]
        else:
            return message

    def receiveWhisperTalk(self, avatarId, avatarName, message):
        # TODO: Chat Log
        pass

    def receiveGuildTalk(self, senderAvId, avatarName, message):
        # TODO: Chat Log
        pass

    def receiveGameMessage(self, message):
        # TODO: Chat Log
        pass

    def receiveSystemMessage(self, message):    
        # TODO: Chat Log
        pass

    def receiveGuildMessage(self, avId, name, message):
        # TODO: Chat Log
        pass

    def receiveGuildUpdateMessage(self, message, senderId, senderName, receiverId, receiverName, extraInfo = None):
        # TODO: Chat Log
        pass

    def receiveFriendUpdate(self, friendId, friendName, isOnline):
        if isOnline:
            onlineMessage = OTPLocalizer.FriendOnline
        else:
            onlineMessage = OTPLocalizer.FriendOffline
        
        # TODO: Chat Log
        pass

    def receiveGuildUpdate(self, memberId, memberName, isOnline):
        if base.cr.identifyFriend(memberId):
            return
        
        if isOnline:
            onlineMessage = OTPLocalizer.GuildMemberOnline
        else:
            onlineMessage = OTPLocalizer.GuildMemberOffline
        
        # TODO: Chat Log
        pass

    def receiveEmote(self, av, messageIndex):
        message = self.SCDecoder.decodeSCEmoteWhisperMsg(messageIndex, av.getName())
        
        # TODO: Chat Log
        pass

    def sendOpenTalk(self, message):
        try:
            message.encode('ascii')
        except UnicodeEncodeError:
            base.talkAssistant.receiveGameMessage("Non-ASCII messages are not permitted.")
            return

        if base.cr.wantMagicWords and len(message) > 0 and message[0] == '~':
            messenger.send('magicWord', [message])
        else:
            base.cr.chatAgent.sendChatMessage(message)

    def sendWhisperTalk(self, message, receiverAvId):
        # This is Pirates specific... which goes against all things OTP. But oh well.
        # Route through the PFMUD.
        base.cr.piratesFriendsManager.sendUpdate('sendTalkWhisper', [receiverAvId, message])

    def sendGuildTalk(self, message):
        if localAvatar.guildId:
            base.cr.guildManager.sendTalk(message)

    def sendOpenSpeedChat(self, type, messageIndex):
        if type == SPEEDCHAT_NORMAL:
            messenger.send(SCChatEvent)
            messenger.send('chatUpdateSC', [messageIndex])
            base.localAvatar.b_setSC(messageIndex)
        elif type == SPEEDCHAT_EMOTE:
            messenger.send('chatUpdateSCEmote', [messageIndex])
            messenger.send(SCEmoteChatEvent)
            base.localAvatar.b_setSCEmote(messageIndex)
        elif type == SPEEDCHAT_CUSTOM:
            messenger.send('chatUpdateSCCustom', [messageIndex])
            messenger.send(SCCustomChatEvent)
            base.localAvatar.b_setSCCustom(messageIndex)

    def sendAvatarWhisperSpeedChat(self, type, messageIndex, receiverId):
        if type == SPEEDCHAT_NORMAL:
            base.localAvatar.whisperSCTo(messageIndex, receiverId)
            message = self.SCDecoder.decodeSCStaticTextMsg(messageIndex)
        elif type == SPEEDCHAT_EMOTE:
            base.localAvatar.whisperSCEmoteTo(messageIndex, receiverId)
            message = self.SCDecoder.decodeSCEmoteWhisperMsg(messageIndex, localAvatar.getName())
        elif type == SPEEDCHAT_CUSTOM:
            base.localAvatar.whisperSCCustomTo(messageIndex, receiverId)
            message = self.SCDecoder.decodeSCCustomMsg(messageIndex)
        
        # TODO: Chat Log
        pass

    def sendGuildSpeedChat(self, type, msgIndex):
        if base.localAvatar.guildId:
            base.cr.guildManager.sendSC(msgIndex)

    def getWhisperReplyId(self):
        if self.lastWhisper:
            return self.lastWhisper

        return 0
