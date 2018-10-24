from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer, ColorInterpolationManager
from panda3d.core import ColorBlendAttrib, ModelNode, Point3, Vec3, Vec4
# File: V (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from EffectController import EffectController
from PooledEffect import PooledEffect
import random

class VoodooSouls(PooledEffect, EffectController):
    cardScale = 64.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('phase_2/models/effects/particleMaps')
        self.card = model.find('**/particleDarkSmoke')
        if not VoodooSouls.particleDummy:
            VoodooSouls.particleDummy = render.attachNewNode(ModelNode('VoodooSoulsParticleDummy'))
            VoodooSouls.particleDummy.setDepthWrite(0)
            VoodooSouls.particleDummy.setColorScaleOff()
            VoodooSouls.particleDummy.setLightOff()

        self.effectColor = Vec4(1, 1, 1, 1)
        self.f = ParticleEffect.ParticleEffect('VoodooSouls')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('SphereVolumeEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(512)
        self.p0.setBirthRate(0.02)
        self.p0.setLitterSize(4)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(1.0)
        self.p0.factory.setLifespanSpread(0.25)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(90.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setFinalAngle(900.0)
        self.p0.factory.setFinalAngleSpread(0.0)
        self.p0.factory.setAngularVelocity(300.0)
        self.p0.factory.setAngularVelocitySpread(100.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 0.25, Vec4(1.0, 1.0, 1.0, 0.0), Vec4(1.0, 1.0, 1.0, 0.5), 1)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.25, 1.0, Vec4(1.0, 1.0, 1.0, 0.5), Vec4(0.5, 0.200, 1.0, 0.0), 1)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.001 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.02 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.001 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.02 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(4.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, -3.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(1.0)


    def createTrack(self):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy), Func(self.f.reparentTo, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100), Wait(2.0), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(1.0), self.endEffect)


    def setEffectColor(self, color):
        self.effectColor = Vec4(1, 1, 1, 0) - (Vec4(1, 1, 1, 1) - color) / 1.75
        self.p0.renderer.getColorInterpolationManager().clearToInitial()
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 0.25, Vec4(1.0, 1.0, 1.0, 0.0), Vec4(1.0, 1.0, 1.0, 0.5), 1)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.25, 1.0, Vec4(1.0, 1.0, 1.0, 0.5), self.effectColor, 1)


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
