# File: S (Python 2.4)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from pirates.piratesgui.GameOptions import Options
from PooledEffect import PooledEffect
from EffectController import EffectController
import random

class ShipFire(PooledEffect, EffectController):
    cardScale = 64.0

    def __init__(self, effectParent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if effectParent:
            self.reparentTo(effectParent)

        self.duration = 10.0
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/particleFire2')
        self.setDepthWrite(0)
        self.setFogOff()
        self.setLightOff()
        self.setColorScaleOff()
        self.setBin('fixed', 60)
        self.f = ParticleEffect.ParticleEffect('ShipFire')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('LineEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(48)
        self.p0.setBirthRate(0.01)
        self.p0.setLitterSize(2)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.setFloorZ(-1.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(360.0)
        self.p0.factory.setLifespanBase(0.75)
        self.p0.factory.setLifespanSpread(0.25)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(350.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 0.90000000000000002, 0.90000000000000002, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(1.0, 0.59999999999999998, 0.20000000000000001, 1.0), Vec4(0.5, 0.20000000000000001, 0.20000000000000001, 0.5), 1)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(-0.75)
        self.p0.emitter.setAmplitudeSpread(0.25)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 10.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.setEffectScale(1.0)


    def createTrack(self, lod = Options.SpecialEffectsHigh):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.f.start, self, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(self.duration), self.endEffect)


    def setScale(self, scale = VBase3(1, 1, 1)):
        self.setEffectScale(scale[0])


    def setEffectScale(self, scale):
        self.p0.renderer.setInitialXScale(0.016 * self.cardScale * scale)
        self.p0.renderer.setInitialYScale(0.016 * self.cardScale * scale)
        self.p0.renderer.setFinalXScale(0.01 * self.cardScale * scale)
        self.p0.renderer.setFinalYScale(0.01 * self.cardScale * scale)
        self.p0.emitter.setAmplitude(-0.80000000000000004 * scale)
        self.p0.emitter.setAmplitudeSpread(0.25 * scale)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 4.0) * scale)
        self.p0.emitter.setEndpoint1(Point3(-2.5 * scale, 0.0, 0.0))
        self.p0.emitter.setEndpoint2(Point3(2.5 * scale, 0.0, 0.0))


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
