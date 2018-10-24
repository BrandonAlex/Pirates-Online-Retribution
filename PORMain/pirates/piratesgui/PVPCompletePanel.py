from panda3d.core import TextNode, VBase4
# File: P (Python 2.4)

from direct.gui.DirectGui import *
from pirates.piratesgui.BorderFrame import BorderFrame
from pirates.piratesgui.GuiButton import GuiButton
from pirates.piratesgui import PiratesGuiGlobals
from pirates.pvp import PVPGlobals
from pirates.piratesgui.ScoreFrame import ScoreFrame
from pirates.treasuremap.RewardItemGui import RewardItemGui
from pirates.piratesgui.StatRowGui import StatRowGui
from pirates.piratesgui.StatRowHeadingGui import StatRowHeadingGui
from pirates.piratesbase import PLocalizer

class PVPCompletePanel(BorderFrame):
    SUMMARY_PAGE = 1
    DETAILS_PAGE = 2

    def __init__(self, name, pvp):
        self.width = PiratesGuiGlobals.PVPCompletePanelWidth
        self.height = PiratesGuiGlobals.PVPCompletePanelHeight
        BorderFrame.__init__(self, frameSize = (self.width * 0.149, self.width * 0.848, self.height * 0.815, self.height), modelName = 'pir_m_gui_frm_subframe', imageColorScale = VBase4(0.75, 0.75, 0.946, 0.75))
        self.secondLayer = BorderFrame(parent = self, relief = None, frameSize = (self.width * 0.149, self.width * 0.848, self.height * 0.815, self.height), modelName = 'pir_m_gui_frm_subframe', imageColorScale = VBase4(0.75, 0.75, 0.9, 0.75))
        self.initialiseoptions(PVPCompletePanel)
        self.endButton = GuiButton(parent = self, text = PLocalizer.PVPExit, command = pvp.requestPVPLeave, pos = (1.25, 0, 0.100), image = GuiButton.redGenericButton, image_scale = 0.598)
        self.endButton.setBin('gui-fixed', 4)
        self.name = name
        self.title = DirectLabel(parent = self, relief = None, text = name, text_align = TextNode.ACenter, text_scale = 0.070, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1, pos = (1.25, 0, 1.62))
        if pvp.hasTeams():
            team1Score = '0'
            team2Score = '0'
            for stat in pvp.scoreboardHolder.getItemList():
                if stat['Team'] == 1:
                    team1Score = stat['Score']
                    continue
                if stat['Team'] == 2:
                    team2Score = stat['Score']
                    continue

            self.team1ScoreLabel = DirectLabel(parent = self, relief = None, text = PLocalizer.PVPTeamScore % (1, team1Score), text_align = TextNode.ACenter, text_scale = 0.0400, text_fg = PVPGlobals.getTeamColor(1), text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1, pos = (1.05, 0, 1.55))
            self.team2ScoreLabel = DirectLabel(parent = self, relief = None, text = PLocalizer.PVPTeamScore % (2, team2Score), text_align = TextNode.ACenter, text_scale = 0.0400, text_fg = PVPGlobals.getTeamColor(2), text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1, pos = (1.45, 0, 1.55))

        self.outcome = DirectLabel(parent = self, relief = None, text = '', text_align = TextNode.ACenter, text_scale = 0.0598, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1, pos = (1.25, 0, 1.45))
        if pvp.hasTeams():
            if team1Score > team2Score:
                self.outcome['text_fg'] = PVPGlobals.getTeamColor(1)
            elif team2Score > team1Score:
                self.outcome['text_fg'] = PVPGlobals.getTeamColor(2)


        self.borderTwo = BorderFrame(parent = self, relief = None, frameSize = (self.width * 0.149, self.width * 0.848, 0, self.height * 0.800000), modelName = 'pir_m_gui_frm_subframe', imageColorScale = VBase4(0.75, 0.75, 0.9, 0.75))
        self.borderTwoSecondLayer = BorderFrame(parent = self.borderTwo, relief = None, frameSize = (self.width * 0.149, self.width * 0.848, 0, self.height * 0.800000), modelName = 'pir_m_gui_frm_subframe', imageColorScale = VBase4(0.75, 0.75, 0.9, 0.75))
        self.two = ScoreFrame(PiratesGuiGlobals.PVPCompletePageWidth - 1.0, PiratesGuiGlobals.PVPCompletePageHeight, pvp.statsHolder, 0, sortOrder = 2)
        self.two.reparentTo(self.borderTwo)
        self.two.setPos(0.450, 0, -0.149)
        self.two.setup()
        self.game = pvp


    def setOutcome(self, outcome):
        self.outcome['text'] = outcome


    def destroy(self):
        self.borderTwoSecondLayer.destroy()
        self.borderTwoSecondLayer = None
        self.borderTwo.destroy()
        self.borderTwo = None
        self.two.destroy()
        self.two = None
        self.secondLayer.destroy()
        self.secondLater = None
        self.game = None
        BorderFrame.destroy(self)
