from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer
from panda3d.core import ColorBlendAttrib, Point3, Vec3, Vec4
# File: L (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from PooledEffect import PooledEffect
from EffectController import EffectController

class LootSparks(PooledEffect, EffectController):
    cardScale = 64.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleSpark')
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()
        self.setColorScaleOff()
        self.effectColor = Vec4(1, 1, 1, 1)
        self.f = ParticleEffect.ParticleEffect('HealSparks')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('RingEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(16)
        self.p0.setBirthRate(0.100)
        self.p0.setLitterSize(2)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(1.25)
        self.p0.factory.setLifespanSpread(0.25)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1, 1, 1, 1))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(0)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.setEffectScale(1.0)


    def createTrack(self, delay = 0.0):
        self.startEffect = Sequence(Func(self.p0.clearToInitial), Func(self.p0.setBirthRate, 0.12), Func(self.f.start, self, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(3.0), self.endEffect)


    def setEffectScale(self, scale):
        self.p0.renderer.setInitialXScale(0.01 * self.cardScale * scale)
        self.p0.renderer.setFinalXScale(0.002 * self.cardScale * scale)
        self.p0.renderer.setInitialYScale(0.01 * self.cardScale * scale)
        self.p0.renderer.setFinalYScale(0.002 * self.cardScale * scale)
        self.p0.emitter.setAmplitude(-0.299 * scale)
        self.p0.emitter.setAmplitudeSpread(0.4 * scale)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 1.5) * scale)
        self.p0.emitter.setRadius(0.75 * scale)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
        self.adjustIval = None
