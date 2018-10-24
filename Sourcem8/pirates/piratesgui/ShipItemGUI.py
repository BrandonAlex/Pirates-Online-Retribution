# File: S (Python 2.4)

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui import InventoryItemGui
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.uberdog import UberDogGlobals
from pirates.battle import WeaponGlobals
from pirates.economy import EconomyGlobals
from pirates.economy.EconomyGlobals import *
from pirates.reputation import ReputationGlobals
from pirates.piratesbase import Freebooter

class ShipItemGUI(InventoryItemGui.InventoryItemGui):

    def __init__(self, data, trade = 0, buy = 0, sell = 0, use = 0, **kw):
        optiondefs = ()
        self.defineoptions(kw, optiondefs)
        InventoryItemGui.InventoryItemGui.__init__(self, data, trade, buy, sell, use)
        self.initialiseoptions(ShipItemGUI)
        repId = InventoryType.SailingRep
        self.checkLevel(repId, self.minLvl)
        self.flattenStrong()


    def createGui(self):
        (item, quantity) = self.data
        name = PLocalizer.InventoryTypeNames[item]
        self.price = EconomyGlobals.getItemCost(item)
        repId = InventoryType.SailingRep
        itemTypeName = PLocalizer.InventoryTypeNames.get(repId)
        self.itemType = itemTypeName
        if self.sell:
            self.price /= 2

        card = loader.loadModel('models/textureCards/shipRenders')
        if item in [
            ItemId.INTERCEPTOR_L1,
            ItemId.INTERCEPTOR_L2,
            ItemId.INTERCEPTOR_L3]:
            myTexCard = card.find('**/Interceptor_Render*')
        elif item in [
            ItemId.MERCHANT_L1,
            ItemId.MERCHANT_L2,
            ItemId.MERCHANT_L3]:
            myTexCard = card.find('**/Merchant_Render*')
        elif item in [
            ItemId.WARSHIP_L1,
            ItemId.WARSHIP_L2,
            ItemId.WARSHIP_L3]:
            myTexCard = card.find('**/Warship_Render*')
        else:
            myTexCard = card.find('**/Warship_Render*')
        myTex = myTexCard.findAllTextures()[0]
        card.remove_node()
        del card
        self.minLvl = EconomyGlobals.getItemMinLevel(item)
        self.miscText = None
        self.picture = DirectFrame(parent = self, relief = None, state = DGG.DISABLED, image = myTex, image_scale = 0.059999999999999998, pos = (0.085000000000000006, 0, 0.074999999999999997))
        self.picture.setTransparency(1)
        self.nameTag = DirectLabel(parent = self, state = DGG.DISABLED, relief = None, text = name, text_scale = PiratesGuiGlobals.TextScaleMed * PLocalizer.getHeadingScale(2), text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, pos = (0.16, 0, 0.105), textMayChange = 0)
        self.costText = DirectLabel(parent = self, relief = None, state = DGG.DISABLED, geom = self.coinImage, geom_scale = 0.12, geom_pos = Vec3(-0.01, 0, 0.01), text = str(self.price), text_scale = PiratesGuiGlobals.TextScaleSmall, text_align = TextNode.ARight, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 11, text_pos = (-0.029999999999999999, 0, 0), pos = (self.width - 0.035000000000000003, 0, 0.105), text_font = PiratesGlobals.getInterfaceFont())


    def showDetails(self, event):
        pass


    def hideDetails(self, event):
        pass


    def createHelpbox(self, args = None):
        pass


    def checkLevel(self, repId, minLvl):
        inv = localAvatar.getInventory()
        if inv:
            repAmt = inv.getAccumulator(repId)
            if not Freebooter.getPaidStatus(base.localAvatar.getDoId()):
                (item, quantity) = self.data
                if item != ItemId.INTERCEPTOR_L1 and item != ItemId.MERCHANT_L1:
                    if not self.miscText:
                        self.miscText = DirectLabel(parent = self, relief = None, text = '', text_scale = PiratesGuiGlobals.TextScaleSmall, text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 11, text_pos = (0.050000000000000003, 0, 0), pos = (0.16, 0, 0.025000000000000001))

                    self['image_color'] = Vec4(1, 0.5, 0.5, 1)
                    self.miscText['text_fg'] = PiratesGuiGlobals.TextFG8
                    self.miscText['text'] = PLocalizer.noFreebooterCap
                    subCard = loader.loadModel('models/gui/toplevel_gui')
                    appendMe = DirectFrame(parent = self, relief = None, pos = (self.width - 0.40500000000000003, 0, -0.014999999999999999), state = DGG.DISABLED, geom = subCard.find('**/pir_t_gui_gen_key_subscriber'), geom_scale = 0.12, geom_pos = (0.059999999999999998, 0, 0.059999999999999998))
                    subCard.remove_node()

            elif minLvl > ReputationGlobals.getLevelFromTotalReputation(repId, repAmt)[0]:
                if not self.miscText:
                    self.miscText = DirectLabel(parent = self, relief = None, text = '', text_scale = PiratesGuiGlobals.TextScaleSmall, text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 11, pos = (0.16, 0, 0.025000000000000001))

                self['image_color'] = Vec4(1, 0.5, 0.25, 1)
                self['state'] = DGG.DISABLED
                self.miscText['text_fg'] = PiratesGuiGlobals.TextFG8
                self.miscText['text'] = PLocalizer.LevelRequirement % minLvl
