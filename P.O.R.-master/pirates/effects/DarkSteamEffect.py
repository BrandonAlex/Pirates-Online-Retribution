from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from pirates.piratesgui.GameOptions import Options
from EffectController import EffectController
from PooledEffect import PooledEffect
import random

class DarkSteamEffect(PooledEffect, EffectController):
    cardScale = 64.0
    
    def __init__(self, parent = None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        if parent is not None:
            self.reparentTo(parent)
        
        if not DarkSteamEffect.particleDummy:
            DarkSteamEffect.particleDummy = base.effectsRoot.attachNewNode(ModelNode('DarkSteamParticleDummy'))
            DarkSteamEffect.particleDummy.setDepthWrite(0)
            DarkSteamEffect.particleDummy.setLightOff()
        
        self.f = ParticleEffect.ParticleEffect('DarkSteamEffect')
        self.f.reparentTo(self)
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/particleWhiteSmoke')
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('RectangleEmitter')
        self.f.addParticles(self.p0)
        self.p0.setBirthRate(0.5)
        self.p0.setLitterSize(1)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(10.0)
        self.p0.factory.setLifespanSpread(2.0)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(0.25)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(0)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.setEffectScale(1.0)

    
    def createTrack(self, lod = Options.SpecialEffectsHigh):
        if lod == Options.SpecialEffectsHigh:
            self.p0.setPoolSize(12)
        else:
            self.p0.setPoolSize(6)
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 1.0), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy), Func(self.f.reparentTo, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 0.0), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(10.0), self.endEffect)

    
    def setScale(self, scale = VBase3(1, 1, 1)):
        self.setEffectScale(scale[0])

    
    def setEffectScale(self, scale):
        self.p0.renderer.setInitialXScale(0.5 * self.cardScale * scale)
        self.p0.renderer.setFinalXScale(1.0 * self.cardScale * scale)
        self.p0.renderer.setInitialYScale(0.5 * self.cardScale * scale)
        self.p0.renderer.setFinalYScale(1.0 * self.cardScale * scale)
        self.p0.emitter.setAmplitude(2.0 * scale)
        self.p0.emitter.setAmplitudeSpread(1.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, -3.0, 12.0) * scale)
        self.p0.emitter.setMinBound(Point2(-10.0, -1.0) * scale)
        self.p0.emitter.setMaxBound(Point2(10.0, 1.0) * scale)

    
    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)

    
    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)


