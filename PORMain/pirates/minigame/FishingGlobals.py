from panda3d.core import Point3, Vec3, Vec4
# File: F (Python 2.4)

from pirates.inventory import ItemGlobals
from pirates.piratesbase import PLocalizer
from pirates.uberdog.UberDogGlobals import InventoryType
from pirates.world.LocationConstants import LocationIds
from pirates.piratesbase import PiratesGlobals
from pirates.inventory import DropGlobals
import random
fishingRodScreenPosition = (-0.5, 0.0, 0.0)
struggleDangerThreshold = 5.0
maxStruggleTime = 15.0
struggleTimeDangerThreshold = 5.0
saveFishingRodAngle = -45.0
loseFishingRodAngle = 40.0
fishingRodInitSlope = 1.0
fishingRodInclineDegree = 0.100
humanPulledfishingRodBackDegree = 10.0
handleSpinningSpeed = 4.0
clickingRateThreshold = 1.0
fullyOffscreenXOffset = 30.0
ItemDropChance = 45
legendaryMusicIntroDuration = 2.0
legendaryFishArrivalDelay = 2.2
waveToLegendaryFishDuration = 5.0
cameraPosLegendaryFinal = Point3(-15.0, 0.0, 12.0)
cameraHprLegendaryFinal = Point3(-90.0, -10.0, 0.0)
legendaryFishShowDuration = 5.0
wantDebugCollisionVisuals = False
legendaryTransitionTextDuration = 1.60
legendaryFishShowChance = 0.0299
timeBetweenLegendaryFishTests = 5.0
ROD_JOURNEYMAN_COST = 1000
ROD_MASTER_COST = 10000
lurePositionRangesForLegendaryFishingGame = {
    'xRange': (45.0, 80.0),
    'zRange': (-40.0, -75.0) }
staminaReduceValue = 0.02
fishingStaminaBarColor = [
    (1.0, 0.0, 0.0, 0.696),
    (1.0, 0.5, 0.0, 0.696),
    (1.0, 1.0, 0.0, 0.696),
    (0.0, 1.0, 0.0, 0.696),
    (0.0, 1.0, 0.0, 0.696)]
legendaryFishingReelingSpeedMultiplier = (9, 0, 5.78)
todBackdropColor = {
    PiratesGlobals.TOD_BASE: [
        Vec4(0.5, 0.5, 0.5, 1),
        Vec4(0.5, 0.5, 0.5, 1),
        Vec4(0.5, 0.5, 0.5, 1),
        Vec4(0.5, 0.5, 0.5, 1)],
    PiratesGlobals.TOD_DAWN: [
        Vec4(0.100, 0.179, 0.28000, 1),
        Vec4(0.550000, 0.576, 0.565, 1),
        Vec4(0.38, 0.348, 0.4, 1),
        Vec4(0.848, 0.65, 0.598, 1)],
    PiratesGlobals.TOD_DAY: [
        Vec4(0.16, 0.348, 0.5, 1),
        Vec4(0.800000, 1, 0.9, 1),
        Vec4(0.52, 0.63, 0.696, 1),
        Vec4(1, 0.88, 0.815, 1)],
    PiratesGlobals.TOD_DUSK: [
        Vec4(0.100, 0.149, 0.299, 1),
        Vec4(0.33, 0.299, 0.320, 1),
        Vec4(0.299, 0.22, 0.28000, 1),
        Vec4(0.5, 0.33, 0.4, 1)],
    PiratesGlobals.TOD_NIGHT: [
        Vec4(0.0598, 0.140, 0.299, 1),
        Vec4(0.12, 0.299, 0.450, 1),
        Vec4(0.100, 0.179, 0.418, 1),
        Vec4(0.22, 0.299, 0.5, 1)],
    PiratesGlobals.TOD_STARS: [
        Vec4(0.0400, 0.12, 0.299, 1),
        Vec4(0.100, 0.25, 0.4, 1),
        Vec4(0.100, 0.149, 0.348, 1),
        Vec4(0.299, 0.28000, 0.44, 1)],
    PiratesGlobals.TOD_HALLOWEEN: [
        Vec4(0.050000, 0.200, 0.348, 1),
        Vec4(0.149, 0.299, 0.348, 1),
        Vec4(0.100, 0.170, 0.299, 1),
        Vec4(0.25, 0.320, 0.450, 1)],
    PiratesGlobals.TOD_FULLMOON: [
        Vec4(0.050000, 0.200, 0.348, 1),
        Vec4(0.149, 0.299, 0.348, 1),
        Vec4(0.100, 0.170, 0.299, 1),
        Vec4(0.25, 0.320, 0.450, 1)],
    PiratesGlobals.TOD_HALFMOON: [
        Vec4(0.050000, 0.200, 0.348, 1),
        Vec4(0.149, 0.299, 0.348, 1),
        Vec4(0.100, 0.170, 0.299, 1),
        Vec4(0.25, 0.320, 0.450, 1)],
    PiratesGlobals.TOD_HALFMOON2: [
        Vec4(0.050000, 0.200, 0.348, 1),
        Vec4(0.149, 0.299, 0.348, 1),
        Vec4(0.100, 0.170, 0.299, 1),
        Vec4(0.25, 0.320, 0.450, 1)],
    PiratesGlobals.TOD_JOLLYINVASION: [
        Vec4(0.050000, 0.200, 0.348, 1),
        Vec4(0.149, 0.299, 0.348, 1),
        Vec4(0.100, 0.170, 0.299, 1),
        Vec4(0.25, 0.320, 0.450, 1)] }
resetTutorialCount = 2
fishSizeToHelpTextScale = {
    'small': 0.4,
    'medium': 0.696,
    'large': 1.0,
    'super': 1.0 }
fightWarningDurations = {
    'small': 0.299,
    'medium': 0.200,
    'large': 0.200,
    'super': 0.200 }
fishToLureHprOffset = (20.0, -60.0, 55.0)
biteWindowStartPercentage = 0.4
biteWindowFinishPercentage = 0.66000
leftFishBarrier = 0
rightFishBarrier = 85.0
leftLureBarrier = 12
rightLureBarrier = 90.0
maxCastDistance = 90.0
fishingSpotPosOffset = (5.46342, -1.46449, 0)
oceanEyeTransitionDuration = 0.5
oceanEyeCameraPosition = (40.0, -70.0, -40.0)
raritySpawnChances = (0.65, 0.25, 0.100)
rodSizeOverride = None
lureSinkingAngles = {
    'Cast': -110.0,
    'Fishing': -40.0,
    'Reeling': -70.0,
    'QuickReel': -90.0 }
fishCountRangePerRodPerLevel = {
    ItemGlobals.FISHING_ROD_1: ((12, 16), (5, 7), (5, 7)),
    ItemGlobals.FISHING_ROD_2: ((8, 10), (10, 12), (5, 7)),
    ItemGlobals.FISHING_ROD_3: ((5, 8), (5, 7), (5, 7)) }
fishSpawnBelowWaterLevelHeight = -3.0
fishingLevelBoundaries = (-33.0, -53.0, -70.0)
fishingLevelBoundariesBoat = (-55.0, -73.0, -90.0)
waterLevelOffset = {
    'land': -4.0,
    'boat': -14.0 }
castDistanceMultiplier = {
    ItemGlobals.FISHING_ROD_1: 0.299,
    ItemGlobals.FISHING_ROD_2: 0.5,
    ItemGlobals.FISHING_ROD_3: 0.696 }
minimumCastDistance = 15.0
minimumCastDistanceOnABoat = 30.0
resetDuration = 0.5
idleDuration = 300
fishAttractionOffset = 1.5
defaultFishingLineColor = Vec4(1.0, 1.0, 1.0, 0.696)
fishingLineHealthToColor = [
    (1.0, 0.0, 0.0, 0.696),
    (1.0, 0.5, 0.0, 0.696),
    (1.0, 1.0, 0.0, 0.696),
    (0.0, 1.0, 0.0, 0.696),
    (0.0, 1.0, 0.0, 0.696)]
fishingLineThickness = 1.5
defaultFishBlendTime = 0.4
fishBlendTimeDict = { }
fishAvoidYVelocity = 1.0
fleeDuration = 3.0
lureFlightDuration = {
    'fsh_bigCast': 0.800000,
    'fsh_smallCast': 0.4 }
lureTypeToModel = {
    'regular': 'models/minigames/pir_m_gam_fsh_regLure.bam',
    'legendary': 'models/minigames/pir_m_gam_fsh_legendLure.bam' }
lureTypeToAttractRadius = {
    'regular': 2.0,
    'legendary': 2.0 }
cameraMovementTolerance = 1.0
unlockLevelToSkillId = {
    3: InventoryType.FishingRodStall,
    4: InventoryType.FishingRodPull,
    6: InventoryType.FishingRodHeal,
    13: InventoryType.FishingRodTug,
    16: InventoryType.FishingRodSink,
    17: InventoryType.FishingRodOceanEye }
skillIdToTutorialId = {
    InventoryType.FishingRodStall: InventoryType.FishingStall,
    InventoryType.FishingRodPull: InventoryType.FishingPull,
    InventoryType.FishingRodHeal: InventoryType.FishingHealLine,
    InventoryType.FishingRodSink: InventoryType.FishingSink,
    InventoryType.FishingRodOceanEye: InventoryType.FishingOceanEye }
castReleaseDelay = {
    'fsh_bigCast': 0.88,
    'fsh_smallCast': 0.83 }
stateToCameraOffsetInfo = {
    'PlayerIdle': (Point3(7.0, -16.0, 4.0), False, False),
    'ChargeCast': (Point3(7.0, -16.0, 4.0), False, False),
    'Cast': [
        Point3(7.0, -32.0, 4.0),
        False,
        False],
    'Fishing': (Point3(7.0, -25.0, 4.0), False, True),
    'Reeling': (Point3(7.0, -25.0, 4.0), False, True),
    'QuickReel': (Point3(7.0, -25.0, 4.0), False, True),
    'FishBiting': (Point3(7.0, -10.0, 4.0), False, True),
    'FishOnHook': (Point3(7.0, -10.0, 4.0), True, False),
    'ReelingFish': (Point3(7.0, -10.0, 4.0), True, False),
    'FishFighting': (Point3(7.0, -10.0, 4.0), True, False),
    'LegendaryFish': (Point3(7.0, -25.0, 4.0), False, True),
    'Lose': (Point3(7.0, -16.0, 4.0), False, True),
    'Reward': (Point3(9.5, -16.0, 4.0), False, False),
    'PulledIn': (Point3(7.0, -16.0, 4.0), False, False),
    'Recap': (Point3(7.0, -16.0, 4.0), False, False),
    'LureStall': (Point3(7.0, -25.0, 4.0), False, True),
    'LureSink': (Point3(7.0, -25.0, 4.0), False, True),
    'FishPullingLure': (Point3(7.0, -16.0, 4.0), True, False),
    'Pause': (Point3(7.0, -25.0, 4.0), False, True) }
waterFogColor = Vec4(0.0299, 0.0299, 0.200, 1.0)
fogDarkness = 100.0
boatSpotIndexToCameraOffset = {
    0: Point3(6.0, -2.0, 3.0),
    3: Point3(6.0, -2.0, 3.0),
    5: Point3(6.0, -2.0, 3.0),
    1: Point3(6.0, -2.0, 3.0),
    2: Point3(6.0, -2.0, 3.0),
    4: Point3(6.0, -2.0, 3.0) }
fishingSpotPosHprBoatInformation = [
    {
        'pos': (-28, 18, 24.75),
        'hpr': (83, 0, 0),
        'fishingSpotHpr': (180, 0, 0) },
    {
        'pos': (27.5, 18, 24.75),
        'hpr': (-82.4, 0, 0),
        'fishingSpotHpr': (0, 0, 0) },
    {
        'pos': (30.1, -10.9, 25),
        'hpr': (-87.2, 0, 0.5),
        'fishingSpotHpr': (0, 0, 0) },
    {
        'pos': (-30.5, -11, 25),
        'hpr': (90.2, 0, -0.696),
        'fishingSpotHpr': (180, 0, 0) },
    {
        'pos': (18, 44.5, 27),
        'hpr': (-68.5, -8.63, 0.230),
        'fishingSpotHpr': (20, 0, 0) },
    {
        'pos': (-18.5, 43.5, 26.8),
        'hpr': (63.2, -6.7, 0.4),
        'fishingSpotHpr': (140, 0, 0) }]
lureVelocities = {
    'Fishing': Vec3(-0.800000, 0.0, -1.5),
    'Reeling': Vec3(-6.0, 0.0, 4.0),
    'FishOnHook': Vec3(0.0, 0.0, -0.598),
    'ReelingFish': Vec3(-6.0, 0.0, 4.0),
    'FishFighting': Vec3(0.299, 0.0, 0.0),
    'QuickReel': Vec3(-18.0, 0.0, 18.0),
    'Lose': Vec3(-18.0, 0.0, 18.0),
    'LureStall': Vec3(0.0, 0.0, 0.0),
    'LureSink': Vec3(0.0, 0.0, -5.0),
    'LegdFishShow': Vec3(-0.800000, 0.0, -1.5),
    'CatchIt': Vec3(1.5, 0.0, -1.25) }
rewardSequenceReelItInDuration = 1.0
fishYTolerance = 0.100
maxLineHealth = 100.0
fishingLevelToHealAmount = {
    1: 1.0,
    2: 1.0,
    3: 1.0,
    4: 1.0,
    5: 1.0,
    6: 25.0,
    7: 25.0,
    8: 25.0,
    9: 25.0,
    10: 25.0,
    11: 25.0,
    12: 50.0,
    13: 50.0,
    14: 50.0,
    15: 50.0,
    16: 50.0,
    17: 50.0,
    18: 50.0,
    19: 75.0,
    20: 75.0 }
fishingLevelToReelSpeed = {
    1: 0.75,
    2: 1.0,
    3: 1.0,
    4: 1.0,
    5: 1.0,
    6: 1.0,
    7: 1.14,
    8: 1.14,
    9: 1.14,
    10: 1.14,
    11: 1.25,
    12: 1.25,
    13: 1.25,
    14: 1.5,
    15: 1.5,
    16: 1.5,
    17: 1.5,
    18: 1.75,
    19: 1.75,
    20: 1.75 }
fishingLevelToPullSpeedBoost = {
    1: 1.0,
    2: 1.0,
    3: 1.0,
    4: 1.5,
    5: 1.5,
    6: 1.5,
    7: 1.5,
    8: 1.5,
    9: 2.0,
    10: 2.0,
    11: 2.0,
    12: 2.0,
    13: 2.0,
    14: 2.0,
    15: 2.0,
    16: 2.0,
    17: 2.0,
    18: 2.0,
    19: 2.5,
    20: 2.5 }
fishingLevelToStallDuration = {
    1: 1.0,
    2: 1.0,
    3: 4.0,
    4: 4.0,
    5: 4.0,
    6: 4.0,
    7: 4.0,
    8: 6.0,
    9: 6.0,
    10: 6.0,
    11: 6.0,
    12: 6.0,
    13: 6.0,
    14: 6.0,
    15: 6.0,
    16: 6.0,
    17: 6.0,
    18: 6.0,
    19: 6.0,
    20: 6.0 }
lureSinkDuration = 3.0
oceanEyeDuration = 5.0
pullDuration = 3.0
lureHelpTextDuration = 2.0
fishAnimations = [
    'bite',
    'fightIdle',
    'reelIdle',
    'swimIdle',
    'turn',
    'turnOpposite',
    'swimIdleOpposite',
    'biteOpposite']
baseFishVelocity = Vec3(0.5, 0.0, 0.0)
baseFishAccel = Vec3(0.0, 0.0, 0.0)
scareAwayVelocityMultiplier = 7.0
fleeVelocityMultiplier = 2.0
makeAllFishOneFishOverride = False
loadOneOfEachFish = False
maxFishWeight = 830
allFishData = [
    {
        'id': InventoryType.Collection_Set10_Part1,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part1],
        'model': 'smComTang',
        'rarity': 0,
        'depth': 0,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (4, 8),
        'strength': 1,
        'speed': 3,
        'experience': 10,
        'gold': 3.0 / 7.0,
        'location': 'both',
        'maxPossiblePerScene': 8,
        'behaviorDict': {
            'name': 'erratic',
            'chanceOfTurning': 0.100,
            'sineMultiplier': 0.299,
            'secondsBetweenChanges': 6.0 },
        'fightDurationRange': (1, 3),
        'restDurationRange': (2, 3),
        'attractionRadius': 2.0,
        'collisionBoxOffset': (0.0, 0.0, 0.0),
        'collisionBoxSize': (2.0, 1.0, 2.0),
        'indicatorHeightOffset': 0.598,
        'size': 'small',
        'swimAnimationMultiplier': 0.4,
        'durationOfFishTurn': 1.7,
        'turnAnimationMultiplier': 0.28000 },
    {
        'id': InventoryType.Collection_Set10_Part2,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part2],
        'model': 'smComChub',
        'rarity': 0,
        'depth': 0,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (8, 12),
        'strength': 1,
        'speed': 2,
        'experience': 15,
        'gold': 5.0 / 10.0,
        'location': 'both',
        'maxPossiblePerScene': 8,
        'restDurationRange': (1, 3),
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'fightDurationRange': (1, 3),
        'attractionRadius': 1.5,
        'collisionBoxOffset': (-0.5, 0.0, 0.0),
        'collisionBoxSize': (2.2, 1.0, 1.5),
        'indicatorHeightOffset': 0.598,
        'size': 'small',
        'swimAnimationMultiplier': 0.38,
        'durationOfFishTurn': 1.89,
        'turnAnimationMultiplier': 0.4 },
    {
        'id': InventoryType.Collection_Set10_Part3,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part3],
        'model': 'smComChromis',
        'rarity': 0,
        'depth': 0,
        'scaleRange': (1.39, 1.8),
        'weightRange': (3, 8),
        'strength': 2,
        'speed': 4,
        'experience': 20,
        'gold': 7.0 / 5.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 6,
        'restDurationRange': (1, 3),
        'fightDurationRange': (1, 3),
        'attractionRadius': 1.0,
        'collisionBoxOffset': (0.0, 0.0, 0.0),
        'collisionBoxSize': (3.0, 1.0, 1.5),
        'indicatorHeightOffset': 0.598,
        'size': 'small',
        'swimAnimationMultiplier': 0.299,
        'durationOfFishTurn': 1.75,
        'turnAnimationMultiplier': 0.200 },
    {
        'id': InventoryType.Collection_Set10_Part4,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part4],
        'model': 'smComAnthias',
        'rarity': 0,
        'depth': 0,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (15, 25),
        'strength': 3,
        'speed': 5,
        'experience': 50,
        'gold': 10.0 / 20.0,
        'location': 'ship',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 6,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 1.0,
        'collisionBoxOffset': (-0.200, 0.0, 0.0),
        'collisionBoxSize': (2.78, 1.0, 1.5),
        'indicatorHeightOffset': 0.598,
        'size': 'small',
        'swimAnimationMultiplier': 0.179,
        'durationOfFishTurn': 1.5,
        'turnAnimationMultiplier': 0.19 },
    {
        'id': InventoryType.Collection_Set10_Part5,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part5],
        'model': 'mdComTuna',
        'rarity': 0,
        'depth': 1,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (150, 200),
        'strength': 3,
        'speed': 6,
        'experience': 50,
        'gold': 25.0 / 175.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'erratic',
            'chanceOfTurning': 0.200,
            'sineMultiplier': 0.299,
            'secondsBetweenChanges': 6.0 },
        'maxPossiblePerScene': 4,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (0.0, 0.0, 0.0),
        'collisionBoxSize': (6.0, 1.0, 3.0),
        'indicatorHeightOffset': 0.598,
        'size': 'medium',
        'swimAnimationMultiplier': 0.200,
        'durationOfFishTurn': 0.598,
        'turnAnimationMultiplier': 0.11 },
    {
        'id': InventoryType.Collection_Set10_Part6,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part6],
        'model': 'mdComParrot',
        'rarity': 0,
        'depth': 1,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (100, 120),
        'strength': 3,
        'speed': 3,
        'experience': 65,
        'gold': 30.0 / 110.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 4,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-0.299, 0.0, 0.0),
        'collisionBoxSize': (6.0, 1.0, 3.0),
        'indicatorHeightOffset': 0.598,
        'size': 'medium',
        'swimAnimationMultiplier': 0.22,
        'durationOfFishTurn': 0.78000,
        'turnAnimationMultiplier': 0.22 },
    {
        'id': InventoryType.Collection_Set10_Part7,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part7],
        'model': 'mdComBarracuda',
        'rarity': 0,
        'depth': 1,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (200, 280),
        'strength': 4,
        'speed': 5,
        'experience': 100,
        'gold': 50.0 / 240.0,
        'location': 'ship',
        'behaviorDict': {
            'name': 'erratic',
            'chanceOfTurning': 0.299,
            'sineMultiplier': 0.299,
            'secondsBetweenChanges': 6.0 },
        'maxPossiblePerScene': 4,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.0, 0.0, 0.0),
        'collisionBoxSize': (10.0, 1.0, 3.0),
        'indicatorHeightOffset': 0.598,
        'size': 'medium',
        'swimAnimationMultiplier': 0.170,
        'durationOfFishTurn': 0.800000,
        'turnAnimationMultiplier': 0.200 },
    {
        'id': InventoryType.Collection_Set10_Part8,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part8],
        'model': 'lgComMarlin',
        'rarity': 1,
        'depth': 2,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (75, 125),
        'strength': 4,
        'speed': 7,
        'experience': 125,
        'gold': 75.0 / 100.0,
        'location': 'ship',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 4,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (0.0, 0.0, 0.0),
        'collisionBoxSize': (15.0, 1.0, 4.0),
        'indicatorHeightOffset': 0.598,
        'size': 'large',
        'swimAnimationMultiplier': 0.179,
        'durationOfFishTurn': 1.0,
        'turnAnimationMultiplier': 0.170 },
    {
        'id': InventoryType.Collection_Set10_Part9,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part9],
        'model': 'lgComTshark',
        'rarity': 0,
        'depth': 2,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (400, 550),
        'strength': 4,
        'speed': 5,
        'experience': 125,
        'gold': 80.0 / 150.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 2,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-2.0, 0.0, 0.0),
        'collisionBoxSize': (14.0, 2.0, 4.5),
        'indicatorHeightOffset': 1.5,
        'size': 'large',
        'swimAnimationMultiplier': 0.170,
        'durationOfFishTurn': 1.39,
        'turnAnimationMultiplier': 0.170 },
    {
        'id': InventoryType.Collection_Set10_Part10,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part10],
        'model': 'smUncomGrouper',
        'rarity': 2,
        'depth': 0,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (4, 8),
        'strength': 5,
        'speed': 1,
        'experience': 35,
        'gold': 45.0 / 5.0,
        'location': 'both',
        'maxPossiblePerScene': 2,
        'restDurationRange': (1, 2),
        'behaviorDict': {
            'name': 'erratic',
            'chanceOfTurning': 0.4,
            'sineMultiplier': 0.299,
            'secondsBetweenChanges': 6.0 },
        'fightDurationRange': (1, 4),
        'attractionRadius': 1.0,
        'collisionBoxOffset': (0.0, 0.0, 0.0),
        'collisionBoxSize': (3.0, 1.0, 1.0),
        'indicatorHeightOffset': 0.598,
        'size': 'small',
        'swimAnimationMultiplier': 0.696,
        'durationOfFishTurn': 0.9,
        'turnAnimationMultiplier': 0.696 },
    {
        'id': InventoryType.Collection_Set10_Part11,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part11],
        'model': 'lgComCoelacanth',
        'rarity': 0,
        'depth': 2,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (400, 500),
        'strength': 4,
        'speed': 4,
        'experience': 60,
        'gold': 80.0 / 450.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 3,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.0, 0.0, 0.0),
        'collisionBoxSize': (13.0, 1.0, 5.0),
        'indicatorHeightOffset': 0.598,
        'size': 'large',
        'swimAnimationMultiplier': 0.27,
        'durationOfFishTurn': 1.5,
        'turnAnimationMultiplier': 0.200 },
    {
        'id': InventoryType.Collection_Set10_Part12,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part12],
        'model': 'smUncomHatchet',
        'rarity': 1,
        'depth': 0,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (4, 8),
        'strength': 3,
        'speed': 5,
        'experience': 30,
        'gold': 20.0 / 5.0,
        'location': 'both',
        'maxPossiblePerScene': 4,
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 4),
        'attractionRadius': 1.0,
        'collisionBoxOffset': (0.0, 0.0, 0.0),
        'collisionBoxSize': (2.5, 1.0, 1.0),
        'indicatorHeightOffset': 0.598,
        'size': 'small',
        'swimAnimationMultiplier': 0.4,
        'durationOfFishTurn': 1.0,
        'turnAnimationMultiplier': 0.260 },
    {
        'id': InventoryType.Collection_Set10_Part13,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part13],
        'model': 'mdUncomLion',
        'rarity': 1,
        'depth': 1,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (70, 85),
        'strength': 3,
        'speed': 4,
        'experience': 75,
        'gold': 40.0 / 80.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'erratic',
            'chanceOfTurning': 0.100,
            'sineMultiplier': 0.299,
            'secondsBetweenChanges': 6.0 },
        'maxPossiblePerScene': 4,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.0, 0.0, 0.0),
        'collisionBoxSize': (5.0, 1.0, 3.0),
        'indicatorHeightOffset': 0.598,
        'size': 'medium',
        'swimAnimationMultiplier': 0.28000,
        'durationOfFishTurn': 1.5,
        'turnAnimationMultiplier': 0.239 },
    {
        'id': InventoryType.Collection_Set10_Part14,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part14],
        'model': 'mdUncomWolf',
        'rarity': 1,
        'depth': 1,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (110, 190),
        'strength': 4,
        'speed': 3,
        'experience': 100,
        'gold': 45.0 / 150.0,
        'location': 'ship',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 4,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.0, 0.0, 0.0),
        'collisionBoxSize': (6.0, 1.0, 3.0),
        'indicatorHeightOffset': 0.598,
        'size': 'medium',
        'swimAnimationMultiplier': 0.299,
        'durationOfFishTurn': 0.800000,
        'turnAnimationMultiplier': 0.27 },
    {
        'id': InventoryType.Collection_Set10_Part15,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part15],
        'model': 'mdUncomChimera',
        'rarity': 2,
        'depth': 1,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (200, 250),
        'strength': 3,
        'speed': 4,
        'experience': 150,
        'gold': 65.0 / 225.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 3,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.5, 0.0, 0.0),
        'collisionBoxSize': (7.0, 1.0, 3.0),
        'indicatorHeightOffset': 0.598,
        'size': 'medium',
        'swimAnimationMultiplier': 0.260,
        'durationOfFishTurn': 0.800000,
        'turnAnimationMultiplier': 0.200 },
    {
        'id': InventoryType.Collection_Set10_Part16,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part16],
        'model': 'mdUncomDragon',
        'rarity': 2,
        'depth': 1,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (180, 240),
        'strength': 4,
        'speed': 6,
        'experience': 200,
        'gold': 70.0 / 210.0,
        'location': 'ship',
        'behaviorDict': {
            'name': 'erratic',
            'chanceOfTurning': 0.4,
            'sineMultiplier': 0.299,
            'secondsBetweenChanges': 6.0 },
        'maxPossiblePerScene': 4,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.0, 0.0, 0.0),
        'collisionBoxSize': (9.0, 1.0, 3.0),
        'indicatorHeightOffset': 0.598,
        'size': 'medium',
        'swimAnimationMultiplier': 0.179,
        'durationOfFishTurn': 0.800000,
        'turnAnimationMultiplier': 0.140 },
    {
        'id': InventoryType.Collection_Set10_Part17,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part17],
        'model': 'lgUncomGoblin',
        'rarity': 1,
        'depth': 2,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (650, 830),
        'strength': 4,
        'speed': 3,
        'experience': 220,
        'gold': 125.0 / 740.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 2,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 2.0,
        'collisionBoxOffset': (-1.5, 0.0, 0.0),
        'collisionBoxSize': (18.0, 1.0, 4.5),
        'indicatorHeightOffset': 2.5,
        'size': 'large',
        'swimAnimationMultiplier': 0.348,
        'durationOfFishTurn': 1.5,
        'turnAnimationMultiplier': 0.239 },
    {
        'id': InventoryType.Collection_Set10_Part18,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part18],
        'model': 'lgUncomAngler',
        'rarity': 2,
        'depth': 2,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (300, 400),
        'strength': 5,
        'speed': 3,
        'experience': 250,
        'gold': 175.0 / 350.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 2,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (0.0, 0.0, 0.0),
        'collisionBoxSize': (8.0, 1.0, 4.0),
        'indicatorHeightOffset': 0.696,
        'size': 'large',
        'swimAnimationMultiplier': 0.27,
        'durationOfFishTurn': 1.60,
        'turnAnimationMultiplier': 0.260 },
    {
        'id': InventoryType.Collection_Set10_Part19,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part19],
        'model': 'lgUncomLump',
        'rarity': 2,
        'depth': 2,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (300, 400),
        'strength': 5,
        'speed': 2,
        'experience': 275,
        'gold': 120.0 / 350.0,
        'location': 'both',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 2,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 2.0,
        'collisionBoxOffset': (-1.0, 0.0, 0.0),
        'collisionBoxSize': (7.0, 1.0, 4.0),
        'indicatorHeightOffset': 0.696,
        'size': 'large',
        'swimAnimationMultiplier': 0.4,
        'durationOfFishTurn': 1.8,
        'turnAnimationMultiplier': 0.299 },
    {
        'id': InventoryType.Collection_Set10_Part20,
        'name': PLocalizer.Collections[InventoryType.Collection_Set10_Part20],
        'model': 'lgUncomMega',
        'rarity': 2,
        'depth': 2,
        'scaleRange': (0.800000, 1.2),
        'weightRange': (600, 800),
        'strength': 6,
        'speed': 4,
        'experience': 300,
        'gold': 130.0 / 700.0,
        'location': 'ship',
        'behaviorDict': {
            'name': 'sineStraight',
            'sineMultiplier': 0.299 },
        'maxPossiblePerScene': 1,
        'restDurationRange': (2, 4),
        'fightDurationRange': (1, 3),
        'attractionRadius': 2.0,
        'collisionBoxOffset': (-2.7, 0.0, 0.0),
        'collisionBoxSize': (16.0, 2.0, 4.5),
        'indicatorHeightOffset': 0.800000,
        'size': 'large',
        'swimAnimationMultiplier': 0.27,
        'durationOfFishTurn': 1.39,
        'turnAnimationMultiplier': 0.22 }]
legendaryFishData = [
    {
        'id': InventoryType.Collection_Set11_Part1,
        'name': PLocalizer.Collections[InventoryType.Collection_Set11_Part1],
        'model': 'lgLegFogbell',
        'type': 'uncommon',
        'chanceThisFishAppears': 0.200,
        'chanceItWillMakeABreakForIt': 0.4,
        'scaleRange': (1.0, 1.0),
        'weightRange': (7, 8),
        'strength': 7,
        'speed': 4.0,
        'swimAnimationMultiplier': 1.0 / 4.0,
        'durationOfFishTurn': 0.0,
        'turnAnimationMultiplier': 1.0 / 4.0,
        'hookRadius': 1,
        'experience': 0,
        'gold': 1000,
        'lure': 'special',
        'rod': 'special',
        'location': 'deepSea',
        'lureInterestTime': 1.0,
        'behaviorDict': {
            'name': 'straight',
            'sineMultiplier': 0.299 },
        'gullibilityStaticLure': 0.100,
        'gullibilityMovingLure': 0.100,
        'restDurationRange': (3.5, 5.0),
        'fightDurationRange': (1.5, 2.5),
        'pullDurationRange': (3.5, 5),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.7, 0.0, 0.0),
        'collisionBoxSize': (12.0, 2.0, 3.0),
        'indicatorHeightOffset': 0.800000,
        'size': 'super',
        'indicatorHeightOffset': 1.0,
        'habitat': 'All',
        'time': 'Allday',
        'stamina': 100,
        'initPosition': (80, -1.0, -60.0),
        'goodbyePosHpr': [
            (90.0, -15.0, -17.0),
            (0, 0, -20)],
        'swimmingDistance': (190, -15.0, -17.0),
        'aboutToBiteLureDuration': 4.0,
        'fishTurnX': 25.0,
        'swimLeftDuration': 5.0,
        'swimRightDuration': 2.0,
        'biteXOffset': 7.0 },
    {
        'id': InventoryType.Collection_Set11_Part2,
        'name': PLocalizer.Collections[InventoryType.Collection_Set11_Part2],
        'chanceThisFishAppears': 0.08,
        'model': 'lgLegFire',
        'type': 'uncommon',
        'size': 'super',
        'scaleRange': (1.0, 1.0),
        'weightRange': (9, 10),
        'chanceItWillMakeABreakForIt': 0.348,
        'strength': 9,
        'speed': 5.0,
        'swimAnimationMultiplier': 1.0 / 5.0,
        'durationOfFishTurn': 0.0,
        'turnAnimationMultiplier': 1.0 / 5.0,
        'hookRadius': 1,
        'experience': 0,
        'gold': 2000,
        'lure': 'special',
        'rod': 'special',
        'location': 'deepSea',
        'lureInterestTime': 1.0,
        'behaviorDict': {
            'name': 'straight',
            'sineMultiplier': 0.299 },
        'gullibilityStaticLure': 0.100,
        'gullibilityMovingLure': 0.100,
        'restDurationRange': (3.5, 5.0),
        'fightDurationRange': (1.5, 2.5),
        'pullDurationRange': (3.5, 5),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.7, 0.0, 0.0),
        'collisionBoxSize': (12.0, 2.0, 3.0),
        'indicatorHeightOffset': 0.800000,
        'size': 'super',
        'indicatorHeightOffset': 1.0,
        'habitat': 'All',
        'time': 'Allday',
        'stamina': 100,
        'initPosition': (80, -1.0, -60.0),
        'goodbyePosHpr': [
            (90.0, -15.0, -15),
            (0, 0, -20)],
        'swimmingDistance': (170, -15.0, -17),
        'aboutToBiteLureDuration': 4.0,
        'fishTurnX': 25.0,
        'swimLeftDuration': 5.0,
        'swimRightDuration': 2.0,
        'biteXOffset': 7.0 },
    {
        'id': InventoryType.Collection_Set11_Part3,
        'name': PLocalizer.Collections[InventoryType.Collection_Set11_Part3],
        'chanceThisFishAppears': 0.200,
        'model': 'lgLegGlittering',
        'type': 'uncommon',
        'size': 'super',
        'scaleRange': (1.0, 1.0),
        'weightRange': (5, 6),
        'chanceItWillMakeABreakForIt': 0.25,
        'strength': 6,
        'speed': 5.0,
        'swimAnimationMultiplier': 1.0 / 5.0,
        'durationOfFishTurn': 0.0,
        'turnAnimationMultiplier': 1.0 / 5.0,
        'hookRadius': 1,
        'experience': 0,
        'gold': 1000,
        'lure': 'special',
        'rod': 'special',
        'location': 'deepSea',
        'lureInterestTime': 1.0,
        'behaviorDict': {
            'name': 'straight',
            'sineMultiplier': 0.299 },
        'gullibilityStaticLure': 0.100,
        'gullibilityMovingLure': 0.100,
        'restDurationRange': (3.5, 5.0),
        'fightDurationRange': (1.5, 2.5),
        'pullDurationRange': (3.5, 5),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.7, 0.0, 0.0),
        'collisionBoxSize': (12.0, 2.0, 3.0),
        'indicatorHeightOffset': 0.800000,
        'size': 'super',
        'indicatorHeightOffset': 1.0,
        'stamina': 100,
        'habitat': 'All',
        'time': 'Allday',
        'initPosition': (80, -1.0, -60.0),
        'goodbyePosHpr': [
            (90.0, -15.0, -15.0),
            (0, 0, -40)],
        'swimmingDistance': (150, -15.0, -18.0),
        'aboutToBiteLureDuration': 4.0,
        'fishTurnX': 35.0,
        'swimLeftDuration': 5.0,
        'swimRightDuration': 2.0,
        'biteXOffset': 7.0 },
    {
        'id': InventoryType.Collection_Set11_Part4,
        'name': PLocalizer.Collections[InventoryType.Collection_Set11_Part4],
        'chanceThisFishAppears': 0.12,
        'model': 'lgLegMossy',
        'type': 'uncommon',
        'size': 'super',
        'scaleRange': (2.28, 2.28),
        'weightRange': (10, 11),
        'chanceItWillMakeABreakForIt': 0.200,
        'strength': 8,
        'hookRadius': 1,
        'experience': 0,
        'gold': 1500,
        'indicatorHeightOffset': 1.0,
        'lure': 'special',
        'rod': 'special',
        'location': 'deepSea',
        'lureInterestTime': 1.0,
        'behaviorDict': {
            'name': 'straight',
            'sineMultiplier': 0.299 },
        'gullibilityStaticLure': 0.100,
        'gullibilityMovingLure': 0.100,
        'restDurationRange': (3.5, 5.0),
        'fightDurationRange': (1.5, 2.5),
        'pullDurationRange': (3.5, 5),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.7, 0.0, 0.0),
        'collisionBoxSize': (12.0, 2.0, 3.0),
        'indicatorHeightOffset': 0.800000,
        'size': 'super',
        'stamina': 100,
        'habitat': 'All',
        'time': 'Allday',
        'initPosition': (80, -1.0, -60.0),
        'goodbyePosHpr': [
            (90.0, -15.0, -12.0),
            (0, 0, -10)],
        'swimmingDistance': (150, -15.0, -18.0),
        'aboutToBiteLureDuration': 4.0,
        'speed': 2.0,
        'swimAnimationMultiplier': 1.0 / 2.0,
        'durationOfFishTurn': 0.0,
        'turnAnimationMultiplier': 1.0 / 2.0,
        'fishTurnX': 50.0,
        'swimLeftDuration': 13.0,
        'swimRightDuration': 6.0,
        'biteXOffset': 5.0 },
    {
        'id': InventoryType.Collection_Set11_Part5,
        'name': PLocalizer.Collections[InventoryType.Collection_Set11_Part5],
        'chanceThisFishAppears': 0.4,
        'model': 'lgLegSpeedy',
        'type': 'uncommon',
        'size': 'super',
        'scaleRange': (1.0, 1.0),
        'weightRange': (6, 7),
        'chanceItWillMakeABreakForIt': 0.299,
        'strength': 5,
        'speed': 6.0,
        'swimAnimationMultiplier': 1.0 / 6.0,
        'durationOfFishTurn': 0.0,
        'turnAnimationMultiplier': 1.0 / 6.0,
        'hookRadius': 1,
        'experience': 0,
        'gold': 700,
        'lure': 'special',
        'rod': 'special',
        'location': 'deepSea',
        'indicatorHeightOffset': 1.0,
        'lureInterestTime': 1.0,
        'behaviorDict': {
            'name': 'straight',
            'sineMultiplier': 0.299 },
        'gullibilityStaticLure': 0.100,
        'gullibilityMovingLure': 0.100,
        'restDurationRange': (3.5, 5.0),
        'fightDurationRange': (1.5, 2.5),
        'pullDurationRange': (3.5, 5),
        'attractionRadius': 3.0,
        'collisionBoxOffset': (-1.7, 0.0, 0.0),
        'collisionBoxSize': (12.0, 2.0, 3.0),
        'indicatorHeightOffset': 0.800000,
        'size': 'super',
        'stamina': 100,
        'habitat': 'All',
        'time': 'Allday',
        'initPosition': (80, -1.0, -60.0),
        'goodbyePosHpr': [
            (90, -15, -17),
            (0, 0, -20)],
        'swimmingDistance': (390, -15.0, -18),
        'aboutToBiteLureDuration': 4.0,
        'fishTurnX': 25.0,
        'swimLeftDuration': 5.0,
        'swimRightDuration': 2.0,
        'biteXOffset': 7.0 }]

RandomList = []

for i, fishData in enumerate(allFishData):
    for j in xrange((3 - fishData['rarity']) * 2):
        RandomList.append(i)

def giveMeAFish(location, depth, fishHisto):
    return allFishData[random.choice(RandomList)]


CollectionToData = { }
for fish in allFishData:
    CollectionToData[fish['id']] = fish


def getModelFromCollection(val):
    data = CollectionToData.get(val, '')
    if data:
        return data['model']
    else:
        return ''


def getFishData(collectionId):
    return CollectionToData.get(collectionId, { })


def inFishingCollection(value):
    return value in CollectionToData

legendaryFishDistribution = ([ x['chanceThisFishAppears'] for x in legendaryFishData ], legendaryFishData)
modelToLegendaryFishData = ([ (x['model'], x) for x in legendaryFishData ])

def getALegendaryFish(model = None):
    if model:
        model = 'lgLeg%s' % model
        if model in modelToLegendaryFishData:
            return modelToLegendaryFishData[model]
        else:
            return DropGlobals.rollDistribution(legendaryFishDistribution)
    else:
        return DropGlobals.rollDistribution(legendaryFishDistribution)

ItemDistributions = [
    [
        40,
        50,
        0,
        10,
        0],
    [
        35,
        35,
        0,
        15,
        15],
    [
        25,
        15,
        0,
        30,
        30],
    [
        0,
        0,
        0,
        50,
        50]]
RarityDistributions = [
    [
        65.485,
        30,
        4.5,
        0.01,
        0],
    [
        49.978,
        40,
        10,
        0.02,
        0.001],
    [
        32.414,
        40,
        25,
        2.5,
        0.085]]
