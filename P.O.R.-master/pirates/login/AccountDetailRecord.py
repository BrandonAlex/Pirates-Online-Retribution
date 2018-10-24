from pirates.piratesbase import PiratesGlobals
import os

class SubDetails:
    def __init__(self):
        self.subAccess = PiratesGlobals.AccessFull
        self.subName = os.getenv('LOGIN_COOKIE', '???')

class AccountDetailRecord:
    def __init__(self):
        self.WLChatEnabled = False
        self.playerAccountId = PiratesGlobals.PiratesSubId
        self.playerName = os.getenv('LOGIN_COOKIE', '???')
        self.subDetails = {self.playerAccountId: SubDetails()}

    def canOpenChatAndNotGetBooted(self):
        return True