from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, ColorInterpolationManager
from panda3d.core import ColorBlendAttrib, Point3, Vec3, Vec4
# File: H (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from PooledEffect import PooledEffect
from EffectController import EffectController
import random

class HellFire(PooledEffect, EffectController):
    cardScale = 128.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/effectSoftGlow')
        self.card2 = model.find('**/particleFire')
        self.speed = 20.0
        self.setDepthWrite(0)
        self.setLightOff()
        self.f = ParticleEffect.ParticleEffect('HellFire')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('RingEmitter')
        self.p1 = Particles.Particles('particles-2')
        self.p1.setFactory('ZSpinParticleFactory')
        self.p1.setRenderer('SpriteParticleRenderer')
        self.p1.setEmitter('SphereSurfaceEmitter')
        self.f.addParticles(self.p0)
        self.f.addParticles(self.p1)
        self.p0.setPoolSize(128)
        self.p0.setBirthRate(0.0299)
        self.p0.setLitterSize(16)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(1.5)
        self.p0.factory.setLifespanSpread(0.5)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(0)
        self.p0.renderer.setInitialXScale(0.0149 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.0299 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.0149 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.0299 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingColor, ColorBlendAttrib.OOneMinusIncomingAlpha)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(1.0, 0.348, 0.0, 1.0), Vec4(0.0, 0.0, 0.0, 0.0), 1)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(10.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, -4.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(0.5)
        self.p1.setPoolSize(128)
        self.p1.setBirthRate(0.200)
        self.p1.setLitterSize(1)
        self.p1.setLitterSpread(0)
        self.p1.setSystemLifespan(0.0)
        self.p1.setLocalVelocityFlag(1)
        self.p1.setSystemGrowsOlderFlag(0)
        self.p1.factory.setLifespanBase(1.2)
        self.p1.factory.setLifespanSpread(0.5)
        self.p1.factory.setMassBase(1.0)
        self.p1.factory.setMassSpread(0.200)
        self.p1.factory.setTerminalVelocityBase(400.0)
        self.p1.factory.setTerminalVelocitySpread(0.0)
        self.p1.factory.setInitialAngle(0.0)
        self.p1.factory.setInitialAngleSpread(20.0)
        self.p1.factory.enableAngularVelocity(1)
        self.p1.factory.setAngularVelocity(0.0)
        self.p1.factory.setAngularVelocitySpread(0.0)
        self.p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p1.renderer.setUserAlpha(1.0)
        self.p1.renderer.setFromNode(self.card2)
        self.p1.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p1.renderer.setXScaleFlag(1)
        self.p1.renderer.setYScaleFlag(1)
        self.p1.renderer.setAnimAngleFlag(1)
        self.p1.renderer.setInitialXScale(0.02 * self.cardScale)
        self.p1.renderer.setInitialYScale(0.02 * self.cardScale)
        self.p1.renderer.setFinalXScale(0.001 * self.cardScale)
        self.p1.renderer.setFinalYScale(0.001 * self.cardScale)
        self.p1.renderer.setNonanimatedTheta(0.0)
        self.p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
        self.p1.renderer.setAlphaDisable(0)
        self.p1.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OOneMinusFbufferAlpha, ColorBlendAttrib.OOneMinusIncomingAlpha)
        self.p1.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(1.0, 1.0, 1.0, 1.0), Vec4(0, 0, 0, 1.0), 1)
        self.p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p1.emitter.setAmplitude(1.5)
        self.p1.emitter.setAmplitudeSpread(0.5)
        self.p1.emitter.setOffsetForce(Vec3(0.0, 0.0, 10.0))
        self.p1.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p1.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p1.emitter.setRadius(0.5)


    def createTrack(self):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.p1.setBirthRate, 0.01), Func(self.p1.clearToInitial), Func(self.f.start, self, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100), Func(self.p1.setBirthRate, 100), Wait(5.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(0.5), self.endEffect)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
