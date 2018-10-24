from panda3d.core import ColorBlendAttrib, Vec4
# File: S (Python 2.4)

from direct.showbase.DirectObject import *
from direct.interval.IntervalGlobal import *
from PooledEffect import PooledEffect
from EffectController import EffectController

class SkullFlash(PooledEffect, EffectController):

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.fadeTime = 0.149
        self.startDelay = 0.0
        self.effectColor = Vec4(1, 1, 1, 1)
        model = loader.loadModel('models/effects/fireworkCards')
        self.effectModel = model.find('**/pir_t_efx_msc_skullGlow')
        self.effectModel.reparentTo(self)
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setBillboardPointWorld()
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()


    def createTrack(self):
        self.effectModel.setColorScale(0, 0, 0, 0)
        fadeBlast = self.effectModel.colorScaleInterval(self.fadeTime, Vec4(0, 0, 0, 0), startColorScale = Vec4(self.effectColor), blendType = 'easeOut')
        scaleBlast = self.effectModel.scaleInterval(self.fadeTime, 2.0, startScale = 1.0, blendType = 'easeOut')
        self.track = Sequence(Wait(self.startDelay), Parallel(fadeBlast, scaleBlast), Func(self.cleanUpEffect))


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
