from panda3d.core import VBase4
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import *
from pirates.ship import ShipGlobals
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui import GuiPanel, GuiButton
from pirates.piratesbase import PLocalizer
from pirates.piratesgui.ShipBar import ShipTabBar
from pirates.piratesgui.BorderFrame import BorderFrame

class ShipSelectionPanel(GuiPanel.GuiPanel):
    notify = directNotify.newCategory('ShipSelectionPanel')
    width = 1.03
    height = 1.45
    scrollBorder = 0.050000
    OWN = 0
    FRIEND = 1
    CREW = 2
    GUILD = 3
    PUBLIC = 4
    NameMap = {
        OWN: PLocalizer.DinghyMyShip,
        FRIEND: PLocalizer.DinghyFriendShip,
        CREW: PLocalizer.DinghyCrewShip,
        GUILD: PLocalizer.DinghyGuildShip,
        PUBLIC: PLocalizer.DinghyPublicShip }
    charGui = None

    def __init__(self, title, doneCallback, pages = [
        OWN]):
        self.titleText = title
        self.doneCallback = doneCallback
        self.pages = pages[:]
        self.scrollFrame = None
        self.shipFrames = {} #dict(lambda [outmost-iterable]: for page in [outmost-iterable]:
#(page, [])(self.pages))
        self.closeButton = None
        self.page = -1
        self.tabBackParent = None
        self.tabFrontParent = None
        GuiPanel.GuiPanel.__init__(self, '', ShipSelectionPanel.width + self.scrollBorder, self.height, showClose = False)
        self.initialiseoptions(ShipSelectionPanel)
        self.setPos(-1.21, 0, -0.680000)
        self.createGui()

    def destroyGui(self):
        if getattr(self, 'title', 0):
            self.title.destroy()
            self.title = None

        if getattr(self, 'scrollFrame', 0):
            self.scrollFrame.destroy()
            self.scrollFrame = None

        self.shipFrames = {} #dict(lambda [outmost-iterable]: for page in [outmost-iterable]:
#(page, [])(self.pages))
        if getattr(self, 'shipBar', 0):
            self.shipBar.destroy()
            self.shipBar = None

        if self.tabBackParent:
            self.tabBackParent.remove_node()
            self.tabBackParent = None

        if self.tabFrontParent:
            self.tabFrontParent.remove_node()
            self.tabFrontParent = None

        if getattr(self, 'closeButton', 0):
            self.closeButton.destroy()
            self.closeButton = None

    def resetGui(self):
        self.destroyGui()
        self.createGui()

    def destroy(self):
        self.destroyGui()
        self.titleText = None
        self.doneCallback = None
        GuiPanel.GuiPanel.destroy(self)

    def createGui(self):
        self.destroyGui()
        box = loader.loadModel('models/gui/gui_title_box').find('**/gui_title_box_top')
        box.setPos(0.540000, 0, 1.36)
        box.setScale(0.25)
        box.reparentTo(self)
        box.flattenStrong()
        if not self.charGui:
            self.charGui = loader.loadModel('models/gui/char_gui')

        self.title = DirectLabel(parent = self, relief = None, text = self.titleText, text_fg = PiratesGuiGlobals.TextFG1, text_font = PiratesGlobals.getPirateFont(), text_scale = PiratesGuiGlobals.TextScaleTitleSmall, text_shadow = PiratesGuiGlobals.TextShadow, pos = (self.width * 0.5, 0, 1.343))
        self.tabBackParent = self.attachNewNode('tabBackParent')
        self.tabBackParent.setZ(1.11)
        self.scrollFrame = DirectScrolledFrame(parent = self, relief = None, state = DGG.NORMAL, manageScrollBars = 0, autoHideScrollBars = 1, frameSize = (0.050000, self.width - 0.100, 0.140, self.height - 0.25), canvasSize = (0.050000, self.width - 0.100, 0.140, self.height - 0.25), verticalScroll_relief = None, verticalScroll_image = self.charGui.find('**/chargui_slider_small'), verticalScroll_frameSize = (0.0, PiratesGuiGlobals.ScrollbarSize, 0.141, self.height - 0.260), verticalScroll_image_scale = (self.height - 0.299, 1, 0.75), verticalScroll_image_hpr = (0, 0, 90), verticalScroll_image_pos = (self.width - PiratesGuiGlobals.ScrollbarSize * 0.5 - 0.0598, 0, self.height * 0.46), verticalScroll_image_color = (0.609, 0.598, 0.598, 1), verticalScroll_thumb_image = (self.charGui.find('**/chargui_slider_node'), self.charGui.find('**/chargui_slider_node_down'), self.charGui.find('**/chargui_slider_node_over')), verticalScroll_thumb_relief = None, verticalScroll_thumb_image_scale = 0.4, verticalScroll_thumb_image_pos = (-0.00500, 0, 0), verticalScroll_resizeThumb = 0, horizontalScroll_relief = None)
        self.scrollFrame.verticalScroll.incButton.destroy()
        self.scrollFrame.verticalScroll.decButton.destroy()
        self.scrollFrame.horizontalScroll.incButton.destroy()
        self.scrollFrame.horizontalScroll.decButton.destroy()
        self.scrollFrame.horizontalScroll.hide()
        self.accept('press-wheel_up-%s' % self.scrollFrame.guiId, self.mouseWheelUp)
        self.accept('press-wheel_down-%s' % self.scrollFrame.guiId, self.mouseWheelDown)
        self.tabFrontParent = self.attachNewNode('tabFrontParent')
        self.tabFrontParent.setZ(1.11)
        frameSize = (self.scrollFrame['frameSize'][0] + 0.01, self.scrollFrame['frameSize'][1] + 0.0400, self.scrollFrame['frameSize'][2] - 0.01, self.scrollFrame['frameSize'][3])
        self.repackScrollFrame()
        self.border = BorderFrame(parent = self.scrollFrame, state = DGG.DISABLED, modelName = 'general_frame_f', frameSize = frameSize, borderScale = 0.149, showBackground = True, bgColorScale = VBase4(0, 0, 0, 1), sortOrder = -1)
        gui = loader.loadModel('models/gui/toplevel_gui')
        geomX = gui.find('**/generic_x')
        self.closeButton = GuiButton.GuiButton(parent = self, pos = (self.width / 2.0, 0, 0.070), text = PLocalizer.TableLeave, text_scale = PiratesGuiGlobals.TextScaleLarge, text_pos = (0.035000, -0.014), textMayChange = 0, geom = (geomX,) * 4, geom_pos = (-0.0598, 0, 0), geom_scale = 0.5, geom0_color = PiratesGuiGlobals.ButtonColor3[0], geom1_color = PiratesGuiGlobals.ButtonColor3[1], geom2_color = PiratesGuiGlobals.ButtonColor3[2], geom3_color = PiratesGuiGlobals.ButtonColor3[3], image3_color = (0.800000, 0.800000, 0.800000, 1), command = self.closePanel)
        self.shipBar = ShipTabBar(self.tabBackParent, self.tabFrontParent, parent = self)
        for t in self.pages:
            self.addTab(t)

        self.refreshTabStates()

    def mouseWheelUp(self, task = None):
        if self.scrollFrame.verticalScroll.isHidden():
            return None

        amountScroll = 0.050000
        if self.scrollFrame.verticalScroll['value'] > 0:
            self.scrollFrame.verticalScroll['value'] -= amountScroll

    def mouseWheelDown(self, task = None):
        if self.scrollFrame.verticalScroll.isHidden():
            return None

        amountScroll = 0.050000
        if self.scrollFrame.verticalScroll['value'] < 1.0:
            self.scrollFrame.verticalScroll['value'] += amountScroll

    def repackScrollFrame(self):
        self.scrollFrame.getCanvas().getChildren().detach()
        frames = self.shipFrames.get(self.page, [])
        if len(frames) < 3:
            xOffset = 0.0918
        else:
            xOffset = 0.08
        padding = 0.02
        canvasHeight = self.scrollBorder - padding
        for frame in frames:
            canvasHeight += frame.getHeight() + padding

        self.scrollFrame['frameSize'] = (self.scrollBorder, ShipSelectionPanel.width, 0.140, self.height - 0.260)
        zStep = -padding
        for frame in frames:
            frame.reparentTo(self.scrollFrame.getCanvas())
            zStep += frame.getHeight() + padding
            frame.setPos(xOffset, 0, canvasHeight - zStep)

        self.scrollFrame['canvasSize'] = (self.scrollBorder, ShipSelectionPanel.width - 0.089, self.scrollBorder, canvasHeight)
        self.scrollFrame['verticalScroll_value'] = 0

    def closePanel(self):
        GuiPanel.GuiPanel.closePanel(self)
        if self.doneCallback:
            self.doneCallback()

    def _addFrame(self, pageId, shipFrame, index = None):
        list = self.shipFrames[pageId]
        if shipFrame in list and index is not None:
            list.remove(shipFrame)

        if shipFrame not in list:
            if index is None:
                list.append(shipFrame)
            else:
                list.insert(index, shipFrame)

        if self.page == pageId:
            self.repackScrollFrame()
        elif shipFrame not in self.shipFrames.get(self.page, []):
            shipFrame.detachNode()

        if self.page == -1:
            self.setPage(pageId)

        self.refreshTabStates()

    def addFrame(self, shipFrame, index = None):
        self._addFrame(self.OWN, shipFrame, index)

    def addFrameOwn(self, shipFrame, index = None):
        self.addFrame(shipFrame, index)

    def addFrameCrew(self, shipFrame, index = None):
        self._addFrame(self.CREW, shipFrame, index)

    def addFrameFriend(self, shipFrame, index = None):
        self._addFrame(self.FRIEND, shipFrame, index)

    def addFrameGuild(self, shipFrame, index = None):
        self._addFrame(self.GUILD, shipFrame, index)

    def addFramePublic(self, shipFrame, index = None):
        self._addFrame(self.PUBLIC, shipFrame, index)

    def removeFrame(self, frame):
        removed = False
        for frameList in self.shipFrames.itervalues():
            if frame in frameList:
                frameList.remove(frame)
                removed = True
                continue

        if removed:
            frame.destroy()
            self.repackScrollFrame()
            self.refreshTabStates()

    def hasFrame(self, shipDoId):
        return bool(self.getFrame(shipDoId))

    def getFrame(self, shipDoId):
        for frameList in self.shipFrames.itervalues():
            for frame in frameList:
                if frame['shipId'] == shipDoId:
                    return frame
                    continue

    def getFrameIndex(self, frame):
        for frameList in self.shipFrames.itervalues():
            for (num, currFrame) in enumerate(frameList):
                if currFrame is frame:
                    return num
                    continue

        return 0

    def setPage(self, id):
        if id != self.page:
            for frame in self.shipFrames.get(self.page, []):
                frame.detachNode()

            self.page = id
            self.shipBar.selectTab(self.NameMap[id])
            for frame in self.shipFrames[self.page]:
                self._addFrame(self.page, frame)

            self.repackScrollFrame()

    def addTab(self, id):
        self.shipBar.addTab(name = self.NameMap[id], command = self.setPage, extraArgs = [
            id], textpos = (0.100, 0.0299, 0))

    def refreshTabStates(self):
        for (id, frames) in self.shipFrames.iteritems():
            if frames:
                self.shipBar.getTab(self.NameMap[id]).setTextBright(True)
                continue
            self.shipBar.getTab(self.NameMap[id]).setTextBright(False)
