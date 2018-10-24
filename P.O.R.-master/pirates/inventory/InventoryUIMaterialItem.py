from direct.gui.DirectGui import *
from pandac.PandaModules import *
from pirates.piratesgui import GuiPanel, PiratesGuiGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from otp.otpbase import OTPLocalizer
from pirates.inventory.InventoryUIGlobals import *
from pirates.battle import WeaponGlobals
from pirates.economy import EconomyGlobals
from pirates.inventory import InventoryUIStackItem

class InventoryUIMaterialItem(InventoryUIStackItem.InventoryUIStackItem):
    
    def __init__(self, manager, itemId, itemTuple, imageScaleFactor = 1.0, showMax = 1, update = False):
        self.itemId = itemId
        InventoryUIStackItem.InventoryUIStackItem.__init__(self, manager, itemTuple, imageScaleFactor = imageScaleFactor, showMax = showMax, update = update)
        self.initialiseoptions(InventoryUIMaterialItem)
        SkillIcons = loader.loadModel('models/textureCards/skillIcons')
        MaterialIcons = loader.loadModel('models/textureCards/shipMaterialIcons')
        self['image'] = MaterialIcons.find('**/%s' % EconomyGlobals.getItemIcons(itemId))
        self.helpFrame = None
        self.cm = CardMaker('itemCard')
        self.cm.setFrame(-0.29999999999999999, 0.29999999999999999, -0.089999999999999997, 0.089999999999999997)
        self.buffer = None
        self.lens = PerspectiveLens()
        self.lens.setNear(0.10000000000000001)
        self.lens.setAspectRatio(0.59999999999999998 / 0.17999999999999999)
        self.realItem = None
        self.iconLabel = None
        self.itemCard = None
        self.portraitSceneGraph = NodePath('PortraitSceneGraph')
        detailGui = loader.loadModel('models/gui/gui_card_detail')
        self.bg = detailGui.find('**/color')
        self.bg.setScale(4)
        self.bg.setPos(0, 17, -6.2999999999999998)
        self.glow = detailGui.find('**/glow')
        self.glow.setScale(3)
        self.glow.setPos(0, 17, -6.2999999999999998)
        self.glow.setColor(1, 1, 1, 0.80000000000000004)
        self.setBin('gui-fixed', 1)
        self.accept('open_main_window', self.createBuffer)
        self.accept('aspectRatioChanged', self.createBuffer)
        self.accept('close_main_window', self.destroyBuffer)
        self['image_scale'] = 0.10000000000000001 * imageScaleFactor

    
    def destroy(self):
        if self.helpFrame:
            self.helpFrame.destroy()
            self.helpFrame = None
        
        self.destroyBuffer()
        if self.itemCard:
            self.itemCard.removeNode()
            del self.itemCard
            self.itemCard = None
        
        if self.iconLabel:
            self.iconLabel.destroy()
            self.iconLabel = None
        
        if self.portraitSceneGraph:
            self.portraitSceneGraph.removeNode()
            del self.portraitSceneGraph
            self.portraitSceneGraph = None
        
        InventoryUIStackItem.InventoryUIStackItem.destroy(self)

    
    def getName(self):
        return PLocalizer.InventoryTypeNames.get(self.itemId)

    
    def getItemId(self):
        return self.itemId

    
    def updateAmount(self, caller = None):
        InventoryUIStackItem.InventoryUIStackItem.updateAmount(self, caller)
        localAvatar.guiMgr.combatTray.skillTray.updateSkillTrayAmounts()
        inventory = localAvatar.getInventory()
        skillQuantity = inventory.getStackQuantity(self.getItemId())
        if skillQuantity >= 2:
            self['text_fg'] = PiratesGuiGlobals.TextFG2
        else:
            self['text_fg'] = PiratesGuiGlobals.TextFG9

    
    def showDetails(self, cell, detailsPos, detailsHeight, event = None):
        self.notify.debug('Item showDetails')
        if self.manager.heldItem and self.manager.locked and cell.isEmpty() and self.isEmpty() or not (self.itemTuple):
            self.notify.debug(' early exit')
            return None
        
        self.helpFrame = DirectFrame(parent = self.manager, relief = None, state = DGG.DISABLED, sortOrder = 1)
        self.helpFrame.setBin('gui-popup', -5)
        detailGui = loader.loadModel('models/gui/gui_card_detail')
        topGui = loader.loadModel('models/gui/toplevel_gui')
        coinImage = topGui.find('**/treasure_w_coin*')
        SkillIcons = loader.loadModel('models/textureCards/skillIcons')
        border = SkillIcons.find('**/base')
        halfWidth = 0.29999999999999999
        halfHeight = 0.20000000000000001
        basePosX = cell.getX(aspect2d)
        basePosZ = cell.getZ(aspect2d)
        cellSizeX = 0.0
        cellSizeZ = 0.0
        if cell:
            cellSizeX = cell.cellSizeX
            cellSizeZ = cell.cellSizeZ
        
        textScale = PiratesGuiGlobals.TextScaleMed
        titleScale = PiratesGuiGlobals.TextScaleTitleSmall
        if len(self.getName()) >= 30:
            titleNameScale = PiratesGuiGlobals.TextScaleLarge
        else:
            titleNameScale = PiratesGuiGlobals.TextScaleExtraLarge
        subtitleScale = PiratesGuiGlobals.TextScaleMed
        iconScalar = 1.5
        borderScaler = 0.25
        splitHeight = 0.01
        vMargin = 0.029999999999999999
        runningVertPosition = 0.29999999999999999
        runningSize = 0.0
        labels = []
        titleColor = PiratesGuiGlobals.TextFG24
        titleLabel = DirectLabel(parent = self, relief = None, text = self.getName(), text_scale = titleNameScale, text_fg = titleColor, text_shadow = PiratesGuiGlobals.TextShadow, text_align = TextNode.ACenter, pos = (0.0, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
        self.bg.setColor(titleColor)
        tHeight = 0.070000000000000007
        titleLabel.setZ(runningVertPosition)
        runningVertPosition -= tHeight
        runningSize += tHeight
        labels.append(titleLabel)
        subtitleLabel = DirectLabel(parent = self, relief = None, text = PLocalizer.InventoryItemClassNames.get(EconomyGlobals.getItemType(self.getId()), ''), text_scale = subtitleScale, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_align = TextNode.ACenter, pos = (0.0, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
        subtHeight = 0.050000000000000003
        subtitleLabel.setZ(subtHeight * 0.5 + runningVertPosition)
        runningVertPosition -= subtHeight
        runningSize += subtHeight
        labels.append(subtitleLabel)
        MaterialIcons = loader.loadModel('models/textureCards/shipMaterialIcons')
        self.iconLabel = DirectLabel(parent = self.portraitSceneGraph, relief = None, image = MaterialIcons.find('**/%s' % EconomyGlobals.getItemIcons(self.getItemId())), pos = (0.0, 2.5, 0.0))
        iHeight = 0.17999999999999999
        self.createBuffer()
        self.itemCard.setZ(runningVertPosition - 0.059999999999999998)
        runningVertPosition -= iHeight
        runningSize += iHeight
        labels.append(self.itemCard)
        description = PLocalizer.WeaponDescriptions.get(self.getId())
        if not description:
            description = PLocalizer.WeaponDescriptions.get(self.getItemId())
        
        if description:
            descriptionLabel = DirectLabel(parent = self, relief = None, text = description, text_scale = textScale, text_wordwrap = halfWidth * 2.0 * (0.94999999999999996 / textScale), text_align = TextNode.ALeft, pos = (-halfWidth + textScale * 0.5, 0.0, runningVertPosition), text_pos = (0.0, -textScale))
            dHeight = descriptionLabel.getHeight() + 0.02
            runningVertPosition -= dHeight
            runningSize += dHeight
            labels.append(descriptionLabel)
        
        runningVertPosition -= 0.02
        runningSize += 0.02
        panels = self.helpFrame.attachNewNode('panels')
        topPanel = panels.attachNewNode('middlePanel')
        detailGui.find('**/top_panel').copyTo(topPanel)
        topPanel.setScale(0.080000000000000002)
        topPanel.reparentTo(self.helpFrame)
        middlePanel = panels.attachNewNode('middlePanel')
        detailGui.find('**/middle_panel').copyTo(middlePanel)
        middlePanel.setScale(0.080000000000000002)
        middlePanel.reparentTo(self.helpFrame)
        placement = 0
        i = 0
        heightMax = -0.080000000000000002
        currentHeight = runningVertPosition
        if detailsHeight:
            currentHeight = -detailsHeight
        
        while currentHeight < heightMax:
            middlePanel = panels.attachNewNode('middlePanel%s' % 1)
            detailGui.find('**/middle_panel').copyTo(middlePanel)
            middlePanel.setScale(0.080000000000000002)
            middlePanel.reparentTo(self.helpFrame)
            if currentHeight + 0.20000000000000001 >= heightMax:
                difference = heightMax - currentHeight
                placement += (0.16800000000000001 / 0.20000000000000001) * difference
                currentHeight += difference
            else:
                placement += 0.16800000000000001
                currentHeight += 0.20000000000000001
            middlePanel.setZ(-placement)
            i += 1
        bottomPanel = panels.attachNewNode('bottomPanel')
        detailGui.find('**/bottom_panel').copyTo(bottomPanel)
        bottomPanel.setScale(0.080000000000000002)
        bottomPanel.setZ(-placement)
        bottomPanel.reparentTo(self.helpFrame)
        colorPanel = panels.attachNewNode('colorPanel')
        detailGui.find('**/color').copyTo(colorPanel)
        colorPanel.setScale(0.080000000000000002)
        colorPanel.setColor(titleColor)
        colorPanel.reparentTo(self.helpFrame)
        lineBreakTopPanel = panels.attachNewNode('lineBreakTopPanel')
        detailGui.find('**/line_break_top').copyTo(lineBreakTopPanel)
        lineBreakTopPanel.setScale(0.080000000000000002, 0.080000000000000002, 0.070000000000000007)
        lineBreakTopPanel.setZ(0.0080000000000000002)
        lineBreakTopPanel.reparentTo(self.helpFrame)
        panels.flattenStrong()
        self.helpFrame['frameSize'] = (-halfWidth, halfWidth, -(runningSize + vMargin), vMargin)
        totalHeight = self.helpFrame.getHeight() - 0.10000000000000001
        for label in labels:
            label.reparentTo(self.helpFrame)
        
        if basePosX > 0.0:
            newPosX = basePosX - halfWidth + cellSizeX * 0.45000000000000001
        else:
            newPosX = basePosX + halfWidth + cellSizeX * 0.45000000000000001
        if basePosZ > 0.0:
            newPosZ = basePosZ + cellSizeZ * 0.45000000000000001
        else:
            newPosZ = basePosZ + totalHeight - cellSizeZ * 0.75
        if detailsPos:
            (newPosX, newPosZ) = detailsPos
        
        self.helpFrame.setPos(newPosX, 0, newPosZ)

    
    def hideDetails(self, event = None):
        if self.helpFrame:
            self.helpFrame.destroy()
            self.helpFrame = None
        
        self.destroyBuffer()
        if self.iconLabel:
            self.iconLabel.destroy()
        

    
    def createBuffer(self):
        self.destroyBuffer()
        self.buffer = base.win.makeTextureBuffer('par', 256, 256)
        self.buffer.setOneShot(True)
        self.cam = base.makeCamera(win = self.buffer, scene = self.portraitSceneGraph, clearColor = Vec4(1), lens = self.lens)
        self.cam.node().getDisplayRegion(0).setIncompleteRender(False)
        self.cam.reparentTo(self.portraitSceneGraph)
        self.bg.reparentTo(self.cam)
        self.glow.reparentTo(self.cam)
        if self.itemCard:
            self.itemCard.removeNode()
        
        tex = self.buffer.getTexture()
        self.itemCard = NodePath(self.cm.generate())
        self.itemCard.setTexture(tex, 1)
        if self.helpFrame:
            self.itemCard.reparentTo(self.helpFrame)
        

    
    def destroyBuffer(self):
        if self.buffer:
            base.graphicsEngine.removeWindow(self.buffer)
            self.buffer = None
            self.bg.detachNode()
            self.glow.detachNode()
            self.cam.removeNode()
            self.cam = None
        


