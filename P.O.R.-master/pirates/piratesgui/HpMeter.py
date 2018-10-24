from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from pirates.reputation import ReputationGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import PiratesGlobals

class HpMeter(DirectFrame):
    FADEOUT_TIME = 8.0

    def __init__(self, name = '', width = 0.40000000000000002, height = 0.025000000000000001, fadeOut = 0, parent = None, originAtMidPt = False):
        DirectFrame.__init__(self, relief = None, parent = parent)
        self.initialiseoptions(HpMeter)
        self.fadeOut = fadeOut
        self.level = 0
        self.value = 0
        self.max = 0
        self.name = name
        self.doId = 0
        self.fader = None
        self.categoryLabel = DirectLabel(parent = self, relief = None, text = self.name, text_scale = height + 0.0050000000000000001, text_align = TextNode.ALeft, text_fg = PiratesGuiGlobals.TextFG1, text_shadow = PiratesGuiGlobals.TextShadow, pos = (0, 0, height + 0.014999999999999999), textMayChange = 1, text_font = PiratesGlobals.getPirateOutlineFont())
        if originAtMidPt:
            meterPos = (-width / 2.0, 0, 0)
        else:
            meterPos = (0, 0, 0)
        self.meter = DirectWaitBar(parent = self, relief = DGG.RAISED, borderWidth = (0.0040000000000000001, 0.0040000000000000001), range = self.max, value = self.value, frameColor = (0, 0, 0, 1), barColor = (0.10000000000000001, 0.10000000000000001, 0.69999999999999996, 1), pos = meterPos, frameSize = (0, width, 0, height))
        self.valueLabel = DirectLabel(parent = self.meter, relief = None, text = '', text_scale = PiratesGuiGlobals.TextScaleTiny, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, pos = (0.20000000000000001, 0, 0.0050000000000000001), textMayChange = 1)
        self.update(self.value, self.max)
        if not base.config.GetBool('display-enemyHp', 0):
            self.valueLabel.hide()



    def destroy(self):
        taskMgr.remove('hpMeterHideTask')
        if self.fader:
            self.fader.pause()

        self.fader = None
        DirectFrame.destroy(self)


    def update(self, value, maxVal):
        if self.fader:
            self.fader.pause()

        self.fader = None
        self.value = max(value, 0)
        self.max = maxVal
        self.showMeter()
        self.valueLabel['text'] = '%s / %s' % (self.value, self.max)
        self.meter['range'] = self.max
        self.meter['value'] = self.value
        if not self.max:
            return None

        hpFraction = float(self.value) / float(self.max)
        if hpFraction >= 0.5:
            self.meter['barColor'] = (0.10000000000000001, 0.69999999999999996, 0.10000000000000001, 1)
        elif hpFraction >= 0.25:
            self.meter['barColor'] = (1.0, 1.0, 0.10000000000000001, 1)
        else:
            self.meter['barColor'] = (1.0, 0.0, 0.0, 1)
        if self.fadeOut:
            taskMgr.remove('hpMeterHideTask')
            taskMgr.doMethodLater(self.FADEOUT_TIME, self.hidePopup, 'hpMeterHideTask')



    def setMeterName(self, name, level, doId):
        self.name = name
        self.level = level
        self.doId = doId
        name = '%s  \x01smallCaps\x01%s%s\x02' % (self.name, PLocalizer.Lv, self.level)
        self.categoryLabel['text'] = name


    def hidePopup(self, task):
        if self.fader:
            self.fader.pause()

        self.fader = None
        fadeOut = LerpFunctionInterval(self.setAlphaScale, fromData = self.getColorScale()[3], toData = 0, duration = 1.0)
        self.fader = Sequence(fadeOut, Func(self.hideMeter))
        self.fader.start()


    def showMeter(self):
        self.show()
        self.setAlphaScale(1.0)


    def hideMeter(self):
        self.hide()


