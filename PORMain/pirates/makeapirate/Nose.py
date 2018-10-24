global damper
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.ShowBaseGlobal import *
from direct.showbase import DirectObject
from direct.fsm import StateData
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
from pirates.piratesbase import PLocalizer
from CharGuiBase import CharGuiSlider, CharGuiPicker
import random
import MakeAPirateGlobals
damper = 0.5
sliderRange = (-0.5, 0.5)

class Nose(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('Nose')

    def __init__(self, main = None):
        self.main = main.main
        self.parent = main.parent
        self.avatar = main.avatar
        self.mode = None
        self.load()


    def enter(self):
        self.notify.debug('enter')
        self.showNoseCollections()
        self.loadExtraArgs()
        if self.mode == None:
            self.mode = -1



    def exit(self):
        self.hide()


    def load(self):
        self.notify.debug('loading nose')
        self.setupButtons()
        self.loadGUI()
        self.loadExtraArgs()


    def loadGUI(self):
        self.pgs1 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseBridgeWidth, range=(-0.2, 0.8), command = self.updateControlShape)
        self.pgs1.setPos(-0.4, 0, -0.299)
        self.pgs2 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseNostrilWidth, range=(0.0, 0.1), command = self.updateControlShape)
        self.pgs2.setPos(-0.4, 0, -0.550000)
        self.pgs3 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseLength, range=(-0.5, 0.5), command = self.updateControlShape)
        self.pgs3.setPos(-0.4, 0, -0.800000)
        self.pgs4 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseBump, range=(-0.5, 0.5), command = self.updateControlShape)
        self.pgs4.setPos(-0.4, 0, -1.05)
        self.pgs5 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseNostrilAngle, range=(-0.5, 0.5), command = self.updateControlShape)
        self.pgs5.setPos(-0.4, 0, -1.3)
        self.pgs6 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseNostrilHeight, range=(-0.2,0.2), command = self.updateControlShape)
        self.pgs6.setPos(-0.4, 0, -1.55)
        self.pgs7 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseBridgeBroke, range=(-1.0, 1.0), command = self.updateControlShape)
        self.pgs7.setPos(-0.4, 0, -1.8)
        self.pgs8 = CharGuiSlider(self.main, parent = self.noseFrame, text = PLocalizer.NoseNostrilBroke, range=(-1.0, 1.0), command = self.updateControlShape)
        self.pgs8.setPos(-0.4, 0, -2.0498)
        self.pgs = [
            self.pgs1,
            self.pgs2,
            self.pgs3,
            self.pgs4,
            self.pgs5,
            self.pgs6,
            self.pgs7,
            self.pgs8]


    def unload(self):
        self.notify.debug('called Nose unload')
        del self.main
        del self.parent
        del self.avatar


    def loadExtraArgs(self):
        self.pgs1['extraArgs'] = [
            self.pgs1,
            'noseBridgeWidth']
        self.pgs2['extraArgs'] = [
            self.pgs2,
            'noseNostrilWidth']
        self.pgs3['extraArgs'] = [
            self.pgs3,
            'noseLength',
            135]
        self.pgs4['extraArgs'] = [
            self.pgs4,
            'noseBump',
            135]
        self.pgs5['extraArgs'] = [
            self.pgs5,
            'noseNostrilAngle',
            135]
        self.pgs6['extraArgs'] = [
            self.pgs6,
            'noseNostrilHeight',
            135]
        self.pgs7['extraArgs'] = [
            self.pgs7,
            'noseBridgeBroke']
        self.pgs8['extraArgs'] = [
            self.pgs8,
            'noseNostrilBroke']


    def showNoseCollections(self):
        self.noseFrame.show()


    def hideNoseCollections(self):
        self.noseFrame.hide()


    def hide(self):
        self.hideNoseCollections()
        self.saveDNA()


    def setupButtons(self):
        self.noseFrame = DirectFrame(parent = self.parent, relief = None, text = PLocalizer.NoseFrameTitle, text_fg = (1, 1, 1, 1), text_scale = 0.179, text_pos = (0, -0.050000), pos = (0, 0, 0.200), scale = 0.696)
        self.noseFrame.hide()


    def saveDNA(self):
        self.avatar.pirate.setNoseBridgeWidth(self.pgs1.node().getValue())
        self.avatar.pirate.setNoseNostrilWidth(self.pgs2.node().getValue())
        self.avatar.pirate.setNoseLength(self.pgs3.node().getValue())
        self.avatar.pirate.setNoseBump(self.pgs4.node().getValue())
        self.avatar.pirate.setNoseNostrilAngle(self.pgs5.node().getValue())
        self.avatar.pirate.setNoseNostrilHeight(self.pgs6.node().getValue())
        self.avatar.pirate.setNoseBridgeBroke(self.pgs7.node().getValue())
        self.avatar.pirate.setNoseNostrilBroke(self.pgs8.node().getValue())


    def restore(self):
        self.pgs1.node().setValue(self.avatar.dna.getNoseBridgeWidth())
        self.pgs2.node().setValue(self.avatar.dna.getNoseNostrilWidth())
        self.pgs3.node().setValue(self.avatar.dna.getNoseLength())
        self.pgs4.node().setValue(self.avatar.dna.getNoseBump())
        self.pgs5.node().setValue(self.avatar.dna.getNoseNostrilAngle())
        self.pgs6.node().setValue(self.avatar.dna.getNoseNostrilHeight())
        self.pgs7.node().setValue(self.avatar.dna.getNoseBridgeBroke())
        self.pgs8.node().setValue(self.avatar.dna.getNoseNostrilBroke())


    def reset(self):
        for i in xrange(0, len(self.pgs)):
            self.resetSlider(self.pgs[i])

        self.saveDNA()


    def resetSlider(self, slider):
        slider.node().setValue(0.0)


    def randomPick(self):
        global damper
        damper = 1.0
        for i in xrange(0, len(self.pgs)):
            slider = self.pgs[i]
            self.resetSlider(slider)
            if self.avatar.pirate.gender == 'f':
                if slider == self.pgs4:
                    continue
                elif slider == self.pgs7:
                    continue
                elif slider == self.pgs8:
                    continue


            if random.choice([
                0,
                1]):
                value = random.random() * damper
                toss = 0
                if slider['range'][0] < 0:
                    toss = random.choice([
                        0,
                        1])

                if toss:
                    slider.node().setValue(-value)
                else:
                    slider.node().setValue(value)

        self.saveDNA()


    def weightedRandomPick(self):
        if self.avatar.pirate.gender == 'f':
            noseRanges = MakeAPirateGlobals.FEMALE_NOSE_RANGES
        else:
            noseRanges = MakeAPirateGlobals.MALE_NOSE_RANGES
        for i in xrange(0, len(self.pgs)):
            slider = self.pgs[i]
            self.resetSlider(slider)
            coinFlip = random.choice([
                0,
                1,
                1])
            if slider in [
                self.pgs7,
                self.pgs8] and coinFlip:
                value = 0
            else:
                minValue = noseRanges[i][0]
                maxValue = noseRanges[i][1]
                variation = maxValue - minValue
                value = minValue + random.random() * variation
            slider.node().setValue(value)

        self.saveDNA()


    def updateControlShape(self, pgs, extraArgs1 = None, extraArgs2 = None):
        if extraArgs1 != None:
            self.avatar.pirate.setControlValue(pgs.node().getValue(), extraArgs1)

        self.main.handleQuarterView(extraArgs2)
