from panda3d.core import TextNode
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import *
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui import ShipItemList
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui import GuiPanel
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import GuiButton
from pirates.piratesgui import DialogButton
from pirates.piratesgui import BarChart
from pirates.uberdog.UberDogGlobals import *
from pirates.economy.EconomyGlobals import *
from pirates.economy import EconomyGlobals
from pirates.ship import ShipGlobals
from pirates.piratesgui import NamePanelGui
from pirates.inventory import InventoryGlobals

class ShipStoreGUI(GuiPanel.GuiPanel):
    notify = directNotify.newCategory('ShipStoreGUI')
    width = (PiratesGuiGlobals.InventoryItemGuiWidth + PiratesGuiGlobals.ScrollbarSize + 0.06) * 2
    height = 1.35
    columnWidth = PiratesGuiGlobals.InventoryItemGuiWidth + PiratesGuiGlobals.ScrollbarSize + 0.05
    ShipIconTable = {
        ItemId.INTERCEPTOR_L1: 'Interceptor_Render',
        ItemId.INTERCEPTOR_L2: 'Interceptor_Render',
        ItemId.INTERCEPTOR_L3: 'Interceptor_Render',
        ItemId.MERCHANT_L1: 'Merchant_Render',
        ItemId.MERCHANT_L2: 'Merchant_Render',
        ItemId.MERCHANT_L3: 'Merchant_Render',
        ItemId.WARSHIP_L1: 'Warship_Render',
        ItemId.WARSHIP_L2: 'Warship_Render',
        ItemId.WARSHIP_L3: 'Warship_Render',
        ItemId.SHIP_OF_THE_LINE: 'Warship_Render',
        ItemId.EL_PATRONS_SHIP: 'Warship_Render',
        ItemId.P_SKEL_PHANTOM: 'Warship_Render',
        ItemId.P_SKEL_REVENANT: 'Warship_Render',
        ItemId.P_SKEL_CEREBUS: 'Warship_Render',
        ItemId.P_NAVY_KINGFISHER: 'Warship_Render',
        ItemId.P_EITC_WARLORD: 'Warship_Render',
        ItemId.HMS_VICTORY: 'Warship_Render',
        ItemId.HMS_NEWCASTLE: 'Warship_Render',
        ItemId.HMS_INVINCIBLE: 'Warship_Render',
        ItemId.EITC_INTREPID: 'Warship_Render',
        ItemId.EITC_CONQUERER: 'Warship_Render',
        ItemId.EITC_LEVIATHAN: 'Warship_Render',
        ItemId.NAVY_FERRET: 'Warship_Render',
        ItemId.NAVY_BULWARK: 'Warship_Render',
        ItemId.NAVY_PANTHER: 'Warship_Render',
        ItemId.NAVY_GREYHOUND: 'Warship_Render',
        ItemId.NAVY_VANGUARD: 'Warship_Render',
        ItemId.NAVY_CENTURION: 'Warship_Render',
        ItemId.NAVY_KINGFISHER: 'Warship_Render',
        ItemId.NAVY_MONARCH: 'Warship_Render',
        ItemId.NAVY_MAN_O_WAR: 'Warship_Render',
        ItemId.NAVY_PREDATOR: 'Warship_Render',
        ItemId.NAVY_COLOSSUS: 'Warship_Render',
        ItemId.NAVY_DREADNOUGHT: 'Warship_Render',
        ItemId.NAVY_BASTION: 'Warship_Render',
        ItemId.NAVY_ELITE: 'Warship_Render',
        ItemId.EITC_SEA_VIPER: 'Warship_Render',
        ItemId.EITC_SENTINEL: 'Warship_Render',
        ItemId.EITC_CORVETTE: 'Warship_Render',
        ItemId.EITC_BLOODHOUND: 'Warship_Render',
        ItemId.EITC_IRONWALL: 'Warship_Render',
        ItemId.EITC_MARAUDER: 'Warship_Render',
        ItemId.EITC_BARRACUDA: 'Warship_Render',
        ItemId.EITC_OGRE: 'Warship_Render',
        ItemId.EITC_WARLORD: 'Warship_Render',
        ItemId.EITC_CORSAIR: 'Warship_Render',
        ItemId.EITC_BEHEMOTH: 'Warship_Render',
        ItemId.EITC_JUGGERNAUT: 'Warship_Render',
        ItemId.EITC_TYRANT: 'Warship_Render',
        ItemId.SKEL_PHANTOM: 'Warship_Render',
        ItemId.SKEL_REVENANT: 'Warship_Render',
        ItemId.SKEL_STORM_REAPER: 'Warship_Render',
        ItemId.SKEL_BLACK_HARBINGER: 'Warship_Render',
        ItemId.SKEL_DEATH_OMEN: 'Warship_Render',
        ItemId.SKEL_SHADOW_CROW_FR: 'Warship_Render',
        ItemId.SKEL_HELLHOUND_FR: 'Warship_Render',
        ItemId.SKEL_BLOOD_SCOURGE_FR: 'Warship_Render',
        ItemId.SKEL_SHADOW_CROW_SP: 'Warship_Render',
        ItemId.SKEL_HELLHOUND_SP: 'Warship_Render',
        ItemId.SKEL_BLOOD_SCOURGE_SP: 'Warship_Render',
        ItemId.HUNTER_VENGENCE: 'Warship_Render',
        ItemId.HUNTER_TALLYHO: 'Warship_Render' }

    def __init__(self, inventory, name):
        GuiPanel.GuiPanel.__init__(self, name, self.width, self.height, showClose = False)
        self.setPos(-1.25, 0, -0.66)
        self.initialiseoptions(ShipStoreGUI)
        self.balance = 0
        self.purchaseInventory = [
            [
                ItemId.INTERCEPTOR_L1,
                1]]
        self.sellInventory = []
        self.statData = []
        self.namePanel = None
        self.updateStats()
        self.storeInventory = ShipItemList.ShipItemList(inventory, self.height - 0.1, buy = PiratesGuiGlobals.InventoryAdd)
        self.storeInventory.reparentTo(self)
        self.storeInventory.setPos(0.02, 0, 0.02)
        self.purchaseTitle = DirectFrame(parent = self, relief = None, text = PLocalizer.InventoryTypeNames[self.purchaseInventory[0][0]], text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleLarge, text_pos = (0.03, 0.01), text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1)
        self.purchaseTitle.setPos(self.storeInventory.width, 0, 0.707 + (self.height - 0.065) / 2.5)
        self.card = loader.loadModel('models/textureCards/shipRenders')
        self.shipImage = DirectFrame(parent = self, relief = DGG.FLAT, image_scale = 0.2, frameColor = (0, 0, 0, 1.0), borderWidth = PiratesGuiGlobals.BorderWidthSmall, pad = (0.01, 0.01), frameSize = (-0.26, 0.26, -0.185, 0.185), textMayChange = 1, pos = (self.width * 0.72, 0, 1))
        self.shipImage.setTransparency(1)
        barChartWidth = self.width - self.storeInventory.width + 0.04
        self.shipStats = BarChart.BarChart(self.statData, 0.25, barChartWidth, PLocalizer.ShipProfile, PiratesGuiGlobals.TextFG1)
        self.shipStats.reparentTo(self)
        self.shipStats.setPos(self.storeInventory.width + 0.03, 0, 0.12)
        self.descText = DirectFrame(parent = self, relief = None, text = PLocalizer.ShipDescriptions[self.purchaseInventory[0][0]], text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleMed, text_pos = (0.03, 0.01), text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, frameColor = (0, 0, 0, 0), frameSize = (0.02, self.width - self.storeInventory.width - 0.02, 0, 0.05), textMayChange = 1, text_wordwrap = 18, pos = (self.storeInventory.width, 0, 0.75))
        self.balanceTitle = DirectFrame(parent = self, relief = None, text = PLocalizer.Cost, text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleLarge, text_pos = (0.31, 0.411), text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 0, pos = (self.columnWidth, 0, -0.01))
        self.goldTitle = DirectFrame(parent = self, relief = None, text = '%s:' % PLocalizer.MoneyName, text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleLarge, text_pos = (0.31, 0.411), text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 0, pos = (self.columnWidth, 0, 0.04))
        coinImage = loader.loadModel('models/gui/toplevel_gui').find('**/treasure_w_coin*')
        self.balanceValue = DirectFrame(parent = self, relief = None, text = str(self.balance), text_align = TextNode.ARight, text_scale = PiratesGuiGlobals.TextScaleLarge, text_pos = (0.53, 0.411), text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1, image = coinImage, image_scale = 0.15, image_pos = (0.56, 0, 0.425), pos = (self.columnWidth, 0, -0.01))
        self.goldValue = DirectFrame(parent = self, relief = None, text = str(localAvatar.getMoney()), text_align = TextNode.ARight, text_scale = PiratesGuiGlobals.TextScaleLarge, text_pos = (0.53, 0.411), text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 0, image = coinImage, image_scale = 0.15, image_pos = (0.56, 0, 0.425), pos = (self.columnWidth, 0, 0.04))
        coinImage.remove_node()
        self.commitButton = DialogButton.DialogButton(command = self.handleCommitPurchase, buttonStyle = DialogButton.DialogButton.YES, parent = self, relief = None, text = PLocalizer.PurchaseCommit, text_fg = PiratesGuiGlobals.TextFG2, text_scale = PiratesGuiGlobals.TextScaleLarge, textMayChange = 0, pos = (self.width - 0.39, 0, 0.07), sortOrder = 0)
        self.closeButton = DialogButton.DialogButton(command = self.closePanel, buttonStyle = DialogButton.DialogButton.NO, parent = self, relief = None, text = PLocalizer.lClose, text_fg = PiratesGuiGlobals.TextFG2, text_scale = PiratesGuiGlobals.TextScaleLarge, textMayChange = 0, pos = (self.width - 0.145, 0, 0.07))
        self.updateProfile()
        self.accept(InventoryGlobals.getCategoryChangeMsg(localAvatar.getInventoryId(), InventoryType.ItemTypeMoney), self.updateBalance)
        self.accept(PiratesGuiGlobals.InventoryBuyEvent, self.handleBuyItem)
        self.accept(PiratesGuiGlobals.InventorySellEvent, self.handleSellItem)
        self.acceptOnce('escape', self.closePanel)
        base.ssg = self


    def updateProfile(self):
        imageName = self.ShipIconTable.get(self.purchaseInventory[0][0])
        myTexCard = self.card.find('**/' + imageName + '*')
        myTex = myTexCard.findAllTextures()[0]
        self.purchaseTitle['text'] = PLocalizer.InventoryTypeNames[self.purchaseInventory[0][0]]
        self.descText['text'] = (PLocalizer.ShipDescriptions[self.purchaseInventory[0][0]],)
        self.shipImage['image'] = myTex
        self.shipImage['image_scale'] = 0.25
        self.updateStats()
        self.shipStats.refreshBars(self.statData)
        self.updateBalance()

    def updateStats(self):
        self.statData = []
        stats = ShipGlobals.getShipConfig(self.purchaseInventory[0][0])
        maxStats = ShipGlobals.getMaxShipStats()
        self.statData.append([
            PLocalizer.Hull,
            stats['hp'],
            maxStats['hp']])
        self.statData.append([
            PLocalizer.Speed,
            int(stats['sp'] / 10),
            4 + maxStats['sp'] / 10])
        self.statData.append([
            PLocalizer.Speed,
            int(stats['maxSpeed'] / 10),
            4 + maxStats['maxSpeed'] / 10])
        self.statData.append([
            PLocalizer.Cannon,
            stats['maxCannons'],
            maxStats['maxCannons']])
        self.statData.append([
            PLocalizer.Broadsides,
            stats['maxBroadsides'],
            maxStats['maxBroadsides']])
        self.statData.append([
            PLocalizer.Cargo,
            stats['maxCargo'],
            maxStats['maxCargo']])
        self.statData.append([
            PLocalizer.Crew,
            stats['maxCrew'],
            maxStats['maxCrew']])


    def closePanel(self):
        if self.namePanel:
            self.namePanel.destroy()
            self.namePanel = None

        if self.card:
            self.card.remove_node()

        messenger.send('exitStore')
        self.ignoreAll()


    def handleBuyItem(self, data, useCode):
        if useCode == PiratesGuiGlobals.InventoryAdd:
            self.purchaseInventory = [
                data]
            self.updateProfile()
        elif useCode == PiratesGuiGlobals.InventoryRemove:
            pass



    def handleSellItem(self, data, useCode):
        self.updateBalance()


    def handleCommitPurchase(self):
        if self.purchaseInventory == [] and self.sellInventory == []:
            base.localAvatar.guiMgr.createWarning(PLocalizer.EmptyPurchaseWarning, PiratesGuiGlobals.TextFG6)
            return None

        inventory = base.localAvatar.getInventory()
        if inventory:
            if inventory.getGoldInPocket() < self.balance:
                base.localAvatar.guiMgr.createWarning(PLocalizer.NotEnoughMoneyWarning, PiratesGuiGlobals.TextFG6)
                return None

            if self.balance < 0 and inventory.getGoldInPocket() + self.balance > InventoryGlobals.GOLD_CAP:
                base.localAvatar.guiMgr.createWarning(PLocalizer.CannotHoldGoldWarning, PiratesGuiGlobals.TextFG6)
                return None

            if len(inventory.getShipDoIdList()) >= inventory.getCategoryLimit(InventoryCategory.SHIPS):
                base.localAvatar.guiMgr.createWarning(PLocalizer.CannotHoldShipWarning, PiratesGuiGlobals.TextFG6)
                return None


        nameData = [
            PLocalizer.PirateShipPrefix.keys(),
            PLocalizer.PirateShipSuffix.keys()]
        self.namePanel = NamePanelGui.NamePanelGui(PLocalizer.NamePanelTitle, nameData)
        self.namePanel.setPos(0.2, 0, 0)
        self.lockStore()
        self.acceptOnce('returnStore', self.unlockStore)
        self.acceptOnce('nameChosen', self.handleCommitPurchasePart2)


    def handleCommitPurchasePart2(self, shipNames):
        self.ignore('returnStore')
        self.ignore('nameChosen')
        nameIndices = []
        nameIndices.append(shipNames)
        ShipStoreGUI.notify.debug('Make Purchase - Buying: %s, Selling: %s' % (self.purchaseInventory, self.sellInventory))
        messenger.send('makeShipSale', [
            self.purchaseInventory,
            self.sellInventory,
            nameIndices])


    def updateBalance(self, extraArgs = None):
        self.balance = 0
        for item in self.purchaseInventory:
            self.balance += EconomyGlobals.getItemCost(item[0])

        if self.balance > 0:
            self.balanceTitle['text'] = PLocalizer.Cost
            self.balanceValue['text'] = str(abs(self.balance))
        elif self.balance < 0:
            self.balanceTitle['text'] = PLocalizer.Gain
            self.balanceValue['text'] = str(abs(self.balance))
        else:
            self.balanceTitle['text'] = PLocalizer.Cost
            self.balanceValue['text'] = str(abs(self.balance))
        inventory = base.localAvatar.getInventory()
        if inventory:
            if inventory.getGoldInPocket() < self.balance:
                self.commitButton['frameColor'] = PiratesGuiGlobals.ButtonColor3
            elif len(inventory.getShipDoIdList()) >= inventory.getCategoryLimit(InventoryCategory.SHIPS):
                self.commitButton['frameColor'] = PiratesGuiGlobals.ButtonColor3
            else:
                self.commitButton['frameColor'] = PiratesGuiGlobals.ButtonColor4



    def lockStore(self):
        self.commitButton['state'] = DGG.DISABLED
        self.commitButton['frameColor'] = (0.4, 0.4, 0.4, 1)


    def unlockStore(self):
        self.commitButton['state'] = DGG.NORMAL
        self.updateBalance()


    def purchaseConfirmation(self):
        pass
