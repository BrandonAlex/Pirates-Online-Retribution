from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
import random
from pirates.piratesgui.GameOptions import Options
from PooledEffect import PooledEffect
from EffectController import EffectController

class BlackSmoke(PooledEffect, EffectController):
    cardScale = 64.0
    
    def __init__(self, parent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if parent is not None:
            self.reparentTo(parent)
        
        self._accelerateTime = 0
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/particleBlackSmoke')
        if not BlackSmoke.particleDummy:
            BlackSmoke.particleDummy = base.effectsRoot.attachNewNode(ModelNode('BlackSmokeParticleDummy'))
            BlackSmoke.particleDummy.setDepthWrite(0)
            BlackSmoke.particleDummy.setColorScaleOff()
            BlackSmoke.particleDummy.setLightOff()
        
        self.duration = 10.0
        self.f = ParticleEffect.ParticleEffect('BlackSmoke')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('DiscEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(32)
        self.p0.setBirthRate(0.25)
        self.p0.setLitterSize(2)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.setFloorZ(-5.0)
        self.p0.factory.setLifespanBase(2.5)
        self.p0.factory.setLifespanSpread(1.5)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.20000000000000001)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(30.0)
        self.p0.factory.enableAngularVelocity(0)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(0.80000000000000004)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.13 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.13 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.40000000000000002 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.40000000000000002 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
        self.p0.emitter.setAmplitude(3.0)
        self.p0.emitter.setAmplitudeSpread(1.5)
        self.p0.emitter.setOffsetForce(Vec3(2.0, 2.0, 25.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 1.0))
        self.p0.emitter.setRadius(4.0)

    
    def startLoop(self, lod = None, accelerateTime = 0):
        self._accelerateTime = accelerateTime
        EffectController.startLoop(self, lod)

    
    def createTrack(self, lod = Options.SpecialEffectsHigh):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.25), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy))
        if self._accelerateTime > 0:
            self.startEffect.append(Func(self.accelerate, self._accelerateTime))
        
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(4.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(self.duration), self.endEffect)

    
    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)

    
    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)

    
    def accelerate(self, time):
        self.p0.accelerate(time, 1, 0.050000000000000003)

    
    def setDensity(self, density):
        self.p0.emitter.setAmplitude(4.5 * density)
        self.p0.renderer.setFinalXScale(0.59999999999999998 * density * self.cardScale)
        self.p0.renderer.setFinalYScale(0.59999999999999998 * density * self.cardScale)
        self.p0.renderer.setUserAlpha(max(1.0 * density, 0.25))
        self.p0.emitter.setRadius(10.0 * density)
        self.p0.factory.setLifespanBase(3.0 * density + 1.0)
        self.p0.factory.setLifespanSpread(0.5 + density)


