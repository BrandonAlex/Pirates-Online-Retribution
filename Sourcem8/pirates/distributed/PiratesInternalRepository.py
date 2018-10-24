from direct.distributed.AstronInternalRepository import AstronInternalRepository
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from otp.distributed.OtpDoGlobals import *

from PiratesNetMessengerAI import PiratesNetMessengerAI

class PiratesInternalRepository(AstronInternalRepository):
    GameGlobalsId = OTP_DO_ID_PIRATES
    dbId = 4003

    def __init__(self, baseChannel, serverId=None, dcFileNames=None,
                 dcSuffix='AI', connectMethod=None, threadedNet=None):
        if connectMethod is None:
            connectMethod = self.CM_NATIVE
        AstronInternalRepository.__init__(
            self, baseChannel, serverId=serverId, dcFileNames=dcFileNames,
            dcSuffix=dcSuffix, connectMethod=connectMethod, threadedNet=threadedNet)

    def getAvatarIdFromSender(self):
        return int(self.getMsgSender() & 0xFFFFFFFF)

    def getAccountIdFromSender(self):
        return int((self.getMsgSender()>>32) & 0xFFFFFFFF)

    def systemMessage(self, message, channel):
        msgDg = PyDatagram()
        msgDg.addUint16(6)
        msgDg.addString(message)

        dg = PyDatagram()
        dg.addServerHeader(channel, self.ourChannel, CLIENTAGENT_SEND_DATAGRAM)
        dg.addString(msgDg.getMessage())
        self.send(dg)

    def systemMsgAll(self, message):
        self.systemMessage(message, 10)

    def getApiKey(self):
        try:
            f = open('../deployment/site/api.key', 'rb')
            key = f.read()
            f.close()

            return key.strip()

        except:
            return 'dev'

    def handleConnected(self):
        self.__messenger = PiratesNetMessengerAI(self)

    def prepareMessage(self, message, sentArgs=[]):
        return self.__messenger.prepare(message, sentArgs)

    def sendNetEvent(self, message, sentArgs=[]):
        self.__messenger.send(message, sentArgs)

    def handleDatagram(self, di):
        msgType = self.getMsgType()

        if msgType == self.__messenger.msgType:
            self.__messenger.handle(msgType, di)
            return

        AstronInternalRepository.handleDatagram(self, di)

    def claimOwnership(self, channelId):
        datagram = PyDatagram()
        datagram.addServerHeader(channelId, self.ourChannel,
                                 STATESERVER_OBJECT_SET_AI)
        datagram.addChannel(self.ourChannel)
        self.send(datagram)

    def _isValidPlayerLocation(self, parentId, zoneId):
        parent = self.doId2do.get(parentId)
        if not parent:
            return False

        if hasattr(parent, 'isValidZone'):
            return parent.isValidZone(zoneId)

        return True

    def getAvatarExitEvent(self, avId):
        return 'distObjDelete-%d' % avId
