# File: S (Python 2.4)

from pandac.PandaModules import *
from direct.showbase.DirectObject import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
import random
from pirates.piratesbase import PiratesGlobals
from PooledEffect import PooledEffect
from EffectController import EffectController

class ScatterShot(PooledEffect, EffectController):
    cardScale = 64.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('models/effects/particleMaps')
        self.flame = model.find('**/particleFlame')
        self.flame.setBillboardAxis(0)
        self.flame.setPos(0, 0, 1)
        self.flame.reparentTo(self)
        self.flash = model.find('**/particleSpark')
        self.flash.setBillboardPointWorld()
        self.flash.setColorScale(1, 0.69999999999999996, 0.59999999999999998, 1)
        self.flash.reparentTo(self)
        self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()


    def createTrack(self):
        scaleFlame = self.flame.scaleInterval(0.10000000000000001, Vec3(2, 2, 4), startScale = Vec3(6, 6, 8))
        scaleFlash = self.flash.scaleInterval(0.074999999999999997, 5, startScale = 15)
        self.track = Sequence(Func(self.flame.show), Func(self.flash.show), Parallel(scaleFlame, scaleFlash), Func(self.flame.hide), Func(self.flash.hide), Func(self.cleanUpEffect))


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
