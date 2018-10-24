from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, ColorInterpolationManager
from panda3d.core import ModelNode, NodePath, Point3, Vec3, Vec4
# File: E (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from EffectController import EffectController

class EruptionSmoke(NodePath, EffectController):
    cardScale = 64.0

    def __init__(self):
        NodePath.__init__(self, 'EruptionSmoke')
        EffectController.__init__(self)
        self.particleDummy = self.attachNewNode(ModelNode('EruptionSmokeParticleDummy'))
        self.particleDummy.setDepthWrite(0)
        self.particleDummy.setColorScaleOff()
        self.particleDummy.setLightOff()
        self.particleDummy.setBin('fixed', 15)
        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleWhiteSmoke')
        self.f = ParticleEffect.ParticleEffect('EruptionSmoke')
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('SphereSurfaceEmitter')
        self.duration = 10.0
        self.p0.setPoolSize(16)
        self.p0.setBirthRate(1.0)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(8.0)
        self.p0.factory.setLifespanSpread(2.0)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(180.0)
        self.p0.factory.setFinalAngle(0.0)
        self.p0.factory.setFinalAngleSpread(360.0)
        self.p0.factory.enableAngularVelocity(0)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 0.100, Vec4(1, 0.25, 0, 0), Vec4(1, 0.4, 0.25, 1.0))
        self.p0.renderer.getColorInterpolationManager().addConstant(0.100, 0.4, Vec4(1, 0.4, 0.25, 1))
        self.p0.renderer.getColorInterpolationManager().addLinear(0.4, 1.0, Vec4(1, 0.4, 0.25, 1.0), Vec4(0.0, 0.0, 0.0, 1.0))
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
        self.p0.emitter.setAmplitude(0.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(60.0)
        self.f.addParticles(self.p0)


    def setEffectScale(self, effectScale):
        if self.p0:
            self.p0.renderer.setInitialXScale(1.5 * self.cardScale * effectScale)
            self.p0.renderer.setFinalXScale(4.0 * self.cardScale * effectScale)
            self.p0.renderer.setInitialYScale(1.5 * self.cardScale * effectScale)
            self.p0.renderer.setFinalYScale(4.0 * self.cardScale * effectScale)
            self.p0.emitter.setAmplitude(60.0 * effectScale)
            self.p0.emitter.setAmplitudeSpread(10.0 * effectScale)
            self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 60.0) * effectScale)
            self.p0.emitter.setRadius(60.0 * effectScale)



    def createTrack(self):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.5), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100), Wait(10.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(self.duration), self.endEffect)
