from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, LinearCylinderVortexForce, LinearDistanceForce, LinearJitterForce, LinearSinkForce
from panda3d.core import ModelNode, Point3, Vec3, Vec4
from panda3d.ai import Flock
# File: R (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from EffectController import EffectController
from PooledEffect import PooledEffect
from pirates.piratesgui.GameOptions import Options
import random

class RavenFlock(PooledEffect, EffectController):
    flockId = 0

    def __init__(self, parent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.fId = RavenFlock.flockId
        RavenFlock.flockId = RavenFlock.flockId + 1
        if parent is not None:
            self.reparentTo(parent)

        self.speed = 20.0
        if not RavenFlock.particleDummy:
            RavenFlock.particleDummy = render.attachNewNode(ModelNode('WaspCloudParticleDummy'))
            RavenFlock.particleDummy.setDepthWrite(0)

        self.f = ParticleEffect.ParticleEffect('RavenFlock')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.f.addParticles(self.p0)
        self.p1 = Particles.Particles('particles-2')
        self.p1.setFactory('ZSpinParticleFactory')
        self.p1.setRenderer('SpriteParticleRenderer')
        self.f.addParticles(self.p1)
        self.p2 = Particles.Particles('particles-3')
        self.p2.setFactory('ZSpinParticleFactory')
        self.p2.setRenderer('SpriteParticleRenderer')
        self.f.addParticles(self.p2)
        f0 = ForceGroup.ForceGroup('forceGroup-1')
        force0 = LinearCylinderVortexForce(5.0, 5.0, 0.5, 0.62, 0)
        force0.setVectorMasks(1, 1, 0)
        force0.setActive(1)
        f0.addForce(force0)
        force1 = LinearSinkForce(Point3(0.0, 0.0, 0.0), LinearDistanceForce.FTONEOVERRSQUARED, 1.0, 0.050000, 0)
        force1.setVectorMasks(1, 1, 0)
        force1.setActive(1)
        f0.addForce(force1)
        force2 = LinearJitterForce(0.5, 0)
        force2.setVectorMasks(1, 1, 1)
        force2.setActive(1)
        f0.addForce(force2)
        self.f.addForceGroup(f0)
        self.p0.setPoolSize(30)
        self.p0.setBirthRate(4.5)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(40.0)
        self.p0.factory.setLifespanSpread(10.0)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(20.0)
        self.p0.factory.enableAngularVelocity(0)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(20.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setAnimateFramesEnable(True)
        self.p0.renderer.setAnimateFramesRate(6.0)
        self.p0.renderer.addTextureFromNode('models/effects/particleRaven_tflip', '**/*')
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.5)
        self.p0.renderer.setFinalXScale(0.5)
        self.p0.renderer.setInitialYScale(0.5)
        self.p0.renderer.setFinalYScale(0.5)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.setEmitter('DiscEmitter')
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(0.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.5))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 10.0))
        self.p0.emitter.setRadius(10.0)
        self.p1.setPoolSize(30)
        self.p1.setBirthRate(2.5)
        self.p1.setLitterSize(1)
        self.p1.setLitterSpread(0)
        self.p1.setSystemLifespan(0.0)
        self.p1.setLocalVelocityFlag(1)
        self.p1.setSystemGrowsOlderFlag(0)
        self.p1.factory.setLifespanBase(40.0)
        self.p1.factory.setLifespanSpread(10.0)
        self.p1.factory.setMassBase(1.0)
        self.p1.factory.setMassSpread(0.0)
        self.p1.factory.setTerminalVelocityBase(400.0)
        self.p1.factory.setTerminalVelocitySpread(0.0)
        self.p1.factory.setInitialAngle(0.0)
        self.p1.factory.setInitialAngleSpread(20.0)
        self.p1.factory.enableAngularVelocity(0)
        self.p1.factory.setAngularVelocity(0.0)
        self.p1.factory.setAngularVelocitySpread(20.0)
        self.p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p1.renderer.setUserAlpha(1.0)
        self.p1.renderer.setAnimateFramesEnable(True)
        self.p1.renderer.setAnimateFramesRate(6.0)
        self.p1.renderer.addTextureFromNode('models/effects/particle3Ravens_tflip', '**/*')
        self.p1.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p1.renderer.setXScaleFlag(1)
        self.p1.renderer.setYScaleFlag(1)
        self.p1.renderer.setAnimAngleFlag(1)
        self.p1.renderer.setInitialXScale(0.4)
        self.p1.renderer.setFinalXScale(0.4)
        self.p1.renderer.setInitialYScale(0.4)
        self.p1.renderer.setFinalYScale(0.4)
        self.p1.renderer.setNonanimatedTheta(0.0)
        self.p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p1.renderer.setAlphaDisable(0)
        self.p1.setEmitter('DiscEmitter')
        self.p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p1.emitter.setAmplitude(0.0)
        self.p1.emitter.setAmplitudeSpread(0.0)
        self.p1.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p1.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.5))
        self.p1.emitter.setRadiateOrigin(Point3(0.0, 0.0, 10.0))
        self.p1.emitter.setRadius(10.0)
        self.p2.setPoolSize(30)
        self.p2.setBirthRate(2.5)
        self.p2.setLitterSize(1)
        self.p2.setLitterSpread(0)
        self.p2.setSystemLifespan(0.0)
        self.p2.setLocalVelocityFlag(1)
        self.p2.setSystemGrowsOlderFlag(0)
        self.p2.factory.setLifespanBase(40.0)
        self.p2.factory.setLifespanSpread(10.0)
        self.p2.factory.setMassBase(1.0)
        self.p2.factory.setMassSpread(0.0)
        self.p2.factory.setTerminalVelocityBase(400.0)
        self.p2.factory.setTerminalVelocitySpread(0.0)
        self.p2.factory.setInitialAngle(0.0)
        self.p2.factory.setInitialAngleSpread(20.0)
        self.p2.factory.enableAngularVelocity(0)
        self.p2.factory.setAngularVelocity(0.0)
        self.p2.factory.setAngularVelocitySpread(20.0)
        self.p2.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p2.renderer.setUserAlpha(1.0)
        self.p2.renderer.setAnimateFramesEnable(True)
        self.p2.renderer.setAnimateFramesRate(6.0)
        self.p2.renderer.addTextureFromNode('models/effects/particleSingleRaven_tflip', '**/*')
        self.p2.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p2.renderer.setXScaleFlag(1)
        self.p2.renderer.setYScaleFlag(1)
        self.p2.renderer.setAnimAngleFlag(1)
        self.p2.renderer.setInitialXScale(0.200)
        self.p2.renderer.setFinalXScale(0.200)
        self.p2.renderer.setInitialYScale(0.200)
        self.p2.renderer.setFinalYScale(0.200)
        self.p2.renderer.setNonanimatedTheta(0.0)
        self.p2.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p2.renderer.setAlphaDisable(0)
        self.p2.setEmitter('DiscEmitter')
        self.p2.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p2.emitter.setAmplitude(0.0)
        self.p2.emitter.setAmplitudeSpread(0.0)
        self.p2.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p2.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.5))
        self.p2.emitter.setRadiateOrigin(Point3(0.0, 0.0, 10.0))
        self.p2.emitter.setRadius(10.0)


    def startLoop(self, lod = None, accelerateTime = 0):
        self._accelerateTime = accelerateTime
        EffectController.startLoop(self, lod)
        taskMgr.doMethodLater(15.0, self.checkDensity, 'ravenDensityTask %s' % self.fId)


    def checkDensity(self, task = None):
        if not base.cr.timeOfDayManager:
            return task.done

        currentTime = base.cr.timeOfDayManager.getCurrentIngameTime()
        if currentTime > 6.5 and currentTime < 19.5:
            self.p0.setBirthRate(4.5)
            self.p1.setBirthRate(2.5)
            self.p2.setBirthRate(2.5)
        else:
            self.p0.setBirthRate(20.0)
            self.p1.setBirthRate(10.0)
            self.p2.setBirthRate(10.0)
        taskMgr.doMethodLater(15.0, self.checkDensity, 'ravenDensityTask %s' % self.fId)
        if task:
            return task.done



    def createTrack(self, lod = Options.SpecialEffectsHigh):
        fadeIn = self.particleDummy.colorInterval(1.0, Vec4(1, 1, 1, 1), startColor = Vec4(0.0, 0.0, 0.0, 1))
        fadeOut = self.particleDummy.colorInterval(0.5, Vec4(0, 0, 0, 1), startColor = Vec4(1, 1, 1, 1))
        self.setScale(10, 10, 5)
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 4.5), Func(self.p0.clearToInitial), Func(self.p1.setBirthRate, 2.5), Func(self.p1.clearToInitial), Func(self.p2.setBirthRate, 2.5), Func(self.p2.clearToInitial), Func(self.f.start, self, self), Func(self.f.reparentTo, self), fadeIn)
        self.endEffect = Sequence(Func(self.wrtReparentTo, render), Parallel(fadeOut, Func(self.p0.setBirthRate, 100), Func(self.p1.setBirthRate, 100), Func(self.p2.setBirthRate, 100)), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(2.0), self.endEffect)


    def cleanUpEffect(self):
        taskMgr.remove('ravenDensityTask %s' % self.fId)
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
