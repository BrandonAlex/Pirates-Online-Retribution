from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import globalClockDelta
from direct.directnotify import DirectNotifyGlobal
from TimeOfDayManagerBase import TimeOfDayManagerBase
from pirates.piratesbase import TODGlobals
from direct.distributed.ClockDelta import globalClockDelta
import TODGlobals
import time

class DistributedTimeOfDayManagerAI(DistributedObjectAI, TimeOfDayManagerBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTimeOfDayManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        TimeOfDayManagerBase.__init__(self)
        self.isPaused = False
        self.cycleType = TODGlobals.TOD_REGULAR_CYCLE
        self.cycleSpeed = 1
        self.tempTime = globalClockDelta.getFrameNetworkTime(bits = 32)
        self.startingNetTime = globalClockDelta.networkToLocalTime(self.tempTime)
        self.timeOffset = 0
        self.envSubEntry = []
        self.isJolly = 0

    def syncTOD(self, cycleType, cycleSpeed, startingNetTime, timeOffset):
        self.cycleType = cycleType
        self.cycleSpeed = cycleSpeed
        self.startingNetTime = startingNetTime
        self.timeOffset = timeOffset

    def getSyncTOD(self):
        return (self.cycleType, self.cycleSpeed, self.startingNetTime, self.timeOffset)

    def setIsPaused(self, isPaused):
        self.isPaused = isPaused

    def getIsPaused(self):
        return self.isPaused

    def requestSync(self):
        pass #TODO

    def setEnvSubs(self, envSubEntry):
        self.envSubEntry = envSubEntry

    def getEnvSubs(self):
        return self.envSubEntry

    def setMoonPhaseChange(self, fromCurrent, startPhase, targetPhase, targetTime):
        self.fromCurrent = fromCurrent
        self.startPhase = startPhase
        self.targetPhase = targetPhase
        self.targetTime = targetTime

    def getMoonPhaseChange(self):
        return (0, 0, 0, 0) #TODO!

    def setMoonJolly(self, isJolly):
        self.isJolly = isJolly

    def getMoonJolly(self):
        return self.isJolly
