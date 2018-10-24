from panda3d.core import TextNode, Vec4
# File: V (Python 2.4)

from direct.gui.DirectGui import *
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui.DialMeter import DialMeter
from pirates.piratesgui.BorderFrame import BorderFrame

class VitaeMeter(DirectFrame):

    def __init__(self, parent, **kw):
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(VitaeMeter)
        toplevel_gui = loader.loadModel('models/gui/toplevel_gui')
        self.vitaeDial = DialMeter(parent = self, pos = (0.85, 0, 0.11), meterColor = Vec4(0.84, 0.21, 0.21, 1), baseColor = Vec4(0, 0, 0, 1), scale = 0.233)
        icon = toplevel_gui.find('**/morale_skull*')
        self.vitaeIcon = DirectFrame(parent = self, state = DGG.NORMAL, relief = None, image = icon, pos = (0.85, 0, 0.11), image_scale = 0.475)
        detailLabel = DirectLabel(relief = None, state = DGG.DISABLED, text = PLocalizer.VitaeDesc, text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleExtraLarge, text_fg = PiratesGuiGlobals.TextFG1, text_wordwrap = 15, text_shadow = (0, 0, 0, 1), pos = (0.0, 0, -0.0251), textMayChange = 0, sortOrder = 91)
        height = -(detailLabel.getHeight() + 0.01)
        width = max(0.25, detailLabel.getWidth() + 0.041)
        self.helpBox = BorderFrame(parent = self, state = DGG.DISABLED, modelName = 'general_frame_f', frameSize = (-0.041, width, height, 0.053), pos = (1, 0, -0.040), sortOrder = 90)
        detailLabel.reparentTo(self.helpBox)
        self.helpBox.hide()
        self.helpBox.setClipPlaneOff()
        self.meterLabel = DirectLabel(parent = self.vitaeDial, relief = None, pos = (0, 0, -0.48), text = PLocalizer.Vitae, text_scale = 0.22, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getPirateOutlineFont(), textMayChange = 1)
        self.vitaeIcon.bind(DGG.WITHIN, self.showDetails)
        self.vitaeIcon.bind(DGG.WITHOUT, self.hideDetails)


    def showDetails(self, event):
        self.helpBox.show()


    def hideDetails(self, event):
        self.helpBox.hide()


    def update(self, level, range, val):
        self.vitaeDial.hide()
        Range = range * 1.0009
        if level > 0:
            self.vitaeDial.update(val, Range)
            self.vitaeDial.show()
