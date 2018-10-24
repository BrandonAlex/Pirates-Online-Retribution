# File: R (Python 2.4)

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.task.Task import Task
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import GuiPanel
from pirates.piratesgui import PiratesGuiGlobals

class RequestButton(DirectButton):

    def __init__(self, text, command, width = 1.0):
        self.charGui = loader.loadModel('models/gui/char_gui')
        buttonImage = (self.charGui.find('**/chargui_text_block_large'), self.charGui.find('**/chargui_text_block_large_down'), self.charGui.find('**/chargui_text_block_large_over'))
        DirectButton.__init__(self, relief = None, pos = (0, 0, 0), text = text, text_scale = PiratesGuiGlobals.TextScaleLarge, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_pos = (0.040000000000000001, 0.025000000000000001), image = buttonImage, image_scale = (0.29999999999999999 * width, 0.29999999999999999, 0.29999999999999999), image_pos = (0.050000000000000003, 0.0, 0.035000000000000003), command = command)
        self.initialiseoptions(RequestButton)
        self.charGui.remove_node()
