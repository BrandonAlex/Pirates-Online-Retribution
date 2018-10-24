from panda3d.core import TextNode
# File: L (Python 2.4)

from direct.gui.DirectGui import *
from pirates.piratesgui import ButtonListItem
from pirates.piratesgui import PiratesGuiGlobals
import types
from pirates.piratesgui.BorderFrame import BorderFrame

class LookoutListItem(ButtonListItem.ButtonListItem):

    def __init__(self, itemInfo, imageTexCardName, itemHeight, itemWidth, parent = None, parentList = None, textScale = None, txtColor = None, wantFrame = False, **kw):
        ButtonListItem.ButtonListItem.__init__(self, itemInfo, itemHeight, itemWidth, parent, parentList, textScale, txtColor)
        self.initialiseoptions(LookoutListItem)
        lookoutUI = loader.loadModel(imageTexCardName)
        iconImage = itemInfo.get('Icon')
        self.imageRef = None
        if iconImage:
            self.imageRef = lookoutUI.find('**/' + iconImage)

        self.descText = itemInfo.get('Desc')
        self.title = None
        self.desc = None
        self.icon = None
        self.activityListBorderFrame = None
        self.wantFrame = wantFrame
        self.bind(DGG.ENTER, self.mouseEnter)
        self.bind(DGG.EXIT, self.mouseLeave)


    def _createIface(self):
        xOff = 0.02
        wordwrap = 20
        yOff = 0.065
        if self.imageRef:
            self.icon = OnscreenImage(image = self.imageRef, pos = (0.100, 0, 0.082000), scale = (0.598, 0.598, 0.598), parent = self)
            xOff = 0.200
            wordwrap = 15

        if self.descText:
            self.desc = DirectLabel(parent = self, state = DGG.DISABLED, relief = None, text = self.descText, text_align = TextNode.ALeft, text_scale = 0.0299, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = wordwrap, textMayChange = 1, pos = (xOff + 0.01, 0, 0.055))
            yOff = 0.0950

        self.title = DirectLabel(parent = self, state = DGG.DISABLED, relief = None, text = self.item, text_align = TextNode.ALeft, text_scale = 0.070, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, textMayChange = 1, pos = (xOff, 0, yOff))
        if self.wantFrame:
            self.createListFrame()



    def _destroyIface(self):
        if self.icon:
            self.icon.remove_node()
            self.icon = None

        if self.title:
            self.title.remove_node()
            self.title = None

        if self.desc:
            self.desc.remove_node()
            self.desc = None



    def _handleItemChange(self):
        self._destroyIface()
        self._createIface()


    def setSelected(self, selected):
        self.selected = selected
        return None
        if selected:
            print 'selected'
            self.createListFrame()
        else:
            self.clearListFrame()


    def createListFrame(self):
        self.clearListFrame()
        self.activityListBorderFrame = BorderFrame(parent = self, pos = (0.375, 0, 0.082000), scale = (0.75, 1, 0.165), borderScale = 0.200)
        self.activityListBorderFrame.setBackgroundVisible(False)
        self.activityListBorderFrame.setColorScale(0.4, 0.4, 0.4, 1)


    def clearListFrame(self):
        if self.activityListBorderFrame:
            self.activityListBorderFrame.remove_node()
            self.activityListBorderFrame = None



    def mouseEnter(self, event):
        if self.wantFrame == False:
            self.createListFrame()

        if self.activityListBorderFrame:
            self.activityListBorderFrame.setColorScale(1, 1, 1, 1)
            self.activityListBorderFrame['borderScale'] = 0.25



    def mouseLeave(self, event):
        if self.wantFrame and self.activityListBorderFrame:
            self.activityListBorderFrame.setColorScale(0.4, 0.4, 0.4, 1)
            self.activityListBorderFrame['borderScale'] = 0.200
        else:
            self.clearListFrame()
