from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.task import Task
from direct.distributed import DoInterestManager
from otp.distributed.OtpDoGlobals import *
_PiratesDistrictStatInterest = None
_PiratesDistrictStatInterestComplete = 0
_trashObject = DirectObject.DirectObject()

def EventName():
    return 'ShardPopulationSet'


def isOpen():
    global _PiratesDistrictStatInterest
    return _PiratesDistrictStatInterest is not None


def isComplete():
    global _PiratesDistrictStatInterestComplete
    return _PiratesDistrictStatInterestComplete


def open(event = None):
    global _trashObject
    global _PiratesDistrictStatInterest
    if not isOpen():

        def _CompleteProc(event):
            global _PiratesDistrictStatInterestComplete
            _PiratesDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            return

        _trashObject.acceptOnce(EventName(), _CompleteProc)
        _PiratesDistrictStatInterest = base.cr.addInterest(OTP_DO_ID_PIRATES, OTP_ZONE_ID_DISTRICTS_STATS, EventName(), EventName())
    elif isComplete():
        messenger.send(EventName())


def refresh(event = None):
    global _PiratesDistrictStatInterest
    if isOpen():
        if isComplete():
            messenger.send(EventName())
            if event is not none:
                messenger.send(event)
    else:

        def _CompleteProc(event):
            global _PiratesDistrictStatInterestComplete
            _PiratesDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            close()
            return

        _trashObject.acceptOnce(EventName(), _CompleteProc, [event])
        _PiratesDistrictStatInterest = base.cr.addInterest(OTP_DO_ID_PIRATES, OTP_ZONE_ID_DISTRICTS_STATS, EventName(), EventName())


def close():
    global _PiratesDistrictStatInterest
    global _PiratesDistrictStatInterestComplete
    if isOpen():
        _PiratesDistrictStatInterestComplete = 0
        base.cr.removeInterest(_PiratesDistrictStatInterest, None)
        _PiratesDistrictStatInterest = None
    return


class PiratesDistrictStats(DistributedObject.DistributedObject):
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.PiratesDistrictId = 0

    def setPiratesDistrictId(self, value):
        self.PiratesDistrictId = value

    def setAvatarCount(self, avatarCount):
        if self.PiratesDistrictId in self.cr.activeDistrictMap:
            self.cr.activeDistrictMap[self.PiratesDistrictId].avatarCount = avatarCount

    def setNewAvatarCount(self, newAvatarCount):
        if self.PiratesDistrictId in self.cr.activeDistrictMap:
            self.cr.activeDistrictMap[self.PiratesDistrictId].newAvatarCount = newAvatarCount

    def setStats(self, avatarCount, newAvatarCount):
        self.setAvatarCount(avatarCount)
        self.setNewAvatarCount(newAvatarCount)
