# File: C (Python 2.4)

from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
from direct.showbase.PythonUtil import Functor
from pandac.PandaModules import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui.TabBar import TopTab, TabBar

class ChatTab(TopTab):

    def __init__(self, tabBar, name, text_xyz = None, **kw):
        optiondefs = (('modelName', 'general_frame_c', None), ('frameSize', (0, 0.22, 0.0, 0.10000000000000001), None), ('borderScale', 0.13500000000000001, None), ('bgBuffer', 0.14000000000000001, None), ('label', name, None), ('textMayChange', 1, None))
        self.defineoptions(kw, optiondefs)
        TopTab.__init__(self, tabBar, name)
        self.initialiseoptions(ChatTab)
        text_pos = (0.11700000000000001, 0.040000000000000001, 0)
        if text_xyz:
            text_pos = text_xyz

        self.myTextScale = PiratesGuiGlobals.TextScaleLarge * 1.1000000000000001
        self.myLabel = DirectLabel(parent = self, relief = None, state = DGG.DISABLED, text = self['label'], text_scale = self.myTextScale, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, text_pos = text_pos, text_font = PiratesGlobals.getInterfaceFont(), textMayChange = 1)


    def destroy(self):
        self.myLabel = None
        TopTab.destroy(self)


    def setBoxWidth(self, percentage):
        iPercentage = 1.0 / percentage
        self.myLabel['text_scale'] = (self.myTextScale * iPercentage, self.myTextScale, self.myTextScale)



class ChatTabBar(TabBar):

    def refreshTabs(self):
        for (x, name) in enumerate(self.tabOrder):
            tab = self.tabs[name]
            tab.setPos(0.070000000000000007 + 0.19500000000000001 * (x + self.offset), 0, 0.059999999999999998)
            tab.reparentTo(self.bParent)

        for name in reversed(self.tabOrder):
            tab = self.tabs[name]
            tab.reparentTo(self.bParent)

        self.activeIndex = max(0, min(self.activeIndex, len(self.tabOrder) - 1))
        if len(self.tabOrder):
            name = self.tabOrder[self.activeIndex]
            tab = self.tabs[name]
            tab.reparentTo(self.fParent)
            tab.setZ(0.076999999999999999)



    def makeTab(self, name, **kw):
        return ChatTab(self, name)


    def stash(self):
        TabBar.stash(self)


    def setBoxWidth(self, percentage):
        for key in self.tabs:
            self.tabs[key].setBoxWidth(percentage)




class WhisperTab(TopTab):

    def __init__(self, tabBar, name, **kw):
        optiondefs = (('modelName', 'general_frame_c', None), ('frameSize', (0, 0.745, 0.0, 0.11), None), ('borderScale', 0.13500000000000001, None), ('bgBuffer', 0.14000000000000001, None))
        self.defineoptions(kw, optiondefs)
        TopTab.__init__(self, tabBar, name)
        self.initialiseoptions(ChatTab)



class WhisperTabBar(TabBar):

    def refreshTabs(self):
        for (x, name) in enumerate(self.tabOrder):
            tab = self.tabs[name]
            tab.setPos(0.070000000000000007 + 0.71999999999999997 * (x + self.offset), 0, 0.059999999999999998)
            tab.reparentTo(self.bParent)

        for name in reversed(self.tabOrder):
            tab = self.tabs[name]
            tab.reparentTo(self.bParent)

        self.activeIndex = max(0, min(self.activeIndex, len(self.tabOrder) - 1))
        if len(self.tabOrder):
            name = self.tabOrder[self.activeIndex]
            tab = self.tabs[name]
            tab.reparentTo(self.fParent)
            tab.setZ(0.076999999999999999)



    def makeTab(self, name, **kw):
        newWhisperTab = WhisperTab(self, name)
        if hasattr(self, 'percentage'):
            newWhisperTab.setBoxWidth(self.percentage)

        return newWhisperTab



class ChatBar(DirectFrame, FSM):

    def __init__(self, parent, chatMgr, whiteListEntry, *args, **kw):
        optiondefs = (('relief', None, None), ('state', DGG.DISABLED, None), ('frameSize', (0, 1, 0, 0.75), None), ('frameColor', (1, 0, 1, 0.20000000000000001), None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent, *args, **kw)
        self.initialiseoptions(ChatBar)
        FSM.__init__(self, 'ChatBar')
        if base.config.GetBool('whitelist-chat-enabled', 0):
            pass
        self.whiteListEnabled = base.cr.accountDetailRecord.WLChatEnabled
        self.openChatEnabled = base.cr.accountDetailRecord.canOpenChatAndNotGetBooted()
        if not self.whiteListEnabled:
            pass
        self.noChat = not (self.openChatEnabled)
        self.chatTabs = None
        self.whisperTabs = None
        self.chatMgr = chatMgr
        self.slideIval = None
        self.whisperNameLabel = None
        self.whisperPrefixLabel = None
        self.percentage = 1.0
        self.iPercentage = 1.0
        self.myTextScale = PiratesGuiGlobals.TextScaleLarge * 1.1000000000000001
        self.setupGui(whiteListEntry)
        self.request('Hidden')


    def destroy(self):
        self.cleanup()
        self.stopSlideIval()
        DirectFrame.destroy(self)
        self.cleanupGui()
        self.chatMgr = None


    def setBoxWidth(self, percentage):
        iPercentage = 1.0 / percentage
        self.setScale(percentage, 1.0, 1.0)
        self.chatTabs.setBoxWidth(percentage)
        self.speedButton.setScale(iPercentage, 1.0, 1.0)
        self.emoteButton.setScale(iPercentage, 1.0, 1.0)
        self.startChatButton.setScale(iPercentage, 1.0, 1.0)
        self.percentage = percentage
        self.iPercentage = iPercentage
        if self.whisperNameLabel:
            self.whisperNameLabel['text_scale'] = (self.myTextScale * iPercentage, self.myTextScale, self.myTextScale)
            self.whisperNameLabel['text_pos'] = (0.20999999999999999 * self.iPercentage, 0.040000000000000001, 0)

        if self.whisperPrefixLabel:
            self.whisperPrefixLabel['text_scale'] = (self.myTextScale * iPercentage, self.myTextScale, self.myTextScale)



    def setupGui(self, whiteListEntry):
        self.stopSlideIval()
        if self.chatTabs:
            self.chatTabs.destroy()

        if self.whisperTabs:
            self.whisperTabs.destroy()

        self.removeChildren()
        gui = loader.loadModel('models/gui/chat_frame_b')
        skullbg = loader.loadModel('models/gui/chat_frame_a')
        skullbg2 = loader.loadModel('models/gui/chat_frame_a')
        skullgui = loader.loadModel('models/gui/chat_frame_skull')
        emoteGfxbg = loader.loadModel('models/gui/chat_frame_a')
        icons = loader.loadModel('models/gui/toplevel_gui')
        charGui = loader.loadModel('models/gui/char_gui')
        scale = Vec3(0.20000000000000001, 1.0, 0.20000000000000001)
        offset = (0.5, 0, 0.38)
        speedChatBg = self.attachNewNode('speedChatBg')
        skullbg.find('**/pPlane11').reparentTo(speedChatBg)
        speedChatBg.setScale(scale)
        speedChatBg.setPos(*offset)
        speedChatBg.flattenStrong()
        emoteBg = self.attachNewNode('emoteBg')
        skullbg2.find('**/pPlane11').reparentTo(emoteBg)
        emoteBg.setScale(scale)
        emoteBg.setPos(0.59099999999999997, 0, 0.38)
        emoteBg.flattenStrong()
        self.chatEntryBackground = self.attachNewNode('chatEntryBackground')
        self.chatEntryBackground.setX(-0.90000000000000002)
        self.backTabParent = self.chatEntryBackground.attachNewNode('backTabs')
        textEntryGeom = self.chatEntryBackground.attachNewNode('textEntryBg')
        gui.find('**/pPlane12').reparentTo(textEntryGeom)
        textEntryGeom.setScale(scale)
        textEntryGeom.setPos(*offset)
        textEntryGeom.flattenStrong()
        self.chatEntryVisNode = textEntryGeom.attachNewNode('chatEntryVis')
        self.chatEntryVisNode.hide()
        self.chatEntryVisNode.setAlphaScale(0)
        whiteListEntry.reparentTo(self.chatEntryVisNode)
        if self.noChat:

            def noshow():
                pass

            whiteListEntry.show = noshow
            whiteListEntry.hide()
        else:
            whiteListEntry.setPos(0.20000000000000001, 0, 0.035999999999999997)
        self.frontTabParent = self.chatEntryBackground.attachNewNode('frontTab', sort = 2)
        self.speedButton = DirectButton(parent = self, relief = None, frameSize = (-0.055, 0.044999999999999998, -0.055, 0.044999999999999998), geom = (icons.find('**/chat_bubble_icon'), icons.find('**/chat_bubble_icon'), icons.find('**/chat_bubble_icon_over')), geom_scale = 0.25, pos = (0.14000000000000001, 0, 0.044999999999999998), rolloverSound = None, command = self.chatMgr.activateSpeedChat)
        self.emoteButton = DirectButton(parent = self, relief = None, frameSize = (-0.055, 0.044999999999999998, -0.055, 0.044999999999999998), geom = (charGui.find('**/*head'), charGui.find('**/*head'), charGui.find('**/*head_over')), geom_scale = 0.29999999999999999, pos = (0.049000000000000002, 0, 0.044999999999999998), rolloverSound = None, command = self.chatMgr.activateEmoteChat)
        tGui = loader.loadModel('models/gui/triangle')
        triangle = (tGui.find('**/triangle'), tGui.find('**/triangle_down'), tGui.find('**/triangle_over'))
        self.startChatButton = DirectButton(parent = self, relief = None, image = triangle, image_scale = 0.065000000000000002, pos = (0.23100000000000001, 0.0, 0.050000000000000003), rolloverSound = None, command = self.chatMgr.activateChat)
        self.chatTabs = ChatTabBar(parent = self, backParent = self.backTabParent, frontParent = self.frontTabParent)
        allTab = self.chatTabs.addTab('All', label = PLocalizer.ChatTabAll, command = self.chatMgr.activateChat, extraArgs = [
            'All'])
        crewTab = self.chatTabs.addTab('Crew', label = PLocalizer.ChatTabCrew, command = self.chatMgr.activateChat, extraArgs = [
            'Crew'])
        guildTab = self.chatTabs.addTab('Guild', label = PLocalizer.ChatTabGuild, command = self.chatMgr.activateChat, extraArgs = [
            'Guild'])
        shipPVPTab = self.chatTabs.addTab('ShipPVP', label = PLocalizer.ChatTabShipPVP, command = self.chatMgr.activateChat, frameSize = (0, 0.23999999999999999, 0.0, 0.10000000000000001), textMayChange = 1, extraArgs = [
            'ShipPVP'])
        self.chatTabs.stash()
        self.whisperTabs = WhisperTabBar(parent = self, backParent = self.backTabParent, frontParent = self.frontTabParent)
        whisperNameTab = self.whisperTabs.addTab('Name')
        whisperCancelTab = self.whisperTabs.addTab('Cancel', command = self.whisperCanceled)
        self.whisperTabs.stash()
        whisperCancelTab['frameSize'] = (0, 0.105, 0.0, 0.11)
        self.whisperPrefixLabel = DirectLabel(parent = whisperNameTab, relief = None, state = DGG.DISABLED, text = PLocalizer.ProfilePageWhisper + ':', text_scale = (self.myTextScale * self.iPercentage, self.myTextScale, self.myTextScale), text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, text_pos = (0.033000000000000002, 0.040000000000000001, 0), text_font = PiratesGlobals.getInterfaceFont())
        DirectLabel(parent = whisperCancelTab, relief = None, state = DGG.DISABLED, text = 'X', text_scale = (self.myTextScale * 1.1799999999999999, self.myTextScale * 1.1799999999999999, self.myTextScale * 1.1799999999999999), text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, text_pos = (0.052999999999999999, 0.042999999999999997, 0), text_font = PiratesGlobals.getInterfaceFont())
        self.whisperTabs.stash()
        self.request('Hidden')


    def cleanupGui(self):
        self.whisperPrefixLabel = None
        self.chatEntryBackground = None
        self.backTabParent = None
        self.frontTabParent = None
        self.speedButton = None
        self.emoteButton = None
        self.startChatButton = None
        if self.chatTabs:
            self.chatTabs.destroy()
            self.chatTabs = None

        if self.whisperTabs:
            self.whisperTabs.destroy()
            self.whisperTabs = None



    def whisperCanceled(self):
        self.chatMgr.whisperCanceled()


    def refreshTabStates(self):
        if self.getCurrentOrNextState() not in ('Off', 'Hidden', 'Whisper'):
            if not self.chatMgr.crewChatAllowed:
                self.chatTabs.getTab('Crew').stash()
            else:
                self.chatTabs.getTab('Crew').unstash()
            if not self.chatMgr.guildChatAllowed:
                self.chatTabs.getTab('Guild').stash()
            else:
                self.chatTabs.getTab('Guild').unstash()
            if not self.chatMgr.shipPVPChatAllowed:
                self.chatTabs.getTab('ShipPVP').stash()
            else:
                self.chatTabs.getTab('ShipPVP').unstash()



    def stopSlideIval(self):
        if self.slideIval and self.slideIval.isPlaying():
            self.slideIval.pause()



    def enterHidden(self):
        self.stopSlideIval()
        self.slideIval = Sequence(Func(self.chatEntryVisNode.setAlphaScale, 0), Func(self.chatEntryVisNode.hide), self.chatEntryBackground.posInterval(0.25, Point3(-0.90000000000000002, 0, 0), blendType = 'easeIn'), Func(self.startChatButton.show), Func(self.chatEntryBackground.hide))
        self.slideIval.start()


    def exitHidden(self):
        self.stopSlideIval()
        self.slideIval = Sequence(Func(self.chatEntryVisNode.show), Func(self.chatEntryBackground.show), Func(self.startChatButton.hide), self.chatEntryBackground.posInterval(0.25, Point3(0, 0, 0), blendType = 'easeOut'), Func(self.chatEntryVisNode.setAlphaScale, 1))
        self.slideIval.start()


    def enterAll(self):
        self.chatTabs.unstash()
        self.whisperTabs.stash()
        self.chatTabs.selectTab('All')
        self.refreshTabStates()


    def exitAll(self):
        pass


    def enterCrew(self):
        self.chatTabs.unstash()
        self.whisperTabs.stash()
        self.chatTabs.selectTab('Crew')
        self.refreshTabStates()


    def exitCrew(self):
        pass


    def enterGuild(self):
        self.chatTabs.unstash()
        self.whisperTabs.stash()
        self.chatTabs.selectTab('Guild')
        self.refreshTabStates()


    def enterShipPVP(self):
        self.chatTabs.unstash()
        self.whisperTabs.stash()
        self.chatTabs.selectTab('ShipPVP')
        self.refreshTabStates()


    def exitShipPVP(self):
        pass


    def exitGuild(self):
        pass


    def enterWhisper(self, avatarName = 'John Sharkbait', whisperId = 0):
        self.whisperName = avatarName
        self.whisperId = whisperId
        self.chatTabs.stash()
        self.whisperTabs.unstash()
        if self.whisperNameLabel:
            self.whisperNameLabel.destroy()

        self.whisperNameLabel = DirectLabel(parent = self.whisperTabs.getTab('Name'), relief = None, state = DGG.DISABLED, text = avatarName, text_scale = (self.myTextScale * self.iPercentage, self.myTextScale, self.myTextScale), text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_pos = (0.20999999999999999 * self.iPercentage, 0.040000000000000001, 0), text_font = PiratesGlobals.getInterfaceFont())


    def exitWhisper(self):
        self.whisperName = ''
        self.whisperId = 0
        if self.whisperNameLabel and 0:
            self.whisperNameLabel.destroy()
            self.whisperNameLabel = None
