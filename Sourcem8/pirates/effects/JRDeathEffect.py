# File: J (Python 2.4)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from EffectController import EffectController
from PooledEffect import PooledEffect
import random

class JRDeathEffect(PooledEffect, EffectController):
    card2Scale = 64.0
    cardScale = 64.0

    def __init__(self, parent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if parent is not None:
            self.reparentTo(parent)

        if not JRDeathEffect.particleDummy:
            JRDeathEffect.particleDummy = render.attachNewNode(ModelNode('JRDeathEffectParticleDummy'))
            JRDeathEffect.particleDummy.setColorScaleOff()
            JRDeathEffect.particleDummy.setLightOff()
            JRDeathEffect.particleDummy.setFogOff()
            JRDeathEffect.particleDummy.setDepthWrite(0)

        self.effectScale = 1.0
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/particleEvilSmoke')
        self.card2 = model.find('**/particleWhiteSmoke')
        self.f = ParticleEffect.ParticleEffect('JRDeathEffect')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('SphereSurfaceEmitter')
        self.p1 = Particles.Particles('particles-2')
        self.p1.setFactory('PointParticleFactory')
        self.p1.setRenderer('SpriteParticleRenderer')
        self.p1.setEmitter('RingEmitter')
        self.f.addParticles(self.p0)
        self.f.addParticles(self.p1)
        f0 = ForceGroup.ForceGroup('gravity')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, -20.0), 1.0, 1)
        force0.setActive(1)
        f0.addForce(force0)
        f1 = ForceGroup.ForceGroup('Noise')
        force1 = LinearNoiseForce(1.0, 0)
        force1.setVectorMasks(1, 1, 1)
        force1.setActive(1)
        f1.addForce(force1)
        self.f.addForceGroup(f0)
        self.f.addForceGroup(f1)
        self.p0.setPoolSize(128)
        self.p0.setBirthRate(5.0)
        self.p0.setLitterSize(128)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(1.75)
        self.p0.factory.setLifespanSpread(0.5)
        self.p0.factory.setMassBase(4.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(90.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(500.0)
        self.p0.factory.setAngularVelocitySpread(100.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingColor, ColorBlendAttrib.OOne)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 0.59999999999999998, Vec4(1.0, 1.0, 0.20000000000000001, 1.0), Vec4(0.80000000000000004, 0.59999999999999998, 0.25, 0.75), 1)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.59999999999999998, 1.0, Vec4(0.80000000000000004, 0.59999999999999998, 0.25, 0.75), Vec4(0.5, 0.25, 0.0, 0.0), 1)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(1.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 7.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(1.0)
        self.p1.setPoolSize(128)
        self.p1.setBirthRate(0.01)
        self.p1.setLitterSize(3)
        self.p1.setLitterSpread(0)
        self.p1.setSystemLifespan(0.0)
        self.p1.setLocalVelocityFlag(1)
        self.p1.setSystemGrowsOlderFlag(0)
        self.p1.factory.setLifespanBase(1.8)
        self.p1.factory.setLifespanSpread(0.20000000000000001)
        self.p1.factory.setMassBase(1.0)
        self.p1.factory.setMassSpread(0.20000000000000001)
        self.p1.factory.setTerminalVelocityBase(400.0)
        self.p1.factory.setTerminalVelocitySpread(0.0)
        self.p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p1.renderer.setUserAlpha(1.0)
        self.p1.renderer.setFromNode(self.card2)
        self.p1.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p1.renderer.setXScaleFlag(1)
        self.p1.renderer.setYScaleFlag(1)
        self.p1.renderer.setAnimAngleFlag(0)
        self.p1.renderer.setNonanimatedTheta(0.0)
        self.p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p1.renderer.setAlphaDisable(0)
        self.p1.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.5, 0.59999999999999998, 0.14999999999999999, 1.0), Vec4(0.59999999999999998, 0.75, 0.0, 0.0), 1)
        self.p1.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
        self.p1.emitter.setAmplitudeSpread(0.0)
        self.p1.emitter.setOffsetForce(Vec3(0.0, 0.0, 10.0))
        self.p1.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 0.0))
        self.p1.emitter.setRadiateOrigin(Point3(0.0, 0.0, 10.0))
        self.p1.emitter.setRadius(1.0)
        self.p1.emitter.setRadiusSpread(0.0)


    def setupSize(self):
        self.p0.renderer.setInitialXScale(0.050000000000000003 * self.effectScale * self.card2Scale)
        self.p0.renderer.setFinalXScale(0.029999999999999999 * self.effectScale * self.card2Scale)
        self.p0.renderer.setInitialYScale(0.029999999999999999 * self.effectScale * self.card2Scale)
        self.p0.renderer.setFinalYScale(0.080000000000000002 * self.effectScale * self.card2Scale)
        self.p1.renderer.setInitialXScale(0.025000000000000001 * self.effectScale * self.card2Scale)
        self.p1.renderer.setFinalXScale(0.050000000000000003 * self.effectScale * self.card2Scale)
        self.p1.renderer.setInitialYScale(0.025000000000000001 * self.effectScale * self.card2Scale)
        self.p1.renderer.setFinalYScale(0.050000000000000003 * self.effectScale * self.card2Scale)
        self.p1.emitter.setAmplitude(8.0 * self.effectScale)


    def createTrack(self):
        self.startEffect = Sequence(Func(self.setupSize), Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.p1.setBirthRate, 0.01), Func(self.p1.clearToInitial), Func(self.f.start, self, self.particleDummy))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100), Func(self.p1.setBirthRate, 100), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(1.0), self.endEffect)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
