from pandac.PandaModules import VBase4
from pirates.piratesbase import PLocalizer
from pirates.piratesbase import PiratesGlobals
from pirates.ai import HolidayGlobals
from pirates.inventory import ItemGlobals
import random
from pirates.inventory.ItemConstants import DYE_COLORS
HAT = 0
SHIRT = 1
VEST = 2
COAT = 3
PANT = 4
BELT = 5
SOCK = 6
SHOE = 7
DYE_COLOR_LEVEL = {
    0: [
        0,
        1,
        2,
        3,
        4],
    5: [
        5,
        6,
        7,
        8,
        9],
    10: [
        10,
        11,
        12,
        13,
        14],
    15: [
        15,
        16,
        17,
        18,
        19],
    20: [
        20,
        21,
        22,
        23,
        24],
    25: [
        25,
        26,
        27,
        28,
        29,
        30,
        31] }
UNDERWEAR = {
    'm': {
        SHIRT: (0, 0, 0),
        PANT: (2, 2, 0) },
    'f': {
        SHIRT: (0, 0, 0),
        PANT: (1, 2, 0) } }
CLOTHING_NUMBER = {
    'HAT': HAT,
    'SHIRT': SHIRT,
    'VEST': VEST,
    'COAT': COAT,
    'BELT': BELT,
    'PANT': PANT,
    'SHOE': SHOE }
CLOTHING_STRING = {
    HAT: 'HAT',
    SHIRT: 'SHIRT',
    VEST: 'VEST',
    COAT: 'COAT',
    BELT: 'BELT',
    PANT: 'PANT',
    SHOE: 'SHOE' }
CLOTHING_NAMES = {
    0: {
        'MALE': {
            0: 'None',
            1: 'Captain',
            2: 'Tricorn',
            3: 'Navy',
            4: 'EITC',
            5: 'Admiral',
            6: 'Bandana Full',
            7: 'Bandana Regular',
            8: 'Beanie',
            9: 'Barbossa',
            10: 'French',
            11: 'Spanish',
            12: 'French 1',
            13: 'French 2',
            14: 'French 3',
            15: 'Spanish 1',
            16: 'Spanish 2',
            17: 'Spanish 3',
            18: 'Land 1',
            19: 'Land 2',
            20: 'Land 3',
            21: 'Holiday',
            22: 'Party 1',
            23: 'Party 2',
            24: 'GM' },
        'FEMALE': {
            0: 'None',
            1: 'Dress',
            2: 'Redcoat',
            3: 'Navy w/ Feather',
            4: 'Worker',
            5: 'Bandana Full',
            6: 'Bandana Regular',
            7: 'French',
            8: 'Spanish',
            9: 'French 1',
            10: 'French 2',
            11: 'French 3',
            12: 'Spanish 1',
            13: 'Spanish 2',
            14: 'Spanish 3',
            15: 'Land 1',
            16: 'Land 2',
            17: 'Land 3',
            18: 'Holiday',
            19: 'Party 1',
            20: 'Party 2',
            21: 'GM',
            22: 'Tricorn',
            23: 'Beanie' } },
    1: {
        'MALE': {
            0: 'None',
            1: 'Tanktop',
            2: 'Sleeveless',
            3: 'Short Sleeve Round',
            4: 'Short Sleeve V-Neck Closed',
            5: 'Short Sleeve V-Neck Open',
            6: 'Long Sleeve Lowcut Puffy',
            7: 'Long Sleeve V-Neck Closed',
            8: 'Long Sleeve V-Neck Open',
            9: 'Apron',
            10: 'Dealer',
            11: 'Long Sleeve Puffy',
            12: 'Long Sleeve High Neck Puffy' },
        'FEMALE': {
            0: 'Short Sleeve',
            1: 'Short Sleeve Puffy',
            2: 'Long Sleeve Puffy',
            3: 'Long Sleeve Lowcut',
            4: 'Long Sleeve Collar',
            5: 'Long Sleeve Tall Collar',
            6: 'Dress' } },
    2: {
        'MALE': {
            0: 'None',
            1: 'Open',
            2: 'Closed',
            3: 'Long Closed' },
        'FEMALE': {
            0: 'None',
            1: 'Closed',
            2: 'Lowcut',
            3: 'Corset High',
            4: 'Corset Low',
            5: 'Navy' } },
    3: {
        'MALE': {
            0: 'None',
            1: 'Long',
            2: 'Short',
            3: 'Navy',
            4: 'EITC' },
        'FEMALE': {
            0: 'None',
            1: 'Long',
            2: 'Short',
            3: 'Navy',
            3: 'EITC' } },
    4: {
        'MALE': {
            0: 'Long Tucked',
            1: 'Long Untucked',
            2: 'Shorts',
            3: 'Short Pants',
            4: 'Navy',
            5: 'EITC',
            6: 'Apron' },
        'FEMALE': {
            0: 'Short Pants',
            1: 'Shorts',
            2: 'Skirt',
            3: 'Gypsy Dress',
            4: 'Shopkeeper Dress',
            5: 'Navy' } },
    5: {
        'MALE': {
            0: 'None',
            1: 'Sash',
            2: 'Sash',
            3: 'Strap w/ Oval Buckle',
            4: 'Strap w/ Oval Buckle',
            5: 'Strap w/ Square Buckle',
            6: 'Strap w/ Oval Buckle',
            7: 'Strap w/ Oval Buckle',
            8: 'Strap w/ Oval Buckle',
            9: 'Sash',
            10: 'Sash',
            11: 'Sash',
            12: 'Sash',
            13: 'Strap w/ Oval Buckle',
            14: 'Strap w/ Oval Buckle',
            15: 'Strap w/ Square Buckle',
            16: 'Strap w/ Square Buckle',
            17: 'Sash',
            18: 'Strap w/ Square Buckle',
            19: 'Strap w/ Square Buckle' },
        'FEMALE': {
            0: 'None',
            1: 'Sash',
            2: 'Sash',
            3: 'Sasg',
            4: 'Sash',
            5: 'Strap w/ Square Buckle',
            6: 'Strap w/ Square Buckle',
            7: 'Strap w/ Square Buckle',
            8: 'Strap w/ Square Buckle',
            9: 'Strap w/ Square Buckle',
            10: 'Strap w/ Square Buckle',
            11: 'Sash',
            12: 'Sash',
            13: 'Strap w/ Square Buckle',
            14: 'Strap w/ Square Buckle',
            15: 'Sash',
            16: 'Strap w/ Square Buckle',
            17: 'Strap w/ Square Buckle',
            18: 'Sash' } },
    7: {
        'MALE': {
            0: 'None',
            1: 'Tall',
            2: 'Medium',
            3: 'Navy',
            4: 'India',
            5: 'None' },
        'FEMALE': {
            0: 'None',
            1: 'Short',
            2: 'Medium',
            3: 'Knee High',
            4: 'Tall',
            5: 'Navy' } } }
SELECTION_CHOICES = {
    'DEFAULT': {
        'MALE': {
            'FACE': [
                0,
                1,
                2,
                3],
            'HAIR': [
                0,
                1,
                2,
                5,
                6,
                9,
                11,
                12],
            'BEARD': [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                8,
                9],
            'MUSTACHE': [
                0,
                1,
                2,
                3],
            'HAT': {
                0: [
                    0] },
            'SHIRT': {
                1: [
                    0,
                    1,
                    2],
                4: [
                    1,
                    2,
                    3] },
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2] },
            'COAT': {
                0: [
                    0] },
            'PANT': {
                0: [
                    1,
                    2],
                1: [
                    0] },
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                3: [
                    0],
                5: [
                    0] },
            'SHOE': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2] } },
        'FEMALE': {
            'FACE': [
                0,
                1,
                2,
                3],
            'HAIR': [
                0,
                2,
                3,
                5,
                8,
                9,
                10,
                11,
                13,
                14,
                16],
            'HAT': {
                0: [
                    0] },
            'SHIRT': {
                0: [
                    0],
                1: [
                    1],
                2: [
                    0],
                3: [
                    2] },
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3] },
            'COAT': {
                0: [
                    0] },
            'PANT': {
                0: [
                    0,
                    1],
                2: [
                    0] },
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                5: [
                    0],
                6: [
                    0] },
            'SHOE': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0],
                3: [
                    0] } } },
    'NPC': {
        'MALE': {
            'FACE': [
                0,
                1,
                2,
                3,
                4,
                5,
                6],
            'HAIR': [
                0,
                1,
                2,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13],
            'HAT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                7: [
                    0,
                    1,
                    2,
                    3,
                    4],
                8: [
                    0,
                    1,
                    2,
                    3],
                9: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                10: [
                    0],
                11: [
                    0],
                12: [
                    0,
                    1,
                    2],
                13: [
                    0,
                    1],
                14: [
                    0,
                    1],
                15: [
                    0,
                    1,
                    2],
                16: [
                    0,
                    1,
                    2,
                    3],
                17: [
                    0,
                    1,
                    2,
                    3],
                18: [
                    0,
                    1,
                    2],
                19: [
                    0,
                    1],
                20: [
                    0,
                    1],
                21: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                22: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                23: [
                    0,
                    1,
                    2,
                    3,
                    4],
                24: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5] },
            'SHIRT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                5: [
                    0,
                    1,
                    2],
                6: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                7: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                8: [
                    0,
                    1,
                    2],
                9: [
                    0,
                    1,
                    2],
                10: [
                    0],
                11: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16],
                12: [
                    0] },
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6] },
            'COAT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                3: [
                    0],
                4: [
                    0] },
            'PANT': {
                0: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0,
                    1,
                    2] },
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0],
                7: [
                    0],
                8: [
                    0],
                9: [
                    0],
                10: [
                    0],
                11: [
                    0],
                12: [
                    0],
                13: [
                    0],
                14: [
                    0],
                15: [
                    0],
                16: [
                    0],
                17: [
                    0],
                18: [
                    0],
                19: [
                    0] },
            'SHOE': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                3: [
                    0,
                    1,
                    2,
                    4,
                    5],
                4: [
                    0],
                5: [
                    0,
                    1] } },
        'FEMALE': {
            'FACE': [
                0,
                1,
                2,
                3,
                4],
            'HAIR': [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19],
            'HAT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                6: [
                    0,
                    1,
                    2,
                    3,
                    4],
                7: [
                    0,
                    1],
                8: [
                    0],
                9: [
                    0,
                    1,
                    2],
                10: [
                    0,
                    1],
                11: [
                    0,
                    1],
                12: [
                    0,
                    1,
                    2],
                13: [
                    0,
                    1,
                    2,
                    3],
                14: [
                    0,
                    1,
                    2,
                    3],
                15: [
                    0,
                    1,
                    2],
                16: [
                    0,
                    1],
                17: [
                    0,
                    1],
                18: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                19: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                20: [
                    0,
                    1,
                    2,
                    3,
                    4],
                21: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5],
                22: [
                    0],
                23: [
                    0,
                    1,
                    2,
                    3,
                    4] },
            'SHIRT': {
                0: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23],
                5: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                6: [
                    0,
                    1,
                    2,
                    3] },
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13],
                3: [
                    0,
                    1,
                    2,
                    4,
                    5,
                    6],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5] },
            'COAT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14],
                3: [
                    0],
                4: [
                    0] },
            'PANT': {
                0: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18],
                3: [
                    0,
                    1],
                4: [
                    0,
                    1],
                5: [
                    0] },
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0],
                7: [
                    0],
                8: [
                    0],
                9: [
                    0],
                10: [
                    0],
                11: [
                    0],
                12: [
                    0],
                13: [
                    0],
                14: [
                    0],
                15: [
                    0],
                16: [
                    0],
                17: [
                    0],
                18: [
                    0] },
            'SHOE': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                5: [
                    0] } } } }
textures = {
    'MALE': {
        'HAT': [
            [
                [
                    'hat_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_hat_captain_leather',
                    VBase4(36 / 255.0, 26 / 255.0, 9 / 255.0, 1.0)],
                [
                    'PM_hat_captain_baron',
                    VBase4(36 / 255.0, 26 / 255.0, 9 / 255.0, 1.0)],
                [
                    'PM_hat_captain_prince',
                    VBase4(36 / 255.0, 26 / 255.0, 9 / 255.0, 1.0)],
                [
                    'PM_hat_captain_privateer',
                    VBase4(36 / 255.0, 26 / 255.0, 9 / 255.0, 1.0)]],
            [
                [
                    'hat_tricorn_brown',
                    VBase4(43 / 255.0, 48 / 255.0, 62 / 255.0, 1.0)],
                [
                    'hat_tricorn_orange',
                    VBase4(125 / 255.0, 59 / 255.0, 37 / 255.0, 1.0)],
                [
                    'hat_tricorn_black_skull',
                    VBase4(33 / 255.0, 37 / 255.0, 36 / 255.0, 1.0)],
                [
                    'hat_tricorn_navy_goldtrim',
                    VBase4(32 / 255.0, 51 / 255.0, 78 / 255.0, 1.0)],
                [
                    'hat_tricorn_valentines',
                    VBase4(132 / 255.0, 51 / 255.0, 51 / 255.0, 1.0)],
                [
                    'hat_tricorn_mardiGras',
                    VBase4(132 / 255.0, 51 / 255.0, 51 / 255.0, 1.0)]],
            [
                [
                    'hat_navy',
                    VBase4(63 / 255.0, 63 / 255.0, 63 / 255.0, 1.0)],
                [
                    'hat_navy_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_navy_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_eitc',
                    VBase4(42 / 255.0, 42 / 255.0, 42 / 255.0, 1.0)]],
            [
                [
                    'hat_admiral',
                    VBase4(49 / 255.0, 49 / 255.0, 49 / 255.0, 1.0)]],
            [
                [
                    'hat_bandana_plain',
                    VBase4(149 / 255.0, 149 / 255.0, 149 / 255.0, 1.0)],
                [
                    'hat_bandana_full_blue',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'hat_bandana_full_skullcrossbones',
                    VBase4(47 / 255.0, 47 / 255.0, 47 / 255.0, 1.0)],
                [
                    'hat_bandanna_full_blue_patches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandanna_full_blue_zigzag',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_full_polkadot_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'pir_t_clo_upt_bandana_thanks08',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_china',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_bandana_plain',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_full_blue',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'hat_bandana_full_skullcrossbones',
                    VBase4(47 / 255.0, 47 / 255.0, 47 / 255.0, 1.0)],
                [
                    'hat_bandanna_full_blue_patches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandanna_full_blue_zigzag',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_beanie_plain',
                    VBase4(96 / 255.0, 91 / 255.0, 82 / 255.0, 1.0)],
                [
                    'hat_beanie_black_crossbones',
                    VBase4(12 / 255.0, 10 / 255.0, 11 / 255.0, 1.0)],
                [
                    'hat_beanie_blue_skull',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_greensilk',
                    VBase4(0 / 255.0, 128 / 255.0, 0 / 255.0, 1.0)],
                [
                    'hat_beanie_brown_beads',
                    VBase4(0 / 255.0, 128 / 255.0, 0 / 255.0, 1.0)],
                [
                    'hat_beanie_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_barbossa+hat_barbossa_feather',
                    VBase4(43 / 255.0, 48 / 255.0, 62 / 255.0, 1.0)],
                [
                    'hat_barb_style_brown+hat_barb_style_brown_feather',
                    VBase4(78 / 255.0, 64 / 255.0, 55 / 255.0, 1.0)],
                [
                    'hat_barossa_style_hat_blue_knit_band+hat_barossa_style_hat_blue_knit_band_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_barossa_style_hat_brown_buttons+hat_barossa_style_hat_brown_buttons_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_barossa_style_hat_brown_purple_feather+hat_barossa_style_hat_brown_purple_feather_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_barbossa+hat_barbossa_advanced_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_barbossa_intermediate_outfit+hat_barbossa_intermediate_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french+hat_french_feather',
                    VBase4(32 / 255.0, 60 / 255.0, 25 / 255.0, 1.0)],
                [
                    'hat_tricorn_assassin+hat_feather_assassin',
                    VBase4(32 / 255.0, 60 / 255.0, 25 / 255.0, 1.0)],
                [
                    'hat_tricorn_peacock+hat_feather_peacock',
                    VBase4(32 / 255.0, 60 / 255.0, 25 / 255.0, 1.0)],
                [
                    'hat_tricorn_scourge+hat_feather_scourge',
                    VBase4(32 / 255.0, 60 / 255.0, 25 / 255.0, 1.0)]],
            [
                [
                    'hat_barbossa+hat_spanish_feather',
                    VBase4(75 / 255.0, 50 / 255.0, 25 / 255.0, 1.0)],
                [
                    'hat_spanish_zombie+hat_feather_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french_1_blue_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_1_dkgreen_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_1_violet_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french_2_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_2_brown_leather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french_3_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_3_navyblue_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_spanish_1_black',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_1_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_1_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_spanish_2_bronze',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_2_steel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_2_steel_embossed',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_2_steel_rusted',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_spanish_3_black_redband',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_3_brown_leather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_3_burgundy_black',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_3_grey_brownband',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_land_1_black_blueband',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_1_brown_leather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_1_straw',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_land_2_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_2_blue_red_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_land_3_steel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_3_steel_goldinlay',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_holiday_blue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_blue_white_stripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_green',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_orange',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_red_white',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_red_white_stripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_violet',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_white',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_party_1_blue_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_green_orange',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_lightblue_pink',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_orange_green',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_pink_lightblue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_purple_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_red_blue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_red_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_yellow_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_yellow_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_party_2_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_blue_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_brown_blackband_buckle',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_green_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_StPatricks',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_gm_black_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_dkgreen_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_gold_black_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_red_black_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_red_dkgreen_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_rose_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_mushroom',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'SHIRT': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_shirt_tanktop_sweatstained',
                    VBase4(180 / 255.0, 178 / 255.0, 178 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_stripes',
                    VBase4(179 / 255.0, 164 / 255.0, 147 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_plain',
                    VBase4(228 / 255.0, 227 / 255.0, 227 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_buttons',
                    VBase4(192 / 255.0, 165 / 255.0, 154 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_suspenders',
                    VBase4(218 / 255.0, 200 / 255.0, 174 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_scourge',
                    VBase4(218 / 255.0, 200 / 255.0, 174 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_seaserpent',
                    VBase4(218 / 255.0, 200 / 255.0, 174 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_nosleeves_stripe',
                    VBase4(145 / 255.0, 123 / 255.0, 94 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_ties',
                    VBase4(193 / 255.0, 200 / 255.0, 201 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_leatherfront',
                    VBase4(169 / 255.0, 177 / 255.0, 185 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_centerseam',
                    VBase4(234 / 255.0, 233 / 255.0, 211 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_bluethreebutton',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_palegreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_purplesidebuckle',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_salmon',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_flax_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_silk_blue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_silk_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_silk_white',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_short_round_frontlacing',
                    VBase4(79 / 255.0, 85 / 255.0, 90 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_frontbuttons',
                    VBase4(70 / 255.0, 51 / 255.0, 38 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_stripes',
                    VBase4(131 / 255.0, 126 / 255.0, 137 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_leather_cloth',
                    VBase4(227 / 255.0, 194 / 255.0, 132 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_blue_whitecollar',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_cloth_black',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_cloth_caramel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_darkbrown_buckle',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_greengold_whitecollar',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_browncollar',
                    VBase4(175 / 255.0, 162 / 255.0, 144 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_fabricwaistband',
                    VBase4(110 / 255.0, 110 / 255.0, 98 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_leatherwaistband',
                    VBase4(123 / 255.0, 85 / 255.0, 80 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_yellowcollar',
                    VBase4(116 / 255.0, 161 / 255.0, 158 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_browncollar',
                    VBase4(175 / 255.0, 162 / 255.0, 144 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_fabricwaistband',
                    VBase4(110 / 255.0, 110 / 255.0, 98 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_leatherwaistband',
                    VBase4(123 / 255.0, 85 / 255.0, 80 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_yellowcollar',
                    VBase4(116 / 255.0, 161 / 255.0, 158 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_long_sleeve_puffy_ClothWithTies',
                    VBase4(170 / 255.0, 161 / 255.0, 142 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_cloth_brown_leather',
                    VBase4(154 / 255.0, 146 / 255.0, 132 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_plain',
                    VBase4(210 / 255.0, 216 / 255.0, 220 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_center_tie',
                    VBase4(207 / 255.0, 192 / 255.0, 161 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_cream_orangevest',
                    VBase4(95 / 255.0, 47 / 255.0, 17 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_white_brownpillowvest',
                    VBase4(77 / 255.0, 48 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_white_brownvest',
                    VBase4(36 / 255.0, 26 / 255.0, 20 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_white_redvest',
                    VBase4(89 / 255.0, 21 / 255.0, 30 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_white_redvest_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_browncollar',
                    VBase4(175 / 255.0, 162 / 255.0, 144 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_fabricwaistband',
                    VBase4(110 / 255.0, 110 / 255.0, 98 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_leatherwaistband',
                    VBase4(123 / 255.0, 85 / 255.0, 80 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_yellowcollar',
                    VBase4(116 / 255.0, 161 / 255.0, 158 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_tan_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 2550.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_apron',
                    VBase4(82 / 255.0, 88 / 255.0, 93 / 255.0, 1.0)],
                [
                    'PM_shirt_apron_black',
                    VBase4(82 / 255.0, 88 / 255.0, 93 / 255.0, 1.0)],
                [
                    'PM_shirt_apron_black',
                    VBase4(82 / 255.0, 88 / 255.0, 93 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_dealer',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_long_sleeve_puffy_cincodemayo',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_halloween',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_thanksgiving',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_guyfawkes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_valentines',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_winterholiday',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_caribbeanday',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_carnival',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_chinesenewyear',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_firstfall',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_newyearseve',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_stpatricks',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_summersolstice',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_wintersolstice',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_firstspring',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_mardiGras',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_long_sleeve_highneck_plain',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 2550.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_highneck_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 2550.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_highneck_baron',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 2550.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_highneck_peacock',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 2550.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_highneck_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 2550.0, 1.0)]]],
        'VEST': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_vest_open_leather_silk',
                    VBase4(172 / 255.0, 108 / 255.0, 60 / 255.0, 1.0)],
                [
                    'PM_vest_open_PatchworkDark',
                    VBase4(104 / 255.0, 112 / 255.0, 107 / 255.0, 1.0)],
                [
                    'PM_vest_open_belts',
                    VBase4(96 / 255.0, 75 / 255.0, 53 / 255.0, 1.0)],
                [
                    'PM_vest_open_clasp',
                    VBase4(91 / 255.0, 109 / 255.0, 109 / 255.0, 1.0)],
                [
                    'PM_vest_open_buttons',
                    VBase4(70 / 255.0, 98 / 255.0, 108 / 255.0, 1.0)],
                [
                    'PM_vest_open_blue_silverbuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_open_brown_blacklapel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_open_brown_redscarf',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_open_green_blacklapel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_open_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_vest_closed_silk_stripe_lapel',
                    VBase4(118 / 255.0, 101 / 255.0, 73 / 255.0, 1.0)],
                [
                    'PM_vest_closed_clasp',
                    VBase4(151 / 255.0, 127 / 255.0, 101 / 255.0, 1.0)],
                [
                    'PM_vest_closed_lapel',
                    VBase4(187 / 255.0, 158 / 255.0, 108 / 255.0, 1.0)],
                [
                    'PM_vest_closed_leathertop',
                    VBase4(198 / 255.0, 190 / 255.0, 168 / 255.0, 1.0)],
                [
                    'PM_vest_closed_stripe',
                    VBase4(174 / 255.0, 163 / 255.0, 163 / 255.0, 1.0)],
                [
                    'PM_vest_closed_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_closed_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_vest_long_closed_a',
                    VBase4(145 / 255.0, 141 / 255.0, 130 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_brown_whitecollar',
                    VBase4(71 / 255.0, 37 / 255.0, 3 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_rust',
                    VBase4(76 / 255.0, 30 / 255.0, 14 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_white_ropebelt',
                    VBase4(92 / 255.0, 91 / 255.0, 79 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_yellowgreen_stripes',
                    VBase4(110 / 255.0, 93 / 255.0, 39 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_blackgold',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'COAT': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_coat_long_braidsandfloralpattern',
                    VBase4(91 / 255.0, 76 / 255.0, 59 / 255.0, 1.0)],
                [
                    'PM_coat_long_braids_embroidery',
                    VBase4(67 / 255.0, 61 / 255.0, 41 / 255.0, 1.0)],
                [
                    'PM_coat_long_cloth_lighttrim',
                    VBase4(143 / 255.0, 144 / 255.0, 164 / 255.0, 1.0)],
                [
                    'PM_coat_long_darktrim_backties',
                    VBase4(93 / 255.0, 79 / 255.0, 53 / 255.0, 1.0)],
                [
                    'PM_coat_long_fabric_leatherbelt',
                    VBase4(32 / 255.0, 44 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_coat_long_french',
                    VBase4(41 / 255.0, 36 / 255.0, 38 / 255.0, 1.0)],
                [
                    'PM_coat_long_leather',
                    VBase4(43 / 255.0, 28 / 255.0, 15 / 255.0, 1.0)],
                [
                    'PM_coat_long_afro',
                    VBase4(86 / 255.0, 74 / 255.0, 41 / 255.0, 1.0)],
                [
                    'PM_coat_long_taupe',
                    VBase4(64 / 255.0, 54 / 255.0, 49 / 255.0, 1.0)],
                [
                    'PM_coat_long_brown',
                    VBase4(69 / 255.0, 42 / 255.0, 21 / 255.0, 1.0)],
                [
                    'PM_coat_long_blue_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_gold_blackbuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_green_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_red_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_blackgold',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_royal',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_baron',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_coat_short_blackwithstitching',
                    VBase4(22 / 255.0, 23 / 255.0, 25 / 255.0, 1.0)],
                [
                    'PM_coat_short_cloth_darkleather_goldtrim',
                    VBase4(85 / 255.0, 86 / 255.0, 60 / 255.0, 1.0)],
                [
                    'PM_coat_short_dark_stringtiesback',
                    VBase4(59 / 255.0, 61 / 255.0, 63 / 255.0, 1.0)],
                [
                    'PM_coat_short_red_blackleathertrim',
                    VBase4(130 / 255.0, 31 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_coat_short_wool_brownleathertrim',
                    VBase4(117 / 255.0, 104 / 255.0, 77 / 255.0, 1.0)],
                [
                    'PM_coat_short_yellow_blacklapel',
                    VBase4(121 / 255.0, 88 / 255.0, 40 / 255.0, 1.0)],
                [
                    'PM_coat_short_purple_blackcollar',
                    VBase4(79 / 255.0, 48 / 255.0, 58 / 255.0, 1.0)],
                [
                    'PM_coat_short_blue_goldtrim',
                    VBase4(33 / 255.0, 51 / 255.0, 59 / 255.0, 1.0)],
                [
                    'PM_coat_short_black_checkerboard',
                    VBase4(33 / 255.0, 51 / 255.0, 59 / 255.0, 1.0)],
                [
                    'PM_coat_short_brown_stripes',
                    VBase4(33 / 255.0, 51 / 255.0, 59 / 255.0, 1.0)],
                [
                    'PM_coat_short_seaserpent',
                    VBase4(33 / 255.0, 51 / 255.0, 59 / 255.0, 1.0)]],
            [
                [
                    'PM_navy',
                    VBase4(148 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)]],
            [
                [
                    'PM_eitc',
                    VBase4(31 / 255.0, 33 / 255.0, 31 / 255.0, 1.0)],
                [
                    'PM_coat_closed_china',
                    VBase4(31 / 255.0, 33 / 255.0, 31 / 255.0, 1.0)],
                [
                    'PM_coat_closed_diplomat',
                    VBase4(31 / 255.0, 33 / 255.0, 31 / 255.0, 1.0)]]],
        'PANT': [
            [
                [
                    'PM_pant_long_pants_tucked_LeatherGoldButtons',
                    VBase4(83 / 255.0, 70 / 255.0, 53 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_leathergoldbuttons_nopatch',
                    VBase4(131 / 255.0, 106 / 255.0, 71 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_cotton_leathersidepocket',
                    VBase4(154 / 255.0, 164 / 255.0, 170 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_leather_buttonfront',
                    VBase4(63 / 255.0, 63 / 255.0, 63 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_cloth_leatherstripes',
                    VBase4(79 / 255.0, 79 / 255.0, 79 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_leather_miniknives',
                    VBase4(79 / 255.0, 79 / 255.0, 79 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_black_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_blue_stripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_brown_sidebuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_greygreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_red_sidebones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_red_yellowstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_bluesidetrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_violet_yellowstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_StPatricks',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_valentines',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_baron',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_china',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_peacock',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_long_pants_untucked_plain3',
                    VBase4(138 / 255.0, 138 / 255.0, 138 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_celticbuttons',
                    VBase4(183 / 255.0, 165 / 255.0, 178 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_twotone',
                    VBase4(186 / 255.0, 182 / 255.0, 187 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_onetone',
                    VBase4(178 / 255.0, 177 / 255.0, 179 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leatherpocket_trim',
                    VBase4(116 / 255.0, 101 / 255.0, 70 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_skullsnaps_suede',
                    VBase4(213 / 255.0, 186 / 255.0, 140 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_skullsnaps_no_cuff',
                    VBase4(218 / 255.0, 191 / 255.0, 145 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_skullsnaps_no_stripe',
                    VBase4(218 / 255.0, 191 / 255.0, 145 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_plain1',
                    VBase4(137 / 255.0, 124 / 255.0, 97 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_plain2',
                    VBase4(61 / 255.0, 66 / 255.0, 64 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_plain',
                    VBase4(131 / 255.0, 117 / 255.0, 107 / 255.0, 1.0)],
                [
                    'zomb_long_pants_untucked',
                    VBase4(144 / 255.0, 135 / 255.0, 111 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_bluegreensash',
                    VBase4(44 / 255.0, 66 / 255.0, 64 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_greenbronzesash',
                    VBase4(41 / 255.0, 37 / 255.0, 16 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_blackgold',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_brownpatches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_chaps',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_greenembroidery',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_greensilk',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_mardiGras',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_white_sidenet',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_white_greenstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_tan_yellowtop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_tan_sidestitch',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_blue_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_shorts_threesidebuttons',
                    VBase4(94 / 255.0, 92 / 255.0, 69 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_3ties',
                    VBase4(184 / 255.0, 160 / 255.0, 107 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_1buttonflap',
                    VBase4(224 / 255.0, 213 / 255.0, 205 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_3buckle',
                    VBase4(122 / 255.0, 122 / 255.0, 99 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_browncloth',
                    VBase4(52 / 255.0, 30 / 255.0, 9 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_short_pants_twotonewithsash',
                    VBase4(92 / 255.0, 108 / 255.0, 126 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_sidepocket',
                    VBase4(126 / 255.0, 109 / 255.0, 97 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_simplecanvas',
                    VBase4(190 / 255.0, 177 / 255.0, 149 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_sideleather',
                    VBase4(203 / 255.0, 184 / 255.0, 163 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_blue_white_top',
                    VBase4(33 / 255.0, 45 / 255.0, 84 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_brown_cloth',
                    VBase4(52 / 255.0, 30 / 255.0, 9 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_light_brown',
                    VBase4(125 / 255.0, 87 / 255.0, 43 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_rust',
                    VBase4(77 / 255.0, 36 / 255.0, 18 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_slate',
                    VBase4(55 / 255.0, 71 / 255.0, 79 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_light_brown_enhance',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_navy',
                    VBase4(156 / 255.0, 145 / 255.0, 132 / 255.0, 1.0)]],
            [
                [
                    'PM_eitc',
                    VBase4(31 / 255.0, 33 / 255.0, 31 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_apron',
                    VBase4(145 / 255.0, 130 / 255.0, 102 / 255.0, 1.0)],
                [
                    'PM_pant_apron_black',
                    VBase4(145 / 255.0, 130 / 255.0, 102 / 255.0, 1.0)],
                [
                    'PM_pant_apron_black',
                    VBase4(145 / 255.0, 130 / 255.0, 102 / 255.0, 1.0)]]],
        'BELT': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_belt_sash_plain',
                    VBase4(195 / 255.0, 193 / 255.0, 188 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_celticbuckle',
                    VBase4(108 / 255.0, 97 / 255.0, 93 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_oval+PM_belt_buckle_oval',
                    VBase4(65 / 255.0, 43 / 255.0, 1 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_LeatherBrown+PM_belt_buckle_SkullGold',
                    VBase4(40 / 255.0, 30 / 255.0, 20 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_black+PM_belt_buckle_square',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_blackleather_01+PM_belt_buckle_goldskull_01',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_brownleather_01+PM_belt_buckle_ovalgold_01',
                    VBase4(41 / 255.0, 29 / 255.0, 14 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_blackleather_01+PM_belt_buckle_ovalgold_02',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_bluegold',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_goldtassel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_pink',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_oval_gold_brownleather+PM_belt_buckle_oval_gold_brownleather',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_oval_goldskull_blackleather+PM_belt_buckle_oval_goldskull_blackleather',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_sculpture_blackbutton+PM_belt_buckle_square_sculpture_blackbutton',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_silver_blueleather+PM_belt_buckle_square_silver_blueleather',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_red_basic_outfit+PM_belt_sash_red_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_advanced_outfit+PM_belt_buckle_square_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_advanced_outfit+PM_belt_buckle_square_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_peacock',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_privateer+PM_belt_buckle_square_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_scourge+PM_belt_buckle_square_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_seaserpent+PM_belt_buckle_square_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_zombie+PM_belt_buckle_square_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'SHOE': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_shoe_tall_boots_TanWithFlap',
                    VBase4(40 / 255.0, 32 / 255.0, 24 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_2buckle',
                    VBase4(17 / 255.0, 16 / 255.0, 14 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_lace',
                    VBase4(60 / 255.0, 47 / 255.0, 33 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_leatherlower',
                    VBase4(35 / 255.0, 27 / 255.0, 24 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_black_furtop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_blue_straps',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_brown_furtop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_brown_laces',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_blue_furtop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_emerald',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_royal',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_spurs',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_StPatricks',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_valentines',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boot_china',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boot_peacock',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boot_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shoe_medium_boots_laced',
                    VBase4(5 / 255.0, 5 / 255.0, 5 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_buckle',
                    VBase4(36 / 255.0, 34 / 255.0, 31 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_lacefront',
                    VBase4(35 / 255.0, 29 / 255.0, 24 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_plain',
                    VBase4(36 / 255.0, 32 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_brown_greentops',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_light_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_mardiGras',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_blue',
                    VBase4(0 / 255.0, 0 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_short_boot_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shoe_navy',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)],
                [
                    'PM_shoe_navy_buckle',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)],
                [
                    'PM_shoe_navy_flap',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)],
                [
                    'PM_shoe_navy_lace',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)],
                [
                    'PM_shoe_navy_singlestrap',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)],
                [
                    'PM_shoe_navy_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_navy_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_eitc',
                    VBase4(16 / 255.0, 16 / 255.0, 16 / 255.0, 1.0)],
                [
                    'PM_shoe_eitc_boots_assassin',
                    VBase4(16 / 255.0, 16 / 255.0, 16 / 255.0, 1.0)],
                [
                    'PM_shoe_eitc_boots_baron',
                    VBase4(16 / 255.0, 16 / 255.0, 16 / 255.0, 1.0)]],
            [
                [
                    'PM_shoe_cuff_boots_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_cuff_boots_redtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_cuff_boots_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_cuff_boots_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_cuff_boots_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_cuff_boots_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_cuff_boots_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]] },
    'FEMALE': {
        'HAT': [
            [
                [
                    'hat_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_hat_dress_base+FP_hat_dress_feather',
                    VBase4(118 / 255.0, 104 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_hat_dress_blue_purplefeather+FP_hat_dress_blue_purplefeather_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_green_stringband+FP_hat_dress_green_stringband_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_pink_bluefeather+FP_hat_dress_pink_bluefeather_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_purple_butterfly+FP_hat_dress_purple_butterfly_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_advanced_outfit+FP_hat_dress_advanced_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_intermediate_outfit+FP_hat_dress_intermediate_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_privateer+FP_hat_feather_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_navy',
                    VBase4(21 / 255.0, 20 / 255.0, 23 / 255.0, 1.0)],
                [
                    'hat_navy_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_navy_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_navy_hat+FP_hat_dress_feather',
                    VBase4(122 / 255.0, 100 / 255.0, 65 / 255.0, 1.0)],
                [
                    'FP_hat_featherhat_baroness+FP_hat_featherhat_feather_baroness',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_feather_hat_prince+FP_hat_feather_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_hat_worker',
                    VBase4(162 / 255.0, 162 / 255.0, 162 / 255.0, 1.0)]],
            [
                [
                    'hat_bandana_plain',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'hat_bandana_full_blue',
                    VBase4(111 / 255.0, 148 / 255.0, 148 / 255.0, 1.0)],
                [
                    'hat_bandana_full_skullcrossbones',
                    VBase4(29 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)],
                [
                    'hat_bandana_full_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_full_redstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_full_polkadot_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'pir_t_clo_upt_bandana_thanks08',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_redsilk',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_china',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_bandana_plain',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'hat_bandana_full_blue',
                    VBase4(111 / 255.0, 148 / 255.0, 148 / 255.0, 1.0)],
                [
                    'hat_bandana_full_skullcrossbones',
                    VBase4(29 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)],
                [
                    'hat_bandana_full_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_bandana_full_redstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french+hat_french_feather',
                    VBase4(32 / 255.0, 60 / 255.0, 25 / 255.0, 1.0)],
                [
                    'hat_tricorn_mardiGras+hat_french_feather_mardiGras',
                    VBase4(32 / 255.0, 60 / 255.0, 25 / 255.0, 1.0)],
                [
                    'hat_tricorn_assassin+hat_feather_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_tricorn_peacock+hat_feather_peacock',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_tricorn_scourge+hat_feather_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_barbossa+hat_spanish_feather',
                    VBase4(75 / 255.0, 50 / 255.0, 25 / 255.0, 1.0)],
                [
                    'hat_spanish_zombie+hat_feather_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french_1_blue_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_1_dkgreen_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_1_violet_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french_2_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_2_brown_leather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_french_3_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_french_3_navyblue_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_spanish_1_black',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_1_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_1_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_spanish_2_bronze',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_2_steel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_2_steel_embossed',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_2_steel_rusted',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_spanish_3_black_redband',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_3_brown_leather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_3_burgundy_black',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_spanish_3_grey_brownband',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_land_1_black_blueband',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_1_brown_leather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_1_straw',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_land_2_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_2_blue_red_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_land_3_steel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_land_3_steel_goldinlay',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_holiday_blue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_blue_white_stripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_green',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_orange',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_red_white',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_red_white_stripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_violet',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_white',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_holiday_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_party_1_blue_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_green_orange',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_lightblue_pink',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_orange_green',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_pink_lightblue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_purple_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_red_blue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_red_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_yellow_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_1_yellow_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_party_2_black_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_blue_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_brown_blackband_buckle',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_green_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_party_2_StPatricks',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_gm_black_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_dkgreen_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_gold_black_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_red_black_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_red_dkgreen_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_gm_rose_skullcrossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_tricorn_valentines',
                    VBase4(60 / 255.0, 25 / 255.0, 25 / 255.0, 1.0)]],
            [
                [
                    'hat_beanie_plain',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_black_crossbones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_blue_skull',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_greensilk',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_brown_beads',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'hat_beanie_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'hat_mushroom',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'SHIRT': [
            [
                [
                    'FP_shirt_short_sleeve_stitch',
                    VBase4(181 / 255.0, 180 / 255.0, 168 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_3button',
                    VBase4(171 / 255.0, 112 / 255.0, 94 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_collar',
                    VBase4(152 / 255.0, 164 / 255.0, 144 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_ties',
                    VBase4(142 / 255.0, 134 / 255.0, 150 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_bluelace',
                    VBase4(80 / 255.0, 101 / 255.0, 111 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_pinkwhite',
                    VBase4(113 / 255.0, 85 / 255.0, 100 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_yellowgold',
                    VBase4(150 / 255.0, 131 / 255.0, 91 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_scourge',
                    VBase4(150 / 255.0, 131 / 255.0, 91 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_seaserpent',
                    VBase4(150 / 255.0, 131 / 255.0, 91 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_short_sleeve_puffy_smFrontLacing',
                    VBase4(195 / 255.0, 205 / 255.0, 174 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_2ties',
                    VBase4(224 / 255.0, 207 / 255.0, 182 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_3button',
                    VBase4(151 / 255.0, 153 / 255.0, 135 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_front_bow',
                    VBase4(157 / 255.0, 106 / 255.0, 110 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_lightgreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_powderblue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_red_creamtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_red_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_puffy_collarbuttons',
                    VBase4(104 / 255.0, 100 / 255.0, 83 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_broach',
                    VBase4(192 / 255.0, 146 / 255.0, 140 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_front_tie',
                    VBase4(173 / 255.0, 181 / 255.0, 198 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_stitch',
                    VBase4(95 / 255.0, 103 / 255.0, 94 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_blue_whitecuffs',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_olivegreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_purple_whitecuffs',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_lowcut_leather_corset_ruffles',
                    VBase4(211 / 255.0, 194 / 255.0, 165 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_3button',
                    VBase4(103 / 255.0, 106 / 255.0, 93 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_ruffles',
                    VBase4(208 / 255.0, 192 / 255.0, 161 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_ties',
                    VBase4(201 / 255.0, 179 / 255.0, 148 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_brown_greensleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_pink_whitecollar',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_white_greysleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_tan_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_collar_lacesleeve',
                    VBase4(170 / 255.0, 166 / 255.0, 177 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_collarbuttons',
                    VBase4(81 / 255.0, 93 / 255.0, 78 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_largestripes',
                    VBase4(107 / 255.0, 65 / 255.0, 64 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_stitches',
                    VBase4(89 / 255.0, 96 / 255.0, 94 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_white_brownvest',
                    VBase4(86 / 255.0, 57 / 255.0, 34 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_white_greenvest',
                    VBase4(54 / 255.0, 56 / 255.0, 56 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_white_redvest',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_caribbeanday',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_cincodemayo',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_guyfawkes',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_halloween',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_summersolstice',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_thanksgiving',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_winterholiday',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_carnival',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_chinesenewyear',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_valentines',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_firstfall',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_firstspring',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_newyearseve',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_stpatricks',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_wintersolstice',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_mardiGras',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_tall_collar_leather_vest_fleur',
                    VBase4(174 / 255.0, 162 / 255.0, 132 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_buttons',
                    VBase4(187 / 255.0, 179 / 255.0, 156 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_stitch',
                    VBase4(149 / 255.0, 138 / 255.0, 113 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_ties',
                    VBase4(237 / 255.0, 228 / 255.0, 203 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_green',
                    VBase4(97 / 255.0, 115 / 255.0, 39 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_lightblue',
                    VBase4(93 / 255.0, 116 / 255.0, 125 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_purplewhite',
                    VBase4(137 / 255.0, 121 / 255.0, 156 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_whiteruff',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_baroness',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_gypsy_dress_a',
                    VBase4(151 / 255.0, 85 / 255.0, 23 / 255.0, 1.0)],
                [
                    'FP_gypsy_dress_b',
                    VBase4(86 / 255.0, 43 / 255.0, 29 / 255.0, 1.0)],
                [
                    'FP_bartender_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)],
                [
                    'FP_shopkeeps_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)]]],
        'VEST': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_vest_closed_clothtwobutton',
                    VBase4(169 / 255.0, 176 / 255.0, 180 / 255.0, 1.0)],
                [
                    'FP_vest_closed_plain',
                    VBase4(188 / 255.0, 191 / 255.0, 165 / 255.0, 1.0)],
                [
                    'FP_vest_closed_stripes',
                    VBase4(162 / 255.0, 170 / 255.0, 175 / 255.0, 1.0)],
                [
                    'FP_vest_closed_ties',
                    VBase4(178 / 255.0, 141 / 255.0, 108 / 255.0, 1.0)],
                [
                    'FP_vest_closed_browngold',
                    VBase4(80 / 255.0, 35 / 255.0, 27 / 255.0, 1.0)],
                [
                    'FP_vest_closed_brownpurple',
                    VBase4(96 / 255.0, 42 / 255.0, 50 / 255.0, 1.0)],
                [
                    'FP_vest_closed_lightgreen',
                    VBase4(93 / 255.0, 91 / 255.0, 57 / 255.0, 1.0)],
                [
                    'FP_vest_closed_redblack',
                    VBase4(23 / 255.0, 15 / 255.0, 15 / 255.0, 1.0)],
                [
                    'FP_vest_closed_whiteblue',
                    VBase4(53 / 255.0, 63 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_vest_closed_yellowgreen',
                    VBase4(104 / 255.0, 78 / 255.0, 26 / 255.0, 1.0)],
                [
                    'FP_vest_closed_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_vest_lowcut_clothtwobutton',
                    VBase4(159 / 255.0, 170 / 255.0, 182 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_onebutton',
                    VBase4(212 / 255.0, 169 / 255.0, 123 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_stripes',
                    VBase4(143 / 255.0, 136 / 255.0, 92 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_ties',
                    VBase4(155 / 255.0, 61 / 255.0, 51 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_bluegold',
                    VBase4(51 / 255.0, 79 / 255.0, 89 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_browngold',
                    VBase4(103 / 255.0, 47 / 255.0, 28 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_greenyellow',
                    VBase4(41 / 255.0, 79 / 255.0, 49 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_lightyellow',
                    VBase4(116 / 255.0, 116 / 255.0, 55 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_purplegold',
                    VBase4(64 / 255.0, 45 / 255.0, 90 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_redblack',
                    VBase4(76 / 255.0, 6 / 255.0, 7 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_brownpillowvest',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_darkbluegold',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_redbrown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_vest_low_cut_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_corset_high_LeatherStraps',
                    VBase4(82 / 255.0, 82 / 255.0, 82 / 255.0, 1.0)],
                [
                    'FP_corset_high_FrillyLacy',
                    VBase4(127 / 255.0, 69 / 255.0, 63 / 255.0, 1.0)],
                [
                    'FP_corset_high_SimpleCanvas',
                    VBase4(118 / 255.0, 106 / 255.0, 61 / 255.0, 1.0)],
                [
                    'zomb_corset_low_fourlaces',
                    VBase4(121 / 255.0, 124 / 255.0, 103 / 255.0, 1.0)],
                [
                    'FP_corset_high_bluegray',
                    VBase4(67 / 255.0, 78 / 255.0, 84 / 255.0, 1.0)],
                [
                    'FP_corset_high_lightblue',
                    VBase4(96 / 255.0, 112 / 255.0, 117 / 255.0, 1.0)],
                [
                    'FP_corset_high_yellow',
                    VBase4(126 / 255.0, 124 / 255.0, 83 / 255.0, 1.0)],
                [
                    'FP_corset_high_peacock',
                    VBase4(126 / 255.0, 124 / 255.0, 83 / 255.0, 1.0)],
                [
                    'FP_corset_high_zombie',
                    VBase4(126 / 255.0, 124 / 255.0, 83 / 255.0, 1.0)]],
            [
                [
                    'FP_corset_low_fourlaces',
                    VBase4(142 / 255.0, 78 / 255.0, 18 / 255.0, 1.0)],
                [
                    'FP_corset_low_print',
                    VBase4(110 / 255.0, 130 / 255.0, 150 / 255.0, 1.0)],
                [
                    'FP_corset_low_ribs',
                    VBase4(243 / 255.0, 224 / 255.0, 186 / 255.0, 1.0)],
                [
                    'FP_corset_low_blue_whitecross',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_corset_low_green_goldbuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_corset_low_white_redvest',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_corset_low_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_corset_low_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_corset_low_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_navy',
                    VBase4(183 / 255.0, 177 / 255.0, 165 / 255.0, 1.0)]]],
        'COAT': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_coat_long_patchwork',
                    VBase4(189 / 255.0, 178 / 255.0, 145 / 255.0, 1.0)],
                [
                    'FP_coat_long_2button',
                    VBase4(179 / 255.0, 155 / 255.0, 130 / 255.0, 1.0)],
                [
                    'FP_coat_long_3buttonstripes',
                    VBase4(85 / 255.0, 94 / 255.0, 97 / 255.0, 1.0)],
                [
                    'FP_coat_long_pockets',
                    VBase4(126 / 255.0, 81 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_coat_long_browngold',
                    VBase4(64 / 255.0, 51 / 255.0, 27 / 255.0, 1.0)],
                [
                    'FP_coat_long_black_whitesleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_blue_white_collar',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_red_whitesleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_purple_enhance_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_redgold_whitesleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_coat_short_crocodileskin',
                    VBase4(104 / 255.0, 102 / 255.0, 68 / 255.0, 1.0)],
                [
                    'FP_coat_short_buttons',
                    VBase4(83 / 255.0, 81 / 255.0, 77 / 255.0, 1.0)],
                [
                    'FP_coat_short_pockets',
                    VBase4(134 / 255.0, 110 / 255.0, 80 / 255.0, 1.0)],
                [
                    'FP_coat_short_stripes',
                    VBase4(153 / 255.0, 131 / 255.0, 95 / 255.0, 1.0)],
                [
                    'FP_coat_short_bluegold',
                    VBase4(40 / 255.0, 45 / 255.0, 56 / 255.0, 1.0)],
                [
                    'FP_coat_short_blue_black_trim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_gold_black_trim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_grey_gold_buttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_white_gold_filagree',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_baroness',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_navy',
                    VBase4(148 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)]],
            [
                [
                    'PM_eitc',
                    VBase4(148 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)],
                [
                    'FP_coat_closed_china',
                    VBase4(148 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)]]],
        'PANT': [
            [
                [
                    'FP_pant_short_pants_patchwork',
                    VBase4(109 / 255.0, 119 / 255.0, 114 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_4buttonflap',
                    VBase4(88 / 255.0, 76 / 255.0, 60 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_frontties',
                    VBase4(54 / 255.0, 58 / 255.0, 58 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_largesidestripe',
                    VBase4(81 / 255.0, 65 / 255.0, 66 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_stitch',
                    VBase4(116 / 255.0, 110 / 255.0, 89 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_striped',
                    VBase4(151 / 255.0, 133 / 255.0, 106 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_red',
                    VBase4(90 / 255.0, 27 / 255.0, 27 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_blue_goldbuttons',
                    VBase4(22 / 255.0, 43 / 255.0, 58 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_brightred',
                    VBase4(92 / 255.0, 13 / 255.0, 12 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_brown',
                    VBase4(58 / 255.0, 53 / 255.0, 39 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_green_goldbuttons',
                    VBase4(48 / 255.0, 74 / 255.0, 32 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_greenstripes',
                    VBase4(23 / 255.0, 44 / 255.0, 43 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_purple',
                    VBase4(43 / 255.0, 29 / 255.0, 42 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_goldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_baroness',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_china',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_pant_shorts_patchwork',
                    VBase4(53 / 255.0, 44 / 255.0, 30 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_fronttie',
                    VBase4(69 / 255.0, 73 / 255.0, 77 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_lightcloth',
                    VBase4(110 / 255.0, 94 / 255.0, 82 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_sidebuttons',
                    VBase4(56 / 255.0, 59 / 255.0, 39 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_sideties',
                    VBase4(78 / 255.0, 57 / 255.0, 51 / 255.0, 1.0)],
                [
                    'zomb_pant_shorts_sidebuttons',
                    VBase4(144 / 255.0, 135 / 255.0, 111 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_green_sidebutton',
                    VBase4(73 / 255.0, 80 / 255.0, 45 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_blue_stripes',
                    VBase4(44 / 255.0, 59 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_brownsilver',
                    VBase4(71 / 255.0, 54 / 255.0, 43 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_pinkgold',
                    VBase4(96 / 255.0, 49 / 255.0, 53 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_purplegold',
                    VBase4(69 / 255.0, 55 / 255.0, 99 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_redblack',
                    VBase4(33 / 255.0, 37 / 255.0, 41 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_redgold',
                    VBase4(117 / 255.0, 20 / 255.0, 20 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_blackredstrips',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_brown_silverbutton',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_brownsilver_enhance',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_green_tealtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_pinkgoldtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_redsilk',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_mardiGras',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_pant_skirt_tan',
                    VBase4(176 / 255.0, 165 / 255.0, 128 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_patchwork',
                    VBase4(107 / 255.0, 103 / 255.0, 67 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_layered',
                    VBase4(110 / 255.0, 63 / 255.0, 51 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_leathertrim',
                    VBase4(151 / 255.0, 138 / 255.0, 99 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_slip',
                    VBase4(187 / 255.0, 179 / 255.0, 160 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_plain',
                    VBase4(115 / 255.0, 132 / 255.0, 137 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_print',
                    VBase4(100 / 255.0, 123 / 255.0, 110 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_red',
                    VBase4(94 / 255.0, 28 / 255.0, 26 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_green',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_lightblue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_pink',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_red_whitebelt',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_greenembroidery',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_greenpurple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_StPatricks',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_red_whitebelt_valentines',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_peacock',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_gypsy_dress_a',
                    VBase4(151 / 255.0, 85 / 255.0, 23 / 255.0, 1.0)],
                [
                    'FP_gypsy_dress_b',
                    VBase4(86 / 255.0, 43 / 255.0, 29 / 255.0, 1.0)]],
            [
                [
                    'FP_bartender_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)],
                [
                    'FP_shopkeeps_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)]],
            [
                [
                    'FP_navy',
                    VBase4(230 / 255.0, 230 / 255.0, 230 / 255.0, 1.0)]]],
        'BELT': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_belt_sash_goldbuckle',
                    VBase4(97 / 255.0, 90 / 255.0, 85 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_pattern',
                    VBase4(46 / 255.0, 48 / 255.0, 17 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_tassles',
                    VBase4(58 / 255.0, 42 / 255.0, 26 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_goldbuckle',
                    VBase4(97 / 255.0, 90 / 255.0, 85 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_black+FP_belt_buckle_square_dark',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_RivetsSkullBuckle+FP_belt_buckle_square',
                    VBase4(31 / 255.0, 23 / 255.0, 13 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_cloth+FP_belt_buckle_corners',
                    VBase4(35 / 255.0, 39 / 255.0, 4 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_studs+FP_belt_buckle_circles',
                    VBase4(41 / 255.0, 35 / 255.0, 19 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_ties+FP_belt_buckle_pattern',
                    VBase4(49 / 255.0, 33 / 255.0, 12 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_weave+FP_belt_buckle_weave',
                    VBase4(52 / 255.0, 43 / 255.0, 27 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_blue_belt',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_red_furtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_brown_silvertrim+FP_belt_buckle_square_brown_silvertrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_gold_design+FP_belt_buckle_square_gold_design',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_red_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_advanced_outfit+FP_belt_buckle_square_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_intermediate_outfit+FP_belt_buckle_square_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_mardiGras',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_assassin',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_bountyhunter',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_corsair',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_peacock',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_privateer+FP_belt_buckle_square_privateer',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_scourge+FP_belt_buckle_square_scourge',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_seaserpent+FP_belt_buckle_square_seaserpent',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_wildfire',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_zombie+FP_belt_buckle_square_zombie',
                    VBase4(255 / 255.0, 0 / 255.0, 0 / 255.0, 1.0)]]],
        'SHOE': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_shoe_short_boots_celticpattern',
                    VBase4(32 / 255.0, 28 / 255.0, 23 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_3buckle',
                    VBase4(33 / 255.0, 27 / 255.0, 11 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_plain',
                    VBase4(34 / 255.0, 25 / 255.0, 18 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_weave',
                    VBase4(34 / 255.0, 31 / 255.0, 20 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_black_torntop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_brown_sidebuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_brown_sidelaces',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_brown_stitching',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_roundbuckle',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_Xmas',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_valentines',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_mardiGras',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_diplomat',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_prince',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shoe_medium_boots_BuckleSkullSole',
                    VBase4(23 / 255.0, 14 / 255.0, 5 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_studs',
                    VBase4(23 / 255.0, 23 / 255.0, 20 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_ties',
                    VBase4(9 / 255.0, 8 / 255.0, 7 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_weavebuckle',
                    VBase4(18 / 255.0, 12 / 255.0, 1 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_black-topstitch',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_brown-sidestitch',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_orange',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_greenpurple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_baroness',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_privateer',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shoe_knee_high_boots_brown',
                    VBase4(20 / 255.0, 17 / 255.0, 14 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_smallchains',
                    VBase4(5 / 255.0, 5 / 255.0, 9 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_buckle',
                    VBase4(17 / 255.0, 15 / 255.0, 12 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_plain',
                    VBase4(47 / 255.0, 35 / 255.0, 14 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_ties',
                    VBase4(36 / 255.0, 24 / 255.0, 8 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_blue',
                    VBase4(30 / 255.0, 44 / 255.0, 56 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_burgundy',
                    VBase4(54 / 255.0, 16 / 255.0, 21 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_lightgreen',
                    VBase4(72 / 255.0, 82 / 255.0, 51 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_tan',
                    VBase4(87 / 255.0, 70 / 255.0, 37 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_goldbuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_StPatricks',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_assassin',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_peacock',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_scourge',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_wildfire',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_zombie',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shoe_tall_boots_celticstraps',
                    VBase4(17 / 255.0, 16 / 255.0, 11 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_1buckle',
                    VBase4(25 / 255.0, 22 / 255.0, 17 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_plain',
                    VBase4(60 / 255.0, 42 / 255.0, 16 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_weave',
                    VBase4(30 / 255.0, 17 / 255.0, 14 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_blue_stitches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_red_anklebelts',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_teal_stitches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_silverstraps',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_violet_stitches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_bountyhunter',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_china',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_corsair',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_seaserpent',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_navy',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)]]] } }
navy_coat_geoms = [
    3,
    4]
navy_pant_geoms = [
    4,
    5]
shopkeep_pant_geoms = [
    6]
quickConfirmSet = set()
for gender in textures.keys():
    if gender == 'MALE':
        genderName = 'm'
    elif gender == 'FEMALE':
        genderName = 'f'

    clothing = textures[gender]
    for clothingType in clothing.keys():
        models = clothing[clothingType]
        for i in xrange(len(models)):
            for j in xrange(len(models[i])):
                quickConfirmSet.add((genderName, clothingType, i, j))





def getRandomClothingColor(level, pick = True):
    possibleColors = [
        0]
    for levelKey in DYE_COLOR_LEVEL:
        if level >= levelKey:
            possibleColors += DYE_COLOR_LEVEL[levelKey]
            continue

    if random.choice([
        0,
        0,
        1]):
        return 0
    else:
        return random.choice(possibleColors)

TYPE_INDEX = 0

def getItemType(itemId):
    item = getItemById(itemId)
    if item:
        return item[TYPE_INDEX]
    else:
        return -1

ClothingTypeNames = {
    HAT: PLocalizer.Hat,
    SHIRT: PLocalizer.Shirt,
    VEST: PLocalizer.Vest,
    COAT: PLocalizer.Coat,
    PANT: PLocalizer.Pants,
    BELT: PLocalizer.Belt,
    SOCK: PLocalizer.Belt,
    SHOE: PLocalizer.Shoes }

def getItemTypeName(itemId):
    itemType = getItemType(itemId)
    return ClothingTypeNames.get(itemType, None)


def getClothingTypeName(typeId):
    return ClothingTypeNames.get(typeId, '')

BASIC_OUTFIT_PART_A = 0
BASIC_OUTFIT_PART_B = 1
BASIC_OUTFIT_PART_C = 2
BASIC_OUTFIT_PART_D = 3
BASIC_OUTFIT_PART_E = 4
INTERMEDIATE_OUTFIT_PART_A = 5
INTERMEDIATE_OUTFIT_PART_B = 6
INTERMEDIATE_OUTFIT_PART_C = 7
INTERMEDIATE_OUTFIT_PART_D = 8
INTERMEDIATE_OUTFIT_PART_E = 9
INTERMEDIATE_OUTFIT_PART_F = 10
ADVANCED_OUTFIT_PART_A = 11
ADVANCED_OUTFIT_PART_B = 12
ADVANCED_OUTFIT_PART_C = 13
ADVANCED_OUTFIT_PART_D = 14
ADVANCED_OUTFIT_PART_E = 15
ADVANCED_OUTFIT_PART_F = 16
ADVANCED_OUTFIT_PART_G = 17
VALENTINES_SHIRT = 18
POKER_BONUS_HAT = 19
questDrops = {
    BASIC_OUTFIT_PART_A: {
        'm': [
            ItemGlobals.RECRUIT_BANDANA,
            0],
        'f': [
            ItemGlobals.RECRUIT_BANDANA,
            0] },
    BASIC_OUTFIT_PART_B: {
        'm': [
            ItemGlobals.RECRUIT_LONG_SLEEVE,
            0],
        'f': [
            ItemGlobals.RECRUIT_TOP,
            0] },
    BASIC_OUTFIT_PART_C: {
        'm': [
            ItemGlobals.RECRUIT_TROUSERS,
            0],
        'f': [
            ItemGlobals.RECRUIT_CAPRIS,
            0] },
    BASIC_OUTFIT_PART_D: {
        'm': [
            ItemGlobals.RECRUIT_SASH,
            0],
        'f': [
            ItemGlobals.RECRUIT_SASH,
            0] },
    BASIC_OUTFIT_PART_E: {
        'm': [
            ItemGlobals.RECRUIT_BOOTS,
            0],
        'f': [
            ItemGlobals.RECRUIT_SHORT_BOOTS,
            0] },
    INTERMEDIATE_OUTFIT_PART_A: {
        'm': [
            ItemGlobals.TRAVELERS_OSTRICH_HAT,
            0],
        'f': [
            ItemGlobals.TRAVELERS_CAVALRY_HAT,
            0] },
    INTERMEDIATE_OUTFIT_PART_B: {
        'm': [
            ItemGlobals.TRAVELERS_PUFFY_SHIRT,
            0],
        'f': [
            ItemGlobals.TRAVELERS_TOP,
            0] },
    INTERMEDIATE_OUTFIT_PART_C: {
        'm': [
            ItemGlobals.TRAVELERS_VEST,
            0],
        'f': [
            ItemGlobals.TRAVELERS_LOOSE_VEST,
            0] },
    INTERMEDIATE_OUTFIT_PART_D: {
        'm': [
            ItemGlobals.TRAVELERS_TROUSERS,
            0],
        'f': [
            ItemGlobals.TRAVELERS_CAPRIS,
            0] },
    INTERMEDIATE_OUTFIT_PART_E: {
        'm': [
            ItemGlobals.SQUARE_TRAVELERS_BELT,
            0],
        'f': [
            ItemGlobals.TRAVELERS_BELT,
            0] },
    INTERMEDIATE_OUTFIT_PART_F: {
        'm': [
            ItemGlobals.TRAVELERS_BOOTS,
            0],
        'f': [
            ItemGlobals.TRAVELERS_TALL_BOOTS,
            0] },
    ADVANCED_OUTFIT_PART_A: {
        'm': [
            ItemGlobals.ADVENTURE_OSTRICH_HAT,
            0],
        'f': [
            ItemGlobals.ADVENTURE_CAVALRY_HAT,
            0] },
    ADVANCED_OUTFIT_PART_B: {
        'm': [
            ItemGlobals.ADVANCED_TANK,
            0],
        'f': [
            ItemGlobals.ADVENTURE_TOP,
            0] },
    ADVANCED_OUTFIT_PART_C: {
        'm': [
            ItemGlobals.OPEN_ADVENTURE_VEST,
            0],
        'f': [
            ItemGlobals.ADVENTURE_VEST,
            0] },
    ADVANCED_OUTFIT_PART_D: {
        'm': [
            ItemGlobals.ADVENTURE_LONG_COAT,
            0],
        'f': [
            ItemGlobals.ADVENTURE_RIDING_COAT,
            0] },
    ADVANCED_OUTFIT_PART_E: {
        'm': [
            ItemGlobals.ADVENTURE_BREECHES,
            0],
        'f': [
            ItemGlobals.ADVENTURE_CAPRIS,
            0] },
    ADVANCED_OUTFIT_PART_F: {
        'm': [
            ItemGlobals.SQUARE_ADVENTURE_BELT,
            0],
        'f': [
            ItemGlobals.ADVENTURE_BELT,
            0] },
    ADVANCED_OUTFIT_PART_G: {
        'm': [
            ItemGlobals.ADVENTURE_BOOTS,
            0],
        'f': [
            ItemGlobals.ADVENTURE_SHORT_BOOTS,
            0] },
    VALENTINES_SHIRT: {
        'm': [
            ItemGlobals.VALENTINES_SHIRT,
            0],
        'f': [
            ItemGlobals.VALENTINES_BLOUSE,
            0] },
    POKER_BONUS_HAT: {
        'm': [
            ItemGlobals.MAGENTA_OSTRICH_HAT,
            0],
        'f': [
            ItemGlobals.PURPLE_CAVALRY_HAT,
            0] } }
quest_items = [
    ItemGlobals.RECRUIT_BANDANA,
    ItemGlobals.RECRUIT_LONG_SLEEVE,
    ItemGlobals.RECRUIT_TOP,
    ItemGlobals.RECRUIT_TROUSERS,
    ItemGlobals.RECRUIT_CAPRIS,
    ItemGlobals.RECRUIT_SASH,
    ItemGlobals.RECRUIT_BOOTS,
    ItemGlobals.RECRUIT_SHORT_BOOTS,
    ItemGlobals.TRAVELERS_OSTRICH_HAT,
    ItemGlobals.TRAVELERS_CAVALRY_HAT,
    ItemGlobals.TRAVELERS_PUFFY_SHIRT,
    ItemGlobals.TRAVELERS_TOP,
    ItemGlobals.TRAVELERS_VEST,
    ItemGlobals.TRAVELERS_LOOSE_VEST,
    ItemGlobals.TRAVELERS_TROUSERS,
    ItemGlobals.TRAVELERS_CAPRIS,
    ItemGlobals.SQUARE_TRAVELERS_BELT,
    ItemGlobals.TRAVELERS_BELT,
    ItemGlobals.TRAVELERS_BOOTS,
    ItemGlobals.TRAVELERS_TALL_BOOTS,
    ItemGlobals.ADVENTURE_OSTRICH_HAT,
    ItemGlobals.ADVENTURE_CAVALRY_HAT,
    ItemGlobals.ADVANCED_TANK,
    ItemGlobals.ADVENTURE_TOP,
    ItemGlobals.OPEN_ADVENTURE_VEST,
    ItemGlobals.ADVENTURE_VEST,
    ItemGlobals.ADVENTURE_LONG_COAT,
    ItemGlobals.ADVENTURE_RIDING_COAT,
    ItemGlobals.ADVENTURE_BREECHES,
    ItemGlobals.ADVENTURE_CAPRIS,
    ItemGlobals.SQUARE_ADVENTURE_BELT,
    ItemGlobals.ADVENTURE_BELT,
    ItemGlobals.ADVENTURE_BOOTS,
    ItemGlobals.ADVENTURE_SHORT_BOOTS,
    ItemGlobals.VALENTINES_SHIRT,
    ItemGlobals.VALENTINES_BLOUSE,
    ItemGlobals.MAGENTA_OSTRICH_HAT,
    ItemGlobals.PURPLE_CAVALRY_HAT]

def subtypeFromId(gen, tpNum, stNum):
    section = CLOTHING_NAMES[tpNum][gen][stNum]
    return section


def texFromId(gen, tpNum, stNum, texNum):
    texture = textures[gen][CLOTHING_STRING[tpNum]][stNum][texNum][0]
    return texture


def getLastModel(gen, type):
    return len(textures[gen][type]) - 1


def getLastTexture(gen, type, model):
    return len(textures[gen][type][model]) - 1


def doesTextureExist(gen, type, modelNum, texNum):

    try:
        model = textures[gen][CLOTHING_STRING[type]][modelNum]
    except:
        return False

    if not model:
        return False

    try:
        texture = model[texNum]
    except:
        return False

    if not texture:
        return False

    return True


def isInMaP(id, gender, type, subT, tex):
    if subT in SELECTION_CHOICES['DEFAULT'][gender][CLOTHING_STRING[type]]:
        if tex in SELECTION_CHOICES['DEFAULT'][gender][CLOTHING_STRING[type]][subT]:
            return True
        else:
            return False
    else:
        return False


def isQuestDrop(id):
    if id in quest_items:
        return True
    else:
        return False


def printList():
    for gender in textures:
        for type in textures[gender]:
            for item in textures[gender][type]:
                for subtype in item:
                    outVal = [
                        int(subtype[1].getX() * 256),
                        int(subtype[1].getY() * 256),
                        int(subtype[1].getZ() * 256)]
                    print str(subtype[0]), str(outVal)


def printList2():
    for gender in textures:
        for type in textures[gender]:
            itemNum = 0
            for item in textures[gender][type]:
                subtypeNum = 0
                for subtype in item:
                    map = False
                    if itemNum in SELECTION_CHOICES['DEFAULT'][gender][type]:
                        if subtypeNum in SELECTION_CHOICES['DEFAULT'][gender][type][itemNum]:
                            map = True

                    print str(subtype[0]) + ';', map
                    subtypeNum = subtypeNum + 1

                itemNum = itemNum + 1
