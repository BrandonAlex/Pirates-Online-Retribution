from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer
from panda3d.core import ModelNode, Point3, Vec3, Vec4
# File: L (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from pirates.piratesgui.GameOptions import Options
from EffectController import EffectController
from PooledEffect import PooledEffect
import random

class LavaSteam(PooledEffect, EffectController):
    cardScale = 64.0

    def __init__(self, parent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if parent is not None:
            self.reparentTo(parent)

        if not LavaSteam.particleDummy:
            LavaSteam.particleDummy = base.effectsRoot.attachNewNode(ModelNode('LavaSteamParticleDummy'))
            LavaSteam.particleDummy.setDepthWrite(0)
            LavaSteam.particleDummy.setLightOff()
            LavaSteam.particleDummy.setBin('fixed', 60)

        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleWhiteSmoke')
        self.f = ParticleEffect.ParticleEffect('LavaSteam')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(32)
        self.p0.setBirthRate(0.299)
        self.p0.setLitterSize(4)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(3.0)
        self.p0.factory.setLifespanSpread(0.5)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(0.4, 0.4, 0.4, 0.299))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(0)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.setEffectScale(1.0)


    def createTrack(self, lod = Options.SpecialEffectsHigh):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.299), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy), Func(self.f.reparentTo, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(10.0), self.endEffect)


    def setEffectScale(self, scale):
        self.p0.renderer.setInitialXScale(0.100 * self.cardScale * scale)
        self.p0.renderer.setFinalXScale(0.299 * self.cardScale * scale)
        self.p0.renderer.setInitialYScale(0.050000 * self.cardScale * scale)
        self.p0.renderer.setFinalYScale(0.200 * self.cardScale * scale)
        self.p0.emitter.setAmplitude(3.0 * scale)
        self.p0.emitter.setAmplitudeSpread(1.5 * scale)
        self.p0.emitter.setOffsetForce(Vec3(1.0, 4.0, 2.0) * scale)
        self.p0.emitter.setRadius(30.0 * scale)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
