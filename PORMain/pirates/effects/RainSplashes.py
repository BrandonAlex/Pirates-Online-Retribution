from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer
from panda3d.core import ColorBlendAttrib, ModelNode, NodePath, Point3, StencilAttrib, Vec3, Vec4
# File: R (Python 2.4)

from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from EffectController import EffectController
import random

class RainSplashes(EffectController, NodePath):
    cardScale = 32.0

    def __init__(self, reference = None):
        NodePath.__init__(self, 'RainSplashes')
        EffectController.__init__(self)
        model = loader.loadModel('models/effects/particleCards')
        self.card = model.find('**/particleSplash2')
        if not RainSplashes.particleDummy:
            RainSplashes.particleDummy = render.attachNewNode(ModelNode('RainSplashesParticleDummy'))
            RainSplashes.particleDummy.setDepthWrite(0)
            RainSplashes.particleDummy.setColorScale(1.0, 1.0, 1.0, 1)
            RainSplashes.particleDummy.setLightOff()
            RainSplashes.particleDummy.setBin('water', 10)
            mask = 16777215
            stencil = StencilAttrib.make(1, StencilAttrib.SCFEqual, StencilAttrib.SOKeep, StencilAttrib.SOKeep, StencilAttrib.SOKeep, 1, mask, mask)
            RainSplashes.particleDummy.setAttrib(stencil)
            if not base.useStencils:
                RainSplashes.particleDummy.hide()


        self.reference = reference
        self.f = ParticleEffect.ParticleEffect('RainSplashes')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('PointParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('TangentRingEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(256)
        self.p0.setBirthRate(0.02)
        self.p0.setLitterSize(20)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(0.25)
        self.p0.factory.setLifespanSpread(0.050000)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        self.p0.renderer.setUserAlpha(0.5)
        self.p0.renderer.setColor(Vec4(0.800000, 0.800000, 1.0, 1.0))
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(0)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setInitialXScale(0.01 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.12 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.01 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.070 * self.cardScale)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
        self.p0.emitter.setAmplitude(1.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.0))
        self.p0.emitter.setExplicitLaunchVector(Vec3(0.0, 0.0, 1.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(300.0)
        self.p0.emitter.setRadiusSpread(250.0)


    def createTrack(self):
        posUpdate = LerpFunctionInterval(self.updatePos, 1.0)
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.02), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy), Func(posUpdate.loop))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(1.0), Func(posUpdate.finish), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(10.0), self.endEffect)


    def updatePos(self, t):
        if self.reference:
            pos = self.reference.getPos(self.getParent())
            self.setPos(pos[0], pos[1], 1.5)



    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)


    def destroy(self):
        EffectController.destroy(self)
