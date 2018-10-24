from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer
from panda3d.core import ModelNode, Point3, VBase3, Vec3, Vec4
# File: G (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
import random
from pirates.piratesgui.GameOptions import Options
from PooledEffect import PooledEffect
from EffectController import EffectController

class GentleSmoke(PooledEffect, EffectController):
    cardScale = 64.0

    def __init__(self, parent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if parent is not None:
            self.reparentTo(parent)

        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleGunSmoke')
        if not GentleSmoke.particleDummy:
            GentleSmoke.particleDummy = render.attachNewNode(ModelNode('BlackSmokeParticleDummy'))
            GentleSmoke.particleDummy.setDepthWrite(0)
            GentleSmoke.particleDummy.setLightOff()
            GentleSmoke.particleDummy.setColorScaleOff()

        self.f = ParticleEffect.ParticleEffect('GentleSmoke')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(6)
        self.p0.setBirthRate(0.25)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.setFloorZ(-10.0)
        self.p0.factory.setLifespanBase(1.10)
        self.p0.factory.setLifespanSpread(0.200)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.200)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(20.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(4.0)
        self.p0.factory.setAngularVelocitySpread(2.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(0.75)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(0.800000, 0.800000, 0.800000, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 1.0))
        self.setEffectScale(1.0)


    def createTrack(self, lod = Options.SpecialEffectsHigh):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.25), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(10.0), self.endEffect)


    def setScale(self, scale = VBase3(1, 1, 1)):
        self.setEffectScale(scale[0])


    def setEffectScale(self, scale):
        self.p0.renderer.setInitialXScale(0.0299 * self.cardScale * scale)
        self.p0.renderer.setInitialYScale(0.0299 * self.cardScale * scale)
        self.p0.renderer.setFinalXScale(0.050000 * self.cardScale * scale)
        self.p0.renderer.setFinalYScale(0.050000 * self.cardScale * scale)
        self.p0.emitter.setAmplitude(0.5 * scale)
        self.p0.emitter.setAmplitudeSpread(0.25 * scale)
        self.p0.emitter.setOffsetForce(Vec3(0.5, 0.5, 5.0) * scale)
        self.p0.emitter.setRadius(1.0 * scale)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
