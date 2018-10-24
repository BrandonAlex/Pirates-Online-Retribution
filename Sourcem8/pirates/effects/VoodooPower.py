# File: V (Python 2.4)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from otp.otpbase import OTPRender
from EffectController import EffectController
from PooledEffect import PooledEffect
import random

class VoodooPower(PooledEffect, EffectController):
    cardScale = 64.0
    card2Scale = 128.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/particleDarkSmoke')
        model = loader.loadModel('models/effects/shockwaves')
        self.card2 = model.find('**/effectFlashRays')
        model = loader.loadModel('models/effects/battleEffects')
        self.card3 = model.find('**/effectVoodooShockwave')
        self.setDepthWrite(0)
        self.setColorScaleOff()
        self.setLightOff()
        self.hide(OTPRender.ShadowCameraBitmask)
        self.scale = 1.0
        self.effectColor = Vec4(1, 1, 1, 1)
        self.expandIval = None
        self.f = ParticleEffect.ParticleEffect('VoodooPower')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('PointEmitter')
        self.p1 = Particles.Particles('particles-2')
        self.p1.setFactory('ZSpinParticleFactory')
        self.p1.setRenderer('SpriteParticleRenderer')
        self.p1.setEmitter('PointEmitter')
        self.p2 = Particles.Particles('particles-3')
        self.p2.setFactory('PointParticleFactory')
        self.p2.setRenderer('SpriteParticleRenderer')
        self.p2.setEmitter('SphereVolumeEmitter')
        self.f.addParticles(self.p0)
        self.f.addParticles(self.p1)
        self.f.addParticles(self.p2)
        self.p0.setPoolSize(128)
        self.p0.setBirthRate(0.01)
        self.p0.setLitterSize(3)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(0.20000000000000001)
        self.p0.factory.setLifespanSpread(0.050000000000000003)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(360.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(0.25)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingColor, ColorBlendAttrib.OOneMinusIncomingAlpha)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(1.0, 1.0, 1.0, 0.5), Vec4(0.75, 0.59999999999999998, 1.0, 0.75), 1)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.001 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.01 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.001 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.02 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(0.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p1.setPoolSize(32)
        self.p1.setBirthRate(100.0)
        self.p1.setLitterSize(1)
        self.p1.setLitterSpread(0)
        self.p1.setSystemLifespan(0.0)
        self.p1.setLocalVelocityFlag(1)
        self.p1.setSystemGrowsOlderFlag(0)
        self.p1.factory.setLifespanBase(0.75)
        self.p1.factory.setLifespanSpread(0.10000000000000001)
        self.p1.factory.setMassBase(1.0)
        self.p1.factory.setMassSpread(0.0)
        self.p1.factory.setTerminalVelocityBase(400.0)
        self.p1.factory.setTerminalVelocitySpread(0.0)
        self.p1.factory.setInitialAngle(0.0)
        self.p1.factory.setInitialAngleSpread(360.0)
        self.p1.factory.enableAngularVelocity(1)
        self.p1.factory.setAngularVelocity(0.0)
        self.p1.factory.setAngularVelocitySpread(0.0)
        self.p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p1.renderer.setUserAlpha(1.0)
        self.p1.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p1.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.10000000000000001, 0.20000000000000001, 1.0, 0.0), Vec4(0.10000000000000001, 0.20000000000000001, 0.75, 1.0), 1)
        self.p1.renderer.setFromNode(self.card2)
        self.p1.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p1.renderer.setXScaleFlag(1)
        self.p1.renderer.setYScaleFlag(1)
        self.p1.renderer.setAnimAngleFlag(1)
        self.p1.renderer.setInitialXScale(0.14999999999999999 * self.card2Scale)
        self.p1.renderer.setFinalXScale(0.0001 * self.card2Scale)
        self.p1.renderer.setInitialYScale(0.14999999999999999 * self.card2Scale)
        self.p1.renderer.setFinalYScale(0.0001 * self.card2Scale)
        self.p1.renderer.setNonanimatedTheta(0.0)
        self.p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p1.renderer.setAlphaDisable(0)
        self.p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p1.emitter.setAmplitude(0.0)
        self.p1.emitter.setAmplitudeSpread(0.0)
        self.p1.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p1.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p1.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p2.setPoolSize(64)
        self.p2.setBirthRate(100.0)
        self.p2.setLitterSize(1)
        self.p2.setLitterSpread(0)
        self.p2.setSystemLifespan(0.0)
        self.p2.setLocalVelocityFlag(0)
        self.p2.setSystemGrowsOlderFlag(0)
        self.p2.factory.setLifespanBase(1.0)
        self.p2.factory.setLifespanSpread(0.0)
        self.p2.factory.setMassBase(1.0)
        self.p2.factory.setMassSpread(0.0)
        self.p2.factory.setTerminalVelocityBase(400.0)
        self.p2.factory.setTerminalVelocitySpread(0.0)
        self.p2.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p2.renderer.setUserAlpha(0.5)
        self.p2.renderer.setFromNode(self.card3)
        self.p2.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p2.renderer.setXScaleFlag(1)
        self.p2.renderer.setYScaleFlag(1)
        self.p2.renderer.setAnimAngleFlag(0)
        self.p2.renderer.setInitialXScale(0.0050000000000000001 * self.card2Scale)
        self.p2.renderer.setFinalXScale(0.012 * self.card2Scale)
        self.p2.renderer.setInitialYScale(0.0050000000000000001 * self.card2Scale)
        self.p2.renderer.setFinalYScale(0.012 * self.card2Scale)
        self.p2.renderer.setNonanimatedTheta(0.0)
        self.p2.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p2.renderer.setAlphaDisable(0)
        self.p2.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.84999999999999998, 0.75, 0.90000000000000002, 0.59999999999999998), Vec4(0.0, 0.0, 0.0, 0.75), 1)
        self.p2.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p2.emitter.setAmplitude(0.20000000000000001)
        self.p2.emitter.setAmplitudeSpread(0.0)
        self.p2.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p2.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p2.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p2.emitter.setRadius(0.14999999999999999)


    def createTrack(self):
        self.scale = 0.10000000000000001
        self.p0.renderer.setInitialXScale(0.0001 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.0001 * self.cardScale)
        self.expandIval = Sequence(Func(self.resize), Wait(0.59999999999999998))
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.f.start, self, self), Func(self.expandIval.loop), Wait(2.0), Func(self.p1.setBirthRate, 0.10000000000000001), Func(self.p1.clearToInitial), Func(self.p2.setBirthRate, 0.029999999999999999), Func(self.p2.clearToInitial), Wait(3.5), Func(self.expandIval.pause))
        self.endEffect = Sequence(Func(self.expandIval.pause), Func(self.p0.setBirthRate, 100.0), Func(self.p1.setBirthRate, 100.0), Func(self.p2.setBirthRate, 100.0), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(0.5), self.endEffect)


    def resize(self):
        if self.p0:
            self.p0.renderer.setFinalXScale(0.02 * self.scale * self.cardScale)
            self.p0.renderer.setFinalYScale(0.029999999999999999 * self.scale * self.cardScale)
            self.scale += 0.10000000000000001



    def setEffectColor(self, color):
        self.effectColor = Vec4(1, 1, 1, 0) - (Vec4(1, 1, 1, 1) - color) / 2.0
        self.p0.renderer.getColorInterpolationManager().clearToInitial()
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(1, 1, 1, 0.5), self.effectColor, 1)
        self.p1.renderer.getColorInterpolationManager().clearToInitial()
        self.p1.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.10000000000000001, 0.20000000000000001, 1.0, 0.0), self.effectColor + Vec4(-0.20000000000000001, -0.10000000000000001, 0, 0.5), 1)
        self.p2.renderer.getColorInterpolationManager().clearToInitial()
        self.p2.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, self.effectColor, Vec4(0.0, 0.0, 0.0, 0.75), 1)


    def cleanUpEffect(self):
        if self.expandIval:
            self.expandIval.pause()
            self.expandIval = None

        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
