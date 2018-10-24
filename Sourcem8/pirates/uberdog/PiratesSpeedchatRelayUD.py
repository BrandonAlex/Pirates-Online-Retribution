from direct.directnotify import DirectNotifyGlobal
from otp.uberdog.SpeedchatRelayUD import SpeedchatRelayUD

class PiratesSpeedchatRelayUD(SpeedchatRelayUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("PiratesSpeedchatRelayUD")
