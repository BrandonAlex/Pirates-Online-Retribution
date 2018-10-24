from panda3d.core import TextNode
# File: P (Python 2.4)

from direct.gui.DirectGui import *
from pirates.piratesgui.GuiButton import GuiButton
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from PotionBoardPiece import PotionBoardPiece
import PotionGlobals

class PotionInfo(DirectFrame):

    def __init__(self, potionGame):
        self.potionGame = potionGame
        DirectFrame.__init__(self, parent = potionGame.dialogs, relief = None)
        self.setPos((-0.5, 0, 0.074))
        guiAssets = loader.loadModel('models/minigames/pir_m_gui_pot_textureCard')
        parch = guiAssets.find('**/pir_t_gui_pot_potionIngredients')
        parch.setScale(3.45, 1, 3.45)
        parch.setPos(0.5, 0, -0.02)
        self.background = parch.copyTo(self)
        self.bQuit = GuiButton(image = (guiAssets.find('**/pir_t_gui_pot_exitIngredients'), guiAssets.find('**/pir_t_gui_pot_exitIngredientsOn'), guiAssets.find('**/pir_t_gui_pot_exitIngredientsOn'), guiAssets.find('**/pir_t_gui_pot_exitIngredients')), scale = (0.299, 0.299, 0.299), command = self.quit)
        self.bQuit.reparentTo(self)
        self.bQuit.setPos(1.673, 0, 0.767)
        self.messageText = PLocalizer.PotionGui['InfoText']
        self.message = DirectLabel(parent = self, relief = None, text = self.messageText, text_scale = PiratesGuiGlobals.TextScaleTitleSmall, text_align = TextNode.ARight, text_fg = PotionGlobals.TextColor, text_shadow = None, pos = (-0.170, 0, 0.71), textMayChange = 0)
        self.pieces = []
        self.pieceLabels = []
        for color in xrange(6):
            for level in xrange(6):
                piece = PotionBoardPiece(self, color, level + 1)
                piece.setPiecePosition(level * 0.112 - 0.277, 0.170 - color * 0.0709000)
                piece.background.setDepthTest(False)
                piece.background.setDepthWrite(False)
                piece.setScale(0.348)
                self.pieces.append(piece)
                piecelabel = DirectLabel(parent = self, relief = None, text = PLocalizer.PotionIngredients[color][level], text_scale = PiratesGuiGlobals.TextScaleMed, text_align = TextNode.ACenter, text_fg = PotionGlobals.TextColor, text_shadow = None, pos = (level * 0.386 - 0.452, 0, 0.438 - color * 0.245), textMayChange = 0)
                self.message = DirectLabel(parent = self, relief = None, text = PLocalizer.PotionIngredients[color][level], text_scale = PiratesGuiGlobals.TextScaleMed, text_align = TextNode.ACenter, text_fg = PotionGlobals.TextColor, text_shadow = None, pos = (level * 0.386 - 0.452, 0, 0.438 - color * 0.245), textMayChange = 0)
                self.pieceLabels.append(piecelabel)


        guiAssets.remove_node()


    def destroy(self):
        self.bQuit.destroy()
        DirectFrame.destroy(self)


    def show(self):
        if self.potionGame.closeCurrentDialog is not None:
            self.potionGame.closeCurrentDialog()

        self.potionGame.closeCurrentDialog = self.cleanUp
        self.potionGame.disableButtons()
        self.unstash()


    def toggle(self):
        if self.isStashed():
            self.show()
        else:
            self.quit()


    def cleanUp(self):
        self.potionGame.closeCurrentDialog = None
        self.potionGame.enableButtons()
        self.stash()


    def quit(self):
        self.cleanUp()
        if self.potionGame.gameFSM.gameStarted:
            self.potionGame.gameFSM.request('Eval')
        else:
            self.potionGame.gameFSM.request('RecipeSelect')
