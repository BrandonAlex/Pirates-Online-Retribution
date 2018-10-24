from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, ColorInterpolationManager
from panda3d.core import ColorBlendAttrib, ModelNode, Point3, VBase3, Vec3, Vec4
# File: M (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from PooledEffect import PooledEffect
from EffectController import EffectController
from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx
import random

class MysticFire(PooledEffect, EffectController):
    cardScale = 64.0
    burningSfx = None

    def __init__(self, effectParent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if effectParent:
            self.reparentTo(effectParent)

        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleFire2')
        if not self.burningSfx:
            self.burningSfx = loadSfx(SoundGlobals.SFX_WEAPON_GRENADE_FIREBOMB)

        if not MysticFire.particleDummy:
            MysticFire.particleDummy = render.attachNewNode(ModelNode('FireParticleDummy'))
            MysticFire.particleDummy.setDepthWrite(0)
            MysticFire.particleDummy.setFogOff()
            MysticFire.particleDummy.setLightOff()
            MysticFire.particleDummy.setColorScaleOff()
            MysticFire.particleDummy.setBin('fixed', 60)

        self.duration = 4.0
        self.effectScale = 1.0
        self.f = ParticleEffect.ParticleEffect('MysticFire')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(64)
        self.p0.setBirthRate(0.01)
        self.p0.setLitterSize(3)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.setFloorZ(-1.0)
        self.p0.factory.setLifespanBase(0.75)
        self.p0.factory.setLifespanSpread(0.25)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(360.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(350.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0.75, 0.848, 0.299, 1.0), Vec4(0.4, 0.848, 0.299, 0.5), 1)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(-1)
        self.p0.emitter.setAmplitudeSpread(0.25)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 15.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))


    def createTrack(self, lod = None):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy), Func(self.f.reparentTo, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, SoundInterval(self.burningSfx, loop = 1, duration = self.duration), self.endEffect)


    def setScale(self, scale = VBase3(1, 1, 1)):
        self.setEffectScale(scale[0])


    def setEffectScale(self, scale):
        self.effectScale = scale
        self.p0.renderer.setInitialXScale(0.050000 * self.cardScale * self.effectScale)
        self.p0.renderer.setInitialYScale(0.050000 * self.cardScale * self.effectScale)
        self.p0.renderer.setFinalXScale(0.0299 * self.cardScale * self.effectScale)
        self.p0.renderer.setFinalYScale(0.0448 * self.cardScale * self.effectScale)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 15.0 * self.effectScale))
        self.p0.emitter.setAmplitude(-1 * self.effectScale)
        self.p0.emitter.setAmplitudeSpread(0.25 * self.effectScale)
        self.p0.emitter.setRadius(6.0 * self.effectScale)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
