from otp.friends.FriendInfo import FriendInfo
from pirates.pirate.PAvatarHandle import PAvatarHandle

class PCFriendPlayerInfo(FriendInfo, PAvatarHandle):

    def makeFromFriendInfo(cls, info):
        out = cls()
        out.avatarName = info.avatarName
        out.playerName = info.playerName
        out.onlineYesNo = info.onlineYesNo
        out.openChatEnabledYesNo = info.openChatEnabledYesNo
        out.openChatFriendshipYesNo = info.openChatFriendshipYesNo
        out.understandableYesNo = info.understandableYesNo
        out.location = info.location
        out.sublocation = info.sublocation
        out.timestamp = info.timestamp
        out.avatarId = info.avatarId
        out.friendPrivs = info.friendPrivs
        out.tokenPrivs = info.tokenPrivs
        return out

    makeFromFriendInfo = classmethod(makeFromFriendInfo)

    def __init__(self, *args, **kw):
        FriendInfo.__init__(self, *args, **kw)
        self.bandId = None

    def setBandId(self, bandMgrId, bandId):
        if (bandMgrId, bandId) != (0, 0):
            self.bandId = (bandMgrId, bandId)
        else:
            self.bandId = None

    def getBandId(self):
        return self.bandId

    def sendTeleportQuery(self, sendToId, localBandMgrId, localBandId, localGuildId, localShardId):
        localAvatar.sendTeleportQuery(sendToId, localBandMgrId, localBandId, localGuildId, localShardId)

    def sendTeleportResponse(self, available, shardId, instanceDoId, areaDoId, sendToId = None):
        localAvatar.sendTeleportResponse(available, shardId, instanceDoId, areaDoId, sendToId)
