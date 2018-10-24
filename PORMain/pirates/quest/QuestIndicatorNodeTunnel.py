from panda3d.core import Point3, TransformState
from pirates.piratesgui.RadarGui import *
from pirates.quest.QuestIndicatorNode import QuestIndicatorNode
from pirates.piratesgui.RadarGui import RADAR_OBJ_TYPE_QUEST
from direct.showbase.PythonUtil import report, StackTrace

class QuestIndicatorNodeTunnel(QuestIndicatorNode):
    LOD_CENTER_OFFSET_X = 30

    def __init__(self, questStep):
        self.pendingStepObj = None
        QuestIndicatorNode.__init__(self, 'TunnelIndicator', [
            self.LOD_CENTER_OFFSET_X], questStep)
        self.arrowNode = None

    def delete(self):
        if self.pendingStepObj:
            base.cr.relatedObjectMgr.abortRequest(self.pendingStepObj)
            self.pendingStepObj = None

        if self.arrowNode:
            self.arrowNode.remove_node()
            self.arrowNode = None

        self.ignore('tunnelSetLinks')
        QuestIndicatorNode.delete(self)

    def placeInWorld(self):

        def stepObjHere(stepObj):
            self.pendingStepObj = None

            def performReparent(tunnelObj = stepObj):
                if tunnelObj == stepObj:
                    areaIndex = tunnelObj.getAreaIndexFromDoId(self.questStep.getOriginDoId())
                    if areaIndex != None:
                        (pos, hpr) = tunnelObj.getConnectorNodePosHpr(areaIndex)
                        t = TransformState.makePosHpr(pos, hpr)
                        ti = t.invertCompose(TransformState.makeIdentity())
                        self.reparentTo(tunnelObj)
                        self.setPos(ti.getPos())
                        self.setHpr(ti.getHpr())
                        self.setPos(self, self.LOD_CENTER_OFFSET_X, 0, 5)
                        parent = base.cr.doId2do[self.questStep.getOriginDoId()]
                        self.wrtReparentTo(parent)
                        self.arrowNode = tunnelObj.attachNewNode('arrowNode')
                        self.arrowNode.setPos(ti.getPos())

            if not stepObj.isConnectorLoaded():
                self.acceptOnce('tunnelSetLinks', performReparent)
            else:
                performReparent()

        if self.pendingStepObj:
            base.cr.relatedObjectMgr.abortRequest(self.pendingStepObj)
            self.pendingStepObj = None

        self.pendingStepObj = base.cr.relatedObjectMgr.requestObjects([
            self.questStep.getStepDoId()], eachCallback = stepObjHere)

    def loadZoneLevel(self, level):
        QuestIndicatorNode.loadZoneLevel(self, level)
        if level == 0:
            self.request('At')
        elif level == 1:
            self.request('Far')

    def unloadZoneLevel(self, level):
        QuestIndicatorNode.unloadZoneLevel(self, level)
        if level == 0:
            self.request('Far')
        elif level == 1:
            self.request('Off')

    def enterAt(self):
        QuestIndicatorNode.enterAt(self)
        self.pendingStepObj = None

    def exitAt(self):
        QuestIndicatorNode.exitAt(self)

    def startFarEffect(self):
        QuestIndicatorNode.startFarEffect(self)
        if self.farEffect:
            self.farEffect.setPos(0, 0, -5)

    def setZoneRadii(self, zoneRadii, zoneCenter = [
        0,
        0]):
        QuestIndicatorNode.setZoneRadii(self, zoneRadii, zoneCenter)
        self.setZoneLODOffset(-1, Point3(-(self.LOD_CENTER_OFFSET_X), 0, 0))
