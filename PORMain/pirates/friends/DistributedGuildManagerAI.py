# STUB

from direct.directnotify import DirectNotifyGlobal
from otp.friends.GuildManagerAI import GuildManagerAI

class DistributedGuildManagerAI(GuildManagerAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGuildManagerAI')

    def __init__(self, air):
        GuildManagerAI.__init__(self, air)

    # sendSCQuest(uint16, uint8, uint16) clsend airecv

    # recvSCQuest(uint32, uint16, uint8, uint16)


