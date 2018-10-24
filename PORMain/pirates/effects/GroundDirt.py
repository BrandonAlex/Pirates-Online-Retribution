from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, LinearVectorForce
from panda3d.core import Point3, Vec3, Vec4
# File: G (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from EffectController import EffectController
from PooledEffect import PooledEffect

class GroundDirt(PooledEffect, EffectController):
    cardScale = 128.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleRockShower')
        self.effectScale = 1.0
        self.setDepthWrite(0)
        self.setLightOff()
        self.setColorScaleOff()
        self.f = ParticleEffect.ParticleEffect('GroundDirt')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.f.addParticles(self.p0)
        self.f0 = ForceGroup.ForceGroup('Grav')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, -10.0), 1.0, 1)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        self.f0.addForce(force0)
        self.f.addForceGroup(self.f0)
        self.p0.setPoolSize(32)
        self.p0.setBirthRate(0.02)
        self.p0.setLitterSize(3)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(2.0)
        self.p0.factory.setLifespanSpread(1.0)
        self.p0.factory.setMassBase(0.5)
        self.p0.factory.setMassSpread(0.25)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(0.299, 0.200, 0, 1))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(0)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(1.5)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 10.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(1.5)


    def createTrack(self):
        self.p0.renderer.setInitialXScale(0.00500 * self.cardScale * self.effectScale)
        self.p0.renderer.setFinalXScale(0.0074 * self.cardScale * self.effectScale)
        self.p0.renderer.setInitialYScale(0.00500 * self.cardScale * self.effectScale)
        self.p0.renderer.setFinalYScale(0.0074 * self.cardScale * self.effectScale)
        self.track = Sequence(Func(self.p0.setBirthRate, 0.02), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy), Wait(0.299), Func(self.p0.setBirthRate, 100), Wait(5.0), Func(self.cleanUpEffect))


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
