from direct.gui.DirectGui import *
from pandac.PandaModules import *
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui.ListFrame import ListFrame
from pirates.piratesgui.ScoreboardItemGui import ScoreboardItemGui
from pirates.piratesgui import GuiPanel
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer

class Scoreboard(DirectFrame):
    
    def __init__(self, name, width, height, results, titleHeight = 1.0):
        DirectFrame.__init__(self, relief = None, state = DGG.NORMAL, frameColor = PiratesGuiGlobals.FrameColor, borderWidth = PiratesGuiGlobals.BorderWidth, pos = (0, 0, -0.029999999999999999))
        self.initialiseoptions(Scoreboard)
        self.width = width
        self.height = height
        self.titleHeight = titleHeight
        self.results = results
        self.listHeight = self.height
        width = self.width - 0.02
        height = self.height - self.titleHeight - 0.17000000000000001
        self.list = ListFrame(width - 0.02, 0, name, self, delayedReveal = 1)
        self.list.setup()
        self.list.reparentTo(self)
        self.setPos(0.01, 0, 0.01)
        self.fixHeight()

    
    def destroy(self):
        self.list.destroy()
        DirectFrame.destroy(self)

    
    def getItemList(self):
        return self.results

    
    def getItemChangeMsg(self):
        return self.taskName('tmRewardChanged')

    
    def addNewResult(self, result):
        self.results.append(result)

    
    def fixHeight(self):
        height = self.height - self.titleHeight - 0.17000000000000001
        items = self.list.items
        itemHeight = 0.0
        for item in items:
            itemHeight += item.getHeight()
        
        newZ = height - itemHeight
        self.list.setZ(newZ)

    
    def createNewItem(self, item, parent, itemType = None, columnWidths = [], color = None):
        width = self.width - 0.02
        height = self.listHeight / (len(self.getItemList()) + 1)
        if height > 0.10000000000000001:
            height = 0.10000000000000001
        
        if item.get('Type') == 'Space':
            height = height / 3
        
        return ScoreboardItemGui(item, width, height, parent)


