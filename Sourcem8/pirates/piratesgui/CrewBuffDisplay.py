# File: C (Python 2.4)

from pandac.PandaModules import *
from direct.showbase import DirectObject
from direct.gui.DirectGui import *
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui.BorderFrame import BorderFrame
from pirates.piratesbase import PiratesGlobals
from pirates.battle import WeaponGlobals
from pirates.uberdog.UberDogGlobals import InventoryType
from pirates.piratesgui.SkillRing import SkillRing

class CrewBuffDisplay(DirectFrame):

    def __init__(self, parent, skillIcon = None, duration = 10, buffName = '', buffDesc = '', **kw):
        DirectFrame.__init__(self, parent)
        self.dummyFrame = None
        self.skillRingFrame = None
        self.skillIconFrame = None
        self.buffNameFrame = None
        self.buffDescFrame = None
        self.buffTitle = None
        self.skillIcon = skillIcon
        self.duration = duration
        self.currTime = duration
        self.buffName = buffName
        self.buffDesc = buffDesc
        self.skillRingIval = None
        self.runInIval = None
        self.loadGui()


    def destroy(self):
        self.ignoreAll()
        if self.skillRingFrame:
            self.skillRingFrame.destroy()
            self.skillRingFrame = None

        if self.skillIconFrame:
            self.skillIconFrame.destroy()
            self.skillIconFrame = None

        if self.buffNameFrame:
            self.buffNameFrame.destroy()
            self.buffNameFrame = None

        if self.buffDescFrame:
            self.buffDescFrame.destroy()
            self.buffDescFrame = None

        if self.buffTitle:
            self.buffTitle.destroy()
            self.buffTitle = None

        if self.dummyFrame:
            self.dummyFrame.destroy()
            self.dummyFrame = None

        DirectFrame.destroy(self)


    def loadGui(self):
        self.dummyFrame = DirectFrame(parent = self, relief = None, pos = (-0.42999999999999999, 0, 1.3799999999999999), sortOrder = -1000)
        self.skillRingFrame = SkillRing(color = Vec4(1, 1, 0, 1))
        self.skillRingFrame.reparentTo(self.dummyFrame)
        self.skillRingFrame.setPos(-0.089999999999999997, 0, -0.029999999999999999)
        self.skillIconFrame = DirectFrame(parent = self.skillRingFrame, pos = (0, 0, 0), relief = None, image = self.skillIcon, image_scale = (0.14000000000000001, 1, 0.14000000000000001))
        self.buffTitle = DirectFrame(parent = self.dummyFrame, relief = None, pos = (-0.16, 0, 0.080000000000000002), text = PLocalizer.CrewBuffCaptainOrder, text_align = TextNode.ALeft, text_scale = 0.050000000000000003, text_pos = (0, 0), text_fg = PiratesGuiGlobals.TextFG13, text_wordwrap = 15, text_shadow = (0, 0, 0, 1), textMayChange = 0, text_font = PiratesGlobals.getInterfaceFont())
        self.buffNameFrame = DirectFrame(parent = self.dummyFrame, relief = None, pos = (0.0, 0, 0.0), text = self.buffName, text_align = TextNode.ALeft, text_scale = 0.047, text_pos = (0, 0), text_fg = PiratesGuiGlobals.TextFG1, text_wordwrap = 15, text_shadow = (0, 0, 0, 1), textMayChange = 0, text_font = PiratesGlobals.getInterfaceFont())
        self.buffDescFrame = DirectFrame(parent = self.dummyFrame, relief = None, pos = (0.0, 0, -0.044999999999999998), text = self.buffDesc, text_align = TextNode.ALeft, text_scale = 0.036999999999999998, text_pos = (0, 0), text_fg = PiratesGuiGlobals.TextFG2, text_wordwrap = 15, text_shadow = (0, 0, 0, 1), textMayChange = 0, text_font = PiratesGlobals.getInterfaceFont())


    def createSkillRingIval(self):
        self.skillRingIval = Sequence(Func(self.skillRingFrame.meterFaceHalf1.setColor, self.skillRingFrame.meterActiveColor, 100), Func(self.skillRingFrame.meterFaceHalf2.setColor, self.skillRingFrame.meterActiveColor, 100), Func(self.skillRingFrame.meterFaceHalf1.setR, -180), Func(self.skillRingFrame.meterFaceHalf2.setR, 0), Func(self.skillRingFrame.meterFaceHalf1.show), Func(self.skillRingFrame.meterFaceHalf2.show), LerpFunc(self.skillRingFrame.meterFaceHalf2.setR, self.duration / 2, 0, 180), Func(self.skillRingFrame.meterFaceHalf2.setColor, Vec4(0, 0, 0, 1), 100), Func(self.skillRingFrame.meterFaceHalf2.setR, 0), LerpFunc(self.skillRingFrame.meterFaceHalf1.setR, self.duration / 2, -180, 0), Func(self.hide))


    def play(self):
        if not self.runInIval:
            self.runInIval = self.dummyFrame.posInterval(0.40000000000000002, Vec3(-0.42999999999999999, 0, 1.3799999999999999), startPos = Vec3(0.0, 0, 1.3799999999999999))

        self.runInIval.start()
        if not self.skillRingIval:
            self.createSkillRingIval()

        if self.skillRingIval:
            self.skillRingIval.start()



    def stop(self):
        if self.skillRingIval:
            self.skillRingIval.pause()
            self.skillRingIval = None

        if self.runInIval:
            self.runInIval.pause()
            self.runInIval = None
