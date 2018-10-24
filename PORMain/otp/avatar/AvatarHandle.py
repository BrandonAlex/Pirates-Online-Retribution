class AvatarHandle:
    dclassName = 'AvatarHandle'

    def getName(self):
        return ''

    def isOnline(self):
        return False

    def isUnderstandable(self):
        return True

    def setTalkWhisper(self, fromAV, avatarName, chat, mods, flags):
        newText, scrubbed = localAvatar.scrubTalk(chat, mods)
        base.talkAssistant.receiveWhisperTalk(fromAV, avatarName, newText)
