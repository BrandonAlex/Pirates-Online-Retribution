from otp.otpbase import OTPTimer
from direct.showbase.ShowBaseGlobal import *
from direct.task import Task
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui import GuiButton
import time

class PiratesTimerHourglass(OTPTimer.OTPTimer):
    ClockImage = None
    
    def __init__(self, showMinutes = 0, mode = None, titleText = '', titleFg = None, infoText = '', cancelText = '', cancelCallback = None):
        self.showMinutes = showMinutes
        self.mode = mode
        OTPTimer.OTPTimer.__init__(self)
        self.initialiseoptions(PiratesTimerHourglass)
        self['text_font'] = PiratesGlobals.getPirateOutlineFont()
        self.setFontColor(Vec4(1, 1, 1, 1))
        if titleText or infoText:
            self.createTimerText(titleText, titleFg, infoText)
        
        if cancelCallback:
            self.createCancelButton(cancelCallback, cancelText)
        
        self.getImage()
        self.slide = False

    
    def getImage(self):
        if PiratesTimerHourglass.ClockImage == None:
            model = loader.loadModel('models/gui/toplevel_gui')
            model.setScale(0.80000000000000004)
            model.flattenLight()
            PiratesTimerHourglass.ClockImage = model.find('**/sandclock')
            model.removeNode()
        
        return PiratesTimerHourglass.ClockImage

    
    def setSlide(self, startTime, endTime, startPosition, endPosition):
        self.slide = True
        self.startTime = startTime
        self.endTime = endTime
        self.startPosition = startPosition
        self.endPosition = endPosition

    
    def setTime(self, currTime):
        if currTime < 0:
            currTime = 0
        
        if self.slide:
            time = self.getElapsedTime()
            if time <= self.startTime:
                self.setPos(self.startPosition)
            
            if time > self.startTime and time < self.endTime:
                duration = self.endTime - self.startTime
                delta_time = self.getElapsedTime() - self.startTime
                t = delta_time / duration
                delta = self.endPosition - self.startPosition
                self.setPos(self.startPosition + delta * t)
            
            if time >= self.endTime:
                self.setPos(self.endPosition)
            
        
        if currTime == self.currentTime:
            return None
        
        self.currentTime = currTime
        if currTime > 60 and self.showMinutes:
            t = time.gmtime(currTime)
            timeStr = '%s:%s' % (t[4], str(t[5]).zfill(2))
            self['text_scale'] = 0.29999999999999999
        else:
            timeStr = str(currTime + 1)
            self['text_scale'] = 0.29999999999999999
        timeStrLen = len(timeStr)
        self['text'] = ''
        if currTime <= 5:
            self['text_fg'] = Vec4(1, 0, 0, 1)
        else:
            self['text_fg'] = self.vFontColor
        if len(timeStr) == 1:
            self['text_scale'] = 0.34000000000000002
            self['text_pos'] = (-0.025000000000000001, -0.125)
        elif len(timeStr) == 2:
            self['text_scale'] = 0.27000000000000002
            self['text_pos'] = (-0.025000000000000001, -0.10000000000000001)
        elif len(timeStr) == 3:
            self['text_scale'] = 0.20000000000000001
            self['text_pos'] = (-0.01, -0.080000000000000002)
        
        self['text'] = timeStr

    
    def createTimerText(self, titleText, titleFg, infoText):
        self.titleText = DirectFrame(parent = self, relief = None, text = titleText, text_align = TextNode.ACenter, text_scale = 0.14999999999999999, text_fg = titleFg, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getPirateOutlineFont(), textMayChange = 1, text_wordwrap = 6, pos = (0, 0, 0.69999999999999996))
        self.infoText = DirectFrame(parent = self, relief = None, text = infoText, text_align = TextNode.ACenter, text_scale = 0.14000000000000001, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getPirateOutlineFont(), textMayChange = 1, text_wordwrap = 6, pos = (0, 0, -0.75))

    
    def createCancelButton(self, cancelCallback, cancelText):
        if self.mode != PiratesGlobals.HIGHSEAS_ADV_WAIT:
            return None
        
        if not base.localAvatar.isCrewCaptain():
            return None
        
        self.cancelButton = GuiButton.GuiButton(helpText = cancelText, command = cancelCallback, borderWidth = PiratesGuiGlobals.BorderWidth, text = PLocalizer.Cancel, frameColor = PiratesGuiGlobals.ButtonColor3, text_fg = PiratesGuiGlobals.TextFG2, text_pos = (0, 0.014999999999999999), frameSize = (-0.089999999999999997, 0.089999999999999997, -0.014999999999999999, 0.065000000000000002), text_scale = PiratesGuiGlobals.TextScaleLarge, pad = (0.01, 0.01), parent = self, pos = (0, 0, -1.55), scale = 2.2999999999999998)


