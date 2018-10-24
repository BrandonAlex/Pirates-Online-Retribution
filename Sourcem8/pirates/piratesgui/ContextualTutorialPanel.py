from direct.gui.DirectGui import *
from pandac.PandaModules import *
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import PLocalizer, PiratesGlobals
from pirates.ship import ShipGlobals
from pirates.piratesgui import GuiButton
from pirates.piratesgui import CheckButton
from pirates.uberdog.UberDogGlobals import InventoryType

class XButton(GuiButton.GuiButton):

    def __init__(self, parent = None, **kw):
        optiondefs = ()
        self.defineoptions(kw, optiondefs)
        GuiButton.GuiButton.__init__(self, parent)
        self.initialiseoptions(XButton)
        mainGui = loader.loadModel('models/gui/gui_main')
        self.glow = OnscreenImage(parent = self, image = mainGui.find('**/icon_glow'), scale = 0.27500000000000002, color = (1.0, 1.0, 1.0, 0.40000000000000002))
        self.glow.hide()
        mainGui.remove_node()
        self.bind(DGG.ENTER, self.highlightOn)
        self.bind(DGG.EXIT, self.highlightOff)


    def highlightOn(self, event):
        self.glow.show()


    def highlightOff(self, event):
        self.glow.hide()



class IgnoreCheck(CheckButton.CheckButton):

    def __init__(self, parent = None, **kw):
        optiondefs = ()
        self.defineoptions(kw, optiondefs)
        CheckButton.CheckButton.__init__(self, parent)
        self.initialiseoptions(IgnoreCheck)
        mainGui = loader.loadModel('models/gui/gui_main')
        self.glow = OnscreenImage(parent = self, image = mainGui.find('**/icon_glow'), scale = 0.22, color = (1.0, 1.0, 1.0, 0.59999999999999998))
        self.glow.hide()
        mainGui.remove_node()
        self.bind(DGG.ENTER, self.highlightOn)
        self.bind(DGG.EXIT, self.highlightOff)


    def setValue(self):
        CheckButton.CheckButton.setValue(self)
        self['geom_hpr'] = (0, 0, 45)
        self['geom_pos'] = (0.02, 0, 0.029999999999999999)
        self['geom_scale'] = 0.40000000000000002
        if hasattr(self, 'glow'):
            self.glow.hide()



    def highlightOn(self, event):
        self.glow.show()
        if not self['value']:
            self['geom'] = self['checkedGeom']
            self['geom_hpr'] = (0, 0, 45)
            self['geom_pos'] = (0.02, 0, 0.029999999999999999)
            self['geom_scale'] = 0.40000000000000002



    def highlightOff(self, event):
        self.glow.hide()
        if not self['value']:
            self['geom'] = None




class ContextualTutorialPanel(DirectFrame):

    def __init__(self):
        topGui = loader.loadModel('models/gui/toplevel_gui')
        mainGui = loader.loadModel('models/gui/gui_main')
        DirectFrame.__init__(self, parent = base.a2dBottomRight, relief = None, pos = (-0.34000000000000002, 0, 0.40000000000000002), frameSize = (-0.25, 0.25, -0.25, 0.25), image = topGui.find('**/pir_t_gui_gen_parchment'), image_scale = (0.315, 0, 0.42499999999999999))
        self.initialiseoptions(ContextualTutorialPanel)
        self.filled = False
        self.contextId = 0
        self.number = 0
        self.type = 0
        self.part = 0
        self.titleLabels = { }
        self.messageLabels = { }
        self.noHintsLabels = { }
        self.bg = OnscreenImage(parent = self, image = mainGui.find('**/background/background_logo'), scale = 0.22, color = (0.42699999999999999, 0.25900000000000001, 0.16800000000000001, 0.40000000000000002), pos = (-0.050000000000000003, 0, 0.10000000000000001))
        self.closeButton = XButton(parent = self, relief = None, pos = (0.25, 0, 0.14999999999999999), image = topGui.find('**/pir_t_gui_gen_Xred'), image_scale = 0.40000000000000002, command = self.closePanel)
        self.noHints = False
        self.noHintsCheck = IgnoreCheck(parent = self, relief = None, image = topGui.find('**/pir_t_gui_gen_box_empty'), checkedGeom = topGui.find('**/pir_t_gui_gen_Check_Red'), pos = (-0.17000000000000001, 0, -0.12), command = self.noHintsCheckCB)
        mainGui.remove_node()
        topGui.remove_node()
        self.hide()


    def setPanel(self, contextId, number, type, part):
        oldData = '%s%s%s' % (self.contextId, self.number, self.part)
        newData = '%s%s%s' % (contextId, number, part)
        if oldData == newData:
            return None

        if oldData in self.titleLabels:
            self.titleLabels[oldData].hide()
            self.messageLabels[oldData].hide()

        self.contextId = contextId
        self.number = number
        self.part = part
        if newData in self.titleLabels:
            self.titleLabels[newData].show()
            self.messageLabels[newData].show()
            self.contextId = contextId
        else:
            title = ''
            message = ''
            if contextId == InventoryType.BuyNewShip:
                if number == 0:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.MERCHANTL1]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.MERCHANTL1]
                elif number == 1:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.WARSHIPL1]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.WARSHIPL1]
                elif number == 2:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.INTERCEPTORL2]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.INTERCEPTORL2]
                elif number == 3:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.MERCHANTL2]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.MERCHANTL2]
                elif number == 4:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.WARSHIPL2]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.WARSHIPL2]
                elif number == 5:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.INTERCEPTORL3]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.INTERCEPTORL3]
                elif number == 6:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.MERCHANTL3]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.MERCHANTL3]
                elif number == 7:
                    title = PLocalizer.ContextPanelTitles.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.WARSHIPL3]
                    message = PLocalizer.ContextPanelMessages.get(contextId) % PLocalizer.ShipClassNames[ShipGlobals.WARSHIPL3]

            elif number:
                title = PLocalizer.ContextPanelTitles.get(contextId).get(number)
                message = PLocalizer.ContextPanelMessages.get(contextId).get(number)
            else:
                title = PLocalizer.ContextPanelTitles.get(contextId)
                message = PLocalizer.ContextPanelMessages.get(contextId)
            if contextId == InventoryType.BrokenHull:
                if part == 1:
                    title = title % PLocalizer.Left
                    message = message % PLocalizer.Left
                else:
                    title = title % PLocalizer.Right
                    message = message % PLocalizer.Right
            elif contextId == InventoryType.SearchableContainers:
                if part == 1:
                    title = title % PLocalizer.ContextTutBuriedTreasure
                else:
                    title = title % PLocalizer.ContextTutSearchableContainers
            elif contextId == InventoryType.NewSkillPoint:
                if part == 1:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.CutlassRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.CutlassRep]
                elif part == 2:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.PistolRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.PistolRep]
                elif part == 3:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.DaggerRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.DaggerRep]
                elif part == 4:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.GrenadeRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.GrenadeRep]
                elif part == 5:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.WandRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.WandRep]
                elif part == 6:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.DollRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.DollRep]
                elif part == 7:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.CannonRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.CannonRep]
                elif part == 8:
                    title = title % PLocalizer.InventoryTypeNames[InventoryType.SailingRep]
                    message = message % PLocalizer.InventoryTypeNames[InventoryType.SailingRep]

            elif contextId == InventoryType.DockCommands and number == 4:
                self.accept('space', self.closePanel)
            elif contextId == InventoryType.ChatPreferences:
                if part == 1:
                    message = message % PLocalizer.SpeedChatPlusPreferences
                else:
                    message = message % PLocalizer.SpeedChatPreferences
            elif contextId == InventoryType.FishingTutorial:
                pass

            if not title:
                return False

            titleLabel = DirectLabel(parent = self, relief = None, text = title, text_align = TextNode.ACenter, text_scale = PiratesGuiGlobals.TextScaleExtraLarge, text_fg = (0.59999999999999998, 0.0, 0.0, 1.0), text_font = PiratesGlobals.getPirateOutlineFont(), text_wordwrap = 8, textMayChange = 1, pos = (0.0, 0, 0.13))
            messageLabel = DirectLabel(parent = self, relief = None, text = message, text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleMed, text_fg = PiratesGuiGlobals.TextFG0, text_font = PiratesGlobals.getPirateFont(), text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 14, textMayChange = 1, pos = (-0.20000000000000001, 0, 0.070000000000000007))
            titleBounds = titleLabel.getBounds()
            messageBounds = messageLabel.getBounds()
            messageLabel.setZ(0.040000000000000001 + titleBounds[2] - (messageBounds[3] + messageBounds[2]) * 0.5)
            if titleBounds[3] - titleBounds[2] > 0.089999999999999997:
                messageLabel.setZ(messageLabel.getZ() + 0.012500000000000001)

            self.filled = True
            self.titleLabels[newData] = titleLabel
            self.messageLabels[newData] = messageLabel
        if self.type in self.noHintsLabels:
            self.noHintsLabels[self.type].hide()

        if type in self.noHintsLabels:
            if contextId in (InventoryType.ChatPreferences, InventoryType.CursedBlades):
                self.noHintsLabels[type].hide()
                self.noHintsCheck.hide()
            else:
                self.noHintsLabels[type].show()
                self.noHintsCheck.show()
        elif self.type in self.noHintsLabels:
            self.noHintsLabels[self.type].hide()

        if contextId in (InventoryType.ChatPreferences, InventoryType.CursedBlades):
            text = ''
        else:
            text = PLocalizer.ContextPanelNoMoreHints % PLocalizer.ContextPanelTypes[type]
        noHintsLabel = DirectLabel(parent = self, relief = None, text = text, text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleSmall, text_fg = PiratesGuiGlobals.TextFG0, textMayChange = 1, pos = (-0.14000000000000001, 0, -0.12))
        if contextId in (InventoryType.ChatPreferences, InventoryType.CursedBlades):
            self.noHintsCheck.hide()
            noHintsLabel.hide()
        else:
            self.noHintsCheck.show()
            noHintsLabel.show()
        self.noHintsLabels[type] = noHintsLabel
        self.type = type
        return True


    def noHintsCheckCB(self, val):
        self.noHints = val


    def isFilled(self):
        return self.filled


    def getContext(self):
        return self.contextId


    def getNumber(self):
        return self.number


    def closePanel(self, args = None):
        if hasattr(base, 'localAvatar') and self.contextId != InventoryType.ChatPreferences:
            if self.noHints:
                base.localAvatar.sendRequestChangeTutType(self.type, 1)

            base.localAvatar.sendRequestSeenContext(self.contextId)

        self.filled = False
        self.noHintsCheck['value'] = 0
        self.noHints = False
        data = '%s%s%s' % (self.contextId, self.number, self.part)
        titleLabel = self.titleLabels.pop(data, 0)
        if titleLabel:
            titleLabel.destroy()

        messageLabel = self.messageLabels.pop(data, 0)
        if messageLabel:
            messageLabel.destroy()

        noHintsLabel = self.noHintsLabels.pop(self.type, 0)
        if noHintsLabel:
            noHintsLabel.destroy()

        self.contextId = 0
        self.number = 0
        self.part = 0
        self.type = 0
        self.hide()


    def destroy(self):
        for data in self.titleLabels:
            self.titleLabels[data].destroy()

        del self.titleLabels
        for data in self.messageLabels:
            self.messageLabels[data].destroy()

        del self.messageLabels
        for type in self.noHintsLabels:
            self.noHintsLabels[type].destroy()

        del self.noHintsLabels
        DirectFrame.destroy(self)
