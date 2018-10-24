from panda3d.core import Buffer, Camera, CardMaker, DisplayRegion, Lens, NodePath, PerspectiveLens, Point3, TextNode, Texture, Vec3, Vec4
# File: I (Python 2.4)

from direct.gui.DirectGui import *
from direct.task.Task import Task
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.battle import WeaponGlobals
from pirates.economy import EconomyGlobals
from pirates.economy.EconomyGlobals import *
from pirates.battle import CannonGlobals
from pirates.uberdog.UberDogGlobals import InventoryType
from pirates.uberdog import UberDogGlobals
from pirates.piratesgui.BorderFrame import BorderFrame
from pirates.reputation import ReputationGlobals
from pirates.piratesgui.InventoryListItem import InventoryListItem
from pirates.inventory import ItemGlobals
from pirates.pirate import TitleGlobals

class InventoryItemGui(InventoryListItem):
    width = PiratesGuiGlobals.InventoryItemGuiWidth
    height = PiratesGuiGlobals.InventoryItemGuiHeight
    available = True

    def __init__(self, data, trade = 0, buy = 0, sell = 0, use = 0, weapon = 0, isDisabled = 0, **kw):
        if (trade and buy and sell and use or weapon) and not isDisabled:
            buttonRelief = DGG.RAISED
            buttonState = DGG.NORMAL
        else:
            buttonRelief = DGG.RIDGE
            buttonState = DGG.DISABLED
        self.loadGui()
        optiondefs = (('relief', None, None), ('state', buttonState, None), ('frameSize', (0, self.width, 0, self.height), None), ('image', InventoryItemGui.genericButton, None), ('image_scale', (0.540000, 1, 0.418), None), ('image_pos', (0.260, 0, 0.08), None), ('pressEffect', 0, None), ('command', self.sendEvents, None))
        self.defineoptions(kw, optiondefs)
        InventoryListItem.__init__(self, data, trade = trade, buy = buy, sell = sell, use = use, weapon = weapon, isDisabled = isDisabled, width = self.width, height = self.height)
        self.initialiseoptions(InventoryItemGui)
        self.createGui()
        self.draggable = abs(self.buy) + abs(self.sell) + abs(self.use) + abs(self.trade) - 1
        if self.draggable > 0:
            self.bind(DGG.B1PRESS, self.dragStart)
            self.bind(DGG.B1RELEASE, self.dragStop)
            self.bind(DGG.B2PRESS, self.dragStart)
            self.bind(DGG.B2RELEASE, self.dragStop)
            self.bind(DGG.B3PRESS, self.dragStart)
            self.bind(DGG.B3RELEASE, self.dragStop)

        if self.weapon:
            self.bind(DGG.B1PRESS, self.equipWeapon)
            self.bind(DGG.B2PRESS, self.equipWeapon)
            self.bind(DGG.B3PRESS, self.equipWeapon)

        self.helpFrame = None
        self.cm = CardMaker('itemCard')
        self.cm.setFrame(-0.299, 0.299, -0.089, 0.089)
        self.buffer = None
        self.lens = PerspectiveLens()
        self.lens.setNear(0.5)
        self.lens.setAspectRatio(0.598 / 0.179)
        self.realItem = None
        self.itemCard = None
        self.portraitSceneGraph = NodePath('PortraitSceneGraph')
        detailGui = loader.loadModel('models/gui/gui_card_detail')
        self.bg = detailGui.find('**/color')
        self.bg.setScale(4)
        self.bg.setPos(0, 17, -6.28)
        self.glow = detailGui.find('**/glow')
        self.glow.setScale(3)
        self.glow.setPos(0, 17, -6.28)
        self.glow.setColor(1, 1, 1, 0.800000)
        self.setBin('gui-fixed', 4)
        self.accept('open_main_window', self.createBuffer)
        self.accept('aspectRatioChanged', self.createBuffer)
        self.accept('close_main_window', self.destroyBuffer)
        self.bind(DGG.ENTER, self.showDetails)
        self.bind(DGG.EXIT, self.hideDetails)


    def loadGui(self):
        if InventoryItemGui.guiLoaded:
            return None

        InventoryListItem.loadGui(self)
        InventoryItemGui.genericButton = (InventoryListItem.topGui.find('**/generic_button'), InventoryListItem.topGui.find('**/generic_button_down'), InventoryListItem.topGui.find('**/generic_button_over'), InventoryListItem.topGui.find('**/generic_button_disabled'))


    def createGui(self):
        itemId = self.data[0]
        self.nameTag = DirectLabel(parent = self, relief = None, state = DGG.DISABLED, text = self.name, text_scale = PiratesGuiGlobals.TextScaleSmall * PLocalizer.getHeadingScale(2), text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, pos = (0.16, 0, 0.105), text_font = PiratesGlobals.getInterfaceFont())
        if itemId in xrange(InventoryType.begin_PistolPouches, InventoryType.end_PistolPouches):
            self.itemTypeFormatted = PLocalizer.makeHeadingString(PLocalizer.InventoryItemClassNames.get(ItemType.PISTOL), 1)
        elif itemId in xrange(InventoryType.begin_DaggerPouches, InventoryType.end_DaggerPouches):
            self.itemTypeFormatted = PLocalizer.makeHeadingString(PLocalizer.InventoryItemClassNames.get(ItemType.DAGGER), 1)
        elif itemId in xrange(InventoryType.begin_GrenadePouches, InventoryType.end_GrenadePouches):
            self.itemTypeFormatted = PLocalizer.makeHeadingString(PLocalizer.GrenadeShort, 1)
        elif itemId in xrange(InventoryType.begin_CannonPouches, InventoryType.end_CannonPouches):
            self.itemTypeFormatted = PLocalizer.makeHeadingString(PLocalizer.ShipCannonShort, 1)
        else:
            self.itemTypeFormatted = PLocalizer.makeHeadingString(self.itemType, 1)
        self.itemTypeName = DirectLabel(parent = self, relief = None, state = DGG.DISABLED, text = self.itemTypeFormatted, text_scale = PiratesGuiGlobals.TextScaleSmall, text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getInterfaceFont(), pos = (0.16, 0, 0.065))
        self.miscText = DirectLabel(parent = self, relief = None, state = DGG.DISABLED, text = '', text_scale = PiratesGuiGlobals.TextScaleSmall, text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 11, pos = (0.16, 0, 0.0250))
        if self.minLvl > 0:
            repId = WeaponGlobals.getRepId(itemId)
            if repId:
                self.checkLevel(repId, self.minLvl)

        trainingReq = EconomyGlobals.getItemTrainingReq(itemId)
        if trainingReq:
            self.checkTrainingReq(trainingReq)

        if EconomyGlobals.getItemCategory(itemId) == ItemType.AMMO:
            skillId = WeaponGlobals.getSkillIdForAmmoSkillId(itemId)
            self.checkSkillReq(skillId)

        self.checkInfamyReq(itemId)
        if self.buy:
            self.checkPlayerInventory(itemId)

        self.costText = DirectLabel(parent = self, relief = None, state = DGG.DISABLED, image = InventoryListItem.coinImage, image_scale = 0.12, image_pos = Vec3(-0.01, 0, 0.01), text = str(self.price), text_scale = PiratesGuiGlobals.TextScaleSmall, text_align = TextNode.ARight, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 11, text_pos = (-0.0299, 0, 0), pos = (self.width - 0.035000, 0, 0.065), text_font = PiratesGlobals.getInterfaceFont())
        if self.quantity and self.quantity > 1:
            self.quantityLabel = DirectLabel(parent = self, relief = None, state = DGG.DISABLED, text = str(self.quantity), frameColor = (0, 0, 0, 1), frameSize = (-0.01, 0.02, -0.01, 0.0250), text_scale = 0.0275, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 11, pos = (0.02, 0, 0.0250), text_font = PiratesGlobals.getPirateBoldOutlineFont())

        geomParams = InventoryItemGui.getGeomParams(itemId)
        self.picture = DirectFrame(parent = self, relief = None, state = DGG.DISABLED, geom = geomParams['geom'], geom_pos = geomParams['geom_pos'], geom_scale = geomParams['geom_scale'], pos = (0.01, 0, 0.01))
        self.flattenStrong()


    def getGeomParams(itemId):
        geomParams = { }
        itemType = EconomyGlobals.getItemType(itemId)
        if itemType <= ItemType.WAND or itemType == ItemType.POTION:
            if itemType == ItemType.POTION:
                geomParams['geom'] = InventoryItemGui.skillIcons.find('**/%s' % ItemGlobals.getIcon(itemId))
            else:
                itemType = ItemGlobals.getType(itemId)
                if ItemGlobals.getIcon(itemId):
                    geomParams['geom'] = InventoryItemGui.weaponIcons.find('**/%s' % ItemGlobals.getIcon(itemId))

            geomParams['geom_scale'] = 0.11
            geomParams['geom_pos'] = (0.08, 0, 0.0680000)
        else:
            itemClass = EconomyGlobals.getItemCategory(itemId)
            itemType = EconomyGlobals.getItemType(itemId)
            if itemType == ItemType.FISHING_ROD or itemType == ItemType.FISHING_LURE:
                asset = EconomyGlobals.getItemIcons(itemId)
                if asset:
                    geomParams['geom'] = InventoryItemGui.fishingIcons.find('**/%s*' % asset)
                    geomParams['geom_scale'] = 0.11
                    geomParams['geom_pos'] = (0.08, 0, 0.0680000)

            elif itemClass == ItemType.WEAPON and itemClass == ItemType.POUCH or itemClass == ItemType.AMMO:
                asset = EconomyGlobals.getItemIcons(itemId)
                if asset:
                    geomParams['geom'] = InventoryItemGui.weaponIcons.find('**/%s*' % asset)
                    geomParams['geom_scale'] = 0.11
                    geomParams['geom_pos'] = (0.08, 0, 0.0680000)

            elif itemClass == ItemType.CONSUMABLE:
                asset = EconomyGlobals.getItemIcons(itemId)
                if asset:
                    geomParams['geom'] = InventoryItemGui.skillIcons.find('**/%s*' % asset)
                    geomParams['geom_scale'] = 0.11
                    geomParams['geom_pos'] = (0.08, 0, 0.0680000)


        if not InventoryType.begin_WeaponCannonAmmo <= itemId or itemId <= InventoryType.end_WeaponCannonAmmo:
            if (InventoryType.begin_WeaponPistolAmmo <= itemId or itemId <= InventoryType.end_WeaponGrenadeAmmo or InventoryType.begin_WeaponDaggerAmmo <= itemId) and itemId <= InventoryType.end_WeaponDaggerAmmo:
                skillId = WeaponGlobals.getSkillIdForAmmoSkillId(itemId)
                if skillId:
                    asset = WeaponGlobals.getSkillIcon(skillId)
                    if asset:
                        geomParams['geom'] = InventoryListItem.skillIcons.find('**/%s' % asset)
                        geomParams['geom_scale'] = 0.149
                        geomParams['geom_pos'] = (0.069, 0, 0.069)


            elif InventoryType.SmallBottle <= itemId and itemId <= InventoryType.LargeBottle:
                geomParams['geom'] = InventoryListItem.topGui.find('**/main_gui_ship_bottle')
                geomParams['geom_scale'] = 0.100
                geomParams['geom_pos'] = (0.069, 0, 0.069)

        return geomParams

    getGeomParams = staticmethod(getGeomParams)

    def checkLevel(self, repId, minLvl):
        inv = localAvatar.getInventory()
        if inv:
            repAmt = inv.getAccumulator(repId)
            if minLvl > ReputationGlobals.getLevelFromTotalReputation(repId, repAmt)[0]:
                self.highlightRed(PLocalizer.LevelRequirement % self.minLvl + ' ' + PLocalizer.InventoryItemClassNames.get(EconomyGlobals.getItemType(self.data[0])))




    def checkTrainingReq(self, trainingReq):
        inv = localAvatar.getInventory()
        if inv:
            amt = inv.getStackQuantity(trainingReq)
            if not amt:
                self.highlightRed(PLocalizer.TrainingRequirement)




    def checkSkillReq(self, skillId):
        if skillId in xrange(InventoryType.begin_FishingLures, InventoryType.end_FishingLures):
            return None

        if skillId:
            if base.localAvatar.getSkillQuantity(skillId) < 2:
                skillName = PLocalizer.getInventoryTypeName(skillId)
                self.highlightRed(PLocalizer.SkillRequirement % skillName)




    def checkInfamyReq(self, itemId):
        landInfamyLevel = ItemGlobals.getLandInfamyRequirement(itemId)
        seaInfamyLevel = ItemGlobals.getSeaInfamyRequirement(itemId)
        if landInfamyLevel and TitleGlobals.getRank(TitleGlobals.LandPVPTitle, localAvatar.getInfamyLand()) < landInfamyLevel:
            self.highlightRed(PLocalizer.LandInfamyRequirement % landInfamyLevel)

        if seaInfamyLevel and TitleGlobals.getRank(TitleGlobals.ShipPVPTitle, localAvatar.getInfamySea()) < seaInfamyLevel:
            self.highlightRed(PLocalizer.SeaInfamyRequirement % seaInfamyLevel)



    def checkPlayerInventory(self, itemId, extraQty = 0):
        if self.available:
            itemCategory = EconomyGlobals.getItemCategory(itemId)
            inventory = base.localAvatar.getInventory()
            currStock = inventory.getStackQuantity(itemId)
            currStockLimit = inventory.getStackLimit(itemId)
            if itemCategory == ItemType.AMMO or itemCategory == ItemType.CONSUMABLE:
                if currStock + extraQty >= currStockLimit and currStockLimit > 0:
                    self.highlightGreen(PLocalizer.InventoryFull % currStockLimit)
                else:
                    self.highlightBox(PLocalizer.InventoryCurrent % (currStock + extraQty, currStockLimit), Vec4(1, 1, 1, 1), PiratesGuiGlobals.TextFG2)
            elif itemCategory == ItemType.WEAPON:
                if currStock >= 1:
                    self.highlightGreen(PLocalizer.InventoryOwned)
                else:
                    inv = base.localAvatar.getInventory()
                    if inv is None:
                        return None

                    itemRep = WeaponGlobals.getRepId(itemId)
                    if itemRep == InventoryType.CutlassRep:
                        options = [
                            InventoryType.CutlassWeaponL1,
                            InventoryType.CutlassWeaponL2,
                            InventoryType.CutlassWeaponL3,
                            InventoryType.CutlassWeaponL4,
                            InventoryType.CutlassWeaponL5,
                            InventoryType.CutlassWeaponL6]
                    elif itemRep == InventoryType.PistolRep:
                        options = [
                            InventoryType.PistolWeaponL1,
                            InventoryType.PistolWeaponL2,
                            InventoryType.PistolWeaponL3,
                            InventoryType.PistolWeaponL4,
                            InventoryType.PistolWeaponL5,
                            InventoryType.PistolWeaponL6]
                    elif itemRep == InventoryType.DaggerRep:
                        options = [
                            InventoryType.DaggerWeaponL1,
                            InventoryType.DaggerWeaponL2,
                            InventoryType.DaggerWeaponL3,
                            InventoryType.DaggerWeaponL4,
                            InventoryType.DaggerWeaponL5,
                            InventoryType.DaggerWeaponL6]
                    elif itemRep == InventoryType.GrenadeRep:
                        options = [
                            InventoryType.GrenadeWeaponL1,
                            InventoryType.GrenadeWeaponL2,
                            InventoryType.GrenadeWeaponL3,
                            InventoryType.GrenadeWeaponL4,
                            InventoryType.GrenadeWeaponL5,
                            InventoryType.GrenadeWeaponL6]
                    elif itemRep == InventoryType.DollRep:
                        options = [
                            InventoryType.DollWeaponL1,
                            InventoryType.DollWeaponL2,
                            InventoryType.DollWeaponL3,
                            InventoryType.DollWeaponL4,
                            InventoryType.DollWeaponL5,
                            InventoryType.DollWeaponL6]
                    elif itemRep == InventoryType.WandRep:
                        options = [
                            InventoryType.WandWeaponL1,
                            InventoryType.WandWeaponL2,
                            InventoryType.WandWeaponL3,
                            InventoryType.WandWeaponL4,
                            InventoryType.WandWeaponL5,
                            InventoryType.WandWeaponL6]
                    else:
                        return None
                    for idx in xrange(len(options)):
                        optionId = options[idx]
                        if optionId == itemId:
                            currIdx = idx
                            for weaponId in options[currIdx:]:
                                if weaponId == itemId:
                                    continue

                                stackAmt = inv.getStackQuantity(weaponId)
                                if stackAmt >= 1:
                                    self.highlightRed(PLocalizer.InventoryLowLevel)
                                    return None
                                    continue


            elif itemCategory == ItemType.POUCH:
                inv = base.localAvatar.getInventory()
                if currStock >= 1:
                    self.highlightGreen(PLocalizer.InventoryOwned)
                else:
                    pistolPouches = [
                        InventoryType.PistolPouchL1,
                        InventoryType.PistolPouchL2,
                        InventoryType.PistolPouchL3]
                    daggerPouches = [
                        InventoryType.DaggerPouchL1,
                        InventoryType.DaggerPouchL2,
                        InventoryType.DaggerPouchL3]
                    grenadePouches = [
                        InventoryType.GrenadePouchL1,
                        InventoryType.GrenadePouchL2,
                        InventoryType.GrenadePouchL3]
                    cannonPouches = [
                        InventoryType.CannonPouchL1,
                        InventoryType.CannonPouchL2,
                        InventoryType.CannonPouchL3]
                    if itemId in pistolPouches:
                        pouchSet = pistolPouches
                    elif itemId in daggerPouches:
                        pouchSet = daggerPouches
                    elif itemId in grenadePouches:
                        pouchSet = grenadePouches
                    elif itemId in cannonPouches:
                        pouchSet = cannonPouches
                    else:
                        pouchSet = []
                    for pouchIdx in xrange(len(pouchSet)):
                        if pouchSet[pouchIdx] == itemId and pouchIdx + 1 < len(pouchSet):
                            for higherPouchIdx in xrange(pouchIdx + 1, len(pouchSet)):
                                stackAmt = inv.getStackQuantity(pouchSet[higherPouchIdx])
                                if stackAmt >= 1:
                                    self.highlightRed(PLocalizer.InventoryLowLevel)
                                    return None
                                    continue






    def highlightRed(self, text = ''):
        self['state'] = DGG.DISABLED
        self['image_color'] = Vec4(0.550000, 0.550000, 0.5, 1)
        self.available = False
        self.highlightBox(text, Vec4(0.75, 0.5, 0.5, 1), PiratesGuiGlobals.TextFG6)


    def highlightGreen(self, text = ''):
        self.highlightBox(text, Vec4(0.5, 0.75, 0.5, 1), PiratesGuiGlobals.TextFG4)


    def highlightBox(self, text, image_color, text_fg):
        self.miscText['text_fg'] = text_fg
        if text != '':
            self.miscText['text'] = text



    def enable(self):
        if self.available:
            self['state'] = DGG.NORMAL



    def disable(self):
        if self.available:
            self['state'] = DGG.DISABLED



    def createHelpbox(self, args = None):
        if self.helpFrame:
            return None

        itemType = EconomyGlobals.getItemType(self.data[0])
        if itemType <= ItemType.WAND or itemType == ItemType.POTION:
            itemId = self.data[0]
            self.helpFrame = DirectFrame(parent = aspect2d, relief = None, state = DGG.DISABLED, sortOrder = 1)
            detailGui = loader.loadModel('models/gui/gui_card_detail')
            topGui = loader.loadModel('models/gui/toplevel_gui')
            coinImage = topGui.find('**/treasure_w_coin*')
            self.SkillIcons = loader.loadModel('models/textureCards/skillIcons')
            self.BuffIcons = loader.loadModel('models/textureCards/buff_icons')
            border = self.SkillIcons.find('**/base')
            halfWidth = 0.299
            halfHeight = 0.200
            textScale = PiratesGuiGlobals.TextScaleMed
            titleScale = PiratesGuiGlobals.TextScaleTitleSmall
            titleNameScale = PiratesGuiGlobals.TextScaleExtraLarge
            subtitleScale = PiratesGuiGlobals.TextScaleMed
            iconScalar = 1.5
            borderScaler = 0.25
            splitHeight = 0.01
            vMargin = 0.0299
            runningVertPosition = 0.299
            runningSize = 0.0
            labels = []
            titleColor = PiratesGuiGlobals.TextFG6
            itemColor = 'itemRed'
            rarity = ItemGlobals.getRarity(itemId)
            rarityText = PLocalizer.getItemRarityName(rarity)
            subtypeText = PLocalizer.getItemSubtypeName(ItemGlobals.getSubtype(itemId))
            if rarity == ItemGlobals.CRUDE:
                titleColor = PiratesGuiGlobals.TextFG24
                itemColor = 'itemBrown'
            elif rarity == ItemGlobals.COMMON:
                titleColor = PiratesGuiGlobals.TextFG13
                itemColor = 'itemYellow'
            elif rarity == ItemGlobals.RARE:
                titleColor = PiratesGuiGlobals.TextFG4
                itemColor = 'itemGreen'
            elif rarity == ItemGlobals.FAMED:
                titleColor = PiratesGuiGlobals.TextFG5
                itemColor = 'itemBlue'

            titleLabel = DirectLabel(parent = self, relief = None, text = PLocalizer.getItemName(itemId), text_scale = titleNameScale, text_fg = titleColor, text_shadow = PiratesGuiGlobals.TextShadow, text_align = TextNode.ACenter, pos = (0.0, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
            self.bg.setColor(titleColor)
            tHeight = 0.070
            titleLabel.setZ(runningVertPosition)
            runningVertPosition -= tHeight
            runningSize += tHeight
            labels.append(titleLabel)
            subtitleLabel = DirectLabel(parent = self, relief = None, text = '\x01slant\x01%s\x02 %s' % (rarityText, subtypeText), text_scale = subtitleScale, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_align = TextNode.ACenter, pos = (0.0, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
            subtHeight = 0.050000
            subtitleLabel.setZ(subtHeight * 0.5 + runningVertPosition)
            runningVertPosition -= subtHeight
            runningSize += subtHeight
            labels.append(subtitleLabel)
            itemType = ItemGlobals.getType(itemId)
            itemSubtype = ItemGlobals.getSubtype(itemId)
            model = ItemGlobals.getModel(itemId)
            if model:
                if itemType == ItemGlobals.GRENADE:
                    self.realItem = loader.loadModel('models/ammunition/' + model)
                elif itemType == ItemGlobals.POTION:
                    self.realItem = loader.loadModel('models/inventory/' + model)
                else:
                    self.realItem = loader.loadModel('models/handheld/' + model)
                if self.realItem:
                    spinBlur = self.realItem.find('**/motion_blur')
                    if spinBlur:
                        spinBlur.hide()

                    if itemSubtype == ItemGlobals.MUSKET:
                        bayonetPart = self.realItem.find('**/bayonet')
                        if bayonetPart:
                            bayonetPart.stash()


                    posHpr = ItemGlobals.getModelPosHpr(model)
                    if posHpr:
                        self.realItem.setPos(posHpr[0], posHpr[1], posHpr[2])
                        self.realItem.setHpr(posHpr[3], posHpr[4], posHpr[5])
                    elif itemType == ItemGlobals.SWORD:
                        self.realItem.setPos(-1.5, 3.0, -0.299)
                        self.realItem.setHpr(90, 170, -90)
                    elif itemSubtype in (ItemGlobals.MUSKET, ItemGlobals.BAYONET):
                        self.realItem.setPos(-1.2, 3.0, -0.100)
                        self.realItem.setHpr(0, 135, 10)
                    elif itemSubtype == ItemGlobals.BLUNDERBUSS:
                        self.realItem.setPos(-0.299, 2.0, 0.0)
                        self.realItem.setHpr(0, 90, 0)
                    elif itemType == ItemGlobals.GUN:
                        self.realItem.setPos(-0.5, 2.0, -0.200)
                        self.realItem.setHpr(0, 90, 0)
                    elif itemType == ItemGlobals.DOLL:
                        self.realItem.setPos(0.0, 1.89, -0.100)
                        self.realItem.setHpr(0, 90, 180)
                    elif itemType == ItemGlobals.DAGGER:
                        self.realItem.setPos(-1.0, 2.0, -0.299)
                        self.realItem.setHpr(90, 170, -90)
                    elif itemType == ItemGlobals.GRENADE:
                        self.realItem.setPos(0.0, 3.5, -0.200)
                        self.realItem.setHpr(0, 0, 0)
                    elif itemType == ItemGlobals.STAFF:
                        self.realItem.setPos(-0.4, 3.0, -0.299)
                        self.realItem.setHpr(-90, 15, -90)
                    elif itemSubtype == ItemGlobals.RAM:
                        self.realItem.setPos(-1.5, 1.5, -0.598)
                        self.realItem.setHpr(70, 160, -90)
                    elif itemType == ItemGlobals.POTION:
                        self.realItem.setPos(0.0, 2.5, -0.4)
                        self.realItem.setHpr(45, 0, 0)
                    else:
                        self.realItem.setPos(0.0, 1.5, -0.0598)
                        self.realItem.setHpr(0, 90, 0)
                    self.realItem.reparentTo(self.portraitSceneGraph)


            iHeight = 0.174
            self.createBuffer()
            self.itemCard.setZ(runningVertPosition - 0.0598)
            runningVertPosition -= iHeight
            runningSize += iHeight
            labels.append(self.itemCard)
            goldLabel = DirectLabel(parent = self, relief = None, image = coinImage, image_scale = 0.12, image_pos = Vec3(0.0250, 0, -0.02), text = str(int(ItemGlobals.getGoldCost(itemId) * ItemGlobals.GOLD_SALE_MULTIPLIER)), text_scale = subtitleScale, text_align = TextNode.ARight, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, pos = (halfWidth - 0.050000, 0.0, runningVertPosition + 0.08), text_pos = (0.0, -textScale))
            labels.append(goldLabel)
            infoText = PLocalizer.ItemAttackStrength % '\x01%s\x01%s\x02' % (itemColor, ItemGlobals.getPower(itemId))
            if itemType == ItemGlobals.GUN:
                infoText += '     %s' % PLocalizer.ItemBarrels % '\x01%s\x01%s\x02' % (itemColor, ItemGlobals.getBarrels(itemId))
                infoText += '     %s' % PLocalizer.ItemRangeStrength % '\x01%s\x01%s\x02' % (itemColor, PLocalizer.getItemRangeName(WeaponGlobals.getRange(itemId)))

            if itemType != ItemGlobals.POTION:
                infoLabel = DirectLabel(parent = self, relief = None, text = infoText, text_scale = textScale, text_align = TextNode.ACenter, pos = (0.0, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                iHeight = 0.08
                runningVertPosition -= iHeight
                runningSize += iHeight
                labels.append(infoLabel)

            specialAttack = None
            if itemType != ItemGlobals.POTION:
                specialAttack = ItemGlobals.getSpecialAttack(itemId)

            if specialAttack:
                attackIcon = self.SkillIcons.find('**/%s' % WeaponGlobals.getSkillIcon(specialAttack))
                specialAttackNameLabel = DirectLabel(parent = self, relief = None, image = border, image_scale = 0.100, geom = attackIcon, geom_scale = 0.100, image_pos = (-0.070, 0.0, -0.050000), geom_pos = (-0.070, 0.0, -0.050000), text = PLocalizer.getInventoryTypeName(specialAttack), text_scale = PiratesGuiGlobals.TextScaleLarge, text_wordwrap = halfWidth * 2.0 * (0.9 / titleScale), text_align = TextNode.ALeft, text_fg = titleColor, text_font = PiratesGlobals.getInterfaceOutlineFont(), text_shadow = PiratesGuiGlobals.TextShadow, pos = (-halfWidth + 0.12 + textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                specialAttackRankLabel = DirectLabel(parent = self, relief = None, text = PLocalizer.ItemRank % ItemGlobals.getSpecialAttackRank(itemId), text_scale = textScale, text_wordwrap = halfWidth * 2.0 * (0.9 / titleScale), text_align = TextNode.ARight, pos = (halfWidth - textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                specialAttackType = WeaponGlobals.getSkillTrack(specialAttack)
                if specialAttackType == WeaponGlobals.BREAK_ATTACK_SKILL_INDEX:
                    specialAttackTypeText = PLocalizer.BreakAttackSkill
                elif specialAttackType == WeaponGlobals.DEFENSE_SKILL_INDEX:
                    specialAttackTypeText = PLocalizer.DefenseSkill
                else:
                    specialAttackTypeText = PLocalizer.WeaponSkill
                specialAttackTypeLabel = DirectLabel(parent = self, relief = None, text = specialAttackTypeText, text_scale = 0.0335, text_wordwrap = halfWidth * 2.78 * (0.9 / titleScale), text_align = TextNode.ALeft, pos = (-halfWidth + 0.12 + textScale * 0.5, 0.0, runningVertPosition - PiratesGuiGlobals.TextScaleLarge), text_pos = (0.0, -textScale))
                specialAttackInfo = PLocalizer.SkillDescriptions.get(specialAttack)
                specialAttackDescriptionText = specialAttackInfo[1]
                specialAttackDescriptionLabel = DirectLabel(parent = self, relief = None, text = specialAttackDescriptionText, text_scale = textScale, text_wordwrap = halfWidth * 2.78 * (0.9 / titleScale), text_align = TextNode.ALeft, pos = (-halfWidth + 0.12 + textScale * 0.5, 0.0, runningVertPosition - specialAttackNameLabel.getHeight() + specialAttackTypeLabel.getHeight() - 0.0598), text_pos = (0.0, -textScale))
                saHeight = specialAttackNameLabel.getHeight() + specialAttackTypeLabel.getHeight() + specialAttackDescriptionLabel.getHeight() - 0.0400
                runningVertPosition -= saHeight
                runningSize += saHeight
                labels.append(specialAttackNameLabel)
                labels.append(specialAttackRankLabel)
                labels.append(specialAttackTypeLabel)
                labels.append(specialAttackDescriptionLabel)

            attributes = ItemGlobals.getAttributes(itemId)
            for i in xrange(0, len(attributes)):
                attributeIcon = self.SkillIcons.find('**/%s' % ItemGlobals.getAttributeIcon(attributes[i][0]))
                if not attributeIcon:
                    attributeIcon = self.BuffIcons.find('**/%s' % ItemGlobals.getAttributeIcon(attributes[i][0]))

                attributeNameLabel = DirectLabel(parent = self, relief = None, image = border, image_scale = 0.050000, geom = attributeIcon, geom_scale = 0.050000, image_pos = (-0.070, 0.0, -0.0299), geom_pos = (-0.070, 0.0, -0.0299), text = PLocalizer.getItemAttributeName(attributes[i][0]), text_scale = PiratesGuiGlobals.TextScaleLarge, text_wordwrap = halfWidth * 2.0 * (0.9 / titleScale), text_align = TextNode.ALeft, text_fg = titleColor, text_font = PiratesGlobals.getInterfaceOutlineFont(), text_shadow = PiratesGuiGlobals.TextShadow, pos = (-halfWidth + 0.12 + textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                attributeRankLabel = DirectLabel(parent = self, relief = None, text = PLocalizer.ItemRank % attributes[i][1], text_scale = textScale, text_wordwrap = halfWidth * 2.0 * (0.9 / titleScale), text_align = TextNode.ARight, pos = (halfWidth - textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                if attributeNameLabel.getHeight() > 0.074:
                    attributeNameSpace = 0.08
                else:
                    attributeNameSpace = PiratesGuiGlobals.TextScaleLarge
                attributeDescriptionLabel = DirectLabel(parent = self, relief = None, text = PLocalizer.getItemAttributeDescription(attributes[i][0]), text_scale = textScale, text_wordwrap = halfWidth * 2.78 * (0.9 / titleScale), text_align = TextNode.ALeft, pos = (-halfWidth + 0.12 + textScale * 0.5, 0.0, runningVertPosition - attributeNameSpace), text_pos = (0.0, -textScale))
                aHeight = attributeNameLabel.getHeight() + attributeDescriptionLabel.getHeight()
                runningVertPosition -= aHeight + splitHeight
                runningSize += aHeight + splitHeight
                labels.append(attributeNameLabel)
                labels.append(attributeRankLabel)
                labels.append(attributeDescriptionLabel)

            skillBoosts = ItemGlobals.getSkillBoosts(itemId)
            for i in xrange(0, len(skillBoosts)):
                boostIcon = self.SkillIcons.find('**/%s' % WeaponGlobals.getSkillIcon(skillBoosts[i][0]))
                boostNameLabel = DirectLabel(parent = self, relief = None, image = border, image_scale = 0.050000, geom = boostIcon, geom_scale = 0.050000, image_pos = (-0.070, 0.0, -0.0299), geom_pos = (-0.070, 0.0, -0.0299), text = PLocalizer.ItemBoost % PLocalizer.getInventoryTypeName(skillBoosts[i][0]), text_scale = textScale, text_wordwrap = halfWidth * 2.0 * (0.9 / titleScale), text_align = TextNode.ALeft, pos = (-halfWidth + 0.12 + textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                boostRankLabel = DirectLabel(parent = self, relief = None, text = '+%s' % str(skillBoosts[i][1]), text_scale = textScale, text_wordwrap = halfWidth * 2.0 * (0.9 / titleScale), text_align = TextNode.ARight, pos = (halfWidth - textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                bHeight = boostNameLabel.getHeight()
                runningVertPosition -= bHeight + splitHeight
                runningSize += bHeight + splitHeight
                labels.append(boostNameLabel)
                labels.append(boostRankLabel)

            description = PLocalizer.getItemFlavorText(itemId)
            if description != '':
                descriptionLabel = DirectLabel(parent = self, relief = None, text = description, text_scale = textScale, text_wordwrap = halfWidth * 2.0 * (0.946 / textScale), text_align = TextNode.ALeft, pos = (-halfWidth + textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                dHeight = descriptionLabel.getHeight() + 0.02
                runningVertPosition -= dHeight
                runningSize += dHeight
                labels.append(descriptionLabel)

            inv = localAvatar.getInventory()
            weaponLevel = 0
            weaponRepId = WeaponGlobals.getRepId(itemId)
            weaponRep = inv.getReputation(weaponRepId)
            weaponReq = ItemGlobals.getWeaponRequirement(itemId)
            weaponText = None
            trainingToken = EconomyGlobals.getItemTrainingReq(itemId)
            trainingAmt = inv.getItemQuantity(trainingToken)
            if weaponReq:
                weaponLevel = ReputationGlobals.getLevelFromTotalReputation(weaponRepId, weaponRep)[0]
                if weaponLevel < weaponReq:
                    weaponColor = PiratesGuiGlobals.TextFG6
                else:
                    weaponColor = (0.4, 0.4, 0.4, 1.0)
                    weaponText = PLocalizer.ItemLevelRequirement % (weaponReq, PLocalizer.getItemTypeName(itemType))
            elif trainingAmt == 0:
                weaponColor = PiratesGuiGlobals.TextFG6
                weaponText = PLocalizer.ItemTrainingRequirement % PLocalizer.getItemTypeName(itemType)

            if trainingAmt == 0:
                if itemType == ItemGlobals.GUN:
                    base.localAvatar.sendRequestContext(InventoryType.GunTrainingRequired)
                elif itemType == ItemGlobals.DOLL:
                    base.localAvatar.sendRequestContext(InventoryType.DollTrainingRequired)
                elif itemType == ItemGlobals.DAGGER:
                    base.localAvatar.sendRequestContext(InventoryType.DaggerTrainingRequired)
                elif itemType == ItemGlobals.STAFF:
                    base.localAvatar.sendRequestContext(InventoryType.StaffTrainingRequired)


            if weaponText:
                weaponReqLabel = DirectLabel(parent = self, relief = None, text = weaponText, text_scale = textScale, text_wordwrap = halfWidth * 2.0 * (1.5 / titleScale), text_fg = weaponColor, text_shadow = PiratesGuiGlobals.TextShadow, text_align = TextNode.ACenter, pos = (0.0, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
                wHeight = weaponReqLabel.getHeight()
                runningVertPosition -= wHeight
                runningSize += wHeight
                labels.append(weaponReqLabel)

            runningVertPosition -= 0.02
            runningSize += 0.02
            panels = self.helpFrame.attachNewNode('panels')
            topPanel = panels.attachNewNode('middlePanel')
            detailGui.find('**/top_panel').copyTo(topPanel)
            topPanel.setScale(0.08)
            topPanel.reparentTo(self.helpFrame)
            middlePanel = panels.attachNewNode('middlePanel')
            detailGui.find('**/middle_panel').copyTo(middlePanel)
            middlePanel.setScale(0.08)
            middlePanel.reparentTo(self.helpFrame)
            placement = 0
            i = 0
            heightMax = -0.08
            currentHeight = runningVertPosition
            while currentHeight < heightMax:
                middlePanel = panels.attachNewNode('middlePanel%s' % 1)
                detailGui.find('**/middle_panel').copyTo(middlePanel)
                middlePanel.setScale(0.08)
                middlePanel.reparentTo(self.helpFrame)
                if currentHeight + 0.200 >= heightMax:
                    difference = heightMax - currentHeight
                    placement += (0.168 / 0.200) * difference
                    currentHeight += difference
                else:
                    placement += 0.168
                    currentHeight += 0.200
                middlePanel.setZ(-placement)
                i += 1
            bottomPanel = panels.attachNewNode('bottomPanel')
            detailGui.find('**/bottom_panel').copyTo(bottomPanel)
            bottomPanel.setScale(0.08)
            bottomPanel.setZ(-placement)
            bottomPanel.reparentTo(self.helpFrame)
            colorPanel = panels.attachNewNode('colorPanel')
            detailGui.find('**/color').copyTo(colorPanel)
            colorPanel.setScale(0.08)
            colorPanel.setColor(titleColor)
            colorPanel.reparentTo(self.helpFrame)
            lineBreakTopPanel = panels.attachNewNode('lineBreakTopPanel')
            detailGui.find('**/line_break_top').copyTo(lineBreakTopPanel)
            lineBreakTopPanel.setScale(0.08, 0.08, 0.070)
            lineBreakTopPanel.setZ(0.008)
            lineBreakTopPanel.reparentTo(self.helpFrame)
            if itemType != ItemGlobals.POTION:
                lineBreakBottomPanel = panels.attachNewNode('lineBreakBottomPanel')
                detailGui.find('**/line_break_bottom').copyTo(lineBreakBottomPanel)
                lineBreakBottomPanel.setScale(0.08, 0.08, 0.070)
                lineBreakBottomPanel.setZ(-0.0149)
                lineBreakBottomPanel.reparentTo(self.helpFrame)

            panels.flattenStrong()
            self.helpFrame['frameSize'] = (-halfWidth, halfWidth, -(runningSize + vMargin), vMargin)
            totalHeight = self.helpFrame.getHeight() - 0.100
            for label in labels:
                label.reparentTo(self.helpFrame)

            self.helpFrame.setBin('gui-fixed', 4)
            self.helpFrame.setPos(self, 0.550000, 0, -0.299)
            zOffset = -0.5 - self.helpFrame.getPos(aspect2d)[2]
            if zOffset >= 0.0:
                self.helpFrame.setPos(self, 0.550000, 0, zOffset - 0.299)

        else:
            weaponInfo = PLocalizer.WeaponDescriptions.get(self.data[0])
            weaponDesc = weaponInfo
            self.helpText = DirectFrame(parent = self, relief = None, text = weaponDesc, state = DGG.DISABLED, text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleSmall, text_fg = PiratesGuiGlobals.TextFG2, text_wordwrap = 13, textMayChange = 0, sortOrder = 91)
            height = -self.helpText.getHeight()
            self.helpFrame = BorderFrame(parent = aspect2d, state = DGG.DISABLED, frameSize = (-0.0299, 0.429, height, 0.050000), sortOrder = 90, borderScale = 0.200)
            self.helpText.reparentTo(self.helpFrame)
            self.helpFrame.setBin('gui-fixed', 4)
            self.helpFrame.setPos(self, 0.25, 0, -0.035000)


    def destroy(self):
        taskMgr.remove('helpInfoTask')
        taskMgr.remove(self.taskName('dragTask'))
        self.destroyBuffer()
        if self.itemCard:
            self.itemCard.remove_node()

        if self.realItem:
            self.realItem.remove_node()

        if self.helpFrame:
            self.helpFrame.destroy()
            self.helpFrame = None

        del self.picture
        if self.weapon:
            taskMgr.remove(DGG.B1PRESS)
            taskMgr.remove(DGG.B2PRESS)
            taskMgr.remove(DGG.B3PRESS)

        InventoryListItem.destroy(self)


    def setDraggable(self, d):
        self.draggable = d


    def dragStart(self, event):
        self.origionalPos = self.getPos(render2d)
        self.origionalParent = self.getParent()
        self.bringToFront()
        self.setColorScale(1, 1, 1, 0.5)
        if self.draggable:
            self.wrtReparentTo(aspect2d)
            taskMgr.remove(self.taskName('dragTask'))
            vWidget2render2d = self.getPos(render2d)
            vMouse2render2d = Point3(event.getMouse()[0], 0, event.getMouse()[1])
            editVec = Vec3(vWidget2render2d - vMouse2render2d)
            task = taskMgr.add(self.dragTask, self.taskName('dragTask'))
            task.editVec = editVec



    def dragTask(self, task):
        if task.time < PiratesGuiGlobals.DragStartDelayTime:
            return Task.cont
        else:
            mwn = base.mouseWatcherNode
            if mwn.hasMouse():
                vMouse2render2d = Point3(mwn.getMouse()[0], 0, mwn.getMouse()[1])
                newPos = vMouse2render2d + task.editVec
                self.setPos(render2d, newPos)
                newPos = self.getPos(aspect2d)
                x = newPos[0]
                z = newPos[2]
                x = x - x % 0.050000
                z = z - z % 0.050000
                x = min(1.3 - self.width, max(-1.3, x))
                z = min(1 - self.height, max(-1, z))
                self.setPos(aspect2d, x, 0.0, z)

            return Task.cont


    def dragStop(self, event):
        self.clearColorScale()
        self.wrtReparentTo(self.origionalParent)
        self.setPos(render2d, self.origionalPos)
        if self.draggable:
            taskMgr.remove(self.taskName('dragTask'))



    def showDetails(self, event):
        taskMgr.doMethodLater(PiratesGuiGlobals.HelpPopupTime, self.createHelpbox, 'helpInfoTask')
        self.createHelpbox()


    def hideDetails(self, event):
        taskMgr.remove('helpInfoTask')
        if self.helpFrame:
            self.helpFrame.destroy()
            self.helpFrame = None



    def createBuffer(self):
        self.destroyBuffer()
        self.buffer = base.win.makeTextureBuffer('par', 256, 256)
        self.buffer.setOneShot(True)
        self.cam = base.makeCamera(win = self.buffer, scene = self.portraitSceneGraph, clearColor = Vec4(1), lens = self.lens)
        self.cam.node().getDisplayRegion(0).setIncompleteRender(False)
        self.cam.reparentTo(self.portraitSceneGraph)
        self.bg.reparentTo(self.cam)
        self.glow.reparentTo(self.cam)
        if self.itemCard:
            self.itemCard.remove_node()

        tex = self.buffer.getTexture()
        self.itemCard = NodePath(self.cm.generate())
        self.itemCard.setTexture(tex, 1)
        if self.helpFrame:
            self.itemCard.reparentTo(self.helpFrame)



    def destroyBuffer(self):
        if self.buffer:
            base.graphicsEngine.removeWindow(self.buffer)
            self.buffer = None
            self.bg.detachNode()
            self.glow.detachNode()
            self.cam.remove_node()
            self.cam = None
