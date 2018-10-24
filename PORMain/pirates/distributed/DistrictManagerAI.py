from pirates.distributed.DistributedPopulationTrackerAI import DistributedPopulationTrackerAI
from pirates.distributed.PiratesDistrictAI import PiratesDistrictAI
from otp.distributed import OtpDoGlobals
from pirates.piratesbase import PiratesGlobals


class DistrictManagerAI:
    POP_MIN = 50
    POP_MAX = 100

    def __init__(self, air):
        self.air = air

        self.population = 0

        self.district = None
        self.popTracker = None

    def generateDistrict(self):
        self.district = PiratesDistrictAI(self.air)
        self.district.setName(self.air.districtName)
        self.district.generateWithRequiredAndId(
            self.air.districtId, OtpDoGlobals.OTP_DO_ID_PIRATES, 2
        )

        self.popTracker = DistributedPopulationTrackerAI(self.air)
        self.popTracker.setShardId(self.air.districtId)
        self.popTracker.setPopulation(self.population)
        self.popTracker.setPopLimits([self.POP_MIN, self.POP_MAX])
        self.popTracker.generateWithRequiredAndId(
            self.air.allocateChannel(), OtpDoGlobals.OTP_DO_ID_PIRATES, 3
        )

    def openDistrict(self):
        self.district.b_setAvailable(1)

    def increasePopulation(self):
        self.population += 1

    def decreasePopulation(self):
        self.population -= 1
