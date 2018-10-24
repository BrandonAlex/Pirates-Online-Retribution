import math
from pirates.piratesgui.GuiPanel import *
from pirates.piratesgui.RequestButton import RequestButton
from pirates.piratesbase import PLocalizer
from pirates.piratesbase import CollectionMap
from pirates.battle import WeaponGlobals
from pirates.uberdog.UberDogGlobals import InventoryType
from pirates.reputation import ReputationGlobals
from pirates.ai import HolidayGlobals
import FishingGlobals

class FishingResults(NodePath):

    def __init__(self, fishingGame):
        NodePath.__init__(self, 'FishingResults')
        self.reparentTo(base.a2dRightCenter)
        self.gameObject = fishingGame
        self.setPos(-1.0, 0.0, -0.25)
        self.background = loader.loadModel('models/minigames/pir_m_gui_fsh_rewardScreen')
        self.background.reparentTo(self)
        self.background.setScale(0.80000000000000004, 0.75, 0.75)
        self.background.setPos(0.65000000000000002, 0.75, 0.75)
        self.bAgain = RequestButton(width = 1.5, text = PLocalizer.FishingGui['PlayAgainButton'], command = self.playAgain)
        self.bAgain.reparentTo(self)
        self.bAgain.setPos(0.57999999999999996, 0, 0.10000000000000001)
        self.bAgain.setScale(1.2, 1.2, 1.2)
        self.titleText = PLocalizer.FishingGui['WinTitle']
        self.messageText = PLocalizer.FishingGui['WinText']
        self.title = DirectLabel(parent = self, relief = None, text = self.titleText, text_scale = PiratesGuiGlobals.TextScaleTitleJumbo, text_font = PiratesGlobals.getPirateOutlineFont(), text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextLT14, pos = (0.62, 0, 1.3), textMayChange = 0)
        self.message = DirectLabel(parent = self, relief = None, text = self.messageText, text_scale = PiratesGuiGlobals.TextScaleTitleSmall, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 17, pos = (0.64000000000000001, 0, 1.1499999999999999), textMayChange = 0)
        self.fishName = None
        self.levelUnlockDetails = None
        self.fishWeight = None
        self.fishXpAmt = 0
        self.fishXp = None
        self.fishXpBonus = None
        self.fishGoldAmt = 0
        self.fishGold = None
        self.fishGoldBonus = None
        self.collectionCard = loader.loadModel('models/gui/treasure_gui')


    def destroy(self):
        self.bAgain.destroy()


    def showAll(self):
        if self.fishName is not None:
            self.fishName.remove_node()

        if self.levelUnlockDetails is not None:
            self.levelUnlockDetails.remove_node()

        if self.fishWeight is not None:
            self.fishWeight.remove_node()

        if self.fishXp is not None:
            self.fishXp.remove_node()

        if self.fishGold is not None:
            self.fishGold.remove_node()

        self.fishName = DirectLabel(parent = self, relief = None, text = self.gameObject.fishManager.activeFish.myData['name'], text_scale = PiratesGuiGlobals.TextScaleTitleMed, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 17, pos = (0.64000000000000001, 0, 1.04), textMayChange = 0)
        unlockText = ''
        newLevel = self.gameObject.getPredictedPlayerFishingLevel(int(self.gameObject.fishManager.activeFish.myData['experience']))
        if newLevel > self.gameObject.levelAtCastStart:
            self.gameObject.currentFishingLevel = newLevel
            unlockText = PLocalizer.FishingGui['LevelUp'] + ' ' + PLocalizer.Minigame_Fishing_Level_Unlocks[newLevel]
            self.gameObject.tutorialManager.showTutorial(InventoryType.FishingLevelGain)
            if newLevel == 10:
                self.gameObject.tutorialManager.showTutorial(InventoryType.FishingLevel10)

            if newLevel in FishingGlobals.unlockLevelToSkillId:
                unlock = FishingGlobals.unlockLevelToSkillId[newLevel]
                if unlock in FishingGlobals.skillIdToTutorialId:
                    tutorialContext = FishingGlobals.skillIdToTutorialId[unlock]
                    self.gameObject.tutorialManager.showTutorial(tutorialContext)



        self.levelUnlockDetails = DirectLabel(parent = self, relief = None, text = unlockText, text_scale = PiratesGuiGlobals.TextScaleTitleSmall, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 16, pos = (0.64000000000000001, 0.0, 0.41999999999999998), textMayChange = 0)
        self.fishXpAmt = self.gameObject.fishManager.activeFish.myData['experience']
        self.fishXp = DirectLabel(parent = self, relief = None, text = '+ ' + str(self.fishXpAmt) + ' ' + PLocalizer.FishingGui['XPLabel'], text_scale = PiratesGuiGlobals.TextScaleTitleSmall, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 17, pos = (0.90000000000000002, 0, 0.63), textMayChange = 1)
        self.fishGoldAmt = int(self.gameObject.fishManager.activeFish.myData['gold'] * self.gameObject.fishManager.activeFish.weight)
        self.fishGold = DirectLabel(parent = self, relief = None, text = '+ ' + str(self.fishGoldAmt) + ' ' + PLocalizer.FishingGui['GoldText'], text_scale = PiratesGuiGlobals.TextScaleTitleSmall, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 17, pos = (0.90000000000000002, 0, 0.54000000000000004), textMayChange = 1)
        self.updateGoldAndXpBonus()
        self.fishWeight = DirectLabel(parent = self, relief = None, text = str(self.gameObject.fishManager.activeFish.weight) + ' ' + PLocalizer.FishingGui['WeightLabel'], text_scale = PiratesGuiGlobals.TextScaleTitleLarge, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 17, pos = (0.40000000000000002, 0, 0.59999999999999998), textMayChange = 0)
        pic_name = CollectionMap.Assets[self.gameObject.fishManager.activeFish.myData['id']]
        fishIcon = self.collectionCard.find('**/%s*' % pic_name)
        self.glow = DirectFrame(parent = self, geom = fishIcon, geom_scale = 1.0, pos = (0.64000000000000001, 0.0, 0.84999999999999998), image = None, relief = None)
        self.setScale(0.75, 0.75, 0.75)
        self.show()


    def updateGoldAndXpBonus(self):
        if self.fishXpBonus is not None:
            self.fishXpBonus.remove_node()

        xpBonus = self.gameObject.distributedFishingSpot.getXpBonus()
        if xpBonus:
            self.fishXp['text'] = '+ ' + str(self.fishXpAmt + xpBonus) + ' ' + PLocalizer.FishingGui['XPLabel']
            self.fishXpBonus = DirectLabel(parent = self, relief = None, text = PLocalizer.FishingGui['XPBonusLabel'] % str(xpBonus), text_scale = PiratesGuiGlobals.TextScaleMed, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG4, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 17, pos = (0.90000000000000002, 0, 0.59999999999999998), textMayChange = 0)

        if self.fishGoldBonus is not None:
            self.fishGoldBonus.remove_node()

        goldBonus = self.gameObject.distributedFishingSpot.getGoldBonus()
        if goldBonus:
            self.fishGold['text'] = '+ ' + str(self.fishGoldAmt + goldBonus) + ' ' + PLocalizer.FishingGui['GoldText']
            self.fishGoldBonus = DirectLabel(parent = self, relief = None, text = PLocalizer.FishingGui['GoldBonusLabel'] % str(goldBonus), text_scale = PiratesGuiGlobals.TextScaleMed, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG4, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 17, pos = (0.90000000000000002, 0, 0.51000000000000001), textMayChange = 0)



    def cleanUp(self):
        self.hide()


    def playAgain(self):
        self.cleanUp()
        if localAvatar.guiMgr.inventoryUIManager.hasPlunder():
            localAvatar.guiMgr.inventoryUIManager.showPlunder()
        elif self.gameObject.fsm.getCurrentOrNextState() != 'PlayerIdle':
            self.gameObject.fsm.request('PlayerIdle')



    def quit(self):
        self.cleanUp()
        self.gameObject.fsm.request('Offscreen')
