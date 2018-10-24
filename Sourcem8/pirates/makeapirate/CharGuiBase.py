from direct.gui.DirectGui import *
from pandac.PandaModules import *

class CharGuiSlider(DirectSlider):

    def __init__(self, main, parent, text, command, range = (-0.5, 0.5)):
        DirectSlider.__init__(self, parent = parent, relief = None, frameSize = (-0.59999999999999998, 0.59999999999999998, 0.10000000000000001, -0.10000000000000001), image = main.charGui.find('**/chargui_slider_small'), image_scale = 1.3300000000000001, thumb_image = (main.charGui.find('**/chargui_slider_node'), main.charGui.find('**/chargui_slider_node_down'), main.charGui.find('**/chargui_slider_node_over')), thumb_scale = 1.2, thumb_relief = None, text = text, text_fg = (1, 1, 1, 1), text_scale = 0.17999999999999999, text_pos = (0.69999999999999996, -0.040000000000000001), text_align = TextNode.ALeft, scale = 1, value = 0, range = range, command = command)
        self.initialiseoptions(CharGuiSlider)



class CharGuiPicker(DirectFrame):

    def __init__(self, main, parent, text, nextCommand, backCommand):
        DirectFrame.__init__(self, parent = parent, relief = None, text = text, text_fg = (1, 1, 1, 1), text_scale = 0.17999999999999999, text_pos = (0, 0), scale = 0.69999999999999996)
        self.initialiseoptions(CharGuiPicker)
        self.nextButton = DirectButton(parent = self, relief = None, image = (main.triangleGui.find('**/triangle'), main.triangleGui.find('**/triangle_down'), main.triangleGui.find('**/triangle_over')), pos = (0.59999999999999998, 0, 0.070000000000000007), scale = 0.20000000000000001, command = nextCommand)
        self.backButton = DirectButton(parent = self, relief = None, image = (main.triangleGui.find('**/triangle'), main.triangleGui.find('**/triangle_down'), main.triangleGui.find('**/triangle_over')), hpr = (0, 0, 180), pos = (-0.59999999999999998, 0, 0.070000000000000007), scale = 0.20000000000000001, command = backCommand)
