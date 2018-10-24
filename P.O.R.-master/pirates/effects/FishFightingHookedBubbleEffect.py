from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from PooledEffect import PooledEffect
from EffectController import EffectController
from otp.otpbase import OTPRender
import random
import math
from pirates.minigame import FishingGlobals

class FishFightingHookedBubbleEffect(PooledEffect, EffectController):
    cardScale = 128.0
    
    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('models/effects/particleMaps')
        self.card = model.find('**/pir_t_efx_env_bubble')
        if not FishFightingHookedBubbleEffect.particleDummy:
            FishFightingHookedBubbleEffect.particleDummy = render.attachNewNode(ModelNode('FishFightingHookedBubbleEffectParticleDummy'))
            FishFightingHookedBubbleEffect.particleDummy.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
            FishFightingHookedBubbleEffect.particleDummy.setDepthWrite(0)
            FishFightingHookedBubbleEffect.particleDummy.setFogOff()
            FishFightingHookedBubbleEffect.particleDummy.setLightOff()
            FishFightingHookedBubbleEffect.particleDummy.setColorScaleOff()
            FishFightingHookedBubbleEffect.particleDummy.setTwoSided(1)
        
        self.f = ParticleEffect.ParticleEffect('FishFightingHookedBubbleEffect')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.f.addParticles(self.p0)
        self.f0 = None
        self.setParticleOptions()

    
    def setLifespanBasedOnDepth(self, fishPos):
        z = math.fabs(fishPos.getZ())
        time = math.sqrt(z) * 1.2
        self.p0.factory.setLifespanBase(time)

    
    def setBubbleSizeBasedOnWeight(self, weight):
        bubbleMin = 0.001
        bubbleMax = 0.0040000000000000001
        bubbleSize = (bubbleMax - bubbleMin) * (weight / FishingGlobals.maxFishWeight) + bubbleMin
        self.p0.renderer.setInitialXScale(bubbleSize * self.cardScale)
        self.p0.renderer.setInitialYScale(bubbleSize * self.cardScale)
        self.p0.renderer.setFinalXScale(bubbleSize * self.cardScale)
        self.p0.renderer.setFinalYScale(bubbleSize * self.cardScale)

    
    def setParticleOptions(self):
        self.p0.setEmitter('SphereSurfaceEmitter')
        if self.f0 != None:
            self.f.removeForceGroup(self.f0)
        
        self.f0 = ForceGroup.ForceGroup('gravity')
        force0 = LinearVectorForce(Vec3(0.0, 0.0, 1.5), 1.0, 0)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        self.f0.addForce(force0)
        force1 = LinearJitterForce(0.5, 0)
        force1.setVectorMasks(0, 0, 1)
        force1.setActive(1)
        self.f0.addForce(force1)
        self.f.addForceGroup(self.f0)
        self.p0.setPoolSize(128)
        self.p0.setBirthRate(5.0)
        self.p0.setLitterSize(6)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(0)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(0.25)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(1.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(-1.5, 0.0, -1.5))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(0.25)

    
    def createTrack(self):
        self.setParticleOptions()
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.5), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 20.0), Wait(10.0), Func(self.cleanUpEffect))
        self.track = Sequence(Wait(0.5), self.startEffect, Wait(0.5), self.endEffect)

    
    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)

    
    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)


