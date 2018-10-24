from pirates.quest.QuestIndicatorNode import QuestIndicatorNode
from pirates.piratesgui.RadarGui import RADAR_OBJ_TYPE_QUEST
from direct.showbase.PythonUtil import report

class QuestIndicatorGridNode(QuestIndicatorNode):

    def __init__(self, name, zoneRadii, questStep):
        self.pendingStepObj = None
        self.stepObj = None
        QuestIndicatorNode.__init__(self, name, zoneRadii, questStep)

    def delete(self):
        self.ignoreAll()
        if self.pendingStepObj:
            base.cr.relatedObjectMgr.abortRequest(self.pendingStepObj)
            self.pendingStepObj = None

        QuestIndicatorNode.delete(self)

    def placeInWorld(self):
        if self.stepObj:
            self.reparentTo(self.stepObj)
            self.setPos(0, 0, 0)
            self.setHpr(0, 0, 0)
            self.setScale(render, 1)
        elif self.pendingStepObj:
            base.cr.relatedObjectMgr.abortRequest(self.pendingStepObj)
            self.pendingStepObj = None

        questStepDoId = self.questStep.getStepDoId()
        self.pendingStepObj = base.cr.relatedObjectMgr.requestObjects([
            questStepDoId], eachCallback = self.stepObjArrived)
        if self.stepObj:
            return None

        originObj = base.cr.doId2do.get(self.questStep.getOriginDoId())
        if originObj:
            posH = self.questStep.getPosH()
            pos = posH[:3]
            h = posH[3]
            self.reparentTo(originObj)
            self.setPos(*pos)
            self.setHpr(h, 0, 0)
            self.setScale(render, 1)

    def loadZoneLevel(self, level):
        QuestIndicatorNode.loadZoneLevel(self, level)
        if level == 0:
            self.request('At')

        if level == 1:
            self.request('Near')

        if level == 2:
            self.request('Far')

    def unloadZoneLevel(self, level):
        QuestIndicatorNode.unloadZoneLevel(self, level)
        if level == 0:
            self.request('Near')

        if level == 1:
            self.request('Far')

        if level == 2:
            self.request('Off')

    def enterFar(self):
        QuestIndicatorNode.enterFar(self)

    def exitFar(self):
        QuestIndicatorNode.exitFar(self)

    def enterNear(self):
        QuestIndicatorNode.enterNear(self)

    def exitNear(self):
        QuestIndicatorNode.exitNear(self)

    def enterAt(self):
        QuestIndicatorNode.enterAt(self)

    def exitAt(self):
        QuestIndicatorNode.exitAt(self)

    def _reparentFarEffectToSelf(self):
        if self.farEffect:
            self.farEffect.wrtReparentTo(self)

    def _reparentFarEffectToOriginObj(self, stepObj):
        if self.farEffect:
            self.farEffect.wrtReparentTo(stepObj.getParent())

    def stepObjArrived(self, stepObj):
        self.pendingStepObj = None
        self.stepObj = stepObj
        self.accept(stepObj.getDisableEvent(), self.stepObjLeft)
        self.placeInWorld()

    def stepObjLeft(self):
        self.stepObj = None
        self.placeInWorld()
