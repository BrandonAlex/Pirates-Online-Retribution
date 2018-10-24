from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, ColorInterpolationManager
from panda3d.core import ModelNode, Point3, Vec3, Vec4
# File: B (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from otp.otpbase import OTPRender
from PooledEffect import PooledEffect
from EffectController import EffectController
import random

class BlackhandCurseSword(PooledEffect, EffectController):
    cardScale = 128.0
    cardScale2 = 64.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.modelParent = self.attachNewNode('ModelParent')
        model = loader.loadModel('models/effects/particleCards')
        self.effectModel = model.find('**/particleWhiteGlow')
        self.effectModel.reparentTo(self.modelParent)
        model = loader.loadModel('models/effects/particleCards')
        self.effectModel2 = model.find('**/particleWhiteGlow')
        self.effectModel2.reparentTo(self.modelParent)
        self.modelParent.setBillboardAxis(0)
        self.modelParent.setBillboardPointWorld()
        self.modelParent.setScale(1.39)
        self.modelParent.setColorScale(0, 0, 0, 1.0)
        self.modelParent.setBin('fixed', 0)
        self.effectActor = Actor.Actor('models/effects/mopath_none', {
            'spin': 'models/effects/mopath_spiral' })
        self.effectActor.setPlayRate(-1.60, 'spin')
        self.effectActor.reparentTo(self)
        self.effectActor.setH(-90)
        self.effectActor.setPos(-0.598, -0.200, 0)
        self.effectActor.setScale(1, 1.2, 1)
        self.effectActor.setBin('fixed', 2)
        self.joint = self.effectActor.find('**/joint1')
        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleEvilSmoke')
        if not self.particleDummy:
            self.particleDummy = render.attachNewNode(ModelNode('FlamingSkullParticleDummy'))
            self.particleDummy.setBin('fixed', 1)

        self.setDepthWrite(0)
        self.setFogOff()
        self.setLightOff()
        self.setColorScaleOff()
        self.hide(OTPRender.ShadowCameraBitmask)
        self.f = ParticleEffect.ParticleEffect('BlackspotCurseSword')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('SphereVolumeEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(64)
        self.p0.setBirthRate(0.200)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(1.2)
        self.p0.factory.setLifespanSpread(0.5)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.200)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(90.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(20.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.001 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.00119 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.00029 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.00029 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.5, 0.5, 0.5, 1.0), Vec4(0, 0, 0, 1.0), 1)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(-0.25)
        self.p0.emitter.setAmplitudeSpread(0.5)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.5))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(0.4)
        self.f2 = ParticleEffect.ParticleEffect('BlackspotPestilence')
        self.f2.reparentTo(self)
        self.p1 = Particles.Particles('particles-1')
        self.p1.setFactory('ZSpinParticleFactory')
        self.p1.setRenderer('SpriteParticleRenderer')
        self.p1.setEmitter('SphereVolumeEmitter')
        self.f2.addParticles(self.p1)
        self.p1.setPoolSize(128)
        self.p1.setBirthRate(0.01)
        self.p1.setLitterSize(2)
        self.p1.setLitterSpread(0)
        self.p1.setSystemLifespan(0.0)
        self.p1.setLocalVelocityFlag(0)
        self.p1.setSystemGrowsOlderFlag(0)
        self.p1.factory.setLifespanBase(1.0)
        self.p1.factory.setLifespanSpread(0.200)
        self.p1.factory.setMassBase(1.0)
        self.p1.factory.setMassSpread(0.0)
        self.p1.factory.setTerminalVelocityBase(400.0)
        self.p1.factory.setTerminalVelocitySpread(0.0)
        self.p1.factory.setInitialAngle(0.0)
        self.p1.factory.setInitialAngleSpread(360.0)
        self.p1.factory.enableAngularVelocity(1)
        self.p1.factory.setAngularVelocity(300.0)
        self.p1.factory.setAngularVelocitySpread(25.0)
        self.p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p1.renderer.setUserAlpha(1.0)
        self.p1.renderer.setFromNode(self.card)
        self.p1.renderer.setXScaleFlag(1)
        self.p1.renderer.setYScaleFlag(1)
        self.p1.renderer.setAnimAngleFlag(1)
        self.p1.renderer.setNonanimatedTheta(0.0)
        self.p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p1.renderer.setAlphaDisable(0)
        self.p1.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.5, 0.5, 0.5, 1.0), Vec4(0, 0, 0, 1.0), 1)
        self.p1.renderer.setInitialXScale(0.001 * self.cardScale2)
        self.p1.renderer.setFinalXScale(0.0001 * self.cardScale2)
        self.p1.renderer.setInitialYScale(0.001 * self.cardScale2)
        self.p1.renderer.setFinalYScale(0.0001 * self.cardScale2)
        self.p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p1.emitter.setAmplitude(0.200)
        self.p1.emitter.setAmplitudeSpread(0.5)
        self.p1.emitter.setOffsetForce(Vec3(0.0, 0.0, -0.450))
        self.p1.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p1.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p1.emitter.setRadius(0.01)


    def createTrack(self):
        self.p0.emitter.setRadius(0.4)
        scalePulse = Sequence(self.effectModel.scaleInterval(0.149, Vec3(1.2, 1.2, 1.2), startScale = Vec3(0.598, 0.598, 0.598), blendType = 'easeIn'), self.effectModel.scaleInterval(0.149, Vec3(0.598, 0.598, 0.598), startScale = Vec3(1.2, 1.2, 1.2), blendType = 'easeOut'))
        self.modelParent.setColorScale(0, 0, 0, 1.0)
        fadeOut = self.modelParent.colorScaleInterval(1.0, Vec4(0, 0, 0, 0), startColorScale = Vec4(0, 0, 0, 1.0), blendType = 'easeIn')
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.0149), Func(self.p0.clearToInitial), Func(self.effectActor.loop, 'spin'), Func(self.f.start, self, self.particleDummy), Func(self.f.reparentTo, self), Func(scalePulse.loop), Func(self.p1.setBirthRate, 0.01), Func(self.p1.clearToInitial), Func(self.f2.start, self.joint, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Func(self.p1.setBirthRate, 100.0), fadeOut, Func(scalePulse.pause), Wait(1.0), Func(self.cleanUpEffect))
        self.track = Sequence(Func(scalePulse.loop), Wait(2.5), self.startEffect, Wait(0.696), Func(self.setOffsetForce), Wait(5.75), Func(self.setOffsetForce), Wait(2.0), Func(self.p0.emitter.setOffsetForce, Vec3(0.0, 0.0, 0.5)), Wait(1.5), self.endEffect)


    def setOffsetForce(self):
        return None
        headPos = localAvatar.headNode.getPos(render)
        handPos = localAvatar.rightHandNode.getPos(render)
        (self.p0.emitter.setOffsetForce(headPos - handPos),)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
