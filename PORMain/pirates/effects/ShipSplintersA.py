from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, LinearVectorForce
from panda3d.core import ModelNode, Point3, Vec3, Vec4
# File: S (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from EffectController import EffectController
from PooledEffect import PooledEffect
from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx
import random

class ShipSplintersA(PooledEffect, EffectController):
    cardScale = 128.0
    SfxNames = (SoundGlobals.SFX_FX_WOOD_IMPACT_01, SoundGlobals.SFX_FX_WOOD_IMPACT_03, SoundGlobals.SFX_FX_WOOD_IMPACT_04)
    splashSfx = []

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleRockShower')
        if not self.splashSfx:
            for audio in self.SfxNames:
                self.splashSfx.append(loadSfx(audio))


        if not ShipSplintersA.particleDummy:
            ShipSplintersA.particleDummy = render.attachNewNode(ModelNode('ShipSplintersAParticleDummy'))
            ShipSplintersA.particleDummy.setDepthWrite(0)

        self.f = ParticleEffect.ParticleEffect('ShipSplintersA')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.f.addParticles(self.p0)
        f0 = ForceGroup.ForceGroup('gravity')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, -30.0), 1.0, 1)
        force0.setActive(1)
        f0.addForce(force0)
        self.f.addForceGroup(f0)
        self.p0.setPoolSize(16)
        self.p0.setBirthRate(0.4)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.setFloorZ(-5.0)
        self.p0.factory.setLifespanBase(2.0)
        self.p0.factory.setLifespanSpread(0.5)
        self.p0.factory.setMassBase(0.450)
        self.p0.factory.setMassSpread(0.200)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(0.299, 0.200, 0, 1))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.035000 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.0598 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.035000 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.0598 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
        self.p0.emitter.setAmplitude(8.0)
        self.p0.emitter.setAmplitudeSpread(4.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 40.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 1.0))
        self.p0.emitter.setRadius(8.0)


    def createTrack(self):
        self.track = Sequence(Func(self.p0.setBirthRate, 0.02), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy), Func(self.f.reparentTo, self), Wait(0.299), Func(self.p0.setBirthRate, 100), Wait(3.0), Func(self.cleanUpEffect))


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
