from direct.distributed.AstronInternalRepository import AstronInternalRepository
from otp.distributed.OtpDoGlobals import *

class PiratesInternalRepository(AstronInternalRepository):
    GameGlobalsId = OTP_DO_ID_PIRATES
    dbId = 4003

    def __init__(self, baseChannel, stateServer=None, dcFileNames=None,
                 dcSuffix='AI', connectMethod=None, threadedNet=None):
        AstronInternalRepository.__init__(
            self, baseChannel, serverId=stateServer, dcFileNames=dcFileNames,
            dcSuffix=dcSuffix, connectMethod=connectMethod, threadedNet=threadedNet)

    def getAvatarIdFromSender(self):
        return self.getMsgSender() & 0xFFFFFFFF

    def getAccountIdFromSender(self):
        return (self.getMsgSender()>>32) & 0xFFFFFFFF