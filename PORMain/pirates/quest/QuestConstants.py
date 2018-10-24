from panda3d.core import Light
from pirates.ship.ShipGlobals import *
from pirates.world.LocationConstants import LocationIds, getLocationList

CANCEL_QUEST = -1
MAXIMUM_MERC_WORK = 16

class QuestActions:
    Decline = 0
    Accept = 1
    Bribe = 2


class QuestItemNotification:
    AlreadyFound = 1
    ProgressMadeGoalMet = 2
    ProgressMadeGoalUnmet = 3
    ValidAttempt = 4
    InvalidAttempt = 5


class QuestItems:
    Key = 0
    SeaChart = 1
    Earring = 2
    RumBarrel = 3
    CrabClaw = 4
    CoinBag = 5
    TattooPattern = 6
    CopperRod = 7
    Blood = 8
    Flag = 9
    List = 10
    ArrestWarrant = 11
    Handkerchief = 12
    BatGuano = 13
    Remedy = 14
    PersonalEffects = 15
    EngravedPearl = 16
    SeveredArm = 17
    GatorSaliva = 18
    Venom = 19
    CursedWood = 20
    Map = 21
    Necklace = 22
    TinShipment = 23
    SandShipment = 24
    GlassRing = 25
    WoodenPlates = 26
    Chicken = 27
    Pig = 28
    Egg = 29
    Tooth = 30
    WaspWings = 31
    GatorScales = 32
    Poison = 33
    Mud = 34
    Grog = 35
    Doll = 36
    Dinghy = 37
    ReleaseOrders = 38
    HoneyBarrel = 39
    Dress = 40
    Dice = 41
    WaspEggs = 42
    Bile = 43
    RumBottle = 44
    Bracelet = 45
    Needle = 46
    KrakenEye = 47
    Powder = 48
    CrocWater = 49
    Entrails = 50
    Splinter = 51
    Dust = 52
    Earth = 53
    Lichen = 54
    Water = 55
    ScorpionEgg = 56
    BloodyTreasure = 57
    Nightshade = 58
    Whisker = 59
    Jar = 60
    Paper = 61
    Bone = 62
    BoneShavings = 63
    Chest = 64
    HookArm = 65
    Diamond = 66
    CigarBox = 67
    GoldChain = 68
    Cargo = 69
    Ladle = 70
    Sugar = 71
    Bottle = 72
    Molasses = 73
    Vanilla = 74
    BoneDust = 75
    SwampGas = 76
    Stinger = 77
    Bladder = 78
    Pint = 79
    Cinnamon = 80
    Coconut = 81
    Feather = 82
    Honey = 83
    Barnacles = 84
    Hairball = 85
    Flea = 86
    Drink = 87
    Schedule = 88
    Hair = 89
    Honeysuckle = 90
    Sap = 91
    Tear = 92
    Perfume = 93
    Oil = 94
    Rum = 95
    Orders = 96
    Salve = 97
    Wax = 98
    Meat = 99
    Plank = 100
    Nail = 101
    Pitch = 102
    Saw = 103
    Ship = 104
    Beam = 105
    Bolt = 106
    Sailcloth = 107
    Rope = 108
    Cannon = 109
    Figure = 110
    Parrot = 111
    Document = 112
    Eye = 113
    Painting = 114
    Treasure = 115
    Straw = 116
    Silk = 117
    Wire = 118
    Bag = 119
    Dirt = 120
    Ring = 121
    Medal = 122
    Reagent = 123
    ChessPiece = 124
    Figurine = 125
    Steel = 126
    Silver = 127
    Tongs = 128
    Coal = 129
    Message = 130
    Knife = 131
    Grenade = 132
    Branch = 133
    ShrunkenHead = 134
    Saltpeter = 135
    Charcoal = 136
    Sulfur = 137
    Fuse = 138
    Flint = 139
    Casing = 140
    Tar = 141
    TeleportTotem = 142
    BatWings = 143
    AlligatorTooth = 144
    EssenceOfWasp = 145
    TortuganArtifact = 146
    CottonYard = 147
    IronBar = 148
    AlligatorTail = 149
    CrabShell = 150
    BatHair = 151
    ScorpionBlood = 152
    ScorpionVenom = 153
    WhiskeyBarrel = 154
    SetOfBarGlasses = 155
    CoalBag = 156
    SmithingTools = 157
    PeterAttackerName = 158
    FlyTrapLeaf = 159
    FlyTrapRoot = 160
    NavyCoat = 161
    FirstMedal = 162
    EyeOfNabai = 163
    DollComponentHead = 164
    DollComponentTorso = 165
    DollComponentArmL = 166
    DollComponentArmR = 167
    DollComponentLegL = 168
    DollComponentLegR = 169
    NavyMuskets = 170
    NavyPants = 171
    SargeantsBadge = 172
    PrisonKey = 173
    FortTreasureDocument = 174
    SewingNeedle = 175
    GuardSchedule = 176
    NavySchedule = 177
    LatrineWater = 178
    MoonlitWater = 179
    BattleSaltWater = 180
    DicePair = 181
    WaterCanteen = 182
    Rubies = 183
    Amethyst = 184
    Sapphire = 185
    FineInk = 186
    Deed = 187
    EITCCoat = 188
    EITCPants = 189
    ShopApplication = 190
    Hide = 191
    Contract = 192
    BloodSample = 193
    Bandages = 194
    MedicalTools = 195
    Diary = 196
    ShipLog = 197
    FamilyHeirlooms = 198
    Gun = 199
    GunOrder = 200
    AntiquePistol = 201
    ShipPlans = 202
    BackgroundCheck = 203
    FineSteelBar = 204
    LeatherStraps = 205
    BladeSharpener = 206
    PirateLorePage = 207
    PirateLoreChest = 208
    PirateLoreBook = 209
    EITCManual = 210
    UnfinishedPirateLoreBook = 211
    GatorEye = 212
    Wasp = 213
    ScorpionEye = 214
    BatEye = 215
    CloudyBlueOrb = 216
    SkeletonRib = 217
    Badge = 218
    WritOfAuthority = 219
    GatorTooth = 220
    BatClaw = 221
    SkeletonBone = 222
    SunkenShipMast = 223
    BattleEarth = 224
    RelicPiece = 225
    CaptTeague = 226
    FlyTrapThread = 227
    RareFeather = 228
    EITCManifest = 229
    BinghamsDiary = 230
    BoltOfCloth = 231
    FineScissors = 232
    SilkThread = 233
    ScarletsPearl = 234
    LetterFromScarlet = 235
    BeltBuckle = 236
    FineShoeDesign = 237
    ScorpionShell = 238
    KrakenCloth = 239
    CursedButtons = 240
    CursedBark = 241
    CursedCloth = 242
    CursedThread = 243
    CursedNeedle = 244
    VoodooArtifact = 245
    RottenMeat = 246
    Compass = 247
    LockgrimsLetter = 248
    Tentacle = 249
    UrchinfistEye = 250
    CursedChest = 251
    FineRum = 252
    LuckyDeck = 253
    NavyShoeString = 254
    NavyAnchor = 255
    EITCParchment = 256
    EmptyFlask = 257
    Sail = 258
    ShipWheel = 259
    NavyFabric = 260
    CursedSailCloth = 261
    SpanishArmor = 262
    SpanishPistolComponent = 263
    GunStock = 264
    BoneHandle = 265
    LockOfHair = 266
    WoodenStatuette = 267
    GunPowder = 268
    Spar = 269
    StolenDaggers = 270
    Gems = 271
    NavySteel = 272
    GoldHandleRapier = 273
    GatorSkin = 274
    Bat = 275
    NavyFlag = 276
    BrassButton = 277
    Crab = 278
    Skull = 279
    Ore = 280
    Cure = 281
    LiverVial = 282
    HairPatch = 283
    GourdShaker = 284
    BileSack = 285
    JunesItem = 286
    LoveLetter = 287
    GallBladder = 288
    GunpowderPouch = 289
    EmptyRumBottle = 290
    SaltedRib = 291
    PearlSack = 292
    VenomSack = 293
    EyeSocket = 294
    Toenail = 295
    GrogBottle = 296
    LightRumBottle = 297
    DarkRumBottle = 298
    FiveYearRum = 299
    TenYearRum = 300
    SkeletonRum = 301
    NavyRum = 302
    EITCRum = 303
    EmptyBottleBox = 304
    WaterBarrel = 305
    MolassesCup = 306
    Charm = 307
    MemoryCure = 308
    ClothPiece = 309
    CaneSugarBarrel = 310
    NutmegCrate = 311
    CursedDarkSugar = 312
    DreadBitters = 313
    CursedBarnacles = 314
    Cutler100 = 315
    SingaporeanRum = 316
    TwentyFiveYearRum = 317
    FishRumBottle = 318
    VoodooRumBottle = 319
    BoneRumBottle = 320
    GatorStomach = 321
    BrassInstrument = 322
    ForgivenessLetter = 323
    Kneecap = 324
    PinkyRing = 325
    Money = 326
    Dagger = 327
    Sword = 328
    Hay = 329
    MedicineKit = 330
    HerbSack = 331
    Bowsprit = 332
    Steelband = 333
    Rudder = 334
    NailBox = 335
    BoltPack = 336
    WaterFlask = 337
    EnlistmentOrder = 338
    DefensePlans = 339
    VoodooRelic = 340
    SecretRecord = 341
    Intelligence = 342
    ExcavationRecord = 343
    LostMap = 344
    CodedOrder = 345
    Journal = 346
    Idol = 347
    DowsingRodPart = 348
    TwistedRoot = 349
    GiantBladder = 350
    FatChicken = 351
    RevivingPotion = 352
    TotemPiece = 353
    CursedSail = 354
    TornSail = 355
    UndeadSail = 356
    TBD = 400

QuestHistoryLen = 300

class PropIds:
    TYPE_BARREL = 0
    TYPE_CRATE = 1
    TYPE_DESK = 2
    TYPE_SHELF = 3
    TYPE_CLOCK = 4
    TYPE_HAYSTACK = 5
    TYPE_WELL = 6
    TYPE_GRAVE = 7
    PR_CRATE_1 = '1175737088.0dxschafe'
    PR_CRATE_2 = '1175737088.0dxschafe0'
    PR_CRATE_3 = '1175737216.0dxschafe'
    PR_CRATE_4 = '1175737216.0dxschafe0'
    PR_CRATE_5 = '1175737216.0dxschafe1'
    PR_CRATE_6 = '1175737216.0dxschafe2'
    PR_CRATE_7 = '1175737216.0dxschafe3'
    PR_CRATE_8 = '1175737216.0dxschafe4'
    PR_CRATE_9 = '1175737216.0dxschafe5'
    PR_CRATE_10 = '1175737344.0dxschafe'
    PR_CRATE_11 = '1175737344.0dxschafe0'
    PR_CRATE_12 = '1175737344.0dxschafe1'
    PR_CRATE_13 = '1175737344.0dxschafe2'
    PR_CRATE_14 = '1175737344.0dxschafe3'
    PR_CRATE_15 = '1175737472.0dxschafe'
    PR_CRATES = 'PortRoyalCrates'
    PR_BARREL_1 = '1177359488.0dxschafe1'
    PR_BARREL_2 = '1177358848.0dxschafe'
    PR_BARREL_3 = '1177358976.0dxschafe'
    PR_BARREL_4 = '1177358976.0dxschafe'
    PR_BARREL_5 = '1177359104.0dxschafe0'
    PR_BARREL_6 = '1177359104.0dxschafe1'
    PR_BARREL_7 = '1177359104.0dxschafe5'
    PR_BARREL_8 = '1177359232.0dxschafe2'
    PR_BARREL_9 = '1177359232.0dxschafe2'
    PR_BARREL_10 = '1177359488.0dxschafe0'
    PR_BARREL_11 = '1177359616.0dxschafe0'
    PR_BARRELS = 'PortRoyalBarrels'
    FC_DESK = '1170742144.0mike'
    FC_SHELF = '1175826048.0dxschafe0'
    FC_CLOCK = '1175826048.0dxschafe1'
    FC_BARREL_EASY_1 = '1177104768.0dxschafe'
    FC_BARREL_EASY_2 = '1177104896.0dxschafe0'
    FC_BARREL_EASY_3 = '1176414336.0dxschafe'
    FC_BARREL_EASY_4 = '1177104768.0dxschafe0'
    FC_EASY_BARRELS = 'FortCharlesEasyBarrels'
    FC_BARREL_MED_1 = '1177108352.0dxschafe'
    FC_BARREL_MED_2 = '1176414976.0dxschafe'
    FC_BARREL_MED_3 = '1177104896.0dxschafe'
    FC_BARREL_MED_4 = '1175826048.0dxschafe'
    FC_MED_BARRELS = 'FortCharlesMedBarrels'
    FC_BARRELS = 'FortCharlesBarrels'
    FC_CRATE_EASY_1 = '1177108096.0dxschafe'
    FC_CRATE_EASY_2 = '1177366400.0dxschafe'
    FC_EASY_CRATES = 'FortCharlesEasyCrates'
    FC_CRATE_MED_1 = '1176414464.0dxschafe'
    FC_CRATE_MED_2 = '1176414336.0dxschafe0'
    FC_CRATE_MED_3 = '1176414976.0dxschafe0'
    FC_CRATE_MED_4 = '1177352320.0dxschafe'
    FC_CRATE_MED_5 = '1177108224.0dxschafe'
    FC_MED_CRATES = 'FortCharlesMedCrates'
    FC_CRATES = 'FortCharlesCrates'
    FC_BARREL_1 = '1231543440.67WDIG'
    FC_BARREL_2 = '1231543631.91WDIG'
    FC_BARREL_3 = '1231543796.28WDIG'
    FC_BARREL_4 = '1231543992.3WDIG'
    FC_CRATE_1 = '1231543714.44WDIG'
    RC_BARREL_1 = '1249580544.0jloehrle'
    RC_BARREL_2 = '1249668352.0jloehrle'
    RC_BARREL_3 = '1249668480.0jloehrle0'
    RC_BARREL_4 = '1249668864.0jloehrle'
    RC_BARREL_5 = '1249668992.0jloehrle0'
    RC_BARREL_6 = '1249668992.0jloehrle2'
    RC_BARREL_7 = '1249675215.17piwanow'
    RC_BARREL_8 = '1249675321.95piwanow'
    RC_BARREL_9 = '1249675573.39piwanow'
    RC_BARREL_10 = '1249675681.75piwanow'
    RC_BARRELS = 'RoyalCavernBarrels'
    BOWDASH_CABINET = '1173148032.0mike'
    T_CRATE_1 = '1173148288.0mike'
    T_CRATE_2 = '1173148416.0mike'
    T_CRATE_3 = '1173148416.0mike0'
    T_ANY_CRATE = 'TAnyCrate'
    T_G_BARREL_1 = '1177008640.0dxschafe2'
    T_G_BARREL_2 = '1245869169.58piwanow'
    T_G_BARREL_3 = '1245869277.98piwanow'
    T_G_BARRELS = 'TortugaGraveyardBarrels'
    T_EITC_DESK = '1186512896.0dxschafe'
    T_OUTPOST_DESK = '1187057664.0dxschafe'
    T_BOATSWAIN_DESK = '1175037824.0dxschafe'
    FD_SHELF = '1236645308.84piwanow'
    FD_CABINET = '1236643835.85piwanow'
    FD_DESK = '1236642958.51piwanow'
    FD_FURNITURE = 'FortDundeeFurniture'
    FD_BARREL_EASY_1 = '1236650303.49piwanow'
    FD_BARREL_EASY_2 = '1236642527.45piwanow'
    FD_BARREL_EASY_3 = '1236653469.65piwanow'
    FD_BARREL_EASY_4 = '1236641682.26piwanow'
    FD_BARREL_EASY_5 = '1236653570.03piwanow'
    FD_BARREL_EASY_6 = '1236654182.74piwanow'
    FD_EASY_BARRELS = 'FortDundeeEasyBarrels'
    FD_BARREL_MED_1 = '1236654427.37piwanow'
    FD_BARREL_MED_2 = '1236653864.7piwanow'
    FD_BARREL_MED_3 = '1236649530.23piwanow'
    FD_BARREL_MED_4 = '1236653217.4piwanow'
    FD_MED_BARRELS = 'FortDundeeMedBarrels'
    FD_BARRELS = 'FortDundeeBarrels'
    FD_CRATE_EASY_1 = '1236642394.7piwanow'
    FD_EASY_CRATES = 'FortDundeeEasyCrates'
    FD_CRATE_MED_1 = '1236654654.51piwanow'
    FD_CRATE_MED_2 = '1236653955.26piwanow'
    FD_CRATE_MED_3 = '1236649655.31piwanow'
    FD_CRATE_MED_4 = '1236653759.28piwanow'
    FD_CRATE_MED_5 = '1236653329.32piwanow'
    FD_MED_CRATES = 'FortDundeeMedCrates'
    FD_CRATES = 'FortDundeeCrates'
    FD_ALL = 'AllFortDundeeCratesBarrels'
    DF_BQ_BARREL_1 = '1249592320.0jloehrle'
    DF_BQ_BARREL_2 = '1249599616.0jloehrle'
    DF_BQ_BARREL_3 = '1249667712.0jloehrle0'
    DF_BQ_BARREL_4 = '1249667712.0jloehrle1'
    DF_BQ_BARREL_5 = '1249667712.0jloehrle2'
    DF_BQ_BARREL_6 = '1249667840.0jloehrle0'
    DF_BQ_BARREL_7 = '1249667968.0jloehrle'
    DF_BQ_BARREL_8 = '1249668096.0jloehrle'
    DF_BQ_BARREL_9 = '1249670439.17piwanow'
    DF_BQ_BARRELS = 'AllBeckettesQuarryBarrels'
    DF_BQ_CRATE_1 = '1249592320.0jloehrle0'
    DF_BQ_CRATE_2 = '1249670524.41piwanow'
    DF_BQ_CRATE_3 = '1249672839.67piwanow'
    DF_BQ_CRATE_4 = '1249672942.16piwanow'
    DF_BQ_CRATE_5 = '1249673025.53piwanow'
    DF_BQ_CRATE_6 = '1249673094.2piwanow'
    DF_BQ_CRATE_7 = '1249673305.92piwanow'
    DF_BQ_CRATE_8 = '1249673649.38piwanow'
    DF_BQ_CRATES = 'AllBeckettesQuarryCrates'
    KH_CRATE_1 = '1177716480.0dxschafe6'
    KH_CRATE_2 = '1177717248.0dxschafe2'
    KH_CRATE_3 = '1177716480.0dxschafe10'
    KH_CRATE_4 = '1177715584.0dxschafe5'
    KH_CRATE_5 = '1177716480.0dxschafe5'
    KH_CRATE_6 = '1177717504.0dxschafe1'
    KH_CRATE_7 = '1177716480.0dxschafe8'
    KH_CRATE_8 = '1177717248.0dxschafe4'
    KH_CRATE_9 = '1177970176.0dxschafe'
    KH_CRATE_10 = '1177716480.0dxschafe11'
    KH_CRATE_11 = '1177716480.0dxschafe2'
    KH_CRATE_12 = '1177716864.0dxschafe'
    KH_CRATE_13 = '1177716480.0dxschafe'
    KH_CRATE_14 = '1177716480.0dxschafe3'
    KH_CRATE_15 = '1177716480.0dxschafe9'
    KH_CRATE_16 = '1177715584.0dxschafe3'
    KH_CRATE_17 = '1177716864.0dxschafe2'
    KH_CRATE_18 = '1177717248.0dxschafe1'
    KH_CRATE_19 = '1177717248.0dxschafe3'
    KH_CRATE_20 = '1177716480.0dxschafe1'
    KH_CRATE_21 = '1177717120.0dxschafe0'
    KH_CRATE_22 = '1177716480.0dxschafe4'
    KH_CRATE_23 = '1177715584.0dxschafe9'
    KH_CRATE_24 = '1177716480.0dxschafe0'
    KH_CRATE_25 = '1177716864.0dxschafe0'
    KH_CRATE_26 = '1176849536.0dxschafe'
    KH_CRATE_27 = '1177717248.0dxschafe'
    KH_CRATE_28 = '1177717248.0dxschafe0'
    KH_CRATE_29 = '1177716992.0dxschafe1'
    KH_CRATE_30 = '1177717120.0dxschafe'
    KH_CRATE_31 = '1177717504.0dxschafe0'
    KH_CRATE_32 = '1177715584.0dxschafe7'
    KH_CRATE_33 = '1177716480.0dxschafe7'
    KH_CRATE_34 = '1177716864.0dxschafe1'
    KH_CRATE_35 = '1177715584.0dxschafe8'
    KH_CRATE_36 = '1177715584.0dxschafe2'
    KH_CRATE_37 = '1177716992.0dxschafe0'
    KH_CRATE_38 = '1177716992.0dxschafe'
    KH_CRATES = 'KingsheadCrates'
    KH_BARREL_1 = '1177717248.0dxschafe6'
    KH_BARREL_2 = '1177715584.0dxschafe'
    KH_BARREL_3 = '1177715328.0dxschafe9'
    KH_BARREL_4 = '1177715584.0dxschafe11'
    KH_BARREL_5 = '1177715712.0dxschafe4'
    KH_BARREL_6 = '1177715712.0dxschafe1'
    KH_BARREL_7 = '1177715584.0dxschafe1'
    KH_BARREL_8 = '1177715712.0dxschafe3'
    KH_BARREL_9 = '1177715584.0dxschafe6'
    KH_BARREL_10 = '1177717248.0dxschafe8'
    KH_BARREL_11 = '1177715584.0dxschafe10'
    KH_BARREL_12 = '1177714048.0dxschafe'
    KH_BARREL_13 = '1177715328.0dxschafe6'
    KH_BARREL_14 = '1177717248.0dxschafe12'
    KH_BARREL_15 = '1177715200.0dxschafe'
    KH_BARREL_16 = '1177717248.0dxschafe5'
    KH_BARREL_17 = '1177717248.0dxschafe10'
    KH_BARREL_18 = '1177713792.0dxschafe0'
    KH_BARREL_19 = '1177717248.0dxschafe14'
    KH_BARREL_20 = '1177717504.0dxschafe'
    KH_BARREL_21 = '1177715584.0dxschafe4'
    KH_BARREL_22 = '1177715328.0dxschafe5'
    KH_BARREL_23 = '1177715328.0dxschafe2'
    KH_BARREL_24 = '1177717248.0dxschafe9'
    KH_BARREL_25 = '1177715328.0dxschafe8'
    KH_BARREL_26 = '1177715328.0dxschafe0'
    KH_BARREL_27 = '1177717248.0dxschafe11'
    KH_BARREL_28 = '1177713792.0dxschafe'
    KH_BARREL_29 = '1177715712.0dxschafe0'
    KH_BARREL_30 = '1177717248.0dxschafe7'
    KH_BARREL_31 = '1177715328.0dxschafe7'
    KH_BARREL_32 = '1177715712.0dxschafe'
    KH_BARREL_33 = '1177715584.0dxschafe0'
    KH_BARREL_34 = '1177715328.0dxschafe1'
    KH_BARREL_35 = '1177715328.0dxschafe3'
    KH_BARREL_36 = '1177713664.0dxschafe0'
    KH_BARREL_37 = '1177713664.0dxschafe2'
    KH_BARREL_38 = '1177717248.0dxschafe13'
    KH_BARREL_39 = '1177715712.0dxschafe2'
    KH_BARREL_40 = '1177715328.0dxschafe4'
    KH_BARREL_41 = '1177713664.0dxschafe'
    KH_BARREL_42 = '1177713664.0dxschafe1'
    KH_BARRELS = 'KingsheadBarrels'
    KH_HAYSTACK_1 = '1176845824.0dxschafe3'
    KH_HAYSTACK_2 = '1176845696.0dxschafe'
    KH_HAYSTACK_3 = '1176845568.0dxschafe'
    KH_HAYSTACKS = 'KingsheadHaystacks'
    KH_WELL_1 = '1176846464.0dxschafe'
    KH_WELL_2 = '1176849152.0dxschafe'
    KH_WELLS = 'KingsheadWells'
    RR_CELLAR_CRATE = '1190669056.0dxschafe1'
    RR_CELLAR_BARREL = '1190669056.0dxschafe'
    RC_GRAVE_1 = '1274813775.1caoconno'
    RC_GRAVE_2 = '1274825998.85caoconno'
    RC_GRAVE_3 = '1274822529.65caoconno'
    RC_GRAVE_4 = '1274808286.12caoconno'
    RC_GRAVES = 'RavensCoveGraves'
    RC_CHEST_1 = '1277252070.81robrusso'
    RC_MINE_SHAFT_1 = '1274137485.25akelts'
    RC_CRATE_1 = '1283970884.42piwanow'
    RC_CRATE_2 = '1283971285.74piwanow'
    RC_CRATE_3 = '1283971449.9piwanow'
    RC_CRATE_4 = '1283971622.15piwanow'
    RC_CRATE_5 = '1283971763.28piwanow'
    RC_CRATES = 'RavensCoveCrates'
    UNDEAD_POKER_TABLE = '1276702867.98caoconno'
    NAVY_BARRELS = 'NavyBarrels'
    NAVY_CRATES = 'NavyCrates'
    VEGAS_GOV_DESK = '1169451658.54Shochet'
    ANY_BARREL = 'AnyBarrel'
    ANY_CRATE = 'AnyCrate'
    ANY_DESK = 'AnyDesk'
    ANY_SHELF = 'AnyShelf'
    ANY_CABINET = 'AnyCabinet'
    ANY_CLOCK = 'AnyClock'
    ANY_HAYSTACK = 'AnyHaystack'
    ANY_WELL = 'AnyWell'
    ANY_GRAVE = 'AnyGrave'
    ANY_CHEST = 'AnyChest'
    ANY_MINE_SHAFT = 'AnyMineShaft'
    WATER_GRAVE = 'waterGrave'
    SOUTH_GRAVE = 'southGrave'
    ANY_PROP = 'AnyProp'
    PropDefs = {
        VEGAS_GOV_DESK: (VEGAS_GOV_DESK,),
        PR_CRATES: (PR_CRATE_1, PR_CRATE_2, PR_CRATE_3, PR_CRATE_4, PR_CRATE_5, PR_CRATE_6, PR_CRATE_7, PR_CRATE_8, PR_CRATE_9, PR_CRATE_10, PR_CRATE_11, PR_CRATE_12, PR_CRATE_13, PR_CRATE_14, PR_CRATE_15),
        PR_BARRELS: (PR_BARREL_1, PR_BARREL_2, PR_BARREL_3, PR_BARREL_4, PR_BARREL_5, PR_BARREL_6, PR_BARREL_7, PR_BARREL_8, PR_BARREL_9, PR_BARREL_10, PR_BARREL_11),
        FC_DESK: (FC_DESK,),
        FC_SHELF: (FC_SHELF,),
        FC_CLOCK: (FC_CLOCK,),
        FC_EASY_BARRELS: (FC_BARREL_EASY_1, FC_BARREL_EASY_2, FC_BARREL_EASY_3, FC_BARREL_EASY_4),
        FC_MED_BARRELS: (FC_BARREL_MED_1, FC_BARREL_MED_2, FC_BARREL_MED_3, FC_BARREL_MED_4),
        FC_BARRELS: (FC_BARREL_EASY_1, FC_BARREL_EASY_2, FC_BARREL_EASY_3, FC_BARREL_EASY_4, FC_BARREL_MED_1, FC_BARREL_MED_2, FC_BARREL_MED_3, FC_BARREL_MED_4, FC_BARREL_1, FC_BARREL_2, FC_BARREL_3, FC_BARREL_4),
        FC_EASY_CRATES: (FC_CRATE_EASY_1, FC_CRATE_EASY_2),
        FC_MED_CRATES: (FC_CRATE_MED_1, FC_CRATE_MED_2, FC_CRATE_MED_3, FC_CRATE_MED_4, FC_CRATE_MED_5),
        FC_CRATES: (FC_CRATE_EASY_1, FC_CRATE_EASY_2, FC_CRATE_MED_1, FC_CRATE_MED_2, FC_CRATE_MED_3, FC_CRATE_MED_4, FC_CRATE_MED_5, FC_CRATE_1),
        RC_BARRELS: (RC_BARREL_1, RC_BARREL_2, RC_BARREL_3, RC_BARREL_4, RC_BARREL_5, RC_BARREL_6, RC_BARREL_7, RC_BARREL_8, RC_BARREL_9, RC_BARREL_10),
        BOWDASH_CABINET: (BOWDASH_CABINET,),
        T_ANY_CRATE: (T_CRATE_1, T_CRATE_2, T_CRATE_3),
        T_G_BARRELS: (T_G_BARREL_1, T_G_BARREL_2, T_G_BARREL_3),
        T_EITC_DESK: (T_EITC_DESK,),
        T_OUTPOST_DESK: (T_OUTPOST_DESK,),
        FD_SHELF: (FD_SHELF,),
        FD_CABINET: (FD_CABINET,),
        FD_DESK: (FD_DESK,),
        FD_FURNITURE: (FD_SHELF, FD_CABINET, FD_DESK),
        FD_EASY_BARRELS: (FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3, FD_BARREL_EASY_4, FD_BARREL_EASY_5, FD_BARREL_EASY_6),
        FD_MED_BARRELS: (FD_BARREL_MED_1, FD_BARREL_MED_2, FD_BARREL_MED_3, FD_BARREL_MED_4),
        FD_BARRELS: (FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3, FD_BARREL_EASY_4, FD_BARREL_EASY_5, FD_BARREL_EASY_6, FD_BARREL_MED_1, FD_BARREL_MED_2, FD_BARREL_MED_3, FD_BARREL_MED_4),
        FD_EASY_CRATES: (FD_CRATE_EASY_1,),
        FD_MED_CRATES: (FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3, FD_CRATE_MED_4, FD_CRATE_MED_5),
        FD_CRATES: (FD_CRATE_EASY_1, FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3, FD_CRATE_MED_4, FD_CRATE_MED_5),
        FD_ALL: (FD_CRATE_EASY_1, FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3, FD_CRATE_MED_4, FD_CRATE_MED_5, FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3, FD_BARREL_EASY_4, FD_BARREL_EASY_5, FD_BARREL_EASY_6, FD_BARREL_MED_1, FD_BARREL_MED_2, FD_BARREL_MED_3, FD_BARREL_MED_4, FD_SHELF, FD_CABINET, FD_DESK),
        DF_BQ_BARRELS: (DF_BQ_BARREL_1, DF_BQ_BARREL_2, DF_BQ_BARREL_3, DF_BQ_BARREL_4, DF_BQ_BARREL_5, DF_BQ_BARREL_6, DF_BQ_BARREL_7, DF_BQ_BARREL_8, DF_BQ_BARREL_9),
        DF_BQ_CRATES: (DF_BQ_CRATE_1, DF_BQ_CRATE_2, DF_BQ_CRATE_3, DF_BQ_CRATE_4, DF_BQ_CRATE_5, DF_BQ_CRATE_6, DF_BQ_CRATE_7, DF_BQ_CRATE_8),
        KH_CRATES: (KH_CRATE_1, KH_CRATE_2, KH_CRATE_3, KH_CRATE_4, KH_CRATE_5, KH_CRATE_6, KH_CRATE_7, KH_CRATE_8, KH_CRATE_9, KH_CRATE_10, KH_CRATE_11, KH_CRATE_12, KH_CRATE_13, KH_CRATE_14, KH_CRATE_15, KH_CRATE_16, KH_CRATE_17, KH_CRATE_18, KH_CRATE_19, KH_CRATE_20, KH_CRATE_21, KH_CRATE_22, KH_CRATE_23, KH_CRATE_24, KH_CRATE_25, KH_CRATE_26, KH_CRATE_27, KH_CRATE_28, KH_CRATE_29, KH_CRATE_30, KH_CRATE_31, KH_CRATE_32, KH_CRATE_33, KH_CRATE_34, KH_CRATE_35, KH_CRATE_36, KH_CRATE_37, KH_CRATE_38),
        KH_BARRELS: (KH_BARREL_1, KH_BARREL_2, KH_BARREL_3, KH_BARREL_4, KH_BARREL_5, KH_BARREL_6, KH_BARREL_7, KH_BARREL_8, KH_BARREL_9, KH_BARREL_10, KH_BARREL_11, KH_BARREL_12, KH_BARREL_13, KH_BARREL_14, KH_BARREL_15, KH_BARREL_16, KH_BARREL_17, KH_BARREL_18, KH_BARREL_19, KH_BARREL_20, KH_BARREL_21, KH_BARREL_22, KH_BARREL_23, KH_BARREL_24, KH_BARREL_25, KH_BARREL_26, KH_BARREL_27, KH_BARREL_28, KH_BARREL_29, KH_BARREL_30, KH_BARREL_31, KH_BARREL_32, KH_BARREL_33, KH_BARREL_34, KH_BARREL_35, KH_BARREL_36, KH_BARREL_37, KH_BARREL_38, KH_BARREL_39, KH_BARREL_40, KH_BARREL_41, KH_BARREL_42),
        KH_HAYSTACKS: (KH_HAYSTACK_1, KH_HAYSTACK_2, KH_HAYSTACK_3),
        KH_WELLS: (KH_WELL_1, KH_WELL_2),
        RC_GRAVES: (RC_GRAVE_1, RC_GRAVE_2, RC_GRAVE_3, RC_GRAVE_4),
        RC_CRATES: (RC_CRATE_1, RC_CRATE_2, RC_CRATE_3, RC_CRATE_4, RC_CRATE_5),
        NAVY_BARRELS: (FC_BARREL_EASY_1, FC_BARREL_EASY_2, FC_BARREL_EASY_3, FC_BARREL_EASY_4, FC_BARREL_MED_1, FC_BARREL_MED_2, FC_BARREL_MED_3, FC_BARREL_MED_4, FC_BARREL_1, FC_BARREL_2, FC_BARREL_3, FC_BARREL_4, FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3, FD_BARREL_EASY_4, FD_BARREL_EASY_5, FD_BARREL_EASY_6, FD_BARREL_MED_1, FD_BARREL_MED_2, FD_BARREL_MED_3, FD_BARREL_MED_4, KH_BARREL_1, KH_BARREL_2, KH_BARREL_3, KH_BARREL_4, KH_BARREL_5, KH_BARREL_6, KH_BARREL_7, KH_BARREL_8, KH_BARREL_9, KH_BARREL_10, KH_BARREL_11, KH_BARREL_12, KH_BARREL_13, KH_BARREL_14, KH_BARREL_15, KH_BARREL_16, KH_BARREL_17, KH_BARREL_18, KH_BARREL_19, KH_BARREL_20, KH_BARREL_21, KH_BARREL_22, KH_BARREL_23, KH_BARREL_24, KH_BARREL_25, KH_BARREL_26, KH_BARREL_27, KH_BARREL_28, KH_BARREL_29, KH_BARREL_30, KH_BARREL_31, KH_BARREL_32, KH_BARREL_33, KH_BARREL_34, KH_BARREL_35, KH_BARREL_36, KH_BARREL_37, KH_BARREL_38, KH_BARREL_39, KH_BARREL_40, KH_BARREL_41, KH_BARREL_42),
        NAVY_CRATES: (FC_CRATE_EASY_1, FC_CRATE_EASY_2, FC_CRATE_MED_1, FC_CRATE_MED_2, FC_CRATE_MED_3, FC_CRATE_MED_4, FC_CRATE_MED_5, FC_CRATE_1, FD_CRATE_EASY_1, FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3, FD_CRATE_MED_4, FD_CRATE_MED_5, KH_CRATE_1, KH_CRATE_2, KH_CRATE_3, KH_CRATE_4, KH_CRATE_5, KH_CRATE_6, KH_CRATE_7, KH_CRATE_8, KH_CRATE_9, KH_CRATE_10, KH_CRATE_11, KH_CRATE_12, KH_CRATE_13, KH_CRATE_14, KH_CRATE_15, KH_CRATE_16, KH_CRATE_17, KH_CRATE_18, KH_CRATE_19, KH_CRATE_20, KH_CRATE_21, KH_CRATE_22, KH_CRATE_23, KH_CRATE_24, KH_CRATE_25, KH_CRATE_26, KH_CRATE_27, KH_CRATE_28, KH_CRATE_29, KH_CRATE_30, KH_CRATE_31, KH_CRATE_32, KH_CRATE_33, KH_CRATE_34, KH_CRATE_35, KH_CRATE_36, KH_CRATE_37, KH_CRATE_38),
        ANY_BARREL: (NAVY_BARRELS, FC_EASY_BARRELS, FC_MED_BARRELS, FC_BARRELS, FD_EASY_BARRELS, FD_MED_BARRELS, FD_BARRELS, KH_BARRELS, RC_BARRELS, PR_BARRELS, PR_BARREL_1, PR_BARREL_2, PR_BARREL_3, PR_BARREL_4, PR_BARREL_5, PR_BARREL_6, PR_BARREL_7, PR_BARREL_8, PR_BARREL_9, PR_BARREL_10, PR_BARREL_11, FC_BARREL_EASY_1, FC_BARREL_EASY_2, FC_BARREL_EASY_3, FC_BARREL_EASY_4, FC_BARREL_MED_1, FC_BARREL_MED_2, FC_BARREL_MED_3, FC_BARREL_MED_4, FC_BARREL_1, FC_BARREL_2, FC_BARREL_3, FC_BARREL_4, FD_BARREL_EASY_1, FD_BARREL_EASY_2, FD_BARREL_EASY_3, FD_BARREL_EASY_4, FD_BARREL_EASY_5, FD_BARREL_EASY_6, FD_BARREL_MED_1, FD_BARREL_MED_2, FD_BARREL_MED_3, FD_BARREL_MED_4, KH_BARREL_1, KH_BARREL_2, KH_BARREL_3, KH_BARREL_4, KH_BARREL_5, KH_BARREL_6, KH_BARREL_7, KH_BARREL_8, KH_BARREL_9, KH_BARREL_10, KH_BARREL_11, KH_BARREL_12, KH_BARREL_13, KH_BARREL_14, KH_BARREL_15, KH_BARREL_16, KH_BARREL_17, KH_BARREL_18, KH_BARREL_19, KH_BARREL_20, KH_BARREL_21, KH_BARREL_22, KH_BARREL_23, KH_BARREL_24, KH_BARREL_25, KH_BARREL_26, KH_BARREL_27, KH_BARREL_28, KH_BARREL_29, KH_BARREL_30, KH_BARREL_31, KH_BARREL_32, KH_BARREL_33, KH_BARREL_34, KH_BARREL_35, KH_BARREL_36, KH_BARREL_37, KH_BARREL_38, KH_BARREL_39, KH_BARREL_40, KH_BARREL_41, KH_BARREL_42, RC_BARREL_1, RC_BARREL_2, RC_BARREL_3, RC_BARREL_4, RC_BARREL_5, RC_BARREL_6, RC_BARREL_7, RC_BARREL_8, RC_BARREL_9, RC_BARREL_10, RR_CELLAR_BARREL, DF_BQ_BARREL_1, DF_BQ_BARREL_2, DF_BQ_BARREL_3, DF_BQ_BARREL_4, DF_BQ_BARREL_5, DF_BQ_BARREL_6, DF_BQ_BARREL_7, DF_BQ_BARREL_8, DF_BQ_BARREL_9, T_G_BARRELS, T_G_BARREL_1, T_G_BARREL_2, T_G_BARREL_3),
        ANY_CRATE: (NAVY_CRATES, PR_CRATES, FC_EASY_CRATES, FC_MED_CRATES, FC_CRATES, T_ANY_CRATE, FD_EASY_CRATES, FD_MED_CRATES, FD_CRATES, KH_CRATES, RC_CRATES, PR_CRATE_1, PR_CRATE_2, PR_CRATE_3, PR_CRATE_4, PR_CRATE_5, PR_CRATE_6, PR_CRATE_7, PR_CRATE_8, PR_CRATE_9, PR_CRATE_10, PR_CRATE_11, PR_CRATE_12, PR_CRATE_13, PR_CRATE_14, PR_CRATE_15, FC_CRATE_EASY_1, FC_CRATE_EASY_2, FC_CRATE_MED_1, FC_CRATE_MED_2, FC_CRATE_MED_3, FC_CRATE_MED_4, FC_CRATE_MED_5, FC_CRATE_1, RR_CELLAR_CRATE, T_CRATE_1, T_CRATE_2, T_CRATE_3, FD_CRATE_EASY_1, FD_CRATE_MED_1, FD_CRATE_MED_2, FD_CRATE_MED_3, FD_CRATE_MED_4, FD_CRATE_MED_5, KH_CRATE_1, KH_CRATE_2, KH_CRATE_3, KH_CRATE_4, KH_CRATE_5, KH_CRATE_6, KH_CRATE_7, KH_CRATE_8, KH_CRATE_9, KH_CRATE_10, KH_CRATE_11, KH_CRATE_12, KH_CRATE_13, KH_CRATE_14, KH_CRATE_15, KH_CRATE_16, KH_CRATE_17, KH_CRATE_18, KH_CRATE_19, KH_CRATE_20, KH_CRATE_21, KH_CRATE_22, KH_CRATE_23, KH_CRATE_24, KH_CRATE_25, KH_CRATE_26, KH_CRATE_27, KH_CRATE_28, KH_CRATE_29, KH_CRATE_30, KH_CRATE_31, KH_CRATE_32, KH_CRATE_33, KH_CRATE_34, KH_CRATE_35, KH_CRATE_36, KH_CRATE_37, KH_CRATE_38, DF_BQ_CRATE_1, DF_BQ_CRATE_2, DF_BQ_CRATE_3, DF_BQ_CRATE_4, DF_BQ_CRATE_5, DF_BQ_CRATE_6, DF_BQ_CRATE_7, DF_BQ_CRATE_8, DF_BQ_CRATES, RC_CRATE_1, RC_CRATE_2, RC_CRATE_3, RC_CRATE_4, RC_CRATE_5),
        ANY_DESK: (FC_DESK, T_EITC_DESK, T_OUTPOST_DESK, FD_DESK, T_BOATSWAIN_DESK),
        ANY_SHELF: (FC_SHELF, FD_SHELF),
        ANY_CLOCK: (FC_CLOCK,),
        ANY_CABINET: (BOWDASH_CABINET, FD_CABINET),
        ANY_HAYSTACK: (KH_HAYSTACKS, KH_HAYSTACK_1, KH_HAYSTACK_2, KH_HAYSTACK_3),
        ANY_WELL: (KH_WELLS, KH_WELL_1, KH_WELL_2),
        ANY_GRAVE: (RC_GRAVES, RC_GRAVE_2, RC_GRAVE_4),
        WATER_GRAVE: (RC_GRAVE_1,),
        SOUTH_GRAVE: (RC_GRAVE_3,),
        ANY_CHEST: (RC_CHEST_1,),
        ANY_MINE_SHAFT: (RC_MINE_SHAFT_1,),
        ANY_PROP: None }


def getPropList(propId):
    return PropIds.PropDefs.get(propId)


def getPropType(propId):
    if propId in PropIds.PropDefs.get(PropIds.ANY_BARREL):
        return PropIds.ANY_BARREL
    elif propId in PropIds.PropDefs.get(PropIds.ANY_CRATE):
        return PropIds.ANY_CRATE
    elif propId in PropIds.PropDefs.get(PropIds.ANY_DESK):
        return PropIds.ANY_DESK
    elif propId in PropIds.PropDefs.get(PropIds.ANY_SHELF):
        return PropIds.ANY_SHELF
    elif propId in PropIds.PropDefs.get(PropIds.ANY_CLOCK):
        return PropIds.ANY_CLOCK
    elif propId in PropIds.PropDefs.get(PropIds.ANY_CABINET):
        return PropIds.ANY_CABINET
    elif propId in PropIds.PropDefs.get(PropIds.ANY_HAYSTACK):
        return PropIds.ANY_HAYSTACK
    elif propId in PropIds.PropDefs.get(PropIds.ANY_WELL):
        return PropIds.ANY_WELL
    elif propId in PropIds.PropDefs.get(PropIds.ANY_GRAVE):
        return PropIds.ANY_GRAVE
    elif propId in PropIds.PropDefs.get(PropIds.WATER_GRAVE):
        return PropIds.WATER_GRAVE
    elif propId in PropIds.PropDefs.get(PropIds.SOUTH_GRAVE):
        return PropIds.SOUTH_GRAVE
    elif propId in PropIds.PropDefs.get(PropIds.ANY_CHEST):
        return PropIds.ANY_CHEST
    elif propId in PropIds.PropDefs.get(PropIds.ANY_MINE_SHAFT):
        return PropIds.ANY_MINE_SHAFT
    else:
        return PropIds.ANY_PROP


class TreasureIds:
    PR_CHEST_1 = '1165018378.63Shochet'
    PR_CHEST_2 = '1165018628.69Shochet'
    PR_CHEST_3 = '1165018665.78Shochet'
    PR_CHEST_4 = '1165018696.72Shochet'
    PR_CHEST_5 = '1165018724.53Shochet'
    PR_CHEST_6 = '1165018774.94Shochet'
    PR_CHEST_7 = '1165018816.39Shochet'
    PR_CHESTS = 'PortRoyalChests'
    PR_ROYAL_CAVERNS_CHEST_1 = '1249581056.0jloehrle'
    PR_ROYAL_CAVERNS_CHEST_2 = '1249581056.0jloehrle0'
    PR_ROYAL_CAVERNS_CHEST_3 = '1249581056.0jloehrle1'
    PR_ROYAL_CAVERNS_CHEST_4 = '1249668480.0jloehrle2'
    PR_ROYAL_CAVERNS_CHEST_5 = '1249668480.0jloehrle3'
    PR_ROYAL_CAVERNS_CHEST_6 = '1249668992.0jloehrle'
    PR_ROYAL_CAVERNS_CHESTS = 'PortRoyalRoyalCavernsChests'
    PR_WICKED_CHEST_1 = '1165197257.5Shochet'
    PR_WICKED_CHEST_2 = '1165197288.56Shochet'
    PR_WICKED_CHEST_3 = '1165197469.59Shochet'
    PR_WICKED_CHEST_4 = '1175901184.0dxschafe'
    PR_WICKED_CHEST_5 = '1175901312.0dxschafe'
    PR_WICKED_CHEST_6 = '1175901440.0dxschafe'
    PR_WICKED_CHEST_7 = '1175901952.0dxschafe'
    PR_WICKED_CHEST_8 = '1175902080.0dxschafe'
    PR_WICKED_CHESTS = 'PortRoyalWickedThicketChests'
    PR_MURKY_CHEST_1 = '1247608960.0jloehrle0'
    PR_MURKY_CHEST_2 = '1247609088.0jloehrle'
    PR_MURKY_CHEST_3 = '1247609088.0jloehrle0'
    PR_MURKY_CHEST_4 = '1249670144.0jloehrle0'
    PR_MURKY_CHEST_5 = '1249670144.0jloehrle1'
    PR_MURKY_CHEST_6 = '1249670144.0jloehrle2'
    PR_MURKY_CHESTS = 'PortRoyalMurkyHollowChests'
    PR_GOVERNOR_G_CHEST_1 = '1176150912.0dxschafe'
    PR_GOVERNOR_G_CHEST_2 = '1176151040.0dxschafe'
    PR_GOVERNOR_G_CHEST_3 = '1176151040.0dxschafe0'
    PR_GOVERNOR_G_CHEST_4 = '1176151040.0dxschafe1'
    PR_GOVERNOR_G_CHEST_5 = '1176151168.0dxschafe0'
    PR_GOVERNOR_G_CHEST_6 = '1176151296.0dxschafe'
    PR_GOVERNOR_G_CHEST_7 = '1176151424.0dxschafe'
    PR_GOVERNOR_G_CHESTS = 'PortRoyalGovernorGardenChests'
    CUTTS_TREASURE = '1178300160.0dxschafe'
    SCORPION_TREASURE = '1177007104.0dxschafe'
    FLYTRAP_TREASURE = '1177021184.0dxschafe'
    T_CHEST_4 = '1178300160.0dxschafe'
    T_CHEST_5 = '1165199625.3Shochet'
    T_CHEST_6 = '1165199876.28Shochet'
    T_CHEST_7 = '1165199908.11Shochet'
    T_CHEST_8 = '1189564672.0dxschafe'
    T_CHEST_9 = '1165200029.95Shochet'
    T_CHEST_10 = '1175102976.0dxschafe'
    T_CHESTS = 'TortugaChests'
    T_W_CHEST_1 = '1165201347.11Shochet'
    T_W_CHEST_2 = '1165201844.27Shochet'
    T_W_CHEST_3 = '1165205254.09Shochet'
    T_W_CHEST_4 = '1177007104.0dxschafe'
    T_W_CHESTS = 'TortugaWildwoodChests'
    T_RN_CHEST_1 = '1165200204.91Shochet'
    T_RN_CHEST_2 = '1165200514.06Shochet'
    T_RN_CHEST_3 = '1165200809.17Shochet'
    T_RN_CHEST_4 = '1176169344.0dxschafe0'
    T_RN_CHEST_5 = '1176169472.0dxschafe'
    T_RN_CHEST_6 = '1176169600.0dxschafe0'
    T_RN_CHEST_7 = '1176169728.0dxschafe'
    T_RN_CHEST_8 = '1177016704.0dxschafe'
    T_RN_CHEST_9 = '1186698880.0dxschafe'
    T_RN_CHESTS = 'TortugaRatsNestChests'
    T_MM_CHEST_1 = '1177021184.0dxschafe'
    T_MM_CHEST_2 = '1177021312.0dxschafe'
    T_MM_CHESTS = 'TortugaMistyMireChests'
    DW_CHEST_1 = '1175533440.0dxschafe'
    DW_CHEST_2 = '1175533440.0dxschafe0'
    DW_CHEST_3 = '1213740055.14WDIG'
    DW_CHEST_4 = '1213740088.81WDIG'
    DW_CHEST_5 = '1213740104.3WDIG'
    DW_CHEST_6 = '1213740118.8WDIG'
    DW_CHEST_7 = '1213740163.47WDIG'
    DW_CHEST_8 = '1213740183.83WDIG'
    DW_CHEST_9 = '1213740223.27WDIG'
    DW_CHEST_10 = '1213740249.55WDIG'
    DW_CHESTS = 'DriftwoodIslandChests'
    DF_CHEST_1 = '1236655362.9piwanow'
    DF_CHEST_2 = '1236655444.04piwanow'
    DF_CHEST_3 = '1236655125.32piwanow'
    DF_CHEST_4 = '1236655200.31piwanow'
    DF_CHEST_5 = '1245460007.72piwanow'
    DF_CHESTS = 'DelFuegoChests'
    DF_CHEST_CAVE_D_1 = '1249592192.0jloehrle2'
    DF_CHEST_CAVE_D_2 = '1249592192.0jloehrle3'
    DF_CHEST_CAVE_D_3 = '1249592192.0jloehrle4'
    DF_CHEST_CAVE_D_4 = '1249667712.0jloehrle3'
    DF_CHEST_CAVE_D_5 = '1249667840.0jloehrle'
    DF_CHEST_CAVE_D_6 = '1249667840.0jloehrle1'
    DF_CHEST_CAVE_D_7 = '1249674074.03piwanow'
    DF_CHEST_CAVE_D = 'DelFuegoCaveDChests'
    KH_CHEST_1 = '1176845952.0dxschafe0'
    KH_CHEST_2 = '1176856832.0dxschafe'
    KH_CHEST_3 = '1176846080.0dxschafe'
    KH_CHESTS = 'KingsheadChests'
    RR_CHEST_1 = '1182807552.0dxschafe0'
    RR_CHEST_2 = '1182807424.0dxschafe'
    RR_CHEST_3 = '1182807552.0dxschafe2'
    RR_CHEST_4 = '1182807552.0dxschafe'
    RR_CHESTS = 'Rumrunner Isle Chests'
    IC_CHEST_1 = '1175105408.0dxschafe'
    IC_CHEST_2 = '1175041664.0dxschafe'
    IC_CHEST_3 = '1175041664.0dxschafe0'
    IC_CHEST_4 = '1175041664.0dxschafe1'
    IC_CHEST_5 = '1175041664.0dxschafe2'
    IC_CHEST_6 = '1175041664.0dxschafe3'
    IC_CHEST_7 = '1175041664.0dxschafe4'
    IC_CHEST_8 = '1175041664.0dxschafe5'
    IC_CHEST_9 = '1175041664.0dxschafe6'
    IC_CHEST_10 = '1175041664.0dxschafe7'
    IC_CHEST_11 = '1210112896.0WDIG'
    IC_CHESTS = 'IslaCangrejosChests'
    IP_CHEST_1 = '1175021696.0dxschafe0'
    IP_WASP_TREASURE = '1186713984.0dxschafe'
    TO_CAVERNS_CHEST_1 = '1249421312.0jloehrle3'
    TO_CAVERNS_CHEST_2 = '1249421440.0jloehrle'
    TO_CAVERNS_CHEST_3 = '1249671936.0jloehrle'
    TO_CAVERNS_CHEST_4 = '1249671936.0jloehrle0'
    TO_CAVERNS_CHEST_5 = '1250881664.0jloehrle'
    TO_CAVERNS_CHESTS = 'TormentaCursedCavernsChests'
    CT_CHEST_1 = '1210109440.0WDIG'
    OI_DJ_TREASURE = '1186714240.0dxschafe0'
    OI_CHEST_1 = '1241481746.85piwanow0'
    OI_CHEST_2 = '1241481818.91piwanow'
    OI_CHEST_3 = '1241481883.74piwanow'
    OI_CHESTS = 'OutcastIsleChests'
    RC_CHEST_1 = '1276642989.73robrusso'
    RC_CHEST_2 = '1276643038.28robrusso'
    RC_CHEST_3 = '1276642926.47robrusso'
    RC_CHEST_4 = '1276643096.08robrusso'
    RC_CHEST_5 = '1277139735.0robrusso'
    RC_CHEST_6 = '1277139936.64robrusso'
    RC_CHEST_7 = '1277140059.72robrusso'
    RC_CHEST_8 = '1277140171.47robrusso'
    RC_CHESTS = 'RavensCoveChests'
    RC_CHESTS_2 = 'RavensCoveChests2'
    ANY_TREASURE = 'AnyTreasure'
    TreasureDefs = {
        PR_CHEST_1: (PR_CHEST_1,),
        PR_CHEST_2: (PR_CHEST_2,),
        PR_CHEST_3: (PR_CHEST_3,),
        PR_CHEST_4: (PR_CHEST_4,),
        PR_CHEST_5: (PR_CHEST_5,),
        PR_CHEST_6: (PR_CHEST_6,),
        PR_CHEST_7: (PR_CHEST_7,),
        PR_CHESTS: (PR_CHEST_1, PR_CHEST_2, PR_CHEST_3, PR_CHEST_4, PR_CHEST_5, PR_CHEST_6, PR_CHEST_7),
        PR_ROYAL_CAVERNS_CHEST_1: (PR_ROYAL_CAVERNS_CHEST_1,),
        PR_ROYAL_CAVERNS_CHEST_2: (PR_ROYAL_CAVERNS_CHEST_2,),
        PR_ROYAL_CAVERNS_CHEST_3: (PR_ROYAL_CAVERNS_CHEST_3,),
        PR_ROYAL_CAVERNS_CHEST_4: (PR_ROYAL_CAVERNS_CHEST_4,),
        PR_ROYAL_CAVERNS_CHEST_5: (PR_ROYAL_CAVERNS_CHEST_5,),
        PR_ROYAL_CAVERNS_CHEST_6: (PR_ROYAL_CAVERNS_CHEST_6,),
        PR_ROYAL_CAVERNS_CHESTS: (PR_ROYAL_CAVERNS_CHEST_1, PR_ROYAL_CAVERNS_CHEST_2, PR_ROYAL_CAVERNS_CHEST_3, PR_ROYAL_CAVERNS_CHEST_4, PR_ROYAL_CAVERNS_CHEST_5, PR_ROYAL_CAVERNS_CHEST_6),
        PR_WICKED_CHESTS: (PR_WICKED_CHEST_1, PR_WICKED_CHEST_2, PR_WICKED_CHEST_3, PR_WICKED_CHEST_4, PR_WICKED_CHEST_5, PR_WICKED_CHEST_6, PR_WICKED_CHEST_7, PR_WICKED_CHEST_8),
        PR_MURKY_CHESTS: (PR_MURKY_CHEST_1, PR_MURKY_CHEST_2, PR_MURKY_CHEST_3, PR_MURKY_CHEST_4, PR_MURKY_CHEST_5, PR_MURKY_CHEST_6),
        PR_GOVERNOR_G_CHEST_1: (PR_GOVERNOR_G_CHEST_1,),
        PR_GOVERNOR_G_CHEST_2: (PR_GOVERNOR_G_CHEST_2,),
        PR_GOVERNOR_G_CHEST_3: (PR_GOVERNOR_G_CHEST_3,),
        PR_GOVERNOR_G_CHEST_4: (PR_GOVERNOR_G_CHEST_4,),
        PR_GOVERNOR_G_CHEST_5: (PR_GOVERNOR_G_CHEST_5,),
        PR_GOVERNOR_G_CHEST_6: (PR_GOVERNOR_G_CHEST_6,),
        PR_GOVERNOR_G_CHEST_7: (PR_GOVERNOR_G_CHEST_7,),
        PR_GOVERNOR_G_CHESTS: (PR_GOVERNOR_G_CHEST_1, PR_GOVERNOR_G_CHEST_2, PR_GOVERNOR_G_CHEST_3, PR_GOVERNOR_G_CHEST_4, PR_GOVERNOR_G_CHEST_5, PR_GOVERNOR_G_CHEST_6, PR_GOVERNOR_G_CHEST_7),
        CUTTS_TREASURE: (CUTTS_TREASURE,),
        SCORPION_TREASURE: (SCORPION_TREASURE,),
        FLYTRAP_TREASURE: (FLYTRAP_TREASURE,),
        T_CHEST_5: (T_CHEST_5,),
        T_CHEST_6: (T_CHEST_6,),
        T_CHEST_7: (T_CHEST_7,),
        T_CHEST_8: (T_CHEST_8,),
        T_CHEST_9: (T_CHEST_9,),
        T_CHEST_10: (T_CHEST_10,),
        T_CHESTS: (T_CHEST_4, T_CHEST_5, T_CHEST_6, T_CHEST_7, T_CHEST_8, T_CHEST_9, T_CHEST_10),
        T_W_CHESTS: (T_W_CHEST_1, T_W_CHEST_2, T_W_CHEST_3, T_W_CHEST_4),
        T_RN_CHESTS: (T_RN_CHEST_1, T_RN_CHEST_2, T_RN_CHEST_3, T_RN_CHEST_4, T_RN_CHEST_5, T_RN_CHEST_6, T_RN_CHEST_7, T_RN_CHEST_8, T_RN_CHEST_9),
        T_MM_CHESTS: (T_MM_CHEST_1, T_MM_CHEST_2),
        DF_CHEST_1: (DF_CHEST_1,),
        DF_CHEST_2: (DF_CHEST_2,),
        DF_CHEST_3: (DF_CHEST_3,),
        DF_CHEST_4: (DF_CHEST_4,),
        DF_CHEST_5: (DF_CHEST_5,),
        DF_CHESTS: (DF_CHEST_1, DF_CHEST_2, DF_CHEST_3, DF_CHEST_4, DF_CHEST_5),
        DF_CHEST_CAVE_D_1: (DF_CHEST_CAVE_D_1,),
        DF_CHEST_CAVE_D_2: (DF_CHEST_CAVE_D_2,),
        DF_CHEST_CAVE_D_3: (DF_CHEST_CAVE_D_3,),
        DF_CHEST_CAVE_D_4: (DF_CHEST_CAVE_D_4,),
        DF_CHEST_CAVE_D_5: (DF_CHEST_CAVE_D_5,),
        DF_CHEST_CAVE_D_6: (DF_CHEST_CAVE_D_6,),
        DF_CHEST_CAVE_D_7: (DF_CHEST_CAVE_D_7,),
        DF_CHEST_CAVE_D: (DF_CHEST_CAVE_D_1, DF_CHEST_CAVE_D_2, DF_CHEST_CAVE_D_3, DF_CHEST_CAVE_D_4, DF_CHEST_CAVE_D_5, DF_CHEST_CAVE_D_6, DF_CHEST_CAVE_D_7),
        TO_CAVERNS_CHESTS: (TO_CAVERNS_CHEST_1, TO_CAVERNS_CHEST_2, TO_CAVERNS_CHEST_3, TO_CAVERNS_CHEST_4, TO_CAVERNS_CHEST_5),
        KH_CHESTS: (KH_CHEST_1, KH_CHEST_2, KH_CHEST_3),
        KH_CHEST_1: (KH_CHEST_1,),
        KH_CHEST_2: (KH_CHEST_2,),
        KH_CHEST_3: (KH_CHEST_3,),
        RR_CHEST_1: (RR_CHEST_1,),
        RR_CHESTS: (RR_CHEST_1, RR_CHEST_2, RR_CHEST_3, RR_CHEST_4),
        CT_CHEST_1: (CT_CHEST_1,),
        DW_CHESTS: (DW_CHEST_1, DW_CHEST_2, DW_CHEST_3, DW_CHEST_4, DW_CHEST_5, DW_CHEST_6, DW_CHEST_7, DW_CHEST_8, DW_CHEST_9, DW_CHEST_10),
        IC_CHEST_1: (IC_CHEST_1,),
        IC_CHEST_9: (IC_CHEST_9,),
        IC_CHEST_11: (IC_CHEST_11,),
        IC_CHESTS: (IC_CHEST_1, IC_CHEST_2, IC_CHEST_3, IC_CHEST_4, IC_CHEST_5, IC_CHEST_6, IC_CHEST_7, IC_CHEST_8, IC_CHEST_9, IC_CHEST_10),
        IP_CHEST_1: (IP_CHEST_1,),
        IP_WASP_TREASURE: (IP_WASP_TREASURE,),
        OI_DJ_TREASURE: (OI_DJ_TREASURE,),
        OI_CHEST_1: (OI_CHEST_1,),
        OI_CHEST_2: (OI_CHEST_1,),
        OI_CHEST_3: (OI_CHEST_1,),
        OI_CHESTS: (OI_CHEST_1, OI_CHEST_2, OI_CHEST_3),
        RC_CHESTS: (RC_CHEST_1, RC_CHEST_2, RC_CHEST_3, RC_CHEST_4),
        RC_CHESTS_2: (RC_CHEST_5, RC_CHEST_6, RC_CHEST_7, RC_CHEST_8),
        ANY_TREASURE: None }


def getTreasureList(treasureId):
    return TreasureIds.TreasureDefs.get(treasureId)


class ShipIds:
    ANY_LARGE_SHIP = 'AnyLargeShip'
    ANY_WARSHIP = 'AnyWarShip'
    ANY_EITC_CORVETTE = 'AnyEITCCorvette'
    ANY_EITC_SEA_VIPER = 'AnyEITCSeaViper'
    ANY_EITC_MARAUDER = 'AnyEITCMarauder'
    ANY_EITC_BARRACUDA = 'AnyEITCBarracuda'
    ANY_FRENCH_SHADOW_CROW = 'AnyFrenchShadowCrow'
    ANY_FRENCH_HELLHOUND = 'AnyFrenchHellhound'
    ANY_FRENCH_BLOOD_SCOURGE = 'AnyFrenchBloodScourge'
    ANY_SPANISH_SHADOW_CROW = 'AnySpanishShadowCrow'
    ANY_SPANISH_HELLHOUND = 'AnySpanishHellhound'
    ANY_SPANISH_BLOOD_SCOURGE = 'AnySpanishBloodScourge'
    ANY_CERBERUS = 'AnyCerberus'
    ShipDefs = {
        INTERCEPTORL1: (NAVY_FERRET, EITC_SEA_VIPER),
        INTERCEPTORL2: (NAVY_GREYHOUND, EITC_BLOODHOUND),
        INTERCEPTORL3: (NAVY_KINGFISHER, EITC_BARRACUDA),
        MERCHANTL1: (NAVY_BULWARK, EITC_SENTINEL),
        MERCHANTL2: (NAVY_VANGUARD, EITC_IRONWALL),
        MERCHANTL3: (NAVY_MONARCH, EITC_OGRE),
        WARSHIPL1: (NAVY_PANTHER, EITC_CORVETTE),
        WARSHIPL2: (NAVY_CENTURION, EITC_MARAUDER),
        WARSHIPL3: (NAVY_MAN_O_WAR, EITC_WARLORD),
        ANY_LARGE_SHIP: (NAVY_BULWARK, EITC_SENTINEL, NAVY_VANGUARD, EITC_IRONWALL, NAVY_MONARCH, EITC_OGRE, NAVY_COLOSSUS, EITC_BEHEMOTH, NAVY_PANTHER, EITC_CORVETTE, NAVY_CENTURION, EITC_MARAUDER, NAVY_MAN_O_WAR, EITC_WARLORD, NAVY_DREADNOUGHT, EITC_JUGGERNAUT),
        ANY_WARSHIP: (NAVY_PANTHER, EITC_CORVETTE, NAVY_CENTURION, EITC_MARAUDER, NAVY_MAN_O_WAR, EITC_WARLORD, NAVY_DREADNOUGHT, EITC_JUGGERNAUT),
        ANY_EITC_CORVETTE: (EITC_CORVETTE,),
        ANY_EITC_SEA_VIPER: (EITC_SEA_VIPER,),
        ANY_EITC_MARAUDER: (EITC_MARAUDER,),
        ANY_EITC_BARRACUDA: (EITC_BARRACUDA,),
        ANY_FRENCH_SHADOW_CROW: (SKEL_SHADOW_CROW_FR,),
        ANY_FRENCH_HELLHOUND: (SKEL_HELLHOUND_FR,),
        ANY_FRENCH_BLOOD_SCOURGE: (SKEL_BLOOD_SCOURGE_FR,),
        ANY_SPANISH_SHADOW_CROW: (SKEL_SHADOW_CROW_SP,),
        ANY_SPANISH_HELLHOUND: (SKEL_HELLHOUND_SP,),
        ANY_SPANISH_BLOOD_SCOURGE: (SKEL_BLOOD_SCOURGE_SP,),
        ANY_CERBERUS: (SKEL_HELLHOUND_FR, SKEL_HELLHOUND_SP) }


def getShipList(shipId):
    return ShipIds.ShipDefs.get(shipId)


class NPCIds:
    DOGGEREL_DAN = '1154731709.64jubutler'
    WILL_TURNER = '1152830677.95jubutler'
    TIA_DALMA_PR = '1154497344.0jubutlerPR'
    ELIZABETH = '1171325040.86MAsaduzz'
    DARBY_DRYDOCK = '1156986248.77jasyeung'
    GRAHAM_MARSH = '1169083104.56sdnaik'
    JEWELER_SMITTY = '1169151219.8mike'
    R_SMITH_PEWTERER = '1157094552.02jasyeung'
    HARBORMASTER = '1156986071.78jasyeung'
    DOCKWORKER_FITZ = '1168748251.22joswilso'
    PICKERT = '1174345216.0dxschafe'
    CASSANDRA = '1175554816.0dxschafe'
    LUCINDA = '1175553664.0dxschafe'
    DAISY = '1175635584.0dxschafe'
    GORDON_GREER = '1169190957.44mike'
    BINGHAM = '1169060460.13mike'
    BLAKELEY = '1169075008.52mike'
    JUNE = '1169075683.22mike'
    EWAN = '1169079172.34sdnaik'
    BARTHOLOMEW_WATKINS = '1157048353.58jasyeung'
    JOSIE_MCKEEDY = '1178234368.0dchiappe1'
    JOSIE_MCREEDY = '1178234368.0dchiappe1'
    SAM_SEABONES = '1154574164.57jubutler'
    PETER_CHIPPARR = '1178654720.0dchiappe'
    SHANE_MCGREENY = '1187219584.0dxschafe0'
    JIM_WAVEMONGER = '1248132224.0jloehrle'
    SOLOMON_ODOUGAL = '1201028352.0dxschafe'
    WILLIAM_TURK = '1175792768.0dxschafe'
    SARAH = '1201109074.66dxschafe'
    EDWARD_SHACKLEBY = '1181263360.0dxschafe'
    EDWARD_STORMHAWK = '1156986020.6jasyeung'
    JOHN_WALLACE = '1181171584.0dxschafe0'
    JACK_ROWDY_ROOSTER = '1209749843.55dxschafe'
    NATHANIEL_TRUEHOUND = '1196896512.0dxschafe'
    CAPTAIN_JOB = '1180720000.0dchiappe1'
    ENSIGN_GRIMM = '1219895971.52mtucker'
    PHILLIP_FULLER = '1181260288.0dxschafe'
    ANGEL_OBONNEY = '1227674362.91WDIG'
    SID_TACKEM = '1229141258.23mtucker'
    ERIN_AMOROUS = '1229145127.43mtucker'
    FLECTHER_BEAKMAN = '1240950699.65ian'
    EMMA = '1179523435.84dchiappe'
    JAMES_MACDOUGAL = '1181261824.0dxschafe'
    CLAYTON_COLLARD = '1181267712.0dxschafe'
    ROSE_SEAFELLOW = '1232061565.89WDIG'
    OLD_GREGG = '1258054417.88Admin'
    BARBOSSA = '1172618710.78sdnaik'
    JACK = '1174954368.0jubutler'
    JOSHAMEE = '1168022298.47Shochet'
    NILL_OFFRILL = '1172630144.0mike'
    CARVER = '1168022348.66Shochet'
    HENDRY_CUTTS = '1169071109.22mike'
    GILADOGA = '1172887552.0mike0'
    DOC_GROG = '1169068641.66mike'
    LE_CERDO = '1169078025.53mike'
    ORINDA = '1169063296.16mike'
    MALLET = '1172276608.0mike'
    BENEDEK = '1169070429.72mike'
    BOWDASH = '1169075474.72mike'
    SCARLET = '1168052247.45mike'
    FABIOLA = '1165199931.31Shochet'
    TOMAS = '1169076564.88mike'
    BUTCHER_BROWN = '1169076109.16mike'
    BEN_FLATTS = '1169076368.97mike'
    BONITA = '1169067906.19mike'
    MILLIE = '1169077360.47mike'
    BLACKSMITH_FLINTY = '1169075869.81mike'
    O_MALLEY = '1165199819.22Shochet'
    SEAMSTRESS_ANNE = '1169077081.52mike'
    JOHNNY_MCVANE = '1169088062.75mike'
    RETAVICK = '1175650176.0dxschafe'
    SIMON_HORNBOW = '1187306240.0dxschafe'
    DAJIN_MING = '1196907776.0dxschafe0'
    LALA_LOVEL = '1201025280.0dxschafe'
    BUTCHER_BROWN = '1169076109.16mike'
    BOATSWAIN_BILL = '1181593472.0dxschafe'
    BIG_PHIL = '1179961216.0dchiappe'
    SLIM = '1179360256.0dchiappe'
    JACK_REDRAT = '1175800576.0dxschafe'
    ALEXANDER_THAYER = '1181606272.0dxschafe'
    ISAIAH_CALLECUTTER = '1196904064.0dxschafe'
    AMELIA_SUNFELLOW = '1212432000.0WDIG1'
    DEDRIE_DUNNAM = '1229139756.35mtucker'
    HORATIO_FOWLER = '1241477820.93ian'
    GUNNER = '1169078705.84mike'
    GARRETT = '1172887552.0mike'
    DUCHAMPS = '1173146624.0mike0'
    MORRIS = '1173147520.0mike'
    ROMANY_BEV = '1157097924.52jasyeung'
    OLIVIER = '1175721216.0dxschafe'
    FERNANDO = '1175733248.0dxschafe'
    PAUPER_PEDRO = '1175730944.0dxschafe'
    RICO = '1175733376.0dxschafe'
    BALTHASAR = '1157097728.52jasyeung'
    VALENTINA = '1177714944.0mike'
    FAKE_VALENTINA = '1111111111.1mwt'
    PERLA_ALODIA = '1201228098.28dxschafe'
    MERCEDES_CORAZON = '1201230131.11dxschafe'
    SHOCHETT_PRYMME = '1157097962.5jasyeung'
    BILLY_MCKIDD = '1190744501.14dxschafe'
    ROLAND_RAGGART = '1207073489.41mtucker'
    ERASMUS_GRIMSDITCH = '1157098075.78jasyeung'
    ADORIA_DOLORES = '1201227181.3dxschafe'
    DELILAH_DUNSMORE = '1219965016.25mtucker'
    MIGUEL_MONTOYA = '1220039541.89mtucker'
    FERRERA = '1157098037.86jasyeung'
    PELAGIA = '1237497701.52piwanow'
    HENRY_LOWMAN = '1241911057.44ian'
    HEARTLESS_ROSALINE = '1237499258.14piwanow'
    CLEMENCE_BASILSHOT = '1237850626.09piwanow'
    BILLY_MCKIDD = '1190744501.14dxschafe'
    TIA_DALMA = '1154497344.0jubutler'
    MACOMO = '1176186151.42mike'
    CARLOS_CIENFUEGOS = '1189456447.08kmuller'
    BASTIEN_CRAVEN = '1169081738.45mike'
    JOHN_SMITH = '1169094482.66mike'
    BRONZE_JOHN = '1169094669.8mike'
    WOODRUFF = '1175101824.0dxschafe'
    SCARY_MARY = '1170739712.0mike'
    DOG_LOCKGRIM = '1214345458.84WDIG'
    MAGGIE_RIGRAGE = '1214345910.48WDIG'
    CAPTAIN_STEADMAN = '1170739968.0mike'
    ALTHEA = '1174342784.0dxschafe'
    CAPTAIN_BILLINGTON = '1174353792.0dxschafe'
    WALLACE = '1174343680.0dxschafe'
    OHENRY = '1174344320.0dxschafe'
    CAPTAIN_ARCHER = '1174345984.0dxschafe'
    TRENT = '1174351616.0dxschafe'
    CAPTAIN_JONES = '1174351232.0dxschafe'
    ALBERTO = '1174350464.0dxschafe'
    JEHAN_CARROU = '1175118080.0dxschafe'
    PENROD = '1175117568.0dxschafe0'
    COLLIER = '1175119104.0dxschafe1'
    CAPTAIN_BARTS = '1175120896.0dxschafe0'
    CAPTAIN_REGINALD = '1176322304.0mike1'
    CAPTAIN_DENNISON = '1176322432.0mike'
    CAPTAIN_HEDLEY = '1176322432.0mike0'
    CAPTAIN_BIGGLETON = '1176322560.0mike'
    CAPTAIN_NORMAN = '1176322560.0mike0'
    CAPTAIN_FITZPATRICK = '1176322688.0mike'
    CAPTAIN_HAMILTON = '1176322688.0mike0'
    CAPTAIN_MONTROSE = '1176322816.0mike'
    LUTHER = '1176322944.0mike'
    OFFICER_MILLER = '1190420608.0dxschafe1'
    COMMANDER_GENTRY = '1190420736.0dxschafe'
    CAPTAIN_ACKERS = '1219104942.43mtucker'
    CAPTAIN_SWAIN = '1219105162.48mtucker'
    BLACK_MACK = '1176334208.0mike0'
    GARCIA_DE_AVARCIA = '1203449603.97akelts'
    PIERRE_LE_PORC = '1202519757.13akelts'
    SPANISH_SHIPWRIGHT = '1203451028.89akelts'
    GENERAL_BLOODLESS = '1247517440.0jloehrle'
    GENERAL_HEX = '1220906480.53mtucker'
    GENERAL_SANDSPINE = '1219434293.16mtucker'
    GENERAL_DARKHART = '1238440501.07piwanow'
    NEBAN_THE_HIRED_GUN = '1219352693.09mtucker'
    REMINGTON_THE_ASSASSIN = '1219367627.94mtucker'
    SAMUEL = '1219339266.79mtucker'
    BONERATTLER = '1219426331.38mtucker'
    UNDEAD_TIMOTHY_DARTAN = '1238441187.46piwanow'
    DREADTOOTH = '1219277508.79mtucker'
    HARDTACK = '1219277509.79mtucker'
    CROQUETTES_DE_CRABE = '1244583168.0jloehrle0'
    SCATTER_SNAP = '1244833920.0jloehrle'
    DEVIL_ROOT = '1244657664.0jloehrle1'
    HIVE_QUEEN = '1244832512.0jloehrle'
    FOULBERTO = '1291327895.46jloehrle'
    LASCHAFE = '1302895055.78jloehrle'
    MALICIOSO = '1218760329.71mtucker'
    VENOM_LASH = '1218760328.71mtucker'
    CLAUDE_DARCIS = '1239930457.38piwanow'
    SAMUEL_SHAW = '1248740960.66piwanow'
    CAPT_EZEKIEL_ROTT = '1248741261.66piwanow'
    BILL_BARRETT = '1248741262.66piwanow'
    NATHAN_GOULD = '1248741263.66piwanow'
    JEREMIAH_DEDMAN = '1248741264.66piwanow'
    EDWARD_BRITTLE = '1274819841.73gcarranza'
    THOMAS_FISHMEISTER = '1274825376.01gcarranza'
    MADAM_ZIGANA = '1274825967.94gcarranza'
    WIDOW_THREADBARREN = '1274892762.3gcarranza'
    SKELETON_POKER_BOUNCER = '1277941714.21robrusso'
    EL_PATRON = '1274889994.04gcarranza'
    KUDGEL = '1274906957.35gcarranza'
    SENOR_FANTIFICO = '1274894542.99gcarranza'
    BEN_CLUBHEART = '1274908180.63gcarranza'
    SANDIE_CLUBHEART = '1274909359.61gcarranza'
    DR_BELLROG = '1274890958.87gcarranza'
    YELLOW_DAN = '1142321958.13sdnaik'
    WILLIAM_TRUEGRIN = '1248203967.73jloehrle'
    WILL_WILDSHOT = '1190743269.78dxschafe'
    IH_NPC_1 = '1278709085.7jloehrle'
    IH_NPC_2 = '1278708908.39jloehrle'
    IH_NPC_3 = '1278548378.92jloehrle'
    SGT_SCRIMMAGE = '1285622621.56robrusso'


class Bribes:
    SMALL = 10
    AVERAGE = 25
    MEDIUM = 50
    LARGE = 100
    HUGE = 500


class PokerPots:
    MINOR = 25
    SMALL = 40
    AVERAGE = 60
    MEDIUM = 80
    LARGE = 150
    HUGE = 400
    BIG = 650
    GIANT = 5000


class ExpRewards:
    TRIVIAL = 25
    SMALL = 100
    MEDIUM = 500
    LARGE = 1000
    HUGE = 2000


class Probability:
    EXTREMELY_RARE = 0.01
    VERY_RARE = 0.1
    RARE = 0.25
    INFREQUENT = 0.5
    FREQUENT = 0.75
    VERY_FREQUENT = 0.9
    ALWAYS = 1.0


class Attempts:
    VERY_RARE = 16
    RARE = 10
    INFREQUENT = 7
    FREQUENT = 4
    VERY_FREQUENT = 2
    ALWAYS = 1


class DoubleRepTime:
    HALFHOUR = 60 * 30
    HOUR = 60 * 60
    TWOHOUR = 60 * 120
    THREEHOUR = 60 * 180


class DowsingRodResults:
    DOWSING_ROD_NOT_AVAILABLE = 0
    DOWSING_ROD_COLDER = 1
    DOWSING_ROD_WARMER = 2
    DOWSING_ROD_HOT = 3
    DOWSING_ROD_SAME = 4
    DOWSING_ROD_COMPLETE = 5
    DOWSING_ROD_FIRST_TIME = 6
    DOWSING_ROD_WARMER_FAR = 7
    DOWSING_ROD_WARMER_CLOSE = 8
    DOWSING_ROD_COLDER_CLOSE = 9
