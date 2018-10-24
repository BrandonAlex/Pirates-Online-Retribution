global __maxHullStats
from pandac.PandaModules import *
from direct.showbase.PythonUtil import Enum
from pirates.uberdog.UberDogGlobals import *
from pirates.uberdog.UberDogGlobals import InventoryType
from direct.actor import Actor
from direct.task import Task
from pirates.inventory import ItemGlobals
import random
import copy
import math

FORMATION_ARROW = 0
FORMATION_CIRCLE = 1
FORMATION_LINE = 2
FORMATION_WALL = 3
FORMATION_DEFAULT = FORMATION_ARROW
FORMATION_ICON_CHEST = 0
FORMATION_ICON_SKULL = 1
FORMATION_AVOID_SPHERE_RADIUS = 100
AI_SHIP = 0
PLAYER_SHIP = 1
CANNONDEFENSE_SHIP = 2
FISHING_SHIP = 3
SEIZEABLE_SHIP = 4
SEIZEABLE_SHIP_TIME = 60 * 30
SHIP_MOVIE_BOARD = 0
SHIP_MOVIE_UNBOARD = 1
SHIP_BOARD_FROM_SWIM = 0
SHIP_BOARD_FROM_WALK = 1
ARMOR_REAR = 0
ARMOR_LEFT = -1
ARMOR_RIGHT = 1
AVOID_SPHERE_RADIUS = 100
SUNK_REPAIR_COST_MULTIPLIER = 2
SHIP_REAR_DAMAGE_BONUS = 1.25

class Styles:
    Undefined = -1
    Player = 0
    Navy = 1
    EITC = 2
    Undead = 3
    BP = 4
    French = 5
    Spanish = 6
    Bandit01 = 7
    Bandit02 = 8
    Bandit03 = 9
    Bandit04 = 10
    Treasure_Navy = 11
    Treasure_EITC = 12
    QueenAnnesRevenge = 13
    BountyHunter_A = 14
    BountyHunter_B = 15
    BountyHunter_C = 16
    BountyHunter_D = 17
    BountyHunter_E = 18
    BountyHunter_F = 19
    BountyHunter_G = 20
    NavyHunter = 21


class Logos:
    Undefined = -1
    NoLogo = 0
    Navy = 200
    BlackPearl = 201
    EITC = 202
    EITC_Emblem = 203
    PVP_French = 210
    PVP_Spanish = 211
    Bandit_Bull = 220
    Bandit_Dagger = 221
    Bandit_Scorpion = 222
    Bandit_Claw = 223
    Treasure_Navy = 230
    Treasure_EITC = 231
    QueenAnnesRevenge = 241
    Bounty_Hunter_Wasp = 242
    Bounty_Hunter_Spider = 243
    Bounty_Hunter_Snake = 244
    Navy_Hunter_Unicorn = 246
    Navy_Hunter_Lion = 247

MAST_LOGO_PLACEMENT_LIST = [
    Logos.Bounty_Hunter_Wasp,
    Logos.Bounty_Hunter_Spider]
INTERCEPTORL1 = 1
INTERCEPTORL2 = 2
INTERCEPTORL3 = 3
MERCHANTL1 = 11
MERCHANTL2 = 12
MERCHANTL3 = 13
WARSHIPL1 = 21
WARSHIPL2 = 22
WARSHIPL3 = 23
WARSHIPCOM = 24
SHIP_OF_THE_LINE = 30
HMS_VICTORY = 31
HMS_NEWCASTLE = 32
HMS_INVINCIBLE = 33
EITC_INTREPID = 34
EITC_CONQUERER = 35
EITC_LEVIATHAN = 36
EL_PATRONS_SHIP = 37
P_SKEL_PHANTOM = 38
P_SKEL_REVENANT = 39
P_SKEL_CEREBUS = 40
P_NAVY_KINGFISHER = 41
P_EITC_WARLORD = 42
NAVY_KRAKEN_HUNTER = 43
BLACK_PEARL = 50
DAUNTLESS = 51
FLYING_DUTCHMAN = 52
GOLIATH = 53
JOLLY_ROGER = 54
QUEEN_ANNES_REVENGE = 55
SKEL_WARSHIPL3 = 60
SKEL_INTERCEPTORL3 = 61
NAVY_FERRET = 80
NAVY_GREYHOUND = 81
NAVY_KINGFISHER = 82
NAVY_PREDATOR = 83
NAVY_BULWARK = 84
NAVY_VANGUARD = 85
NAVY_MONARCH = 86
NAVY_COLOSSUS = 87
NAVY_PANTHER = 88
NAVY_CENTURION = 89
NAVY_MAN_O_WAR = 90
NAVY_DREADNOUGHT = 91
NAVY_ELITE = 92
NAVY_BASTION = 93
EITC_SEA_VIPER = 100
EITC_BLOODHOUND = 101
EITC_BARRACUDA = 102
EITC_CORSAIR = 103
EITC_SENTINEL = 104
EITC_IRONWALL = 105
EITC_OGRE = 106
EITC_BEHEMOTH = 107
EITC_CORVETTE = 108
EITC_MARAUDER = 109
EITC_WARLORD = 110
EITC_JUGGERNAUT = 111
EITC_TYRANT = 112
SKEL_PHANTOM = 120
SKEL_REVENANT = 121
SKEL_STORM_REAPER = 122
SKEL_BLACK_HARBINGER = 123
SKEL_DEATH_OMEN = 124
SKEL_SHADOW_CROW_FR = 125
SKEL_HELLHOUND_FR = 126
SKEL_BLOOD_SCOURGE_FR = 127
SKEL_SHADOW_CROW_SP = 128
SKEL_HELLHOUND_SP = 129
SKEL_BLOOD_SCOURGE_SP = 130
HUNTER_VENGENCE = 160
HUNTER_CUTTER_SHARK = 161
HUNTER_FLYING_STORM = 162
HUNTER_KILLYADED = 163
HUNTER_RED_DERVISH = 164
HUNTER_CENTURY_HAWK = 165
HUNTER_SCORNED_SIREN = 166
HUNTER_TALLYHO = 180
HUNTER_BATTLEROYALE = 181
HUNTER_EN_GARDE = 182
STUMPY_SHIP = 255
PLAYER_SHIPS = (INTERCEPTORL1, INTERCEPTORL2, INTERCEPTORL3, MERCHANTL1, MERCHANTL2, MERCHANTL3, WARSHIPL1, WARSHIPL2, WARSHIPL3, SHIP_OF_THE_LINE, EL_PATRONS_SHIP, P_SKEL_PHANTOM, P_SKEL_REVENANT, P_SKEL_CEREBUS, P_NAVY_KINGFISHER, P_EITC_WARLORD, NAVY_KRAKEN_HUNTER)
MAST_LOGO_PLACEMENT = {
    INTERCEPTORL1: [
        0],
    INTERCEPTORL2: [
        0],
    INTERCEPTORL3: [
        0],
    MERCHANTL1: [
        1],
    MERCHANTL2: [
        1],
    MERCHANTL3: [
        1],
    WARSHIPL1: [
        0],
    WARSHIPL2: [
        0],
    WARSHIPL3: [
        0],
    WARSHIPCOM: [
        0] }
SHIP_CLASS_LIST = [
    'INTERCEPTORL1',
    'INTERCEPTORL2',
    'INTERCEPTORL3',
    'MERCHANTL1',
    'MERCHANTL2',
    'MERCHANTL3',
    'WARSHIPL1',
    'WARSHIPL2',
    'WARSHIPL3',
    'BLACK_PEARL',
    'DAUNTLESS',
    'FLYING_DUTCHMAN',
    'GOLIATH',
    'QUEEN_ANNES_REVENGE',
    'SKEL_WARSHIPL3',
    'SKEL_INTERCEPTORL3',
    'STUMPY_SHIP',
    'NAVY_FERRET',
    'NAVY_GREYHOUND',
    'NAVY_KINGFISHER',
    'NAVY_PREDATOR',
    'NAVY_BULWARK',
    'NAVY_VANGUARD',
    'NAVY_MONARCH',
    'NAVY_COLOSSUS',
    'NAVY_PANTHER',
    'NAVY_CENTURION',
    'NAVY_MAN_O_WAR',
    'NAVY_DREADNOUGHT',
    'EITC_SEA_VIPER',
    'EITC_BLOODHOUND',
    'EITC_BARRACUDA',
    'EITC_CORSAIR',
    'EITC_SENTINEL',
    'EITC_IRONWALL',
    'EITC_OGRE',
    'EITC_BEHEMOTH',
    'EITC_CORVETTE',
    'EITC_MARAUDER',
    'EITC_WARLORD',
    'EITC_JUGGERNAUT',
    'SKEL_PHANTOM',
    'SKEL_REVENANT',
    'SKEL_STORM_REAPER',
    'SKEL_BLACK_HARBINGER',
    'SKEL_DEATH_OMEN',
    'SKEL_SHADOW_CROW_FR',
    'SKEL_HELLHOUND_FR',
    'SKEL_BLOOD_SCOURGE_FR',
    'SKEL_SHADOW_CROW_SP',
    'SKEL_HELLHOUND_SP',
    'SKEL_BLOOD_SCOURGE_SP',
    'HUNTER_VENGENCE']

class Masts:
    Main_Square = 1
    Main_Tri = 2
    Aft_Tri = 3
    Fore_Multi = 4
    Fore_Tri = 5
    Skel_Main_A = 6
    Skel_Main_B = 7
    Skel_Tri = 8
    Skel_Fore = 9
    Skel_Aft = 10


def getMastSetup(shipClass):
    shipInfo = __shipConfigs[shipClass]
    mastInfo = { }
    mastInfo[0] = shipInfo['mastConfig1']
    mastInfo[1] = shipInfo['mastConfig2']
    mastInfo[2] = shipInfo['mastConfig3']
    mastInfo[3] = shipInfo['aftmastConfig']
    mastInfo[4] = shipInfo['foremastConfig']
    return mastInfo


class Prows:
    Skeleton = 1
    Lady = 2


class Cannons:
    L1 = InventoryType.CannonL1
    L2 = InventoryType.CannonL2
    L3 = InventoryType.CannonL3
    L4 = InventoryType.CannonL4
    Skel_L1 = 250
    Skel_L2 = 251
    Skel_L3 = 252
    BP = 254
    Tutorial = 255
    Repeater = 256
    Navy = 257


class Sail:
    MainL1 = 1
    MainL2 = 2
    MainL3 = 3
    ForeL1 = 4
    ForeL2 = 5
    ForeL3 = 6
    AftL1 = 7
    AftL2 = 8
    AftL3 = 9
    Flag = 10


class Ram:
    L1 = 101
    L2 = 102
    L3 = 103
    Skel_L3 = 104


def getMastHealth(shipClass, sp):
    masts = getMastSetup(shipClass)
    total = 0
    for i in xrange(3):
        if masts[i]:
            total += masts[i][1]
            continue

    for i in xrange(3, 5):
        if masts[i]:
            total += masts[i][1] * 0.75
            continue

    modifier = sp / float(total)
    health = [
        0,
        0,
        0,
        0,
        0]
    for i in xrange(3):
        if masts[i]:
            health[i] = int(masts[i][1] * modifier)
            continue

    for i in xrange(3, 5):
        if masts[i]:
            health[i] = int(masts[i][1] * modifier * 0.75)
            continue

    if getModelClass(shipClass) <= INTERCEPTORL3:
        health[0] += health[3]
        health[3] = 0

    return health

__hullArmor = {
    WARSHIPL1: [
        1000,
        2000,
        2000],
    WARSHIPL2: [
        1500,
        3000,
        3000],
    WARSHIPL3: [
        2500,
        5000,
        5000],
    MERCHANTL1: [
        1600,
        1400,
        1400],
    MERCHANTL2: [
        2200,
        2400,
        2400],
    MERCHANTL3: [
        3400,
        4000,
        4000],
    INTERCEPTORL1: [
        800,
        1000,
        1000],
    INTERCEPTORL2: [
        1200,
        1800,
        1800],
    INTERCEPTORL3: [
        2000,
        3600,
        3600],
    SHIP_OF_THE_LINE: [
        50000,
        100000,
        100000],
    SKEL_WARSHIPL3: [
        2800,
        5200,
        5200],
    SKEL_INTERCEPTORL3: [
        2400,
        4200,
        4200],
    BLACK_PEARL: [
        3000,
        5400,
        5400],
    GOLIATH: [
        3200,
        5600,
        5600],
    QUEEN_ANNES_REVENGE: [
        3000,
        4000,
        4000] }

def getHullArmor(modelClass):
    return __hullArmor[modelClass]

defaultAcceleration = 20
defaultMaxSpeed = 120
defaultMaxReverseSpeed = defaultMaxSpeed / 1.5
defaultReverseAcceleration = defaultAcceleration / 1.5
defaultMaxReverseAcceleration = 10
defaultTurn = 6
defaultMaxTurn = 20
defaultShipMass = 1.0
defaultWaterIntake = 0.05
__maxHullStats = { }

def getMaxShipStats():
    if not __maxHullStats:
        for shipClass in PLAYER_SHIPS:
            hullInfo = __shipConfigs[shipClass]
            for key in ('hp', 'sp', 'maxCargo', 'maxCrew', 'maxCannons', 'maxBroadsides', 'rammingPower', 'acceleration', 'maxSpeed', 'reverseAcceleration', 'maxReverseSpeed', 'turn', 'maxTurn'):
                val = hullInfo[key]
                __maxHullStats[key] = max(__maxHullStats.get(key, 0), val)



    return __maxHullStats

__shipConfigs = {
    WARSHIPL1: {
        'setShipClass': WARSHIPL1,
        'modelClass': WARSHIPL1,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 1),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 8,
        'leftBroadsides': [
            Cannons.L2] * 5,
        'rightBroadsides': [
            Cannons.L2] * 5,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 4200,
        'sp': 6000,
        'maxCargo': 8,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 10,
        'rammingPower': 450,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    WARSHIPL2: {
        'setShipClass': WARSHIPL2,
        'modelClass': WARSHIPL2,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 10,
        'leftBroadsides': [
            Cannons.L2] * 7,
        'rightBroadsides': [
            Cannons.L2] * 7,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 8400,
        'sp': 9000,
        'maxCargo': 12,
        'maxCrew': 10,
        'maxCannons': 10,
        'maxBroadsides': 14,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    WARSHIPL3: {
        'setShipClass': WARSHIPL3,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'rightBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 12600,
        'sp': 12000,
        'maxCargo': 16,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 1800,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    SHIP_OF_THE_LINE: {
        'setShipClass': SHIP_OF_THE_LINE,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 24,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    EL_PATRONS_SHIP: {
        'setShipClass': EL_PATRONS_SHIP,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'rightBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'broadsideAmmo': InventoryType.CannonGrapeShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 12600,
        'sp': 12000,
        'maxCargo': 16,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 1800,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    P_SKEL_PHANTOM: {
        'setShipClass': P_SKEL_PHANTOM,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            0,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            0],
        'rightBroadsides': [
            0,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            0],
        'broadsideAmmo': InventoryType.CannonThunderbolt,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': 0,
        'hp': 2500,
        'sp': 6000,
        'maxCargo': 14,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 1600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    P_SKEL_REVENANT: {
        'setShipClass': P_SKEL_REVENANT,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            Cannons.Skel_L2] * 6,
        'rightBroadsides': [
            Cannons.Skel_L2] * 6,
        'broadsideAmmo': InventoryType.CannonFury,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 2500,
        'sp': 6000,
        'maxCargo': 14,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 1600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    P_SKEL_CEREBUS: {
        'setShipClass': P_SKEL_CEREBUS,
        'modelClass': SKEL_INTERCEPTORL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': 0,
        'aftmastConfig': 0,
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 5,
        'leftBroadsides': [
            Cannons.Skel_L2] * 5,
        'rightBroadsides': [
            Cannons.Skel_L2] * 5,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 3000,
        'sp': 6000,
        'maxCargo': 12,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 14,
        'rammingPower': 500,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    P_NAVY_KINGFISHER: {
        'setShipClass': P_NAVY_KINGFISHER,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 6,
        'leftBroadsides': [
            Cannons.L1] * 5,
        'rightBroadsides': [
            Cannons.L1] * 5,
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1200,
        'sp': 4000,
        'maxCargo': 14,
        'maxCrew': 3,
        'maxCannons': 9,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    P_EITC_WARLORD: {
        'setShipClass': P_EITC_WARLORD,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L3] * 12,
        'leftBroadsides': [
            Cannons.L2] * 9,
        'rightBroadsides': [
            Cannons.L2] * 9,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 2100,
        'sp': 6000,
        'maxCargo': 16,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 2400,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_KRAKEN_HUNTER: {
        'setShipClass': NAVY_KRAKEN_HUNTER,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 0,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    HMS_VICTORY: {
        'setShipClass': HMS_VICTORY,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Treasure_Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Treasure_Navy,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    HMS_NEWCASTLE: {
        'setShipClass': HMS_NEWCASTLE,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Treasure_Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Treasure_Navy,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    HMS_INVINCIBLE: {
        'setShipClass': HMS_INVINCIBLE,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Treasure_Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Treasure_Navy,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonExplosive,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    EITC_INTREPID: {
        'setShipClass': EITC_INTREPID,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Treasure_EITC,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Treasure_EITC,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    EITC_CONQUERER: {
        'setShipClass': EITC_CONQUERER,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Treasure_EITC,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Treasure_EITC,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    EITC_LEVIATHAN: {
        'setShipClass': EITC_LEVIATHAN,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.Treasure_EITC,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Treasure_EITC,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': 0,
        'hp': 20000,
        'sp': 15000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    MERCHANTL1: {
        'setShipClass': MERCHANTL1,
        'modelClass': MERCHANTL1,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 1),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 4,
        'leftBroadsides': [
            Cannons.L2] * 5,
        'rightBroadsides': [
            Cannons.L2] * 5,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 3600,
        'sp': 5000,
        'maxCargo': 10,
        'maxCrew': 6,
        'maxCannons': 4,
        'maxBroadsides': 10,
        'rammingPower': 300,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    MERCHANTL2: {
        'setShipClass': MERCHANTL2,
        'modelClass': MERCHANTL2,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 1),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': (Masts.Main_Square, 1),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 8,
        'leftBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'rightBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 7200,
        'sp': 7000,
        'maxCargo': 14,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 18,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    MERCHANTL3: {
        'setShipClass': MERCHANTL3,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 10,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 10800,
        'sp': 10000,
        'maxCargo': 18,
        'maxCrew': 10,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 1200,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    INTERCEPTORL1: {
        'setShipClass': INTERCEPTORL1,
        'modelClass': INTERCEPTORL1,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 2,
        'leftBroadsides': [
            Cannons.L2] * 3,
        'rightBroadsides': [
            Cannons.L2] * 3,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 2400,
        'sp': 4000,
        'maxCargo': 6,
        'maxCrew': 3,
        'maxCannons': 2,
        'maxBroadsides': 6,
        'rammingPower': 150,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    INTERCEPTORL2: {
        'setShipClass': INTERCEPTORL2,
        'modelClass': INTERCEPTORL2,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 6,
        'leftBroadsides': [
            Cannons.L1] * 5,
        'rightBroadsides': [
            Cannons.L1] * 5,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 4800,
        'sp': 6000,
        'maxCargo': 10,
        'maxCrew': 6,
        'maxCannons': 6,
        'maxBroadsides': 10,
        'rammingPower': 300,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    INTERCEPTORL3: {
        'setShipClass': INTERCEPTORL3,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 8,
        'leftBroadsides': [
            Cannons.L1] * 7,
        'rightBroadsides': [
            Cannons.L1] * 7,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 7200,
        'sp': 9000,
        'maxCargo': 14,
        'maxCrew': 9,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    BLACK_PEARL: {
        'setShipClass': BLACK_PEARL,
        'modelClass': BLACK_PEARL,
        'defaultStyle': Styles.BP,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.BlackPearl,
        'cannons': [
            Cannons.BP] * 14,
        'leftBroadsides': [
            Cannons.BP] * 9,
        'rightBroadsides': [
            Cannons.BP] * 9,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 6000,
        'sp': 8000,
        'maxCargo': 20,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 18,
        'rammingPower': 2000,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.7 * defaultTurn,
        'maxTurn': 0.7 * defaultMaxTurn },
    STUMPY_SHIP: {
        'setShipClass': INTERCEPTORL1,
        'modelClass': INTERCEPTORL1,
        'defaultStyle': Styles.Player,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.Tutorial,
            0],
        'leftBroadsides': [],
        'rightBroadsides': [],
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 2400,
        'sp': 4000,
        'maxCargo': 5,
        'maxCrew': 2,
        'maxCannons': 2,
        'maxBroadsides': 0,
        'rammingPower': 150,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.7 * defaultTurn,
        'maxTurn': 0.7 * defaultMaxTurn },
    GOLIATH: {
        'setShipClass': GOLIATH,
        'modelClass': GOLIATH,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L4] * 9,
        'rightBroadsides': [
            Cannons.L4] * 9,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 3500,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 18,
        'maxBroadsides': 18,
        'rammingPower': 900,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 1.2 * defaultMaxSpeed,
        'reverseAcceleration': 0.9 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    QUEEN_ANNES_REVENGE: {
        'setShipClass': QUEEN_ANNES_REVENGE,
        'modelClass': QUEEN_ANNES_REVENGE,
        'defaultStyle': Styles.QueenAnnesRevenge,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 10,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Skeleton,
        'hp': 9000,
        'sp': 10000,
        'maxCargo': 16,
        'maxCrew': 10,
        'maxCannons': 12,
        'maxBroadsides': 22,
        'rammingPower': 1200,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    NAVY_PANTHER: {
        'setShipClass': NAVY_PANTHER,
        'modelClass': WARSHIPL1,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 1),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 6,
        'leftBroadsides': [
            Cannons.L2] * 4,
        'rightBroadsides': [
            Cannons.L2] * 4,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 1700,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 8,
        'maxBroadsides': 10,
        'rammingPower': 150,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_CENTURION: {
        'setShipClass': NAVY_CENTURION,
        'modelClass': WARSHIPL2,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 8,
        'leftBroadsides': [
            Cannons.L2] * 6,
        'rightBroadsides': [
            Cannons.L2] * 6,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 2100,
        'sp': 5000,
        'maxCargo': 3,
        'maxCrew': 6,
        'maxCannons': 10,
        'maxBroadsides': 14,
        'rammingPower': 450,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_MAN_O_WAR: {
        'setShipClass': NAVY_MAN_O_WAR,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 10,
        'leftBroadsides': [
            Cannons.L2] * 8,
        'rightBroadsides': [
            Cannons.L2] * 8,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 2100,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_DREADNOUGHT: {
        'setShipClass': NAVY_DREADNOUGHT,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L4] * 9,
        'rightBroadsides': [
            Cannons.L4] * 9,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 2100,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_ELITE: {
        'setShipClass': NAVY_ELITE,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L4] * 9,
        'rightBroadsides': [
            Cannons.L4] * 9,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 4200,
        'sp': 6000,
        'maxCargo': 5,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_BULWARK: {
        'setShipClass': NAVY_BULWARK,
        'modelClass': MERCHANTL1,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 1),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 4,
        'leftBroadsides': [
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'rightBroadsides': [
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Lady,
        'hp': 1400,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 6,
        'maxCannons': 4,
        'maxBroadsides': 10,
        'rammingPower': 150,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_VANGUARD: {
        'setShipClass': NAVY_VANGUARD,
        'modelClass': MERCHANTL2,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 1),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': (Masts.Main_Square, 1),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 6,
        'leftBroadsides': [
            Cannons.L3] * 5,
        'rightBroadsides': [
            Cannons.L3] * 5,
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Lady,
        'hp': 1800,
        'sp': 5000,
        'maxCargo': 3,
        'maxCrew': 10,
        'maxCannons': 8,
        'maxBroadsides': 18,
        'rammingPower': 300,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_MONARCH: {
        'setShipClass': NAVY_MONARCH,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': (Masts.Main_Square, 2),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 8,
        'leftBroadsides': [
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            0,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'rightBroadsides': [
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            0,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1800,
        'sp': 5500,
        'maxCargo': 3,
        'maxCrew': 14,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_COLOSSUS: {
        'setShipClass': NAVY_COLOSSUS,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 10,
        'leftBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'rightBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1800,
        'sp': 5500,
        'maxCargo': 3,
        'maxCrew': 14,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_BASTION: {
        'setShipClass': NAVY_BASTION,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 10,
        'leftBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'rightBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0],
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 3600,
        'sp': 5500,
        'maxCargo': 5,
        'maxCrew': 14,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    NAVY_FERRET: {
        'setShipClass': NAVY_FERRET,
        'modelClass': INTERCEPTORL1,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 2,
        'leftBroadsides': [],
        'rightBroadsides': [],
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Lady,
        'hp': 1000,
        'sp': 3000,
        'maxCargo': 1,
        'maxCrew': 4,
        'maxCannons': 2,
        'maxBroadsides': 6,
        'rammingPower': 75,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    NAVY_GREYHOUND: {
        'setShipClass': NAVY_GREYHOUND,
        'modelClass': INTERCEPTORL2,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': 0,
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 4,
        'leftBroadsides': [
            Cannons.L1] * 3,
        'rightBroadsides': [
            Cannons.L1] * 3,
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Lady,
        'hp': 1200,
        'sp': 3500,
        'maxCargo': 2,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 10,
        'rammingPower': 225,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    NAVY_KINGFISHER: {
        'setShipClass': NAVY_KINGFISHER,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 6,
        'leftBroadsides': [
            Cannons.L1] * 5,
        'rightBroadsides': [
            Cannons.L1] * 5,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1200,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 450,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    NAVY_PREDATOR: {
        'setShipClass': NAVY_PREDATOR,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.Navy,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.NoLogo,
        'cannons': [
            Cannons.L1] * 8,
        'leftBroadsides': [
            Cannons.L1] * 7,
        'rightBroadsides': [
            Cannons.L1] * 7,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1200,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 450,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    EITC_CORVETTE: {
        'setShipClass': EITC_CORVETTE,
        'modelClass': WARSHIPL1,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 1),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L3] * 6,
        'leftBroadsides': [
            Cannons.L2] * 5,
        'rightBroadsides': [
            Cannons.L2] * 5,
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 1700,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 8,
        'maxBroadsides': 10,
        'rammingPower': 150,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_MARAUDER: {
        'setShipClass': EITC_MARAUDER,
        'modelClass': WARSHIPL2,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L3] * 8,
        'leftBroadsides': [
            Cannons.L2] * 7,
        'rightBroadsides': [
            Cannons.L2] * 7,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': 0,
        'hp': 2100,
        'sp': 5000,
        'maxCargo': 3,
        'maxCrew': 6,
        'maxCannons': 10,
        'maxBroadsides': 14,
        'rammingPower': 450,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_WARLORD: {
        'setShipClass': EITC_WARLORD,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L3] * 12,
        'leftBroadsides': [
            Cannons.L2] * 9,
        'rightBroadsides': [
            Cannons.L2] * 9,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 2100,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_JUGGERNAUT: {
        'setShipClass': EITC_JUGGERNAUT,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 10,
        'rightBroadsides': [
            Cannons.L2] * 10,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 2100,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_TYRANT: {
        'setShipClass': EITC_TYRANT,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 10,
        'rightBroadsides': [
            Cannons.L2] * 10,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 4200,
        'sp': 6000,
        'maxCargo': 5,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_SENTINEL: {
        'setShipClass': EITC_SENTINEL,
        'modelClass': MERCHANTL1,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 1),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 4,
        'leftBroadsides': [
            Cannons.L2] * 5,
        'rightBroadsides': [
            Cannons.L2] * 5,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': Prows.Lady,
        'hp': 1400,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 6,
        'maxCannons': 4,
        'maxBroadsides': 10,
        'rammingPower': 150,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_IRONWALL: {
        'setShipClass': EITC_IRONWALL,
        'modelClass': MERCHANTL2,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 1),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': (Masts.Main_Square, 1),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 6,
        'leftBroadsides': [
            Cannons.L3] * 7,
        'rightBroadsides': [
            Cannons.L3] * 7,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1800,
        'sp': 5000,
        'maxCargo': 3,
        'maxCrew': 10,
        'maxCannons': 8,
        'maxBroadsides': 18,
        'rammingPower': 300,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_OGRE: {
        'setShipClass': EITC_OGRE,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 2),
        'mastConfig3': (Masts.Main_Square, 2),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 8,
        'leftBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2],
        'rightBroadsides': [
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            0,
            0,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2,
            Cannons.L2],
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1800,
        'sp': 5500,
        'maxCargo': 3,
        'maxCrew': 14,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_BEHEMOTH: {
        'setShipClass': EITC_BEHEMOTH,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 10,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonExplosive,
        'prow': Prows.Lady,
        'hp': 1800,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 14,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    EITC_SEA_VIPER: {
        'setShipClass': EITC_SEA_VIPER,
        'modelClass': INTERCEPTORL1,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': 0,
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 2,
        'leftBroadsides': [
            Cannons.L1] * 3,
        'rightBroadsides': [
            Cannons.L1] * 3,
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': Prows.Lady,
        'hp': 1000,
        'sp': 3000,
        'maxCargo': 1,
        'maxCrew': 4,
        'maxCannons': 2,
        'maxBroadsides': 6,
        'rammingPower': 75,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    EITC_BLOODHOUND: {
        'setShipClass': EITC_BLOODHOUND,
        'modelClass': INTERCEPTORL2,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': 0,
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 6,
        'leftBroadsides': [
            Cannons.L1] * 5,
        'rightBroadsides': [
            Cannons.L1] * 5,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': Prows.Lady,
        'hp': 1200,
        'sp': 3500,
        'maxCargo': 2,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 10,
        'rammingPower': 225,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    EITC_BARRACUDA: {
        'setShipClass': EITC_BARRACUDA,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 6,
        'leftBroadsides': [
            Cannons.L1] * 7,
        'rightBroadsides': [
            Cannons.L1] * 7,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': Prows.Lady,
        'hp': 1200,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 450,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    EITC_CORSAIR: {
        'setShipClass': EITC_CORSAIR,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.EITC,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.EITC,
        'cannons': [
            Cannons.L1] * 8,
        'leftBroadsides': [
            Cannons.L1] * 7,
        'rightBroadsides': [
            Cannons.L1] * 7,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': Prows.Lady,
        'hp': 1200,
        'sp': 4000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 450,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    SKEL_PHANTOM: {
        'setShipClass': SKEL_PHANTOM,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            0,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            0],
        'rightBroadsides': [
            0,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            Cannons.Skel_L2,
            0],
        'broadsideAmmo': InventoryType.CannonThunderbolt,
        'cannonAmmo': InventoryType.CannonChainShot,
        'prow': 0,
        'hp': 2500,
        'sp': 6000,
        'maxCargo': 2,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    SKEL_REVENANT: {
        'setShipClass': SKEL_REVENANT,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            Cannons.Skel_L2] * 6,
        'rightBroadsides': [
            Cannons.Skel_L2] * 6,
        'broadsideAmmo': InventoryType.CannonFury,
        'cannonAmmo': InventoryType.CannonRoundShot,
        'prow': 0,
        'hp': 2500,
        'sp': 6000,
        'maxCargo': 2,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    SKEL_STORM_REAPER: {
        'setShipClass': SKEL_STORM_REAPER,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            Cannons.Skel_L2] * 7,
        'rightBroadsides': [
            Cannons.Skel_L2] * 7,
        'broadsideAmmo': InventoryType.CannonThunderbolt,
        'cannonAmmo': InventoryType.CannonThunderbolt,
        'prow': 0,
        'hp': 2500,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    SKEL_BLACK_HARBINGER: {
        'setShipClass': SKEL_BLACK_HARBINGER,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            Cannons.Skel_L2] * 7,
        'rightBroadsides': [
            Cannons.Skel_L2] * 7,
        'broadsideAmmo': InventoryType.CannonFury,
        'cannonAmmo': InventoryType.CannonFury,
        'prow': 0,
        'hp': 2500,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    SKEL_DEATH_OMEN: {
        'setShipClass': SKEL_DEATH_OMEN,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            Cannons.Skel_L2] * 7,
        'rightBroadsides': [
            Cannons.Skel_L2] * 7,
        'broadsideAmmo': InventoryType.CannonFury,
        'cannonAmmo': InventoryType.CannonThunderbolt,
        'prow': 0,
        'hp': 2500,
        'sp': 6000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    JOLLY_ROGER: {
        'setShipClass': JOLLY_ROGER,
        'modelClass': SKEL_WARSHIPL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Main_A, 3),
        'mastConfig2': (Masts.Skel_Main_B, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Skel_Fore, 2),
        'aftmastConfig': (Masts.Skel_Aft, 2),
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 6,
        'leftBroadsides': [
            Cannons.Skel_L2] * 7,
        'rightBroadsides': [
            Cannons.Skel_L2] * 7,
        'broadsideAmmo': InventoryType.CannonThunderbolt,
        'cannonAmmo': InventoryType.CannonExplosive,
        'prow': 0,
        'hp': 20000,
        'sp': 18000,
        'maxCargo': 10,
        'maxCrew': 8,
        'maxCannons': 8,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    SKEL_SHADOW_CROW_FR: {
        'setShipClass': SKEL_SHADOW_CROW_FR,
        'modelClass': SKEL_INTERCEPTORL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': 0,
        'aftmastConfig': 0,
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 5,
        'leftBroadsides': [
            Cannons.Skel_L2] * 5,
        'rightBroadsides': [
            Cannons.Skel_L2] * 5,
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonFury,
        'prow': 0,
        'hp': 2500,
        'sp': 5000,
        'maxCargo': 1,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    SKEL_HELLHOUND_FR: {
        'setShipClass': SKEL_HELLHOUND_FR,
        'modelClass': SKEL_INTERCEPTORL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': 0,
        'aftmastConfig': 0,
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 5,
        'leftBroadsides': [
            Cannons.Skel_L2] * 5,
        'rightBroadsides': [
            Cannons.Skel_L2] * 5,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 3000,
        'sp': 5000,
        'maxCargo': 2,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    SKEL_BLOOD_SCOURGE_FR: {
        'setShipClass': SKEL_BLOOD_SCOURGE_FR,
        'modelClass': SKEL_INTERCEPTORL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': 0,
        'aftmastConfig': 0,
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 5,
        'leftBroadsides': [
            Cannons.Skel_L2] * 5,
        'rightBroadsides': [
            Cannons.Skel_L2] * 5,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonThunderbolt,
        'prow': 0,
        'hp': 4000,
        'sp': 5000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    SKEL_SHADOW_CROW_SP: {
        'setShipClass': SKEL_SHADOW_CROW_SP,
        'modelClass': SKEL_INTERCEPTORL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': 0,
        'aftmastConfig': 0,
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 5,
        'leftBroadsides': [
            Cannons.Skel_L2] * 5,
        'rightBroadsides': [
            Cannons.Skel_L2] * 5,
        'broadsideAmmo': InventoryType.CannonChainShot,
        'cannonAmmo': InventoryType.CannonFury,
        'prow': 0,
        'hp': 2500,
        'sp': 5000,
        'maxCargo': 1,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    SKEL_HELLHOUND_SP: {
        'setShipClass': SKEL_HELLHOUND_SP,
        'modelClass': SKEL_INTERCEPTORL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': 0,
        'aftmastConfig': 0,
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 5,
        'leftBroadsides': [
            Cannons.Skel_L2] * 5,
        'rightBroadsides': [
            Cannons.Skel_L2] * 5,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 3000,
        'sp': 6000,
        'maxCargo': 2,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    SKEL_BLOOD_SCOURGE_SP: {
        'setShipClass': SKEL_BLOOD_SCOURGE_SP,
        'modelClass': SKEL_INTERCEPTORL3,
        'defaultStyle': Styles.Undead,
        'mastConfig1': (Masts.Skel_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': 0,
        'aftmastConfig': 0,
        'sailLogo': 0,
        'cannons': [
            Cannons.Skel_L3] * 5,
        'leftBroadsides': [
            Cannons.Skel_L2] * 5,
        'rightBroadsides': [
            Cannons.Skel_L2] * 5,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonThunderbolt,
        'prow': 0,
        'hp': 4000,
        'sp': 8000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 6,
        'maxBroadsides': 14,
        'rammingPower': 600,
        'acceleration': 1.2 * defaultAcceleration,
        'maxSpeed': 0.9 * defaultMaxSpeed,
        'reverseAcceleration': 0.8 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.8 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    HUNTER_VENGENCE: {
        'setShipClass': HUNTER_VENGENCE,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.BountyHunter_A,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Bounty_Hunter_Wasp,
        'cannons': [
            Cannons.L3] * 12,
        'leftBroadsides': [
            Cannons.L2] * 10,
        'rightBroadsides': [
            Cannons.L2] * 10,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonExplosive,
        'prow': 0,
        'hp': 9000,
        'sp': 30000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.5 * defaultAcceleration,
        'maxSpeed': 1.2 * defaultMaxSpeed,
        'reverseAcceleration': 1.0 * defaultReverseAcceleration,
        'maxReverseSpeed': 1.0 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    HUNTER_CUTTER_SHARK: {
        'setShipClass': HUNTER_CUTTER_SHARK,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.BountyHunter_B,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Bandit_Claw,
        'cannons': [
            Cannons.L3] * 8,
        'leftBroadsides': [
            Cannons.L2] * 7,
        'rightBroadsides': [
            Cannons.L2] * 7,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 6400,
        'sp': 24000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 12,
        'maxBroadsides': 16,
        'rammingPower': 450,
        'acceleration': 2.0 * defaultAcceleration,
        'maxSpeed': 2.0 * defaultMaxSpeed,
        'reverseAcceleration': 1.0 * defaultReverseAcceleration,
        'maxReverseSpeed': 1.0 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    HUNTER_FLYING_STORM: {
        'setShipClass': HUNTER_FLYING_STORM,
        'modelClass': INTERCEPTORL3,
        'defaultStyle': Styles.BountyHunter_C,
        'mastConfig1': (Masts.Main_Tri, 2),
        'mastConfig2': 0,
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Tri, 1),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Bounty_Hunter_Snake,
        'cannons': [
            Cannons.L3] * 8,
        'leftBroadsides': [
            Cannons.L2] * 7,
        'rightBroadsides': [
            Cannons.L2] * 7,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonThunderbolt,
        'prow': 0,
        'hp': 6400,
        'sp': 24000,
        'maxCargo': 2,
        'maxCrew': 3,
        'maxCannons': 12,
        'maxBroadsides': 16,
        'rammingPower': 450,
        'acceleration': 2.0 * defaultAcceleration,
        'maxSpeed': 2.0 * defaultMaxSpeed,
        'reverseAcceleration': 1.0 * defaultReverseAcceleration,
        'maxReverseSpeed': 1.0 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    HUNTER_KILLYADED: {
        'setShipClass': HUNTER_KILLYADED,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.BountyHunter_D,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.Bounty_Hunter_Spider,
        'cannons': [
            Cannons.L3] * 10,
        'leftBroadsides': [
            Cannons.L2] * 10,
        'rightBroadsides': [
            Cannons.L2] * 10,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 9200,
        'sp': 25500,
        'maxCargo': 5,
        'maxCrew': 14,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    HUNTER_RED_DERVISH: {
        'setShipClass': HUNTER_RED_DERVISH,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.BountyHunter_E,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Bandit_Scorpion,
        'cannons': [
            Cannons.L3] * 12,
        'leftBroadsides': [
            Cannons.L2] * 10,
        'rightBroadsides': [
            Cannons.L2] * 10,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonExplosive,
        'prow': 0,
        'hp': 9000,
        'sp': 30000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.5 * defaultAcceleration,
        'maxSpeed': 1.2 * defaultMaxSpeed,
        'reverseAcceleration': 1.0 * defaultReverseAcceleration,
        'maxReverseSpeed': 1.0 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    HUNTER_CENTURY_HAWK: {
        'setShipClass': HUNTER_CENTURY_HAWK,
        'modelClass': MERCHANTL3,
        'defaultStyle': Styles.BountyHunter_F,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 2),
        'aftmastConfig': 0,
        'sailLogo': Logos.Bandit_Dagger,
        'cannons': [
            Cannons.L3] * 10,
        'leftBroadsides': [
            Cannons.L2] * 10,
        'rightBroadsides': [
            Cannons.L2] * 10,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 9200,
        'sp': 25500,
        'maxCargo': 5,
        'maxCrew': 14,
        'maxCannons': 10,
        'maxBroadsides': 24,
        'rammingPower': 600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn },
    HUNTER_SCORNED_SIREN: {
        'setShipClass': HUNTER_SCORNED_SIREN,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.BountyHunter_G,
        'mastConfig1': (Masts.Main_Square, 2),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Bandit_Claw,
        'cannons': [
            Cannons.L3] * 12,
        'leftBroadsides': [
            Cannons.L2] * 10,
        'rightBroadsides': [
            Cannons.L2] * 10,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonExplosive,
        'prow': 0,
        'hp': 9000,
        'sp': 10000,
        'maxCargo': 3,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.5 * defaultAcceleration,
        'maxSpeed': 1.2 * defaultMaxSpeed,
        'reverseAcceleration': 1.0 * defaultReverseAcceleration,
        'maxReverseSpeed': 1.0 * defaultMaxReverseAcceleration,
        'turn': 0.8 * defaultTurn,
        'maxTurn': 0.8 * defaultMaxTurn },
    HUNTER_TALLYHO: {
        'setShipClass': HUNTER_TALLYHO,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.NavyHunter,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Navy_Hunter_Unicorn,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonFirebrand,
        'cannonAmmo': InventoryType.CannonExplosive,
        'prow': 0,
        'hp': 20000,
        'sp': 45000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    HUNTER_BATTLEROYALE: {
        'setShipClass': HUNTER_BATTLEROYALE,
        'modelClass': SHIP_OF_THE_LINE,
        'defaultStyle': Styles.NavyHunter,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': (Masts.Main_Square, 3),
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Navy_Hunter_Lion,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L2] * 12,
        'rightBroadsides': [
            Cannons.L2] * 12,
        'broadsideAmmo': InventoryType.CannonExplosive,
        'cannonAmmo': InventoryType.CannonFirebrand,
        'prow': 0,
        'hp': 20000,
        'sp': 45000,
        'maxCargo': 8,
        'maxCrew': 12,
        'maxCannons': 14,
        'maxBroadsides': 12,
        'rammingPower': 3600,
        'acceleration': 1.0 * defaultAcceleration,
        'maxSpeed': 0.7 * defaultMaxSpeed,
        'reverseAcceleration': 0.6 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.6 * defaultMaxReverseAcceleration,
        'turn': 0.5 * defaultTurn,
        'maxTurn': 0.5 * defaultMaxTurn },
    HUNTER_EN_GARDE: {
        'setShipClass': HUNTER_EN_GARDE,
        'modelClass': WARSHIPL3,
        'defaultStyle': Styles.NavyHunter,
        'mastConfig1': (Masts.Main_Square, 3),
        'mastConfig2': (Masts.Main_Square, 3),
        'mastConfig3': 0,
        'foremastConfig': (Masts.Fore_Multi, 3),
        'aftmastConfig': (Masts.Aft_Tri, 1),
        'sailLogo': Logos.Navy_Hunter_Unicorn,
        'cannons': [
            Cannons.L3] * 14,
        'leftBroadsides': [
            Cannons.L4] * 9,
        'rightBroadsides': [
            Cannons.L4] * 9,
        'broadsideAmmo': InventoryType.CannonRoundShot,
        'cannonAmmo': InventoryType.CannonThunderbolt,
        'prow': 0,
        'hp': 10000,
        'sp': 36000,
        'maxCargo': 5,
        'maxCrew': 8,
        'maxCannons': 14,
        'maxBroadsides': 20,
        'rammingPower': 900,
        'acceleration': 1.1 * defaultAcceleration,
        'maxSpeed': 0.8 * defaultMaxSpeed,
        'reverseAcceleration': 0.7 * defaultReverseAcceleration,
        'maxReverseSpeed': 0.7 * defaultMaxReverseAcceleration,
        'turn': 0.6 * defaultTurn,
        'maxTurn': 0.6 * defaultMaxTurn } }

def getShipConfig(shipClass):
    hullInfo = __shipConfigs.get(shipClass)
    return hullInfo


def getModelClass(shipClass):
    shipData = getShipConfig(shipClass)
    if shipData:
        return shipData['modelClass']

    return 0

__shipRepairCostMultiplier = {
    INTERCEPTORL1: 0.15,
    MERCHANTL1: 0.2,
    WARSHIPL1: 0.25,
    INTERCEPTORL2: 0.15,
    MERCHANTL2: 0.2,
    WARSHIPL2: 0.25,
    INTERCEPTORL3: 0.15,
    MERCHANTL3: 0.2,
    WARSHIPL3: 0.25,
    SHIP_OF_THE_LINE: 0.5,
    GOLIATH: 0.25,
    BLACK_PEARL: 0.25,
    SKEL_WARSHIPL3: 0.25,
    SKEL_INTERCEPTORL3: 0.25,
    JOLLY_ROGER: 0.0 }

def getRepairCostMult(modelClass):
    return __shipRepairCostMultiplier.get(modelClass)


def getRepairCost(ship, hull = None, cabin = None, masts = [], sails = [], prow = None, ram = None):
    return calcRepairCost(ship.maxHp, ship.Hp, ship.maxSp, ship.Sp, ship.modelClass)


def calcRepairCost(maxHp, Hp, maxSp, Sp, modelClass):
    totalCost = 0
    totalCost += (maxHp - Hp) + (maxSp - Sp) / 2
    if Hp <= 0:
        totalCost = totalCost * SUNK_REPAIR_COST_MULTIPLIER

    mult = getRepairCostMult(modelClass)
    if mult:
        totalCost *= mult

    totalCost = totalCost / 100.0
    return int(math.ceil(totalCost))

__enemyAIShipSpeed = {
    WARSHIPL1: ([
        50,
        100,
        115,
        135], [
        10,
        10]),
    WARSHIPL2: ([
        50,
        100,
        115,
        135], [
        10,
        10]),
    WARSHIPL3: ([
        50,
        100,
        115,
        135], [
        10,
        10]),
    MERCHANTL1: ([
        45,
        90,
        105,
        125], [
        6,
        6]),
    MERCHANTL2: ([
        45,
        90,
        105,
        125], [
        6,
        6]),
    MERCHANTL3: ([
        45,
        90,
        105,
        125], [
        6,
        6]),
    INTERCEPTORL1: ([
        55,
        110,
        125,
        145], [
        16,
        16]),
    INTERCEPTORL2: ([
        55,
        110,
        125,
        145], [
        16,
        16]),
    INTERCEPTORL3: ([
        55,
        110,
        125,
        145], [
        16,
        16]),
    QUEEN_ANNES_REVENGE: ([
        52,
        105,
        120,
        140], [
        13,
        13]),
    HUNTER_VENGENCE: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_CUTTER_SHARK: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_FLYING_STORM: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_KILLYADED: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_RED_DERVISH: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_CENTURY_HAWK: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_SCORNED_SIREN: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_TALLYHO: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_BATTLEROYALE: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HUNTER_EN_GARDE: ([
        100,
        150,
        200,
        250], [
        20,
        20]),
    HMS_VICTORY: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    HMS_NEWCASTLE: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    HMS_INVINCIBLE: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    EITC_INTREPID: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    EITC_CONQUERER: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    EITC_LEVIATHAN: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    NAVY_KRAKEN_HUNTER: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    STUMPY_SHIP: ([
        8,
        8,
        8,
        8], [
        6,
        6]),
    BLACK_PEARL: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    GOLIATH: ([
        50,
        100,
        150,
        200], [
        14,
        14]),
    JOLLY_ROGER: ([
        70,
        130,
        145,
        165], [
        20,
        20]),
    NAVY_PANTHER: ([
        25,
        60,
        105,
        125], [
        7,
        7]),
    NAVY_CENTURION: ([
        30,
        65,
        110,
        130], [
        8,
        8]),
    NAVY_MAN_O_WAR: ([
        35,
        70,
        115,
        135], [
        9,
        9]),
    NAVY_DREADNOUGHT: ([
        35,
        70,
        115,
        135], [
        9,
        9]),
    NAVY_ELITE: ([
        35,
        70,
        115,
        135], [
        9,
        9]),
    NAVY_BULWARK: ([
        20,
        50,
        95,
        115], [
        5,
        5]),
    NAVY_VANGUARD: ([
        25,
        55,
        100,
        120], [
        6,
        6]),
    NAVY_MONARCH: ([
        30,
        60,
        105,
        125], [
        7,
        7]),
    NAVY_COLOSSUS: ([
        30,
        60,
        105,
        125], [
        7,
        7]),
    NAVY_BASTION: ([
        30,
        60,
        105,
        125], [
        7,
        7]),
    NAVY_FERRET: ([
        30,
        70,
        115,
        135], [
        10,
        10]),
    NAVY_GREYHOUND: ([
        35,
        75,
        120,
        140], [
        11,
        11]),
    NAVY_KINGFISHER: ([
        40,
        80,
        125,
        145], [
        12,
        12]),
    NAVY_PREDATOR: ([
        40,
        80,
        125,
        145], [
        12,
        12]),
    EITC_CORVETTE: ([
        25,
        60,
        105,
        125], [
        7,
        7]),
    EITC_MARAUDER: ([
        30,
        65,
        110,
        130], [
        8,
        8]),
    EITC_WARLORD: ([
        35,
        70,
        115,
        135], [
        9,
        9]),
    EITC_JUGGERNAUT: ([
        35,
        70,
        115,
        135], [
        9,
        9]),
    EITC_TYRANT: ([
        35,
        70,
        115,
        135], [
        9,
        9]),
    EITC_SENTINEL: ([
        20,
        50,
        95,
        115], [
        5,
        5]),
    EITC_IRONWALL: ([
        25,
        55,
        100,
        120], [
        6,
        6]),
    EITC_OGRE: ([
        30,
        60,
        105,
        125], [
        7,
        7]),
    EITC_BEHEMOTH: ([
        30,
        60,
        105,
        125], [
        7,
        7]),
    EITC_SEA_VIPER: ([
        30,
        70,
        115,
        135], [
        10,
        10]),
    EITC_BLOODHOUND: ([
        35,
        75,
        120,
        140], [
        11,
        11]),
    EITC_BARRACUDA: ([
        40,
        80,
        125,
        145], [
        12,
        12]),
    EITC_CORSAIR: ([
        40,
        80,
        125,
        145], [
        12,
        12]),
    SKEL_PHANTOM: ([
        35,
        70,
        115,
        135], [
        10,
        10]),
    SKEL_REVENANT: ([
        35,
        70,
        115,
        135], [
        11,
        11]),
    SKEL_STORM_REAPER: ([
        40,
        75,
        120,
        140], [
        11,
        11]),
    SKEL_BLACK_HARBINGER: ([
        40,
        75,
        120,
        140], [
        12,
        12]),
    SKEL_DEATH_OMEN: ([
        45,
        80,
        125,
        145], [
        12,
        12]),
    SKEL_SHADOW_CROW_FR: ([
        40,
        80,
        125,
        145], [
        12,
        12]),
    SKEL_HELLHOUND_FR: ([
        40,
        80,
        125,
        145], [
        13,
        13]),
    SKEL_BLOOD_SCOURGE_FR: ([
        45,
        85,
        130,
        150], [
        14,
        14]),
    SKEL_SHADOW_CROW_SP: ([
        40,
        80,
        125,
        145], [
        12,
        12]),
    SKEL_HELLHOUND_SP: ([
        40,
        80,
        125,
        145], [
        13,
        13]),
    SKEL_BLOOD_SCOURGE_SP: ([
        45,
        85,
        130,
        150], [
        14,
        14]) }

def getAIShipSpeed(shipClass):
    speedList = __enemyAIShipSpeed.get(shipClass)
    if speedList:
        return speedList
    else:
        return ([], [])

KrakenLocators = {
    INTERCEPTORL1: ((Point3(40, 20, -5), 0.5, Point3(0), 0.9), (Point3(40, -40, -5), 0.5, Point3(0), 0.9)),
    INTERCEPTORL2: ((Point3(50, 40, -5), 0.75, Point3(0), 0.9), (Point3(50, -70, -5), 0.75, Point3(0), 0.9)),
    INTERCEPTORL3: ((Point3(60, 80, 0), 0.8, Point3(0), 0.9), (Point3(60, -30, 0), 0.8, Point3(0), 0.9)),
    MERCHANTL1: ((Point3(30, 50, -5), 0.6, Point3(0), 0.9), (Point3(40, -10, -5), 0.6, Point3(0), 0.9), (Point3(40, -70, -5), 0.6, Point3(0), 0.9)),
    MERCHANTL2: ((Point3(50, 50, 0), 0.8, Point3(0), 0.9), (Point3(50, -10, 0), 0.8, Point3(0), 0.9), (Point3(50, -70, 0), 0.8, Point3(0), 0.9)),
    MERCHANTL3: ((Point3(60, 50, 0), 1, Point3(0), 0.9), (Point3(70, -10, 0), 1, Point3(0), 0.9), (Point3(70, -120, 0), 1, Point3(0), 0.9)),
    WARSHIPL1: ((Point3(30, 50, -15), 0.6, Point3(0, 22, 0), 0.7), (Point3(40, -10, -15), 0.6, Point3(0), 0.8), (Point3(40, -70, -15), 0.6, Point3(0), 0.8)),
    WARSHIPL2: ((Point3(40, 90, -15), 0.8, Point3(10, 25, 0), 0.8), (Point3(50, 10, -15), 0.8, Point3(0), 0.9), (Point3(50, -70, -15), 0.8, Point3(0), 0.9)),
    WARSHIPL3: ((Point3(50, 90, -15), 1, Point3(-20, 15, 0), 0.6), (Point3(60, 10, -15), 1, Point3(0), 0.8), (Point3(60, -120, -15), 1, Point3(0), 0.9)),
    SHIP_OF_THE_LINE: ((Point3(50, 90, -15), 1, Point3(-20, 15, 0), 0.6), (Point3(60, 10, -15), 1, Point3(0), 0.8), (Point3(60, -120, -15), 1, Point3(0), 0.9)) }
__shipSplitOffsets = {
    INTERCEPTORL1: (10.0, 0),
    INTERCEPTORL2: (2.0, 0),
    INTERCEPTORL3: (5.0, 0),
    MERCHANTL1: (13.0, -1),
    MERCHANTL2: (0.0, 1),
    MERCHANTL3: (5.0, 0),
    WARSHIPL1: (5.0, -1),
    WARSHIPL2: (-5.0, -1),
    WARSHIPL3: (0.0, -1),
    SHIP_OF_THE_LINE: (0.0, -1),
    HMS_VICTORY: (0.0, -1),
    HMS_NEWCASTLE: (0.0, -1),
    HMS_INVINCIBLE: (0.0, -1),
    EITC_INTREPID: (0.0, -1),
    EITC_CONQUERER: (0.0, -1),
    EITC_LEVIATHAN: (0.0, -1),
    NAVY_KRAKEN_HUNTER: (0.0, -1),
    BLACK_PEARL: (0.0, -1),
    GOLIATH: (0.0, -1) }

def getShipSplitOffset(modelClass):
    offset = __shipSplitOffsets.get(modelClass)
    if offset:
        return offset[0]
    else:
        return 0.0

INVALID_TEAM = -1
PLAYER_TEAM = 0
UNDEAD_TEAM = 1
NAVY_TEAM = 2
TRADING_CO_TEAM = 3
FRENCH_UNDEAD_TEAM = 7
SPANISH_UNDEAD_TEAM = 8
VOODOO_ZOMBIE_TEAM = 10
BOUNTY_HUNTER_TEAM = 11
LEVEL_INDEX = 0
TEAM_INDEX = 1
ENABLED_INDEX = 2
shipData = {
    HMS_VICTORY: [
        80,
        NAVY_TEAM,
        1],
    HMS_NEWCASTLE: [
        80,
        NAVY_TEAM,
        1],
    HMS_INVINCIBLE: [
        80,
        NAVY_TEAM,
        1],
    EITC_INTREPID: [
        80,
        TRADING_CO_TEAM,
        1],
    EITC_CONQUERER: [
        80,
        TRADING_CO_TEAM,
        1],
    EITC_LEVIATHAN: [
        80,
        TRADING_CO_TEAM,
        1],
    NAVY_KRAKEN_HUNTER: [
        80,
        NAVY_TEAM,
        1],
    NAVY_FERRET: [
        2,
        NAVY_TEAM,
        1],
    NAVY_BULWARK: [
        6,
        NAVY_TEAM,
        1],
    NAVY_PANTHER: [
        9,
        NAVY_TEAM,
        1],
    NAVY_GREYHOUND: [
        12,
        NAVY_TEAM,
        1],
    NAVY_VANGUARD: [
        16,
        NAVY_TEAM,
        1],
    NAVY_CENTURION: [
        19,
        NAVY_TEAM,
        1],
    NAVY_KINGFISHER: [
        22,
        NAVY_TEAM,
        1],
    NAVY_MONARCH: [
        26,
        NAVY_TEAM,
        1],
    NAVY_MAN_O_WAR: [
        29,
        NAVY_TEAM,
        1],
    NAVY_PREDATOR: [
        32,
        NAVY_TEAM,
        1],
    NAVY_COLOSSUS: [
        36,
        NAVY_TEAM,
        1],
    NAVY_DREADNOUGHT: [
        39,
        NAVY_TEAM,
        1],
    NAVY_BASTION: [
        60,
        NAVY_TEAM,
        1],
    NAVY_ELITE: [
        70,
        NAVY_TEAM,
        1],
    GOLIATH: [
        40,
        NAVY_TEAM,
        1],
    BLACK_PEARL: [
        30,
        PLAYER_TEAM,
        1],
    QUEEN_ANNES_REVENGE: [
        40,
        VOODOO_ZOMBIE_TEAM,
        1],
    HUNTER_VENGENCE: [
        50,
        BOUNTY_HUNTER_TEAM,
        1],
    HUNTER_CUTTER_SHARK: [
        50,
        BOUNTY_HUNTER_TEAM,
        1],
    HUNTER_FLYING_STORM: [
        50,
        BOUNTY_HUNTER_TEAM,
        1],
    HUNTER_KILLYADED: [
        50,
        BOUNTY_HUNTER_TEAM,
        1],
    HUNTER_RED_DERVISH: [
        50,
        BOUNTY_HUNTER_TEAM,
        1],
    HUNTER_CENTURY_HAWK: [
        50,
        BOUNTY_HUNTER_TEAM,
        1],
    HUNTER_SCORNED_SIREN: [
        50,
        BOUNTY_HUNTER_TEAM,
        1],
    HUNTER_TALLYHO: [
        60,
        NAVY_TEAM,
        1],
    HUNTER_BATTLEROYALE: [
        60,
        NAVY_TEAM,
        1],
    HUNTER_EN_GARDE: [
        60,
        NAVY_TEAM,
        1],
    EITC_SEA_VIPER: [
        7,
        TRADING_CO_TEAM,
        1],
    EITC_SENTINEL: [
        11,
        TRADING_CO_TEAM,
        1],
    EITC_CORVETTE: [
        14,
        TRADING_CO_TEAM,
        1],
    EITC_BLOODHOUND: [
        17,
        TRADING_CO_TEAM,
        1],
    EITC_IRONWALL: [
        21,
        TRADING_CO_TEAM,
        1],
    EITC_MARAUDER: [
        24,
        TRADING_CO_TEAM,
        1],
    EITC_BARRACUDA: [
        27,
        TRADING_CO_TEAM,
        1],
    EITC_OGRE: [
        31,
        TRADING_CO_TEAM,
        1],
    EITC_WARLORD: [
        34,
        TRADING_CO_TEAM,
        1],
    EITC_CORSAIR: [
        37,
        TRADING_CO_TEAM,
        1],
    EITC_BEHEMOTH: [
        41,
        TRADING_CO_TEAM,
        1],
    EITC_JUGGERNAUT: [
        44,
        TRADING_CO_TEAM,
        1],
    EITC_TYRANT: [
        70,
        TRADING_CO_TEAM,
        1],
    SKEL_PHANTOM: [
        18,
        UNDEAD_TEAM,
        1],
    SKEL_REVENANT: [
        26,
        UNDEAD_TEAM,
        1],
    SKEL_STORM_REAPER: [
        31,
        UNDEAD_TEAM,
        1],
    SKEL_BLACK_HARBINGER: [
        36,
        UNDEAD_TEAM,
        1],
    SKEL_DEATH_OMEN: [
        42,
        UNDEAD_TEAM,
        1],
    JOLLY_ROGER: [
        60,
        UNDEAD_TEAM,
        1],
    SKEL_SHADOW_CROW_FR: [
        18,
        FRENCH_UNDEAD_TEAM,
        1],
    SKEL_HELLHOUND_FR: [
        21,
        FRENCH_UNDEAD_TEAM,
        1],
    SKEL_BLOOD_SCOURGE_FR: [
        28,
        FRENCH_UNDEAD_TEAM,
        1],
    SKEL_SHADOW_CROW_SP: [
        18,
        SPANISH_UNDEAD_TEAM,
        1],
    SKEL_HELLHOUND_SP: [
        21,
        SPANISH_UNDEAD_TEAM,
        1],
    SKEL_BLOOD_SCOURGE_SP: [
        28,
        SPANISH_UNDEAD_TEAM,
        1] }

def getShipTeam(shipClass):
    if shipClass in shipData:
        return shipData[shipClass][TEAM_INDEX]
    else:
        return PLAYER_TEAM

BaseLevel = {
    INTERCEPTORL1: 2,
    MERCHANTL1: 4,
    WARSHIPL1: 8,
    INTERCEPTORL2: 12,
    MERCHANTL2: 16,
    WARSHIPL2: 20,
    INTERCEPTORL3: 26,
    MERCHANTL3: 30,
    WARSHIPL3: 34,
    QUEEN_ANNES_REVENGE: 32,
    BLACK_PEARL: 40,
    SKEL_WARSHIPL3: 32,
    SKEL_INTERCEPTORL3: 26,
    JOLLY_ROGER: 60,
    GOLIATH: 50,
    SHIP_OF_THE_LINE: 80,
    QUEEN_ANNES_REVENGE: 40 }
__shipLevelStatMultiplier = {
    0: (0.5, 0, 10),
    1: (0.7, 0, 15),
    2: (0.9, 0, 20),
    3: (1.1, 0, 25),
    4: (1.3, 0, 30),
    5: (1.5, 0, 35),
    6: (1.7, 0, 40),
    7: (1.9, 0, 45),
    8: (2.1, 0, 50),
    9: (2.2, 0, 55),
    10: (2.5, 0, 60),
    11: (2.7, 0, 65),
    12: (2.9, 0, 70),
    13: (3.1, 0, 75),
    14: (3.3, 0, 80),
    15: (3.5, 0, 85),
    16: (3.7, 0, 90),
    17: (3.9, 0, 95),
    18: (4.1, 0, 100),
    19: (4.3, 0, 105),
    20: (4.5, 0, 110),
    21: (4.7, 0, 115),
    22: (4.9, 0, 120),
    23: (5.1, 0, 125),
    24: (5.3, 0, 130),
    25: (5.5, 0, 135),
    26: (5.7, 0, 140),
    27: (5.9, 0, 145),
    28: (6.1, 0, 150),
    29: (6.3, 0, 155),
    30: (6.5, 0, 160),
    31: (6.7, 0, 165),
    32: (6.9, 0, 170),
    33: (7.1, 0, 175),
    34: (7.3, 0, 180),
    35: (7.5, 0, 185),
    36: (7.7, 0, 190),
    37: (7.9, 0, 195),
    38: (8.1, 0, 200),
    39: (8.3, 0, 205),
    40: (8.5, 0, 210),
    41: (8.7, 0, 215),
    42: (8.9, 0, 220),
    43: (9.1, 0, 225),
    44: (9.3, 0, 230),
    45: (9.5, 0, 235),
    46: (9.7, 0, 240),
    47: (9.9, 0, 245),
    48: (10.1, 0, 250),
    49: (10.3, 0, 255),
    50: (10.5, 0, 260),
    51: (10.7, 0, 265),
    52: (10.9, 0, 270),
    53: (11.1, 0, 275),
    54: (11.3, 0, 280),
    55: (11.5, 0, 285),
    56: (11.7, 0, 290),
    57: (11.9, 0, 295),
    58: (12.1, 0, 300),
    59: (12.3, 0, 305),
    60: (12.5, 0, 310),
    61: (12.7, 0, 315),
    62: (12.9, 0, 320),
    63: (13.1, 0, 325),
    64: (13.3, 0, 330),
    65: (13.5, 0, 335),
    66: (13.7, 0, 340),
    67: (13.9, 0, 345),
    68: (14.1, 0, 350),
    69: (14.3, 0, 355),
    70: (14.5, 0, 360),
    71: (14.7, 0, 365),
    72: (14.9, 0, 370),
    73: (15.1, 0, 375),
    74: (15.3, 0, 380),
    75: (15.5, 0, 385),
    76: (15.7, 0, 390),
    77: (15.9, 0, 395),
    78: (16.1, 0, 400),
    79: (16.3, 0, 405),
    80: (16.5, 0, 410),
    81: (16.7, 0, 415),
    82: (16.9, 0, 420),
    83: (17.1, 0, 425),
    84: (17.3, 0, 430),
    85: (17.5, 0, 435),
    86: (17.7, 0, 440),
    87: (17.9, 0, 445),
    88: (18.1, 0, 450),
    89: (18.3, 0, 455),
    90: (18.5, 0, 460),
    91: (18.7, 0, 465),
    92: (18.9, 0, 470),
    93: (19.1, 0, 475),
    94: (19.3, 0, 480),
    95: (19.5, 0, 485),
    96: (19.7, 0, 490),
    97: (19.9, 0, 495),
    98: (20.1, 0, 505),
    99: (20.3, 0, 500),
    100: (20.5, 0, 515) }

def getModifiedShipStats(level):
    modifiers = __shipLevelStatMultiplier.get(level)
    return modifiers


def getShipExp(level):
    modifiers = __shipLevelStatMultiplier.get(level)
    if modifiers:
        return modifiers[2]

    return modifiers


def getRandomShipLevel(shipClass):
    notRandomized = (JOLLY_ROGER, BLACK_PEARL, GOLIATH)
    baselevel = getShipLevel(shipClass)
    if shipClass not in notRandomized:
        baselevel += random.randint(-1, 1)

    baselevel = min(len(__shipLevelStatMultiplier.keys()) - 1, baselevel)
    return baselevel


def getShipLevel(shipClass):
    if shipClass in shipData:
        value = shipData[shipClass][LEVEL_INDEX]
        if value == None:
            set_trace()

        return value
    else:
        return 2

WaterlineOffsets = {
    INTERCEPTORL1: -4,
    INTERCEPTORL2: -4,
    INTERCEPTORL3: -4,
    MERCHANTL1: -4,
    MERCHANTL2: -4,
    MERCHANTL3: -4,
    WARSHIPL1: -4,
    WARSHIPL2: -4,
    WARSHIPL3: -4,
    QUEEN_ANNES_REVENGE: -4,
    BLACK_PEARL: -10,
    GOLIATH: -10,
    SKEL_WARSHIPL3: -4,
    SKEL_INTERCEPTORL3: -4,
    SHIP_OF_THE_LINE: -10 }
TiltFakeMass = {
    INTERCEPTORL1: 1.0,
    INTERCEPTORL2: 1.4,
    INTERCEPTORL3: 1.7,
    MERCHANTL1: 2.5,
    MERCHANTL2: 3.0,
    MERCHANTL3: 3.5,
    WARSHIPL1: 2.5,
    WARSHIPL2: 3.0,
    WARSHIPL3: 4.0,
    QUEEN_ANNES_REVENGE: 1.7,
    SHIP_OF_THE_LINE: 4.5,
    BLACK_PEARL: 4.5,
    GOLIATH: 4.5,
    SKEL_INTERCEPTORL3: 1.7,
    SKEL_WARSHIPL3: 4.0 }
SamplePoints = Enum('\n    FL, F, FR,\n     L, C,  R,\n    BL, B, BR,\n    ')
SamplePointOffsets = {
    INTERCEPTORL1: [
        (0, -11),
        {
            SamplePoints.FL: (-13, 29),
            SamplePoints.F: (0, 29),
            SamplePoints.FR: (13, 29),
            SamplePoints.L: (-13, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (13, 0),
            SamplePoints.BL: (-13, -29),
            SamplePoints.B: (0, -29),
            SamplePoints.BR: (13, -29) }],
    INTERCEPTORL2: [
        (0, -8),
        {
            SamplePoints.FL: (-20, 50),
            SamplePoints.F: (0, 50),
            SamplePoints.FR: (20, 50),
            SamplePoints.L: (-20, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (20, 0),
            SamplePoints.BL: (-20, -50),
            SamplePoints.B: (0, -50),
            SamplePoints.BR: (20, -50) },
        -5],
    INTERCEPTORL3: [
        (0, 0),
        {
            SamplePoints.FL: (-26, 50),
            SamplePoints.F: (0, 50),
            SamplePoints.FR: (26, 50),
            SamplePoints.L: (-26, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (26, 0),
            SamplePoints.BL: (-26, -50),
            SamplePoints.B: (0, -50),
            SamplePoints.BR: (26, -50) },
        -5],
    MERCHANTL1: [
        (0, 0),
        {
            SamplePoints.FL: (-23, 33),
            SamplePoints.F: (0, 33),
            SamplePoints.FR: (23, 33),
            SamplePoints.L: (-23, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (23, 0),
            SamplePoints.BL: (-23, -33),
            SamplePoints.B: (0, -33),
            SamplePoints.BR: (23, -33) }],
    MERCHANTL2: [
        (0, 0),
        {
            SamplePoints.FL: (-35, 60),
            SamplePoints.F: (0, 60),
            SamplePoints.FR: (35, 60),
            SamplePoints.L: (-35, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (35, 0),
            SamplePoints.BL: (-35, -60),
            SamplePoints.B: (0, -60),
            SamplePoints.BR: (35, -60) }],
    MERCHANTL3: [
        (0, 0),
        {
            SamplePoints.FL: (-38, 68),
            SamplePoints.F: (0, 68),
            SamplePoints.FR: (38, 68),
            SamplePoints.L: (-38, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (38, 0),
            SamplePoints.BL: (-38, -68),
            SamplePoints.B: (0, -68),
            SamplePoints.BR: (38, -68) }],
    WARSHIPL1: [
        (0, -5),
        {
            SamplePoints.FL: (-22, 45),
            SamplePoints.F: (0, 45),
            SamplePoints.FR: (22, 45),
            SamplePoints.L: (-22, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (22, 0),
            SamplePoints.BL: (-22, -45),
            SamplePoints.B: (0, -45),
            SamplePoints.BR: (22, -45) }],
    WARSHIPL2: [
        (0, 0),
        {
            SamplePoints.FL: (-28, 64),
            SamplePoints.F: (0, 64),
            SamplePoints.FR: (28, 64),
            SamplePoints.L: (-28, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (28, 0),
            SamplePoints.BL: (-28, -64),
            SamplePoints.B: (0, -64),
            SamplePoints.BR: (28, -64) }],
    WARSHIPL3: [
        (0, -5),
        {
            SamplePoints.FL: (-42, 84),
            SamplePoints.F: (0, 84),
            SamplePoints.FR: (42, 84),
            SamplePoints.L: (-42, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (42, 0),
            SamplePoints.BL: (-42, -84),
            SamplePoints.B: (0, -84),
            SamplePoints.BR: (42, -84) }],
    QUEEN_ANNES_REVENGE: [
        (0, 0),
        {
            SamplePoints.FL: (-26, 50),
            SamplePoints.F: (0, 50),
            SamplePoints.FR: (26, 50),
            SamplePoints.L: (-26, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (26, 0),
            SamplePoints.BL: (-26, -50),
            SamplePoints.B: (0, -50),
            SamplePoints.BR: (26, -50) },
        -5],
    SHIP_OF_THE_LINE: [
        (0, -5),
        {
            SamplePoints.FL: (-32, 94),
            SamplePoints.F: (0, 94),
            SamplePoints.FR: (32, 94),
            SamplePoints.L: (-32, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (32, 0),
            SamplePoints.BL: (-32, -94),
            SamplePoints.B: (0, -94),
            SamplePoints.BR: (32, -94) }],
    BLACK_PEARL: [
        (0, -5),
        {
            SamplePoints.FL: (-32, 94),
            SamplePoints.F: (0, 94),
            SamplePoints.FR: (32, 94),
            SamplePoints.L: (-32, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (32, 0),
            SamplePoints.BL: (-32, -94),
            SamplePoints.B: (0, -94),
            SamplePoints.BR: (32, -94) }],
    GOLIATH: [
        (0, -5),
        {
            SamplePoints.FL: (-32, 94),
            SamplePoints.F: (0, 94),
            SamplePoints.FR: (32, 94),
            SamplePoints.L: (-32, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (32, 0),
            SamplePoints.BL: (-32, -94),
            SamplePoints.B: (0, -94),
            SamplePoints.BR: (32, -94) }],
    SKEL_INTERCEPTORL3: [
        (0, 0),
        {
            SamplePoints.FL: (-26, 50),
            SamplePoints.F: (0, 50),
            SamplePoints.FR: (26, 50),
            SamplePoints.L: (-26, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (26, 0),
            SamplePoints.BL: (-26, -50),
            SamplePoints.B: (0, -50),
            SamplePoints.BR: (26, -50) }],
    SKEL_WARSHIPL3: [
        (0, -5),
        {
            SamplePoints.FL: (-42, 84),
            SamplePoints.F: (0, 84),
            SamplePoints.FR: (42, 84),
            SamplePoints.L: (-42, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (42, 0),
            SamplePoints.BL: (-42, -84),
            SamplePoints.B: (0, -84),
            SamplePoints.BR: (42, -84) }],
    JOLLY_ROGER: [
        (0, -5),
        {
            SamplePoints.FL: (-42, 84),
            SamplePoints.F: (0, 84),
            SamplePoints.FR: (42, 84),
            SamplePoints.L: (-42, 0),
            SamplePoints.C: (0, 0),
            SamplePoints.R: (42, 0),
            SamplePoints.BL: (-42, -84),
            SamplePoints.B: (0, -84),
            SamplePoints.BR: (42, -84) }] }
__boardingSphere = {
    WARSHIPL1: ((Vec3(0, 0, 100), 90), 25),
    WARSHIPL2: ((Vec3(0, 0, 100), 90), 45),
    WARSHIPL3: ((Vec3(-6.0, 13.0, 21.9), -90), 60),
    MERCHANTL1: ((Vec3(0, 0, 100), 90), 25),
    MERCHANTL2: ((Vec3(8, -11, 33), 90), 40),
    MERCHANTL3: ((Vec3(0, 0, 100), 90), 55),
    INTERCEPTORL1: ((Vec3(2.74993, 23.197, 9.27622), 90), 25),
    INTERCEPTORL2: ((Vec3(0, 0, 100), 90), 35),
    INTERCEPTORL3: ((Vec3(11.9, -1.7117, 21.8932), -29), 45),
    QUEEN_ANNES_REVENGE: ((Vec3(11.9, -1.7117, 21.8932), -29), 45),
    SHIP_OF_THE_LINE: ((Vec3(-6.0, 13.0, 21.9), -90), 60),
    BLACK_PEARL: ((Vec3(-6.0, 13.0, 21.9), -90), 60),
    GOLIATH: ((Vec3(-6.0, 13.0, 21.9), -90), 60),
    STUMPY_SHIP: ((Vec3(2.74993, 23.197, 9.27622), 90), 25),
    SKEL_WARSHIPL3: ((Vec3(-6.0, 13.0, 21.9), -90), 60),
    SKEL_INTERCEPTORL3: ((Vec3(11.9, -1.7117, 21.8932), -29), 45) }
__exitSphere = {
    WARSHIPL1: (21.26, 13.44, 21.93),
    WARSHIPL2: (21.26, 13.44, 21.93),
    WARSHIPL3: (21.26, 13.44, 21.93),
    MERCHANTL1: (-5.44, 6.735, 12.278),
    MERCHANTL2: (-5.4, 6.735, 12.278),
    MERCHANTL3: (-5.4, 6.735, 12.278),
    INTERCEPTORL1: (2.354, -15.201, 5.493),
    INTERCEPTORL2: (2.354, -15.201, 5.493),
    INTERCEPTORL3: (2.354, -15.201, 5.493),
    QUEEN_ANNES_REVENGE: (2.354, -15.201, 5.493),
    SHIP_OF_THE_LINE: (21.26, 13.44, 21.93),
    BLACK_PEARL: (21.26, 13.44, 21.93),
    GOLIATH: (21.26, 13.44, 21.93),
    SKEL_WARSHIPL3: (21.26, 13.44, 21.93),
    SKEL_INTERCEPTORL3: (2.354, -15.201, 5.493) }
BOARDING_POS_H_INDEX = 0
BOARDING_SCALE_INDEX = 1

def getBoardingSpherePosH(modelClass):
    return __boardingSphere.get(modelClass)[BOARDING_POS_H_INDEX]


def getBoardingSphereScale(modelClass):
    return __boardingSphere.get(modelClass)[BOARDING_SCALE_INDEX]


def getExitSpherePos(modelClass):
    return __exitSphere.get(modelClass)

__boardingRopeHeight = {
    WARSHIPL1: 0.6,
    WARSHIPL2: 0.8,
    WARSHIPL3: 1.0,
    MERCHANTL1: 0.6,
    MERCHANTL2: 0.8,
    MERCHANTL3: 1.0,
    INTERCEPTORL1: 0.5,
    INTERCEPTORL2: 0.7,
    INTERCEPTORL3: 1.0,
    QUEEN_ANNES_REVENGE: 1.0,
    SHIP_OF_THE_LINE: 1.0,
    BLACK_PEARL: 1.0,
    GOLIATH: 1.0,
    SKEL_WARSHIPL3: 1.0,
    SKEL_INTERCEPTORL3: 0.8 }

def getBoardingRopeH(modelClass):
    return __boardingRopeHeight.get(modelClass)

AI_RAM_LATENCY_BUFFER = 500
__rammingSphereValues = {
    WARSHIPL1: (0, 140, 10, 30),
    WARSHIPL2: (0, 160, 15, 40),
    WARSHIPL3: (0, 180, 20, 50),
    MERCHANTL1: (0, 120, 10, 30),
    MERCHANTL2: (0, 140, 15, 40),
    MERCHANTL3: (0, 160, 20, 50),
    INTERCEPTORL1: (0, 110, 10, 30),
    INTERCEPTORL2: (0, 130, 15, 40),
    INTERCEPTORL3: (0, 150, 20, 50),
    QUEEN_ANNES_REVENGE: (0, 150, 20, 50),
    SHIP_OF_THE_LINE: (0, 190, 20, 50),
    BLACK_PEARL: (0, 190, 20, 50),
    GOLIATH: (0, 190, 20, 50),
    SKEL_WARSHIPL3: (0, 180, 20, 50),
    SKEL_INTERCEPTORL3: (0, 150, 20, 50) }

def getRammingSphereScale(modelClass):
    return __rammingSphereValues.get(modelClass)

BROADSIDE_MAX_AUTOAIM_DIST = 2000
BROADSIDE_LEFT = 0
BROADSIDE_RIGHT = 1
__broadsideMaxDelay = {
    WARSHIPL1: 0.6,
    WARSHIPL2: 1.0,
    WARSHIPL3: 1.5,
    MERCHANTL1: 0.8,
    MERCHANTL2: 1.6,
    MERCHANTL3: 1.75,
    INTERCEPTORL1: 0.3,
    INTERCEPTORL2: 0.5,
    INTERCEPTORL3: 0.75,
    SHIP_OF_THE_LINE: 1.2,
    BLACK_PEARL: 1.25,
    GOLIATH: 1.2,
    QUEEN_ANNES_REVENGE: 1.2,
    SKEL_WARSHIPL3: 1.25,
    SKEL_INTERCEPTORL3: 1.0 }

def getBroadsideMaxDelay(modelClass):
    shipData = __broadsideMaxDelay.get(modelClass)
    return shipData

CustomShipRewards = {
    QUEEN_ANNES_REVENGE: [
        {
            100.0: [
                ItemGlobals.MUTINEERS_CHARM] },
        {
            0.02: [
                ItemGlobals.POTION_SUMMON_CHICKEN],
            100.0: [
                ItemGlobals.POTION_CANNON_3,
                ItemGlobals.POTION_PISTOL_3,
                ItemGlobals.POTION_FACECOLOR,
                ItemGlobals.POTION_ACC_3,
                ItemGlobals.POTION_SPEED_3] }] }
