from pirates.piratesbase import PLocalizer
from pirates.piratesbase import PiratesGlobals
from pirates.ship import ShipGlobals
from pirates.uberdog.UberDogGlobals import *
from pirates.uberdog.UberDogGlobals import InventoryType
HULL_DEFAULT = 0
HULL_BASE = 1
HULL_ARMOR1 = 11
HULL_ARMOR2 = 12
HULL_ARMOR3 = 13
HULL_CARGOSHIP1 = 21
HULL_CARGOSHIP2 = 22
HULL_CARGOSHIP3 = 23
HULL_SPEED1 = 31
HULL_SPEED2 = 32
HULL_SPEED3 = 33
HULL_STORMCHASER1 = 41
HULL_STORMCHASER2 = 42
HULL_STORMCHASER3 = 43
HULL_FIRESTORM1 = 51
HULL_FIRESTORM2 = 52
HULL_FIRESTORM3 = 53
HULL_CAPTBLOOD1 = 61
HULL_CAPTBLOOD2 = 62
HULL_CAPTBLOOD3 = 63
HULL_SKULLBONES1 = 71
HULL_SKULLBONES2 = 72
HULL_SKULLBONES3 = 73
HULL_IRONCLAD1 = 81
HULL_IRONCLAD2 = 82
HULL_IRONCLAD3 = 83
RIGGING_DEFAULT = 0
RIGGING_BASE = 1
RIGGING_DEFENSE1 = 11
RIGGING_DEFENSE2 = 12
RIGGING_OFFENSE1 = 21
RIGGING_OFFENSE2 = 22
RIGGING_SPEED1 = 31
RIGGING_SPEED2 = 32
SAILCOLOR_DEFAULT = 0
SAILCOLOR_BASE = 1
SAILCOLOR_RAIDERRED = 11
SAILCOLOR_RAIDERGREEN = 12
SAILCOLOR_RAIDERBLUE = 13
SAILCOLOR_RAIDERORANGE = 14
SAILCOLOR_PATCHWORK = 21
SAILCOLOR_STRIPEGREEN = 31
SAILCOLOR_STRIPEVIOLET = 32
SAILCOLOR_STRIPERED = 33
SAILCOLOR_WHITE = 40
SAILCOLOR_BLACK = 41
SAILCOLOR_GRAY = 42
SAILCOLOR_TAN = 43
SAILCOLOR_OLIVE = 44
SAILCOLOR_BROWN = 45
SAILCOLOR_GOLD = 46
SAILCOLOR_RED = 50
SAILCOLOR_ORANGE = 51
SAILCOLOR_YELLOW = 52
SAILCOLOR_GREEN = 53
SAILCOLOR_CYAN = 54
SAILCOLOR_BLUE = 55
SAILCOLOR_PURPLE = 56
SAILCOLOR_PINK = 60
SAILCOLOR_ROSE = 61
SAILCOLOR_LIME = 62
SAILCOLOR_MAROON = 70
LOGO_DEFAULT = 0
LOGO_BASE = 1
LOGO_BULL = 11
LOGO_DAGGER = 12
LOGO_SCORPION = 13
LOGO_CLAW = 14
LOGO_WASP = 21
LOGO_SPIDER = 22
LOGO_SNAKE = 23
LOGO_HAWK = 24
LOGO_ROSE = 25
LOGO_FLAME = 26
LOGO_SPANISH_BULL = 27
LOGO_WOLF = 28
LOGO_ANGEL = 29
LOGO_DRAGON = 30
LOGO_SHIELD = 31
LOGO_HEART = 32
LOGO_SKULLCROSS = 33
LOGO_OCTOPUS = 34
LOGO_SHARK = 35
LOGO_MERMAID = 36
LOGO_STORMCLOUD = 37
LOGO_BASE_INV = 101
LOGO_BULL_INV = 111
LOGO_DAGGER_INV = 112
LOGO_SCORPION_INV = 113
LOGO_CLAW_INV = 114
LOGO_WASP_INV = 121
LOGO_HAWK_INV = 124
LOGO_ROSE_INV = 125
LOGO_FLAME_INV = 126
LOGO_SPANISH_BULL_INV = 127
LOGO_WOLF_INV = 128
LOGO_ANGEL_INV = 129
LOGO_DRAGON_INV = 130
LOGO_SHIELD_INV = 131
LOGO_HEART_INV = 132
LOGO_SKULLCROSS_INV = 133
LOGO_OCTOPUS_INV = 134
LOGO_SHARK_INV = 135
LOGO_MERMAID_INV = 136
LOGO_STORMCLOUD_INV = 137
HULLS_THAT_CAN_UPGRADE = [
    ShipGlobals.INTERCEPTORL2,
    ShipGlobals.INTERCEPTORL3,
    ShipGlobals.MERCHANTL2,
    ShipGlobals.MERCHANTL3,
    ShipGlobals.WARSHIPL2,
    ShipGlobals.WARSHIPL3,
    ShipGlobals.BRIGL2,
    ShipGlobals.BRIGL3]
HULL_RELATIVE_COST_BASIS = {
    ShipGlobals.INTERCEPTORL1: 1.0,
    ShipGlobals.INTERCEPTORL2: 3.0,
    ShipGlobals.INTERCEPTORL3: 15.0,
    ShipGlobals.MERCHANTL1: 2.0,
    ShipGlobals.MERCHANTL2: 6.0,
    ShipGlobals.MERCHANTL3: 20.0,
    ShipGlobals.WARSHIPL1: 3.0,
    ShipGlobals.WARSHIPL2: 8.0,
    ShipGlobals.WARSHIPL3: 25.0,
    ShipGlobals.BRIGL1: 3.5,
    ShipGlobals.BRIGL2: 10.0,
    ShipGlobals.BRIGL3: 30.0 }
COST_LIST = [
    InventoryType.ItemTypeMoney,
    InventoryType.PineInPocket,
    InventoryType.OakInPocket,
    InventoryType.IronInPocket,
    InventoryType.SteelInPocket,
    InventoryType.CanvasInPocket,
    InventoryType.SilkInPocket,
    InventoryType.GrogInPocket]
HULL_ATTRIBUTE_COMPARE = [
    ('Armor', PLocalizer.ShipUpgradeAttributeArmor),
    ('Speed', PLocalizer.ShipUpgradeAttributeSpeed),
    ('Turning', PLocalizer.ShipUpgradeAttributeTurning),
    ('Cargo', PLocalizer.ShipUpgradeAttributeCargo)]
HULL_TYPES = {
    HULL_DEFAULT: {
        'Name': PLocalizer.HullDefault,
        'Description': PLocalizer.DescriptionBase,
        'Armor': 1.0,
        'Speed': 1.0,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.75, 0.75, 0.69999999999999996, 1.0),
        'Icon': 'pir_t_gui_shp_basic',
        'IconText': '',
        'Upgrades': [
            HULL_ARMOR1,
            HULL_CARGOSHIP1,
            HULL_SPEED1],
        'Downgrades': [
            None,
            None,
            None],
        'Sidegrades': [
            None,
            None],
        'StyleIndex': ShipGlobals.Styles.Player,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 0,
        'Cost': {
            'Fixed': { },
            'Relative': { } } },
    HULL_BASE: {
        'Name': PLocalizer.HullDefault,
        'Description': PLocalizer.DescriptionBase,
        'Armor': 1.0,
        'Speed': 1.0,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.75, 0.75, 0.69999999999999996, 1.0),
        'Icon': 'pir_t_gui_shp_basic',
        'IconText': '',
        'Upgrades': [
            HULL_ARMOR1,
            HULL_CARGOSHIP1,
            HULL_SPEED1],
        'Downgrades': [
            None,
            None,
            None],
        'Sidegrades': [
            None,
            None],
        'StyleIndex': ShipGlobals.Styles.Player,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': { } } },
    HULL_ARMOR1: {
        'Name': PLocalizer.HullReinforced1,
        'Description': PLocalizer.DescriptionReinforced,
        'Armor': 1.1799999999999999,
        'Speed': 0.94999999999999996,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.55000000000000004, 0.5, 0.5, 1.0),
        'Icon': 'pir_t_gui_shp_armor',
        'IconText': 'I',
        'Upgrades': [
            None,
            HULL_ARMOR2,
            None],
        'Downgrades': [
            None,
            HULL_BASE,
            None],
        'Sidegrades': [
            None,
            HULL_CARGOSHIP1],
        'StyleIndex': ShipGlobals.Styles.Reinforced,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 1000,
                InventoryType.IronInPocket: 10 } } },
    HULL_ARMOR2: {
        'Name': PLocalizer.HullReinforced2,
        'Description': PLocalizer.DescriptionReinforced,
        'Armor': 1.3600000000000001,
        'Speed': 0.94999999999999996,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.55000000000000004, 0.5, 0.5, 1.0),
        'Icon': 'pir_t_gui_shp_armor',
        'IconText': 'II',
        'Upgrades': [
            None,
            HULL_ARMOR3,
            None],
        'Downgrades': [
            None,
            HULL_ARMOR1,
            None],
        'Sidegrades': [
            None,
            HULL_CARGOSHIP2],
        'StyleIndex': ShipGlobals.Styles.Reinforced,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 1500,
                InventoryType.IronInPocket: 15 } } },
    HULL_ARMOR3: {
        'Name': PLocalizer.HullReinforced3,
        'Description': PLocalizer.DescriptionReinforced,
        'Armor': 1.54,
        'Speed': 0.90000000000000002,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.55000000000000004, 0.5, 0.5, 1.0),
        'Icon': 'pir_t_gui_shp_armor',
        'IconText': 'III',
        'Upgrades': [
            None,
            HULL_IRONCLAD1,
            HULL_SKULLBONES1],
        'Downgrades': [
            None,
            HULL_ARMOR2,
            None],
        'Sidegrades': [
            None,
            HULL_CARGOSHIP3],
        'StyleIndex': ShipGlobals.Styles.Reinforced,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 2000,
                InventoryType.PineInPocket: 5,
                InventoryType.IronInPocket: 20,
                InventoryType.SteelInPocket: 5 } } },
    HULL_CARGOSHIP1: {
        'Name': PLocalizer.HullCargo1,
        'Description': PLocalizer.DescriptionCargo,
        'Armor': 1.1000000000000001,
        'Speed': 1.0,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.25,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.80000000000000004, 0.65000000000000002, 0.59999999999999998, 1.0),
        'Icon': 'pir_t_gui_shp_cargo',
        'IconText': 'I',
        'Upgrades': [
            None,
            HULL_CARGOSHIP2,
            None],
        'Downgrades': [
            None,
            HULL_BASE,
            None],
        'Sidegrades': [
            HULL_ARMOR1,
            HULL_SPEED1],
        'StyleIndex': ShipGlobals.Styles.CargoShip,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 2000 } } },
    HULL_CARGOSHIP2: {
        'Name': PLocalizer.HullCargo2,
        'Description': PLocalizer.DescriptionCargo,
        'Armor': 1.1499999999999999,
        'Speed': 1.0,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.3999999999999999,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.80000000000000004, 0.65000000000000002, 0.59999999999999998, 1.0),
        'Icon': 'pir_t_gui_shp_cargo',
        'IconText': 'II',
        'Upgrades': [
            None,
            HULL_CARGOSHIP3,
            None],
        'Downgrades': [
            None,
            HULL_CARGOSHIP1,
            None],
        'Sidegrades': [
            HULL_ARMOR2,
            HULL_SPEED2],
        'StyleIndex': ShipGlobals.Styles.CargoShip,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 2500,
                InventoryType.PineInPocket: 10 } } },
    HULL_CARGOSHIP3: {
        'Name': PLocalizer.HullCargo3,
        'Description': PLocalizer.DescriptionCargo,
        'Armor': 1.2,
        'Speed': 1.0,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.6000000000000001,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.80000000000000004, 0.65000000000000002, 0.59999999999999998, 1.0),
        'Icon': 'pir_t_gui_shp_cargo',
        'IconText': 'III',
        'Upgrades': [
            HULL_SKULLBONES1,
            HULL_CAPTBLOOD1,
            HULL_FIRESTORM1],
        'Downgrades': [
            None,
            HULL_CARGOSHIP2,
            None],
        'Sidegrades': [
            HULL_ARMOR3,
            HULL_SPEED3],
        'StyleIndex': ShipGlobals.Styles.CargoShip,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3000,
                InventoryType.PineInPocket: 10,
                InventoryType.OakInPocket: 5 } } },
    HULL_SPEED1: {
        'Name': PLocalizer.HullStreamlined1,
        'Description': PLocalizer.DescriptionStreamlined,
        'Armor': 1.0,
        'Speed': 1.1000000000000001,
        'Turning': 0.90000000000000002,
        'Firepower': 1.0,
        'Cargo': 0.84999999999999998,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.80000000000000004, 0.80000000000000004, 1.0, 1.0),
        'Icon': 'pir_t_gui_shp_streamline',
        'IconText': 'I',
        'Upgrades': [
            None,
            HULL_SPEED2,
            None],
        'Downgrades': [
            None,
            HULL_BASE,
            None],
        'Sidegrades': [
            HULL_CARGOSHIP1,
            None],
        'StyleIndex': ShipGlobals.Styles.Streamlined,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 1000,
                InventoryType.PineInPocket: 10 } } },
    HULL_SPEED2: {
        'Name': PLocalizer.HullStreamlined2,
        'Description': PLocalizer.DescriptionStreamlined,
        'Armor': 1.0,
        'Speed': 1.2,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 0.84999999999999998,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.80000000000000004, 0.80000000000000004, 1.0, 1.0),
        'Icon': 'pir_t_gui_shp_streamline',
        'IconText': 'II',
        'Upgrades': [
            None,
            HULL_SPEED3,
            None],
        'Downgrades': [
            None,
            HULL_SPEED1,
            None],
        'Sidegrades': [
            HULL_CARGOSHIP2,
            None],
        'StyleIndex': ShipGlobals.Styles.Streamlined,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 1500,
                InventoryType.PineInPocket: 20 } } },
    HULL_SPEED3: {
        'Name': PLocalizer.HullStreamlined3,
        'Description': PLocalizer.DescriptionStreamlined,
        'Armor': 1.0,
        'Speed': 1.2,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.80000000000000004, 0.80000000000000004, 1.0, 1.0),
        'Icon': 'pir_t_gui_shp_streamline',
        'IconText': 'III',
        'Upgrades': [
            HULL_FIRESTORM1,
            HULL_STORMCHASER1,
            None],
        'Downgrades': [
            None,
            HULL_SPEED2,
            None],
        'Sidegrades': [
            HULL_CARGOSHIP3,
            None],
        'StyleIndex': ShipGlobals.Styles.Streamlined,
        'BroadsideType': 0,
        'BroadsideAmount': 0.0,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 2000,
                InventoryType.PineInPocket: 20,
                InventoryType.OakInPocket: 10 } } },
    HULL_STORMCHASER1: {
        'Name': PLocalizer.HullStormChaser1,
        'Description': PLocalizer.DescriptionStormChaser,
        'Armor': 1.0,
        'Speed': 1.2,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.59999999999999998, 1.0, 1.0),
        'Icon': 'pir_t_gui_shp_stormchaser',
        'IconText': 'IV',
        'Upgrades': [
            None,
            HULL_STORMCHASER2,
            None],
        'Downgrades': [
            None,
            HULL_SPEED3,
            None],
        'Sidegrades': [
            HULL_FIRESTORM1,
            None],
        'StyleIndex': ShipGlobals.Styles.StormChaser,
        'BroadsideType': InventoryType.CannonThunderbolt,
        'BroadsideAmount': 0.14999999999999999,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 2500,
                InventoryType.PineInPocket: 40,
                InventoryType.IronInPocket: 20,
                InventoryType.OakInPocket: 10 } } },
    HULL_STORMCHASER2: {
        'Name': PLocalizer.HullStormChaser2,
        'Description': PLocalizer.DescriptionStormChaser,
        'Armor': 1.0,
        'Speed': 1.2,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.59999999999999998, 1.0, 1.0),
        'Icon': 'pir_t_gui_shp_stormchaser',
        'IconText': 'V',
        'Upgrades': [
            None,
            HULL_STORMCHASER3,
            None],
        'Downgrades': [
            None,
            HULL_STORMCHASER1,
            None],
        'Sidegrades': [
            HULL_FIRESTORM2,
            None],
        'StyleIndex': ShipGlobals.Styles.StormChaser,
        'BroadsideType': InventoryType.CannonThunderbolt,
        'BroadsideAmount': 0.29999999999999999,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3000,
                InventoryType.PineInPocket: 50,
                InventoryType.IronInPocket: 25,
                InventoryType.OakInPocket: 15 } } },
    HULL_STORMCHASER3: {
        'Name': PLocalizer.HullStormChaser3,
        'Description': PLocalizer.DescriptionStormChaser,
        'Armor': 1.0,
        'Speed': 1.2,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.59999999999999998, 1.0, 1.0),
        'Icon': 'pir_t_gui_shp_stormchaser',
        'IconText': 'VI',
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            HULL_STORMCHASER2,
            None,
            None],
        'Sidegrades': [
            HULL_FIRESTORM3,
            None],
        'StyleIndex': ShipGlobals.Styles.StormChaser,
        'BroadsideType': InventoryType.CannonThunderbolt,
        'BroadsideAmount': 0.45000000000000001,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3500,
                InventoryType.PineInPocket: 60,
                InventoryType.OakInPocket: 20,
                InventoryType.SteelInPocket: 15 } } },
    HULL_FIRESTORM1: {
        'Name': PLocalizer.HullFireStorm1,
        'Description': PLocalizer.DescriptionFirestorm,
        'Armor': 1.0,
        'Speed': 1.1499999999999999,
        'Turning': 1.2,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.29999999999999999, 0.0, 1.0),
        'Icon': 'pir_t_gui_shp_fire',
        'IconText': 'IV',
        'Upgrades': [
            None,
            HULL_FIRESTORM2,
            None],
        'Downgrades': [
            HULL_CARGOSHIP3,
            None,
            HULL_SPEED3],
        'Sidegrades': [
            HULL_CAPTBLOOD1,
            HULL_STORMCHASER1],
        'StyleIndex': ShipGlobals.Styles.FireStorm,
        'BroadsideType': InventoryType.CannonFirebrand,
        'BroadsideAmount': 0.20000000000000001,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 2500,
                InventoryType.PineInPocket: 40,
                InventoryType.IronInPocket: 30,
                InventoryType.OakInPocket: 10 } } },
    HULL_FIRESTORM2: {
        'Name': PLocalizer.HullFireStorm2,
        'Description': PLocalizer.DescriptionFirestorm,
        'Armor': 1.0,
        'Speed': 1.1499999999999999,
        'Turning': 1.2,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.29999999999999999, 0.0, 1.0),
        'Icon': 'pir_t_gui_shp_fire',
        'IconText': 'V',
        'Upgrades': [
            None,
            HULL_FIRESTORM3,
            None],
        'Downgrades': [
            None,
            HULL_FIRESTORM1,
            None],
        'Sidegrades': [
            HULL_CAPTBLOOD2,
            HULL_STORMCHASER2],
        'StyleIndex': ShipGlobals.Styles.FireStorm,
        'BroadsideType': InventoryType.CannonFirebrand,
        'BroadsideAmount': 0.40000000000000002,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3000,
                InventoryType.PineInPocket: 50,
                InventoryType.IronInPocket: 40,
                InventoryType.OakInPocket: 15 } } },
    HULL_FIRESTORM3: {
        'Name': PLocalizer.HullFireStorm3,
        'Description': PLocalizer.DescriptionFirestorm,
        'Armor': 1.0,
        'Speed': 1.1499999999999999,
        'Turning': 1.2,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.29999999999999999, 0.0, 1.0),
        'Icon': 'pir_t_gui_shp_fire',
        'IconText': 'VI',
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            None,
            HULL_FIRESTORM2,
            None],
        'Sidegrades': [
            HULL_CAPTBLOOD3,
            HULL_STORMCHASER3],
        'StyleIndex': ShipGlobals.Styles.FireStorm,
        'BroadsideType': InventoryType.CannonFirebrand,
        'BroadsideAmount': 0.59999999999999998,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3500,
                InventoryType.PineInPocket: 50,
                InventoryType.OakInPocket: 20,
                InventoryType.SteelInPocket: 15 } } },
    HULL_CAPTBLOOD1: {
        'Name': PLocalizer.HullCaptBlood1,
        'Description': PLocalizer.DescriptionCaptBlood,
        'Armor': 1.2,
        'Speed': 1.1000000000000001,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.5,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.40000000000000002, 0.10000000000000001, 1.0),
        'Icon': 'pir_t_gui_shp_hunter',
        'IconText': 'IV',
        'Upgrades': [
            None,
            HULL_CAPTBLOOD2,
            None],
        'Downgrades': [
            None,
            HULL_CARGOSHIP3,
            None],
        'Sidegrades': [
            HULL_SKULLBONES1,
            HULL_FIRESTORM1],
        'StyleIndex': ShipGlobals.Styles.FortuneHunter,
        'BroadsideType': InventoryType.CannonFirebrand,
        'BroadsideAmount': 0.14999999999999999,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 4000,
                InventoryType.IronInPocket: 30,
                InventoryType.OakInPocket: 10 } } },
    HULL_CAPTBLOOD2: {
        'Name': PLocalizer.HullCaptBlood2,
        'Description': PLocalizer.DescriptionCaptBlood,
        'Armor': 1.3,
        'Speed': 1.1000000000000001,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.5,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.40000000000000002, 0.10000000000000001, 1.0),
        'Icon': 'pir_t_gui_shp_hunter',
        'IconText': 'V',
        'Upgrades': [
            None,
            HULL_CAPTBLOOD3,
            None],
        'Downgrades': [
            None,
            HULL_CAPTBLOOD1,
            None],
        'Sidegrades': [
            HULL_SKULLBONES2,
            HULL_FIRESTORM2],
        'StyleIndex': ShipGlobals.Styles.FortuneHunter,
        'BroadsideType': InventoryType.CannonFirebrand,
        'BroadsideAmount': 0.29999999999999999,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 4500,
                InventoryType.IronInPocket: 35,
                InventoryType.OakInPocket: 15,
                InventoryType.SteelInPocket: 5 } } },
    HULL_CAPTBLOOD3: {
        'Name': PLocalizer.HullCaptBlood3,
        'Description': PLocalizer.DescriptionCaptBlood,
        'Armor': 1.3999999999999999,
        'Speed': 1.1000000000000001,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.5,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.40000000000000002, 0.10000000000000001, 1.0),
        'Icon': 'pir_t_gui_shp_hunter',
        'IconText': 'VI',
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            None,
            HULL_CAPTBLOOD2,
            None],
        'Sidegrades': [
            HULL_SKULLBONES3,
            HULL_FIRESTORM3],
        'StyleIndex': ShipGlobals.Styles.FortuneHunter,
        'BroadsideType': InventoryType.CannonFirebrand,
        'BroadsideAmount': 0.45000000000000001,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 5000,
                InventoryType.IronInPocket: 45,
                InventoryType.OakInPocket: 20,
                InventoryType.SteelInPocket: 10 } } },
    HULL_SKULLBONES1: {
        'Name': PLocalizer.HullSkullBones1,
        'Description': PLocalizer.DescriptionSkullBones,
        'Armor': 1.25,
        'Speed': 1.0,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1.0),
        'Icon': 'pir_t_gui_shp_skull',
        'IconText': 'IV',
        'Upgrades': [
            None,
            HULL_SKULLBONES2,
            None],
        'Downgrades': [
            HULL_ARMOR3,
            None,
            HULL_CARGOSHIP3],
        'Sidegrades': [
            HULL_IRONCLAD1,
            HULL_CAPTBLOOD1],
        'StyleIndex': ShipGlobals.Styles.SkullBones,
        'BroadsideType': InventoryType.CannonFury,
        'BroadsideAmount': 0.14999999999999999,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 2500,
                InventoryType.IronInPocket: 30,
                InventoryType.OakInPocket: 10 } } },
    HULL_SKULLBONES2: {
        'Name': PLocalizer.HullSkullBones2,
        'Description': PLocalizer.DescriptionSkullBones,
        'Armor': 1.3999999999999999,
        'Speed': 1.0,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1.0),
        'Icon': 'pir_t_gui_shp_skull',
        'IconText': 'V',
        'Upgrades': [
            None,
            HULL_SKULLBONES3,
            None],
        'Downgrades': [
            None,
            HULL_SKULLBONES1,
            None],
        'Sidegrades': [
            HULL_IRONCLAD2,
            HULL_CAPTBLOOD2],
        'StyleIndex': ShipGlobals.Styles.SkullBones,
        'BroadsideType': InventoryType.CannonFury,
        'BroadsideAmount': 0.33000000000000002,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3000,
                InventoryType.IronInPocket: 40,
                InventoryType.OakInPocket: 15 } } },
    HULL_SKULLBONES3: {
        'Name': PLocalizer.HullSkullBones3,
        'Description': PLocalizer.DescriptionSkullBones,
        'Armor': 1.6499999999999999,
        'Speed': 1.0,
        'Turning': 1.1000000000000001,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1.0),
        'Icon': 'pir_t_gui_shp_skull',
        'IconText': 'VI',
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            None,
            HULL_SKULLBONES2,
            None],
        'Sidegrades': [
            HULL_IRONCLAD3,
            HULL_CAPTBLOOD3],
        'StyleIndex': ShipGlobals.Styles.SkullBones,
        'BroadsideType': InventoryType.CannonFury,
        'BroadsideAmount': 0.5,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3500,
                InventoryType.IronInPocket: 50,
                InventoryType.OakInPocket: 20 } } },
    HULL_IRONCLAD1: {
        'Name': PLocalizer.HullIronclad1,
        'Description': PLocalizer.DescriptionIronClad,
        'Armor': 1.5,
        'Speed': 0.90000000000000002,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.90000000000000002, 0.90000000000000002, 0.59999999999999998, 1.0),
        'Icon': 'pir_t_gui_shp_copperhead',
        'IconText': 'IV',
        'Upgrades': [
            None,
            HULL_IRONCLAD2,
            None],
        'Downgrades': [
            None,
            HULL_ARMOR3,
            None],
        'Sidegrades': [
            None,
            HULL_SKULLBONES1],
        'StyleIndex': ShipGlobals.Styles.IronClad,
        'BroadsideType': InventoryType.CannonExplosive,
        'BroadsideAmount': 0.050000000000000003,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3000,
                InventoryType.IronInPocket: 40,
                InventoryType.SteelInPocket: 10 } } },
    HULL_IRONCLAD2: {
        'Name': PLocalizer.HullIronclad2,
        'Description': PLocalizer.DescriptionIronClad,
        'Armor': 1.6499999999999999,
        'Speed': 0.90000000000000002,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.90000000000000002, 0.90000000000000002, 0.59999999999999998, 1.0),
        'Icon': 'pir_t_gui_shp_copperhead',
        'IconText': 'V',
        'Upgrades': [
            None,
            HULL_IRONCLAD3,
            None],
        'Downgrades': [
            None,
            HULL_IRONCLAD1,
            None],
        'Sidegrades': [
            None,
            HULL_SKULLBONES2],
        'StyleIndex': ShipGlobals.Styles.IronClad,
        'BroadsideType': InventoryType.CannonExplosive,
        'BroadsideAmount': 0.10000000000000001,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 3500,
                InventoryType.IronInPocket: 50,
                InventoryType.SteelInPocket: 20 } } },
    HULL_IRONCLAD3: {
        'Name': PLocalizer.HullIronclad3,
        'Description': PLocalizer.DescriptionIronClad,
        'Armor': 1.8,
        'Speed': 0.90000000000000002,
        'Turning': 1.0,
        'Firepower': 1.0,
        'Cargo': 1.0,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.90000000000000002, 0.90000000000000002, 0.59999999999999998, 1.0),
        'Icon': 'pir_t_gui_shp_copperhead',
        'IconText': 'VI',
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            None,
            HULL_IRONCLAD2,
            None],
        'Sidegrades': [
            None,
            HULL_SKULLBONES3],
        'StyleIndex': ShipGlobals.Styles.IronClad,
        'BroadsideType': InventoryType.CannonExplosive,
        'BroadsideAmount': 0.14999999999999999,
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 4000,
                InventoryType.IronInPocket: 60,
                InventoryType.SteelInPocket: 30 } } } }
RIGGING_TYPES = {
    RIGGING_DEFAULT: {
        'Name': PLocalizer.RiggingBase,
        'Power': None,
        'Texture': None,
        'PreviewColor': (1.0, 0.90000000000000002, 0.80000000000000004, 1.0),
        'Icon': None,
        'StyleIndex': ShipGlobals.Styles.Player,
        'Upgrades': [
            RIGGING_DEFENSE1,
            RIGGING_SPEED1,
            RIGGING_OFFENSE1],
        'Downgrades': [
            None,
            None,
            None],
        'Sidegrades': [
            None,
            None],
        'StyleIndex': ShipGlobals.Styles.Player,
        'Available': 0,
        'Cost': {
            'Fixed': { },
            'Relative': { } },
        'SkillBoosts': { } },
    RIGGING_BASE: {
        'Name': PLocalizer.RiggingBase,
        'Power': None,
        'Texture': None,
        'PreviewColor': (1.0, 0.90000000000000002, 0.80000000000000004, 1.0),
        'Icon': None,
        'StyleIndex': ShipGlobals.Styles.Player,
        'Upgrades': [
            RIGGING_DEFENSE1,
            RIGGING_SPEED1,
            RIGGING_OFFENSE1],
        'Downgrades': [
            None,
            None,
            None],
        'Sidegrades': [
            None,
            None],
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': { } },
        'SkillBoosts': { } },
    RIGGING_DEFENSE1: {
        'Name': PLocalizer.RiggingDefense1,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.90000000000000002, 0.80000000000000004, 0.69999999999999996, 1.0),
        'Icon': 'sail_take_cover',
        'IconText': 'I',
        'StyleIndex': ShipGlobals.Styles.Reinforced,
        'Upgrades': [
            None,
            RIGGING_DEFENSE2,
            None],
        'Downgrades': [
            None,
            RIGGING_BASE,
            None],
        'Sidegrades': [
            None,
            RIGGING_SPEED1],
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 750,
                InventoryType.IronInPocket: 5,
                InventoryType.CanvasInPocket: 5 } },
        'SkillBoosts': {
            InventoryType.SailTakeCover: 1 } },
    RIGGING_DEFENSE2: {
        'Name': PLocalizer.RiggingDefense2,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.90000000000000002, 0.80000000000000004, 0.69999999999999996, 1.0),
        'Icon': 'sail_take_cover',
        'IconText': 'II',
        'StyleIndex': ShipGlobals.Styles.Reinforced,
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            None,
            RIGGING_DEFENSE1,
            None],
        'Sidegrades': [
            None,
            RIGGING_SPEED2],
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 1200,
                InventoryType.SteelInPocket: 10,
                InventoryType.SilkInPocket: 10 } },
        'SkillBoosts': {
            InventoryType.SailTakeCover: 2 } },
    RIGGING_SPEED1: {
        'Name': PLocalizer.RiggingSpeed1,
        'Power': None,
        'Texture': None,
        'PreviewColor': (1.0, 1.0, 1.0, 1.0),
        'Icon': 'sail_full_sail',
        'IconText': 'I',
        'StyleIndex': ShipGlobals.Styles.Streamlined,
        'Upgrades': [
            None,
            RIGGING_SPEED2,
            None],
        'Downgrades': [
            None,
            RIGGING_BASE,
            None],
        'Sidegrades': [
            RIGGING_DEFENSE1,
            RIGGING_OFFENSE1],
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 750,
                InventoryType.CanvasInPocket: 10 } },
        'SkillBoosts': {
            InventoryType.SailFullSail: 1 } },
    RIGGING_SPEED2: {
        'Name': PLocalizer.RiggingSpeed2,
        'Power': None,
        'Texture': None,
        'PreviewColor': (1.0, 1.0, 1.0, 1.0),
        'Icon': 'sail_full_sail',
        'IconText': 'II',
        'StyleIndex': ShipGlobals.Styles.Streamlined,
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            None,
            RIGGING_SPEED1,
            None],
        'Sidegrades': [
            RIGGING_DEFENSE2,
            RIGGING_OFFENSE2],
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 1200,
                InventoryType.CanvasInPocket: 10,
                InventoryType.SilkInPocket: 10 } },
        'SkillBoosts': {
            InventoryType.SailFullSail: 2 } },
    RIGGING_OFFENSE1: {
        'Name': PLocalizer.RiggingOffense1,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.59999999999999998, 0.69999999999999996, 1.0),
        'Icon': 'sail_openfire2',
        'IconText': 'I',
        'StyleIndex': ShipGlobals.Styles.CargoShip,
        'Upgrades': [
            None,
            RIGGING_OFFENSE2,
            None],
        'Downgrades': [
            None,
            RIGGING_BASE,
            None],
        'Sidegrades': [
            RIGGING_SPEED1,
            None],
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 750,
                InventoryType.IronInPocket: 5,
                InventoryType.CanvasInPocket: 5 } },
        'SkillBoosts': {
            InventoryType.SailOpenFire: 1 } },
    RIGGING_OFFENSE2: {
        'Name': PLocalizer.RiggingOffense2,
        'Power': None,
        'Texture': None,
        'PreviewColor': (0.59999999999999998, 0.59999999999999998, 0.69999999999999996, 1.0),
        'Icon': 'sail_openfire2',
        'IconText': 'II',
        'StyleIndex': ShipGlobals.Styles.CargoShip,
        'Upgrades': [
            None,
            None,
            None],
        'Downgrades': [
            None,
            RIGGING_OFFENSE1,
            None],
        'Sidegrades': [
            RIGGING_SPEED2,
            None],
        'Available': 1,
        'Cost': {
            'Fixed': { },
            'Relative': {
                InventoryType.ItemTypeMoney: 1200,
                InventoryType.SteelInPocket: 10,
                InventoryType.SilkInPocket: 10 } },
        'SkillBoosts': {
            InventoryType.SailOpenFire: 2 } } }
SAILCOLOR_TYPES = {
    SAILCOLOR_DEFAULT: {
        'Name': PLocalizer.SailPlain,
        'PreviewColor': (1.0, 1.0, 1.0, 1.0),
        'StyleIndex': ShipGlobals.Styles.Player,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 1 },
            'Relative': { } } },
    SAILCOLOR_BASE: {
        'Name': PLocalizer.SailPlain,
        'PreviewColor': (1.0, 1.0, 1.0, 1.0),
        'StyleIndex': ShipGlobals.Styles.Player,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 1 },
            'Relative': { } } },
    SAILCOLOR_WHITE: {
        'Name': PLocalizer.SailWhite,
        'PreviewColor': (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailWhite,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_TAN: {
        'Name': PLocalizer.SailTan,
        'PreviewColor': (0.59999999999999998, 0.59999999999999998, 0.40000000000000002, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailTan,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 2500 },
            'Relative': { } } },
    SAILCOLOR_OLIVE: {
        'Name': PLocalizer.SailOlive,
        'PreviewColor': (0.45000000000000001, 0.5, 0.40000000000000002, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailOlive,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 2500 },
            'Relative': { } } },
    SAILCOLOR_BLACK: {
        'Name': PLocalizer.SailBlack,
        'PreviewColor': (0.25, 0.25, 0.25, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailBlack,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 10000 },
            'Relative': { } } },
    SAILCOLOR_GRAY: {
        'Name': PLocalizer.SailGray,
        'PreviewColor': (0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailGray,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 2500 },
            'Relative': { } } },
    SAILCOLOR_BROWN: {
        'Name': PLocalizer.SailBrown,
        'PreviewColor': (0.5, 0.34999999999999998, 0.25, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailBrown,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_GOLD: {
        'Name': PLocalizer.SailGold,
        'PreviewColor': (0.59999999999999998, 0.5, 0.050000000000000003, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailGold,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 7500 },
            'Relative': { } } },
    SAILCOLOR_RED: {
        'Name': PLocalizer.SailRed,
        'PreviewColor': (0.5, 0.20000000000000001, 0.20000000000000001, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailRed,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 7500 },
            'Relative': { } } },
    SAILCOLOR_ORANGE: {
        'Name': PLocalizer.SailOrange,
        'PreviewColor': (0.59999999999999998, 0.40000000000000002, 0.20000000000000001, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailOrange,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_YELLOW: {
        'Name': PLocalizer.SailYellow,
        'PreviewColor': (0.69999999999999996, 0.69999999999999996, 0.34999999999999998, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailYellow,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_GREEN: {
        'Name': PLocalizer.SailGreen,
        'PreviewColor': (0.25, 0.45000000000000001, 0.29999999999999999, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailGreen,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_CYAN: {
        'Name': PLocalizer.SailCyan,
        'PreviewColor': (0.45000000000000001, 0.75, 0.75, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailCyan,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_BLUE: {
        'Name': PLocalizer.SailBlue,
        'PreviewColor': (0.29999999999999999, 0.40000000000000002, 0.65000000000000002, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailBlue,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_PURPLE: {
        'Name': PLocalizer.SailPurple,
        'PreviewColor': (0.45000000000000001, 0.40000000000000002, 0.5, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailPurple,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_PINK: {
        'Name': PLocalizer.SailPink,
        'PreviewColor': (0.75, 0.5, 0.59999999999999998, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailPink,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_ROSE: {
        'Name': PLocalizer.SailRose,
        'PreviewColor': (0.5, 0.29999999999999999, 0.40000000000000002, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailRose,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 10000 },
            'Relative': { } } },
    SAILCOLOR_LIME: {
        'Name': PLocalizer.SailLime,
        'PreviewColor': (0.5, 0.20000000000000001, 0.20000000000000001, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailLime,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_MAROON: {
        'Name': PLocalizer.SailMaroon,
        'PreviewColor': (0.5, 0.20000000000000001, 0.20000000000000001, 1.0),
        'StyleIndex': ShipGlobals.Styles.SailMaroon,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 10000 },
            'Relative': { } } },
    SAILCOLOR_RAIDERRED: {
        'Name': PLocalizer.SailRed,
        'PreviewColor': (0.5, 0.59999999999999998, 0.25, 1.0),
        'StyleIndex': ShipGlobals.Styles.Bandit01,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_RAIDERGREEN: {
        'Name': PLocalizer.SailGreen,
        'PreviewColor': (0.25, 0.5, 0.25, 1.0),
        'StyleIndex': ShipGlobals.Styles.Bandit02,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_RAIDERBLUE: {
        'Name': PLocalizer.SailBlue,
        'PreviewColor': (0.40000000000000002, 0.5, 0.69999999999999996, 1.0),
        'StyleIndex': ShipGlobals.Styles.Bandit03,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_RAIDERORANGE: {
        'Name': PLocalizer.SailOrange,
        'PreviewColor': (0.5, 0.25, 0.10000000000000001, 1.0),
        'StyleIndex': ShipGlobals.Styles.Bandit04,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_PATCHWORK: {
        'Name': PLocalizer.SailPatches,
        'PreviewColor': (0.34999999999999998, 0.40000000000000002, 0.29999999999999999, 1.0),
        'StyleIndex': ShipGlobals.Styles.BP,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_STRIPEGREEN: {
        'Name': PLocalizer.SailStripeGreen,
        'PreviewColor': (0.40000000000000002, 1.0, 0.40000000000000002, 1.0),
        'StyleIndex': ShipGlobals.Styles.BountyHunter_A,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_STRIPEVIOLET: {
        'Name': PLocalizer.SailStripeViolet,
        'PreviewColor': (0.80000000000000004, 0.20000000000000001, 0.80000000000000004, 1.0),
        'StyleIndex': ShipGlobals.Styles.BountyHunter_D,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    SAILCOLOR_STRIPERED: {
        'Name': PLocalizer.SailStripeRed,
        'PreviewColor': (0.80000000000000004, 0.20000000000000001, 0.20000000000000001, 1.0),
        'StyleIndex': ShipGlobals.Styles.BountyHunter_B,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } } }
LOGO_TYPES = {
    LOGO_DEFAULT: {
        'Name': PLocalizer.SailLogoBase,
        'StyleIndex': ShipGlobals.Logos.NoLogo,
        'Invert': False,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 1 },
            'Relative': { } } },
    LOGO_BASE: {
        'Name': PLocalizer.SailLogoBase,
        'StyleIndex': ShipGlobals.Logos.NoLogo,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 1 },
            'Relative': { } } },
    LOGO_BASE_INV: {
        'Name': PLocalizer.SailLogoBase,
        'StyleIndex': ShipGlobals.Logos.NoLogo,
        'Invert': False,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 1 },
            'Relative': { } } },
    LOGO_BULL: {
        'Name': PLocalizer.SailLogoBull,
        'StyleIndex': ShipGlobals.Logos.Bandit_Bull,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_DAGGER: {
        'Name': PLocalizer.SailLogoDagger,
        'StyleIndex': ShipGlobals.Logos.Bandit_Dagger,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SCORPION: {
        'Name': PLocalizer.SailLogoScorpion,
        'StyleIndex': ShipGlobals.Logos.Bandit_Scorpion,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_CLAW: {
        'Name': PLocalizer.SailLogoClaw,
        'StyleIndex': ShipGlobals.Logos.Bandit_Claw,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_WASP: {
        'Name': PLocalizer.SailLogoWasp,
        'StyleIndex': ShipGlobals.Logos.Bounty_Hunter_Wasp,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SPIDER: {
        'Name': PLocalizer.SailLogoSpider,
        'StyleIndex': ShipGlobals.Logos.Bounty_Hunter_Spider,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SNAKE: {
        'Name': PLocalizer.SailLogoSnake,
        'StyleIndex': ShipGlobals.Logos.Bounty_Hunter_Snake,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_HAWK: {
        'Name': PLocalizer.SailLogoHawk,
        'StyleIndex': ShipGlobals.Logos.Player_Hawk,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_ROSE: {
        'Name': PLocalizer.SailLogoRose,
        'StyleIndex': ShipGlobals.Logos.Player_Rose,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_FLAME: {
        'Name': PLocalizer.SailLogoFlame,
        'StyleIndex': ShipGlobals.Logos.Player_Flame,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SPANISH_BULL: {
        'Name': PLocalizer.SailLogoSpanishBull,
        'StyleIndex': ShipGlobals.Logos.Player_SpanishBull,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_WOLF: {
        'Name': PLocalizer.SailLogoWolf,
        'StyleIndex': ShipGlobals.Logos.Player_Wolf,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_ANGEL: {
        'Name': PLocalizer.SailLogoAngel,
        'StyleIndex': ShipGlobals.Logos.Player_Angel,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_DRAGON: {
        'Name': PLocalizer.SailLogoDragon,
        'StyleIndex': ShipGlobals.Logos.Player_Dragon,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SHIELD: {
        'Name': PLocalizer.SailLogoShield,
        'StyleIndex': ShipGlobals.Logos.Player_Shield,
        'Invert': False,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_HEART: {
        'Name': PLocalizer.SailLogoHeart,
        'StyleIndex': ShipGlobals.Logos.Player_Heart,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SKULLCROSS: {
        'Name': PLocalizer.SailLogoSkull,
        'StyleIndex': ShipGlobals.Logos.Contest_Skull,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_OCTOPUS: {
        'Name': PLocalizer.SailLogoOctopus,
        'StyleIndex': ShipGlobals.Logos.Contest_Octopus,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SHARK: {
        'Name': PLocalizer.SailLogoShark,
        'StyleIndex': ShipGlobals.Logos.Contest_Shark,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_MERMAID: {
        'Name': PLocalizer.SailLogoMermaid,
        'StyleIndex': ShipGlobals.Logos.Contest_Mermaid,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_STORMCLOUD: {
        'Name': PLocalizer.SailLogoStormCloud,
        'StyleIndex': ShipGlobals.Logos.Contest_StormCloud,
        'Invert': False,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_BULL_INV: {
        'Name': PLocalizer.SailLogoBull,
        'StyleIndex': ShipGlobals.Logos.Bandit_Bull,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_DAGGER_INV: {
        'Name': PLocalizer.SailLogoDagger,
        'StyleIndex': ShipGlobals.Logos.Bandit_Dagger,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SCORPION_INV: {
        'Name': PLocalizer.SailLogoScorpion,
        'StyleIndex': ShipGlobals.Logos.Bandit_Scorpion,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_CLAW_INV: {
        'Name': PLocalizer.SailLogoClaw,
        'StyleIndex': ShipGlobals.Logos.Bandit_Claw,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_WASP_INV: {
        'Name': PLocalizer.SailLogoWasp,
        'StyleIndex': ShipGlobals.Logos.Bounty_Hunter_Wasp,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_HAWK_INV: {
        'Name': PLocalizer.SailLogoHawk,
        'StyleIndex': ShipGlobals.Logos.Player_Hawk,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_ROSE_INV: {
        'Name': PLocalizer.SailLogoRose,
        'StyleIndex': ShipGlobals.Logos.Player_Rose,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_FLAME_INV: {
        'Name': PLocalizer.SailLogoFlame,
        'StyleIndex': ShipGlobals.Logos.Player_Flame,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SPANISH_BULL_INV: {
        'Name': PLocalizer.SailLogoSpanishBull,
        'StyleIndex': ShipGlobals.Logos.Player_SpanishBull,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_WOLF_INV: {
        'Name': PLocalizer.SailLogoWolf,
        'StyleIndex': ShipGlobals.Logos.Player_Wolf,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_ANGEL_INV: {
        'Name': PLocalizer.SailLogoAngel,
        'StyleIndex': ShipGlobals.Logos.Player_Angel,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_DRAGON_INV: {
        'Name': PLocalizer.SailLogoDragon,
        'StyleIndex': ShipGlobals.Logos.Player_Dragon,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SHIELD_INV: {
        'Name': PLocalizer.SailLogoShield,
        'StyleIndex': ShipGlobals.Logos.Player_Shield,
        'Invert': True,
        'Available': 0,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_HEART_INV: {
        'Name': PLocalizer.SailLogoHeart,
        'StyleIndex': ShipGlobals.Logos.Player_Heart,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SKULLCROSS_INV: {
        'Name': PLocalizer.SailLogoSkull,
        'StyleIndex': ShipGlobals.Logos.Contest_Skull,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_OCTOPUS_INV: {
        'Name': PLocalizer.SailLogoOctopus,
        'StyleIndex': ShipGlobals.Logos.Contest_Octopus,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_SHARK_INV: {
        'Name': PLocalizer.SailLogoShark,
        'StyleIndex': ShipGlobals.Logos.Contest_Shark,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_MERMAID_INV: {
        'Name': PLocalizer.SailLogoMermaid,
        'StyleIndex': ShipGlobals.Logos.Contest_Mermaid,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } },
    LOGO_STORMCLOUD_INV: {
        'Name': PLocalizer.SailLogoStormCloud,
        'StyleIndex': ShipGlobals.Logos.Contest_StormCloud,
        'Invert': True,
        'Available': 1,
        'Cost': {
            'Fixed': {
                InventoryType.ItemTypeMoney: 5000 },
            'Relative': { } } } }
UPGRADE_BY_CATINDEX = {
    0: HULL_TYPES,
    1: RIGGING_TYPES,
    2: SAILCOLOR_TYPES,
    3: LOGO_TYPES }

def printGlobals():
    for entryKey in HULL_TYPES:
        hullData = HULL_TYPES[entryKey]
        if hullData['Available'] == 1:
            print 'Hull Type: %s' % hullData['Name']
            print ''
            print '  Upgrade Values'
            for attribName in [
                'Armor',
                'Speed',
                'Turning',
                'Cargo']:
                attribValue = hullData.get(attribName, 1.0)
                print '    %s : %s%%' % (attribName, int(attribValue * 100))
                broadsideType = hullData.get('BroadsideType')
            
            if broadsideType:
                broadsideAmount = int(hullData.get('BroadsideAmount') * 100)
                broadsideName = PLocalizer.InventoryTypeNames.get(broadsideType, 'Error')
                print '    broadsides %s%% %s' % (broadsideAmount, broadsideName)
            
            print ''
            print '  Upgrade Costs'
            costDict = hullData.get('Cost', { })
            for shipClass in HULLS_THAT_CAN_UPGRADE:
                print '    %s' % PLocalizer.ShipClassNames[shipClass]
                for currency in COST_LIST:
                    fixedCost = 0
                    relativeCost = 0
                    if costDict.get('Fixed'):
                        if costDict['Fixed'].get(currency, 0):
                            fixedCost = costDict['Fixed'].get(currency, 0)
                        
                    
                    if costDict.get('Relative'):
                        if costDict['Relative'].get(currency, 0):
                            relativeCost = HULL_RELATIVE_COST_BASIS[shipClass] * costDict['Relative'].get(currency, 0)
                        
                    
                    totalCost = int(fixedCost + relativeCost)
                    if currency == InventoryType.ItemTypeMoney:
                        currencyName = PLocalizer.MoneyName
                    else:
                        currencyName = PLocalizer.InventoryTypeNames.get(currency, 'Unknown Currency')
                    if totalCost:
                        print '      %s %s' % (currencyName, totalCost)
                        continue
                
            
            print ''
            continue
    
    for entryKey in RIGGING_TYPES:
        riggingData = RIGGING_TYPES[entryKey]
        if riggingData['Available'] == 1:
            print 'Sail Type: %s' % riggingData['Name']
            print ''
            print '  Upgrade Values'
            boostInfo = riggingData['SkillBoosts']
            if boostInfo:
                for skillId in boostInfo.keys():
                    skillLevel = boostInfo[skillId]
                    skillName = PLocalizer.InventoryTypeNames[skillId]
                    if skillLevel:
                        print '    %s %s' % (skillName, skillLevel)
                        continue
                
            
            print ''
            print '  Upgrade Costs'
            costDict = riggingData.get('Cost', { })
            for shipClass in HULLS_THAT_CAN_UPGRADE:
                print '    %s' % PLocalizer.ShipClassNames[shipClass]
                for currency in COST_LIST:
                    fixedCost = 0
                    relativeCost = 0
                    if costDict.get('Fixed'):
                        if costDict['Fixed'].get(currency, 0):
                            fixedCost = costDict['Fixed'].get(currency, 0)
                        
                    
                    if costDict.get('Relative'):
                        if costDict['Relative'].get(currency, 0):
                            relativeCost = HULL_RELATIVE_COST_BASIS[shipClass] * costDict['Relative'].get(currency, 0)
                        
                    
                    totalCost = int(fixedCost + relativeCost)
                    if currency == InventoryType.ItemTypeMoney:
                        currencyName = PLocalizer.MoneyName
                    else:
                        currencyName = PLocalizer.InventoryTypeNames.get(currency, 'Unknown Currency')
                    if totalCost:
                        print '      %s %s' % (currencyName, totalCost)
                        continue
                
            
            print ''
            continue
    

