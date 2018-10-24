# File: D (Python 2.4)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from PooledEffect import PooledEffect
from EffectController import EffectController
import random

class DomeExplosion(PooledEffect, EffectController):

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.speed = 0.75
        self.size = 40
        self.explosionSequence = 0
        self.explosion = loader.loadModel('models/effects/explosion_sphere')
        self.explosion.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingColor, ColorBlendAttrib.OOneMinusIncomingAlpha))
        self.explosion.setFogOff()
        self.explosion.setLightOff()
        self.explosion.reparentTo(self)
        self.explosion.setDepthWrite(0)
        self.hide()


    def createTrack(self, rate = 1):
        self.explosion.setScale(1)
        self.explosion.setColorScale(0, 0, 0, 0.65000000000000002)
        fadeBlast = self.explosion.colorScaleInterval(self.speed * 0.5, Vec4(0, 0, 0, 0))
        waitFade = Sequence(Wait(self.speed * 0.5), fadeBlast)
        scaleUp = self.explosion.scaleInterval(self.speed, self.size, startScale = 0.0, blendType = 'easeIn', other = render)
        self.track = Sequence(Func(self.show), Parallel(scaleUp, waitFade), Func(self.hide), Func(self.cleanUpEffect))


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
