from panda3d.core import BitMask32, CollideMask, CollisionHandler, CollisionHandlerEvent, CollisionNode, CollisionSphere, NodePath, Point3, VBase3, VBase4, Vec3, Vec4, lookAt
import math
from direct.gui.DirectGui import *
from direct.task import Task
from direct.fsm.FSM import FSM
from direct.interval.IntervalGlobal import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import TeamUtils
from pirates.piratesbase import PLocalizer
from pirates.band.DistributedBandMember import DistributedBandMember
from pirates.piratesgui.GuiTray import GuiTray
from pirates.piratesgui.RadarObjDef import *
from pirates.world import OceanZone
from pirates.world.LocationConstants import LocationIds
from pirates.map.MinimapObject import MinimapObject
from pirates.map import MinimapGlobals
from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx
from pirates.piratesgui.GameOptions import Options

class RadarZoomFSM(FSM):
    notify = directNotify.newCategory('RadarZoomFSM')
    DEFAULT_LEVELS = (150, 200, 300)

    def __init__(self, radarGui):
        FSM.__init__(self, 'RadarZoom')
        self.radarGui = radarGui
        self.zoomOutSfx = loadSfx(SoundGlobals.SFX_GUI_ZOOM_OUT)
        self.zoomInSfx = loadSfx(SoundGlobals.SFX_GUI_ZOOM_IN)
        self.levels = self.DEFAULT_LEVELS
        self.level = 0


    def destroy(self):
        self.cleanup()
        loader.unloadSfx(self.zoomOutSfx)
        loader.unloadSfx(self.zoomInSfx)
        self.zoomOutSfx = None
        self.zoomInSfx = None


    def _getClosestLevel(self, val):

        def key(a):
            return abs(a - val)

        srt = sorted(self.levels, key = key)
        closest = srt[0]
        return self.levels.index(closest)


    def setLevels(self, levels):
        value = self.levels[self.level]
        self.levels = list(levels)
        self._setLevel(self._getClosestLevel(value))


    def _setLevel(self, level):
        self.level = level
        radius = self.levels[level]
        self.radarGui.setMapScale(radius)


    def defaultFilter(self, request, *args):
        if request == 'in':
            level = max(0, self.level - 1)
        elif request == 'out':
            level = min(len(self.levels) - 1, self.level + 1)
        elif request == 'min':
            level = 0
        elif request == 'max':
            level = len(self.levels) - 1
        else:
            return None
        self._setLevel(level)
        return 'On'



class RadarGui(GuiTray, FSM):
    notify = directNotify.newCategory('RadarGui')
    DEMO_FRIEND = 0
    DEMO_ENEMY = 1

    def __init__(self, parent, av, radius = 200.0, **kw):
        GuiTray.__init__(self, parent, 0.4, 0.4)
        FSM.__init__(self, 'RadarGui')
        self.initialiseoptions(RadarGui)
        self.av = av
        self.radius = radius
        self.battleAvatarTubeRadius = 2.0
        self.demoTunnel = None
        self.demoQuest = None
        self.demoNpc = { }
        guiScale = 0.149
        self.rWidth = (self.width - 0.100) / guiScale
        self.rHeight = (self.height - 0.100) / guiScale
        self._RadarGui__normalizeWithRadius()
        self.camToAvAngle = 0.0
        self.relNode = render.attachNewNode('radarGuiRelNode')
        self.model = loader.loadModel('models/gui/compass_main')
        self.guiTop = self.attachNewNode('compassGuiTop')
        self.guiTop.setScale(guiScale)
        self.guiTop.setPos(self._RadarGui__dX, 0, self._RadarGui__dZ)
        self.background = self.model.find('**/background')
        self.background.setColorScale(1, 1, 1, 0.598)
        self.mapRoot = self.background.attachNewNode('minimap-root')
        self.mapRoot.setScissor(Point3(-1, 1, 0), Point3(1, -1, 0))
        self.mapRoot.setP(90)
        self.mapRoot.setAlphaScale(1, 1)
        self.mapScale = self.mapRoot.attachNewNode('minimap-scale')
        self.minimapSentry = None
        self.frame = self.model.find('**/frame')
        self.frame.flattenStrong()
        self.avArrow = loader.loadModel('models/gui/toplevel_gui').find('**/generic_arrow')
        self.avArrow.setScale(2)
        self.avArrow.setR(90)
        self.dial = self.model.find('**/dial')
        self.dial.flattenStrong()
        self.ring = loader.loadModel('models/gui/gui_main').find('**/compass_radar_in')
        self.ring.hide()
        self.ringIval = None
        self.north = loader.loadModel('models/gui/compass_north')
        self.north.setScale(0.75)
        self.north.setZ(1)
        self.north.reparentTo(self.dial)
        self.arrow = loader.loadModel('models/gui/compass_arrow')
        self.arrow.getChild(0).getChild(0).setHpr(90, 0, 90)
        self.arrow.getChild(0).getChild(0).setY(0.200)
        objectiveGrey = self.model.find('**/icon_objective_grey')
        objectiveGrey.copyTo(self.arrow)
        objectiveGrey.setScale(0.5)
        self.arrow.find('**/icon_objective_grey').setScale(0.800000)
        self.rectangle = NodePath('rectangle')
        rectangleGeom = self.model.find('**/icon_rectangle_hollow')
        rectangleGeom.setHpr(90, 0, 0)
        rectangleGeom.reparentTo(self.rectangle)
        self.background.reparentTo(self.guiTop)
        self.frame.reparentTo(self.guiTop)
        self.ring.reparentTo(self.guiTop)
        self.dial.reparentTo(self.guiTop)
        self.edge = self.guiTop.attachNewNode('edge')
        self.objTop = self.guiTop.attachNewNode('compassObjTop')
        self.zoomInButton = DirectButton(parent = self, relief = None, scale = 0.200, pos = (0.25, 0, 0.25), image = (self.model.find('**/zoomin_button'), self.model.find('**/zoomin_button'), self.model.find('**/zoomin_button_over')), command = self.zoomIn)
        self.zoomOutButton = DirectButton(parent = self, relief = None, scale = 0.200, pos = (0.25, 0, 0.25), image = (self.model.find('**/zoomout_button'), self.model.find('**/zoomout_button'), self.model.find('**/zoomout_button_over')), command = self.zoomOut)
        self.zoomInButton.flattenStrong()
        self.zoomOutButton.flattenStrong()
        guiMain = loader.loadModel('models/gui/gui_main')
        self.minimapButton = DirectButton(parent = self, relief = None, scale = 0.25, pos = (0.11, 0, 0.288), image = (guiMain.find('**/minimap_button'), guiMain.find('**/minimap_button'), guiMain.find('**/minimap_button_over')), command = self.handleMinimapButton)
        self.minimapButton.hide()
        self.modelDict = {
            RADAR_OBJ_TYPE_DEFAULT: [
                self.model.find('**/icon_sphere'),
                None],
            RADAR_OBJ_TYPE_LANDMARK: [
                self.model.find('**/icon_square'),
                self.model.find('**/icon_square_hollow')],
            RADAR_OBJ_TYPE_QUEST: [
                self.model.find('**/icon_objective_grey'),
                self.arrow],
            RADAR_OBJ_TYPE_SHIP: [
                self.model.find('**/icon_ship'),
                None],
            RADAR_OBJ_TYPE_EXIT: [
                self.rectangle,
                self.rectangle] }
        self._RadarGui__radarObjects = { }
        self._RadarGui__cachedRadarObjects = { }
        self.collSphereNodePath = None
        self.setupCollisions()
        self.detachNode()
        self.enterSphereEvent = 'enterradarSphere'
        self.exitSphereEvent = 'exitradarSphere'
        self.zoomFSM = RadarZoomFSM(self)
        self.effectIvals = []
        self.locationLabel = DirectLabel(parent = self, relief = None, text = '', text_font = PiratesGlobals.getPirateOutlineFont(), text_fg = (1.0, 1.0, 1.0, 1.0), text_shadow = (0, 0, 0, 1), text_scale = 0.0400, text_pos = (0.200, -0.0250), text_wordwrap = 7)
        self.locationLabel.hide()
        self.flashCleanupTasks = { }
        self.minimapObjects = []
        self.toggle()


    def destroy(self):
        for (currDoLater, ival) in self.flashCleanupTasks.values():
            taskMgr.remove(currDoLater)
            ival.finish()

        self.flashCleanupTasks = { }
        self.cleanupEffects()
        self.removeCollisions()
        taskMgr.remove('drawRadarTask')
        GuiTray.destroy(self)
        self.guiTop.remove_node()
        del self.mapRoot
        del self.mapScale
        del self.guiTop
        del self.objTop
        del self.background
        del self.frame
        del self.dial
        self.relNode.remove_node()
        del self.relNode
        del self.modelDict
        del self.zoomInButton
        del self.zoomOutButton
        del self.minimapButton
        self.zoomFSM.destroy()
        del self.zoomFSM
        self.locationLabel.destroy()
        del self.av


    def showLocation(self, locationUID):
        locText = PLocalizer.LocationNames.get(locationUID)
        if locText is not None:
            self.locationLabel['text'] = locText
            self.locationLabel.show()
        elif base.localAvatar.ship and base.localAvatar.getTutorialState() > 2:
            pos = base.localAvatar.ship.getPos(render)
            ocean = OceanZone.getOceanZone(pos[0], pos[1])
            oceanText = PLocalizer.LocationNames.get(ocean)
            if oceanText is None:
                oceanText = PLocalizer.LoadingScreen_Ocean
                self.locationLabel['text'] = oceanText
                self.locationLabel.show()

        else:
            self.locationLabel.hide()


    def hideLocationText(self):
        self.locationLabel.hide()


    def _RadarGui__normalizeWithRadius(self):
        self._RadarGui__kX = 0.5 * self.rWidth / self.radius
        self._RadarGui__kZ = 0.5 * self.rHeight / self.radius
        self._RadarGui__dX = 0.5 * self.width
        self._RadarGui__dZ = 0.5 * self.height


    def zoomIn(self):
        self.zoomFSM.request('in')


    def zoomOut(self):
        self.zoomFSM.request('out')


    def setupCollisions(self):
        sphereName = 'radarSphere'
        collSphere = CollisionSphere(0, 0, 0, self.radius - self.battleAvatarTubeRadius)
        collSphere.setTangible(0)
        collSphereNode = CollisionNode(sphereName)
        collSphereNode.addSolid(collSphere)
        collSphereNode.setFromCollideMask(BitMask32.allOff())
        collSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.collSphereNodePath = self.av.attachNewNode(collSphereNode)
        self.collSphereNodePath.stash()
        self.collHandler = CollisionHandlerEvent()
        self.collHandler.addInPattern('enterradarSphere')
        self.collHandler.addOutPattern('exitradarSphere')


    def removeCollisions(self):
        base.cTrav.removeCollider(self.collSphereNodePath)
        if self.collSphereNodePath:
            self.collSphereNodePath.detachNode()



    def getRadarObjects(self):
        return self._RadarGui__radarObjects


    def getRadarAvatarObject(self):
        return self.avArrow


    def radarObjectCollEnter(self, collEntry):
        radarObj = collEntry.getIntoNodePath()
        radarObjId = self.getObjIdFromCollNode(radarObj)
        objType = RADAR_OBJ_TYPE_DEFAULT
        self.addRadarObject(radarObjId, radarObj, objType)


    def getObjIdFromCollNode(self, radarObj):
        doIdStr = radarObj.getNetTag('avId')
        if doIdStr == '':
            doIdStr = radarObj.getNetTag('avIdStr')
            if doIdStr == '':
                return None

            return doIdStr

        radarObjDoId = int(doIdStr)
        return radarObjDoId


    def radarObjectCollExit(self, collEntry):
        radarObj = collEntry.getIntoNodePath()
        radarObjId = self.getObjIdFromCollNode(radarObj)
        self.removeRadarObject(radarObjId)


    def restoreCachedObject(self, objId, srcObjNode):
        self._RadarGui__radarObjects[objId] = self._RadarGui__cachedRadarObjects[objId]
        (radarNode, outOfRangeNode) = self.makeRadarNode(srcObjNode, self._RadarGui__radarObjects[objId]['type'])
        self._RadarGui__radarObjects[objId]['radarObjNode'] = radarNode
        self._RadarGui__radarObjects[objId]['outOfRangeNode'] = outOfRangeNode
        self._RadarGui__radarObjects[objId]['srcObjNode'] = srcObjNode
        del self._RadarGui__cachedRadarObjects[objId]

    def restoreStickyCachedObjects(self):
        cachedKeys = self._RadarGui__cachedRadarObjects.keys()
        for currObjKey in cachedKeys:
            if self._RadarGui__cachedRadarObjects[currObjKey]['type'] != RADAR_OBJ_TYPE_DEFAULT or self._RadarGui__cachedRadarObjects[currObjKey]['type'] != RADAR_OBJ_TYPE_EXIT:
                dummyObjNode = self._RadarGui__cachedRadarObjects[currObjKey]['dummySrcObjNode']
                self.restoreCachedObject(currObjKey, dummyObjNode)
                continue



    def addRadarObject(self, objId, radarObj, objType = RADAR_OBJ_TYPE_DEFAULT, dummySrcObjNode = None, teamId = None, enableUnconvert = False):
        if __dev__:
            import pdb as pdb
            pdb.set_trace()

        if objId in self._RadarGui__radarObjects:
            if objType != RADAR_OBJ_TYPE_DEFAULT:
                if objType == RADAR_OBJ_TYPE_TUTORIAL:
                    objType = RADAR_OBJ_TYPE_DEFAULT
                    self.convertRadarObject(objType, objId, teamId)
                else:
                    self.convertRadarObject(objType, objId, enableUnconvert = enableUnconvert)

            if dummySrcObjNode:
                radarObj = dummySrcObjNode

            if radarObj == None:
                radarObj = self._RadarGui__radarObjects[objId]['srcObjNode']

            self.updateObjRef(radarObj, objId, dummySrcObjNode = dummySrcObjNode)
        elif objId in self._RadarGui__cachedRadarObjects:
            if not radarObj:
                radarObj = self._RadarGui__cachedRadarObjects[objId]['dummySrcObjNode']

            self.restoreCachedObject(objId, radarObj)
            if objType != RADAR_OBJ_TYPE_DEFAULT:
                if objType == RADAR_OBJ_TYPE_TUTORIAL:
                    objType = RADAR_OBJ_TYPE_DEFAULT

                self.convertRadarObject(objType, objId, teamId)

        else:
            srcNode = radarObj
            if radarObj == None:
                srcNode = dummySrcObjNode

            if objType == RADAR_OBJ_TYPE_TUTORIAL:
                objType = RADAR_OBJ_TYPE_DEFAULT
                (radarNode, outOfRangeNode) = self.makeRadarNode(srcNode, objType, objId, teamId = teamId)
            else:
                (radarNode, outOfRangeNode) = self.makeRadarNode(srcNode, objType)
            newRadarObjInfo = {
                'type': objType,
                'radarObjNode': radarNode,
                'outOfRangeNode': outOfRangeNode,
                'srcObjNode': srcNode,
                'dummySrcObjNode': dummySrcObjNode }
            self._RadarGui__radarObjects[objId] = newRadarObjInfo

    def removeRadarObject(self, objId, force = False):
        objInfo = self._RadarGui__radarObjects.get(objId)
        if objInfo:
            if objInfo['type'] == RADAR_OBJ_TYPE_DEFAULT and objInfo['type'] == RADAR_OBJ_TYPE_EXIT or force:
                self.moveRadarObjToCache(objId, skipCache = force)
            else:
                self.updateObjRef(objInfo['dummySrcObjNode'], objId)

    def restoreRadarObject(self, objId):
        restoreResult = self.restoreOldInfo(objId)
        if restoreResult == False:
            self.moveRadarObjToCache(objId, skipCache = True)



    def convertRadarObject(self, toType, objId, teamId = None, enableUnconvert = False):
        if __dev__:
            import pdb
            pdb.set_trace()
        else:
            raise 'RadarException'
        objectInfo = self._RadarGui__radarObjects.get(objId)
        if objectInfo == None:
            return None

        if objectInfo['type'] != toType:
            if enableUnconvert:
                objectInfo['oldInfo'] = {
                    'type': objectInfo['type'],
                    'radarObjNode': objectInfo['radarObjNode'],
                    'outOfRangeNode': objectInfo['outOfRangeNode'],
                    'dummySrcObjNode': objectInfo['dummySrcObjNode'] }

            objectInfo['type'] = toType
            objectInfo['radarObjNode'].hide()
            outOfRangeNode = objectInfo['outOfRangeNode']
            if outOfRangeNode:
                outOfRangeNode.hide()

            (objectInfo['radarObjNode'], objectInfo['outOfRangeNode']) = self.makeRadarNode(objectInfo['srcObjNode'], toType, objId, teamId)
            if objectInfo['type'] == RADAR_OBJ_TYPE_DEFAULT:
                objectInfo['dummySrcObjNode'].hide()
                objectInfo['dummySrcObjNode'] = None

    def updateObjRef(self, object, objId, dummySrcObjNode = None):
        if __dev__:
            import pdb
            pdb.set_trace()
        else:
            raise 'RadarException'
        objectInfo = self._RadarGui__radarObjects[objId]
        if dummySrcObjNode:
            objectInfo['dummySrcObjNode'] = dummySrcObjNode

        objectInfo['srcObjNode'] = object

    def addRadarObjectAtLoc(self, pos, objType = RADAR_OBJ_TYPE_DEFAULT, targetObjId = None, teamId = None, enableUnconvert = False):
        desiredRadarNode = render.attachNewNode('desiredRadarNode')
        desiredRadarNode.setPos(pos)
        self.addRadarObject(targetObjId, None, objType, dummySrcObjNode = desiredRadarNode, teamId = teamId, enableUnconvert = enableUnconvert)

    def removeAllObjects(self):
        objects = self._RadarGui__radarObjects.keys()
        for key in objects:
            self.moveRadarObjToCache(key)



    def moveRadarObjToCache(self, objKey, skipCache = False):
        self.endFlashRadarObject(objKey)
        objInfo = self._RadarGui__radarObjects.pop(objKey, None)
        objInfo['radarObjNode'].remove_node()
        outOfRangeNode = objInfo['outOfRangeNode']
        if outOfRangeNode:
            outOfRangeNode.remove_node()

        if (objInfo['type'] != RADAR_OBJ_TYPE_DEFAULT or objInfo['type'] != RADAR_OBJ_TYPE_EXIT) and skipCache == False:
            objInfo['radarObjNode'] = None
            objInfo['outOfRangeNode'] = None
            objInfo['srcObjNode'] = None
            self._RadarGui__cachedRadarObjects[objKey] = objInfo
        elif (objInfo['type'] == RADAR_OBJ_TYPE_DEFAULT or objInfo['type'] == RADAR_OBJ_TYPE_EXIT) and objInfo['dummySrcObjNode'] and not objInfo['dummySrcObjNode'].isEmpty():
            objInfo['dummySrcObjNode'].remove_node()

    def clearCache(self):
        objects = self._RadarGui__cachedRadarObjects.keys()
        for key in objects:
            objInfo = self._RadarGui__cachedRadarObjects[key]
            objInfo['radarObjNode'].remove_node()
            outOfRangeNode = objInfo['outOfRangeNode']
            if outOfRangeNode:
                outOfRangeNode.remove_node()

            del self._RadarGui__cachedRadarObjects[key]



    def printRadarObjects(self):
        print self._RadarGui__radarObjects


    def getRadarObjects(self):
        return self._RadarGui__radarObjects


    def makeRadarNode(self, obj, objType, objDoId = None, teamId = None):
        model = None
        outOfRangeNode = None
        camH = camera.getH(render)
        if objType != RADAR_OBJ_TYPE_QUEST and obj.getCollideMask().hasBitsInCommon(PiratesGlobals.RadarShipBitmask):
            modelDict = self.modelDict[RADAR_OBJ_TYPE_SHIP]
        else:
            modelDict = self.modelDict[objType]
        model = modelDict[0].copyTo(self.objTop)
        if modelDict[1]:
            outOfRangeNode = modelDict[1].copyTo(self.objTop)

        if objType == RADAR_OBJ_TYPE_DEFAULT:
            status = PiratesGlobals.NEUTRAL
            if teamId:
                status = TeamUtils.teamStatus(localAvatar.getTeam(), teamId)
            elif not objDoId:
                pass
            avId = obj.getNetTag('avId')
            if avId:
                avId = int(avId)
                av = base.cr.doId2do.get(avId)
                if av:
                    if DistributedBandMember.areSameCrew(localAvatar.doId, avId):
                        status = PiratesGlobals.CREW
                    else:
                        status = TeamUtils.friendOrFoe(localAvatar, av)
                else:
                    return (model, outOfRangeNode)

            if status == PiratesGlobals.ENEMY or status == PiratesGlobals.PVP_ENEMY:
                model.setColorScale(MinimapGlobals.MAPCOLOR_ENEMY)
            elif status == PiratesGlobals.FRIEND or status == PiratesGlobals.PVP_FRIEND:
                model.setColorScale(MinimapGlobals.MAPCOLOR_FRIEND)
            elif status == PiratesGlobals.CREW:
                model.setColorScale(MinimapGlobals.MAPCOLOR_FRIEND)
            elif status == PiratesGlobals.NEUTRAL:
                model.setColorScale(MinimapGlobals.MAPCOLOR_NPC)
            else:
                model.setColorScale(MinimapGlobals.MAPCOLOR_NPC)
        elif objType == RADAR_OBJ_TYPE_QUEST:
            model.setColorScale(MinimapGlobals.MAPCOLOR_QUEST)
            if outOfRangeNode:
                outOfRangeNode.setColorScale(MinimapGlobals.MAPCOLOR_QUEST)
                outOfRangeNode.setScale(0.75)


        return (model, outOfRangeNode)

    def enterOn(self):
        self.collSphereNodePath.unstash()
        taskMgr.add(self.draw, 'drawRadarTask', priority = 47)
        self.accept(self.enterSphereEvent, self.radarObjectCollEnter)
        self.accept(self.exitSphereEvent, self.radarObjectCollExit)
        self.accept('-', self.zoomOut)
        self.accept('=', self.zoomIn)
        self.accept('+', self.zoomIn)
        self.reparentTo(base.a2dTopRight)
        self.restoreStickyCachedObjects()
        if hasattr(base, 'localAvatar') and hasattr(localAvatar, 'guiMgr') and localAvatar.guiMgr.getMinimap():
            self.minimapSentry = localAvatar.guiMgr.getMinimap().getSentry()



    def exitOn(self):
        self.minimapSentry = None
        if not self.collSphereNodePath.isSingleton():
            self.collSphereNodePath.stash()

        collisionNode = self.collSphereNodePath.getNode(0)
        self.ignore(self.enterSphereEvent)
        self.ignore(self.exitSphereEvent)
        self.ignore('-')
        self.ignore('=')
        self.ignore('+')
        taskMgr.remove('drawRadarTask')
        self.removeAllObjects()
        if hasattr(self, 'zoomFSM'):
            self.zoomFSM.request('Off')

        self.detachNode()


    def draw(self, task):
        for objId in self._RadarGui__radarObjects:
            objInfo = self._RadarGui__radarObjects[objId]
            objType = objInfo['type']
            radarNode = objInfo['radarObjNode']
            outOfRangeNode = objInfo['outOfRangeNode']
            srcObjNode = objInfo['srcObjNode']
            dummyNode = objInfo['dummySrcObjNode']
            if not self.checkValidSrcObjNode(srcObjNode, objId):
                return Task.cont

            if radarNode and not srcObjNode.getParent().isEmpty():
                self.reparentRadarNode(radarNode)
                (dx, dz, relH, inRange) = self.getXZHRelativeToAV(srcObjNode)
                if objType == RADAR_OBJ_TYPE_EXIT:
                    self.setExitNode(radarNode, srcObjNode, outOfRangeNode, dx, dz, relH, inRange)
                else:
                    self.drawRadarNode(dx, dz, relH, inRange, radarNode)
                self.drawOutOfRangeNode(inRange, outOfRangeNode, srcObjNode)
                self.updateDummyNodePos(dummyNode, srcObjNode)
                continue

        return Task.cont


    def checkValidSrcObjNode(self, srcObjNode, objId):
        if srcObjNode and srcObjNode.isEmpty():
            self.moveRadarObjToCache(objId)
            return False

        return True


    def reparentRadarNode(self, radarNode):
        if radarNode.getParent() != self.objTop:
            radarNode.reparentTo(self.objTop)
            radarNode.setScale(1)



    def drawRadarNode(self, dx, dz, relH, inRange, radarNode):
        if inRange:
            radarNode.show()
            radarNode.setPos(dx, 0, dz)
            radarNode.setR(-relH - 180)
        else:
            radarNode.hide()


    def setExitNode(self, radarNode, srcObjNode, outOfRangeNode, dx, dz, relH, inRange):
        if inRange:
            radarNode.show()
            radarNode.setR((-relH - 180) + 90)
            radarNode.setPos(dx, 0, dz + RADAR_OBJ_EXIT_OFFSET_Z)
            radarNode.getChild(0).getChild(0).setH(90)
        else:
            radarNode.hide()
        outOfRangeNode.getChild(0).getChild(0).setHpr(90, 0, 90)


    def drawOutOfRangeNode(self, inRange, outOfRangeNode, srcObjNode):
        if outOfRangeNode:
            if inRange:
                outOfRangeNode.hide()
            else:
                outOfRangeNode.show()
                (dx, dz, relH, inRange) = self.getXZHRelativeToAV(srcObjNode)
                child = outOfRangeNode.getChild(0)
                child.lookAt(dx, 0, dz)
                vec = VBase3(dx, 0, dz)
                vec.normalize()
                outOfRangeNode.setPos(vec[0], 0, vec[2])



    def updateDummyNodePos(self, dummyNode, srcObjNode):
        if dummyNode and srcObjNode.compareTo(dummyNode) != 0:
            dummyNode.setPos(srcObjNode.getPos(render))



    def updateDial(self, map):
        if map.getRadarAxis() == Options.RadarAxisMap:
            self.dial.setR(0)
            self.north.setR(0)
            self.objTop.setR(0)
        elif map.getRadarAxis() == Options.RadarAxisCamera:
            camH = camera.getH(render)
            self.dial.setR(camH)
            self.north.setR(-camH)
            self.objTop.setR(camH)
            self.camToAvAngle = camH - localAvatar.getH(render)

        map.getRadarAxis() == Options.RadarAxisMap


    def toggle(self, args = None):
        if self.state == 'Off':
            self.request('On')
        elif self.state == 'On':
            self.request('Off')



    def getXZHRelativeToAV(self, srcObjNode):
        self.relNode.setPos(self.av, 0, 0, 0)
        self.relNode.setHpr(render, 0, 0, 0)
        d = srcObjNode.getPos(self.relNode)
        h = srcObjNode.getH(self.relNode)
        d.setZ(0.0)
        inRange = 1
        if d.length() > self.radius:
            inRange = 0
            dNorm = Vec3(d)
            dNorm.normalize()
            d = dNorm * self.radius

        dx = d[0] * self._RadarGui__kX
        dz = d[1] * self._RadarGui__kZ
        return (dx, dz, h, inRange)


    def hideMinimapObjects(self):
        self.minimapObjects = localAvatar.guiMgr.minimap.objects.copy()
        self.minimapObjects.discard(localAvatar.getMinimapObject())
        for obj in self.minimapObjects:
            obj.removeFromMap()



    def restoreMinimapObjects(self):
        minimapObjects = localAvatar.guiMgr.minimap.objects.copy()
        minimapObjects.discard(localAvatar.getMinimapObject())
        for obj in minimapObjects:
            obj.removeFromMap()

        localAvatar.findAllMatches('**/demo-node-*').detach()
        for obj in self.minimapObjects:
            localAvatar.guiMgr.minimap.addObject(obj)

        self.minimapObjects = []


    def toggleDisplay(self, useReceiveEffect = False, destPos = None):
        if self.isHidden() or useReceiveEffect:
            self.show()
            if useReceiveEffect:
                if destPos:
                    self.zoomFSM.setLevels([
                        150])
                    localAvatar.guiMgr.createReceiveEffect(self, explain = True)
                else:
                    localAvatar.guiMgr.createReceiveEffect(self, explain = False)

        else:
            self.hide()


    def clearCloseUp(self):
        self.zoomFSM.request('Zoom1')


    def addEffectIval(self, ival):
        self.effectIvals.append(ival)


    def setCurrentIsland(self, modelPath, minimapNode, footprintObjects, areaUID):
        pass


    def clearCurrentIsland(self):
        pass


    def enterGAInterior(self, modelPath, minimapNode, footprintObjects, interiorUID):
        pass


    def exitGAInterior(self, interiorUID):
        pass


    def getRadarObjNode(self, objId):
        uItem = None
        radarObjInfo = self._RadarGui__radarObjects.get(objId)
        if radarObjInfo == None:
            pass
        1
        inNode = radarObjInfo['radarObjNode']
        outNode = radarObjInfo['outOfRangeNode']
        if inNode == None or inNode.isHidden():
            uItem = outNode
        else:
            uItem = inNode
        if outNode == None or outNode.isHidden():
            uItem = inNode
        else:
            uItem = outNode
        return uItem


    def flashRadarObject(self, objId, duration = None, scaleMin = Point3(0.5, 0.5, 0.5), scaleMax = Point3(1.0, 1.0, 1.0)):
        if duration != None and objId in self.flashCleanupTasks:
            task = self.flashCleanupTasks[objId][0]
            task.delayTime = duration
            task.recalcWakeTime()
            return True

        uItem = self.getRadarObjNode(objId)
        if uItem == None or uItem.isEmpty():
            return False

        displayIval = Sequence(LerpScaleInterval(uItem, duration = 0.5, scale = scaleMax, startScale = scaleMin, blendType = 'noBlend'), LerpScaleInterval(uItem, duration = 0.5, scale = scaleMin, startScale = scaleMax, blendType = 'noBlend'))
        displayIval.loop()
        if duration == None:
            self.addEffectIval([
                displayIval,
                objId])
        else:
            self.flashCleanupTasks[objId] = [
                taskMgr.doMethodLater(duration, self.endFlashRadarObject, 'endRadarObjFlash-' + str(objId), extraArgs = [
                    objId]),
                displayIval]
        return True


    def flashRadarObjectTimed(self, objId, duration = 5.0, scaleMin = Point3(0.75, 0.75, 0.75), scaleMax = Point3(1.25, 1.25, 1.25)):
        self.flashRadarObject(objId, duration, scaleMin = scaleMin, scaleMax = scaleMax)


    def endFlashRadarObject(self, objId):
        flashInfo = self.flashCleanupTasks.pop(objId, None)
        if flashInfo:
            taskMgr.remove(flashInfo[0])
            flashInfo[1].finish()
            uItem = self.getRadarObjNode(objId)
            if uItem and not uItem.isEmpty():
                uItem.setScale(1.0, 1.0, 1.0)


        return Task.done


    def cleanupEffects(self):
        if self.ringIval:
            self.ringIval.pause()
            self.ringIval = None

        for (currIval, currObjId) in self.effectIvals:
            currIval.finish()
            uItem = self.getRadarObjNode(currObjId)
            if uItem and not uItem.isEmpty():
                uItem.setScale(1.0, 1.0, 1.0)
                continue

        self.effectIvals = []


    def refreshRadarObject(self, objId):
        if objId in self._RadarGui__radarObjects:
            outOfRangeNode = self._RadarGui__radarObjects[objId]['outOfRangeNode']
            dummySrcObjNode = self._RadarGui__radarObjects[objId]['dummySrcObjNode']
            type = self._RadarGui__radarObjects[objId]['type']
            radarObjNode = self._RadarGui__radarObjects[objId]['radarObjNode']
            srcObjNode = self._RadarGui__radarObjects[objId]['srcObjNode']
            self.removeRadarObject(objId)
            self.addRadarObject(objId, srcObjNode)



    def restoreOldInfo(self, objId):
        objectInfo = self._RadarGui__radarObjects.get(objId)
        if not objectInfo:
            return True

        if objectInfo['srcObjNode'] is objectInfo['dummySrcObjNode']:
            pass
        offRadar = objectInfo['dummySrcObjNode'] != None
        if __dev__:
            import pdb
            pdb.set_trace()
        else:
            raise 'RadarException'
        if objectInfo and not offRadar:
            if 'oldInfo' in objectInfo:
                objectInfo['type'] = objectInfo['oldInfo']['type']
                radarObjNode = objectInfo.get('radarObjNode')
                if radarObjNode and not radarObjNode.isEmpty():
                    radarObjNode.remove_node()

                objectInfo['radarObjNode'] = objectInfo['oldInfo']['radarObjNode']
                radarObjNode = objectInfo.get('radarObjNode')
                radarObjNodeShown = False
                if radarObjNode and not radarObjNode.isEmpty():
                    radarObjNodeShown = True
                    radarObjNode.show()

                outOfRangeNode = objectInfo.get('outOfRangeNode')
                if outOfRangeNode and not outOfRangeNode.isEmpty():
                    outOfRangeNode.remove_node()

                objectInfo['outOfRangeNode'] = objectInfo['oldInfo']['outOfRangeNode']
                outOfRangeNode = objectInfo.get('outOfRangeNode')
                if outOfRangeNode and not outOfRangeNode.isEmpty():
                    outOfRangeNode.show()

                dummySrcObjNode = objectInfo.get('dummySrcObjNode')
                if dummySrcObjNode and not dummySrcObjNode.isEmpty():
                    dummySrcObjNode.remove_node()

                objectInfo['dummySrcObjNode'] = objectInfo['oldInfo']['dummySrcObjNode']
                if radarObjNodeShown == False and 'dummySrcObjNode' in objectInfo and objectInfo['dummySrcObjNode']:
                    objectInfo['dummySrcObjNode'].show()

                del objectInfo['oldInfo']
            else:
                self.convertRadarObject(RADAR_OBJ_TYPE_DEFAULT, objId)
            return True
        else:
            return False


    def handleMinimapButton(self):
        localAvatar.guiMgr.nextMinimap()


    def setMinimap(self, map):
        self.mapScale.getChildren().detach()
        self.edge.getChildren().detach()
        if map:
            self.avArrow.detachNode()
            if map.allowOnScreen():
                self.minimapButton.show()
            else:
                self.minimapButton.hide()
            map.getRadarNode().reparentTo(self.mapScale)
            if self.getCurrentOrNextState() == 'On':
                self.minimapSentry = map.getSentry()

            (levels, defaultLevel) = map.getZoomLevels()
            self.zoomFSM.setLevels(levels)
            self.zoomFSM._setLevel(defaultLevel)
        else:
            self.avArrow.reparentTo(self.frame)
            self.minimapButton.hide()
            self.minimapSentry = None


    def updateOutOfRange(self, map, minimapObj, icon):
        worldNode = map.getWorldNode()
        avPos = localAvatar.getPos(worldNode)
        objPos = minimapObj.worldNode.getPos(worldNode)
        vec = objPos - avPos
        if map.getRadarAxis() == Options.RadarAxisCamera:
            vec.setZ(0)
            vec = camera.getRelativeVector(worldNode, vec)

        vec.setZ(0)
        if vec.length() < self.radius:
            if icon.hasParent():
                icon.detachNode()

            return None
        elif not icon.hasParent():
            icon.reparentTo(self.edge)

        vec.normalize()
        icon.setR(-math.atan2(vec[1], vec[0]) * 180 / math.pi)


    def setMapScale(self, radius):
        self.radius = radius
        self.mapScale.setScale(1.0 / radius)
        messenger.send('radar-zoom', [
            radius])


    def showGlowRing(self):
        if self.ringIval and self.ringIval.isPlaying():
            return None

        self.ring.show()
        self.ringIval = Sequence(LerpColorScaleInterval(self.ring, 0.75, Vec4(1, 1, 0.299, 1), startColorScale = Vec4(1, 1, 0.299, 0.5)), LerpColorScaleInterval(self.ring, 0.75, Vec4(1, 1, 0.299, 0.5), startColorScale = Vec4(1, 1, 0.299, 1)))
        self.ringIval.loop()


    def hideGlowRing(self):
        if self.ringIval:
            self.ringIval.pause()
            self.ringIval = None

        self.ring.hide()


    def addDemoQuest(self, worldNode):
        self.demoQuest = MinimapDemoQuest(worldNode)
        localAvatar.guiMgr.minimap.addObject(self.demoQuest)


    def removeDemoQuest(self):
        if self.demoQuest:
            self.demoQuest.removeFromMap()
            self.demoQuest = None



    def addDemoTunnel(self, worldNode):
        self.demoTunnel = MinimapDemoTunnel(worldNode)
        localAvatar.guiMgr.minimap.addObject(self.demoTunnel)


    def removeDemoTunnel(self):
        if self.demoTunnel:
            self.demoTunnel.removeFromMap()
            self.demoTunnel = None



    def addDemoNpc(self, worldNode, type):
        self.demoNpc[type] = MinimapDemoNpc(worldNode, type)
        localAvatar.guiMgr.minimap.addObject(self.demoNpc[type])


    def removeDemoNpc(self, type):
        npc = self.demoNpc.pop(type, None)
        if npc:
            npc.removeFromMap()




class MinimapDemoObject(MinimapObject):
    pass


class MinimapDemoTunnel(MinimapDemoObject):
    ICON = None

    def __init__(self, worldNode):
        if not MinimapDemoTunnel.ICON:
            compass = loader.loadModel('models/gui/compass_main')
            MinimapDemoTunnel.ICON = compass.find('**/icon_rectangle_hollow').getChild(0)
            MinimapDemoTunnel.ICON.clearTransform()
            MinimapDemoTunnel.ICON.setHpr(0, 90, 0)

        MinimapDemoObject.__init__(self, 'demo-tunnel', worldNode, self.ICON)
        self.outOfRangeGeom = NodePath('outOfRange')
        icon = MinimapDemoTunnel.ICON.copyTo(self.outOfRangeGeom)
        icon.setPosHpr(1, 0, 0, 0, 0, 90)


    def _addedToMap(self, map):
        self.mapGeom.setScale(300)


    def _updateOnMap(self, map):
        localAvatar.guiMgr.radarGui.updateOutOfRange(map, self, self.outOfRangeGeom)


    def _removedFromMap(self, map):
        self.outOfRangeGeom.detachNode()



class MinimapDemoNpc(MinimapDemoObject):
    ICON = None

    def __init__(self, worldNode, type):
        if not MinimapDemoNpc.ICON:
            gui = loader.loadModel('models/gui/compass_main')
            MinimapDemoNpc.ICON = gui.find('**/icon_sphere')
            MinimapDemoNpc.ICON.clearTransform()
            MinimapDemoNpc.ICON.setHpr(90, 90, 0)
            MinimapDemoNpc.ICON.setScale(200)

        MinimapDemoObject.__init__(self, 'demo-npc', worldNode, self.ICON)
        self.type = type


    def _addedToMap(self, map):
        if self.type == RadarGui.DEMO_FRIEND:
            self.mapGeom.setColorScale(VBase4(0.100, 0.5, 1.0, 0.696), 1)
        elif self.type == RadarGui.DEMO_ENEMY:
            self.mapGeom.setColorScale(VBase4(1.0, 0.0, 0.0, 1), 1)




class MinimapDemoQuest(MinimapDemoObject):
    ICON = None
    ARROW = None

    def __init__(self, worldNode):
        if not MinimapDemoQuest.ICON:
            model = loader.loadModel('models/gui/compass_main')
            MinimapDemoQuest.ICON = model.find('**/icon_objective_grey')
            MinimapDemoQuest.ICON.clearTransform()
            MinimapDemoQuest.ICON.setHpr(0, 90, 0)
            MinimapDemoQuest.ICON.setColorScale(1, 1, 0, 1, 1)
            MinimapDemoQuest.ICON.flattenStrong()

        if not MinimapDemoQuest.ARROW:
            model = loader.loadModel('models/gui/compass_arrow')
            MinimapDemoQuest.ARROW = model.getChild(0).getChild(0).copyTo(NodePath())
            MinimapDemoQuest.ARROW.setScale(0.75)
            MinimapDemoQuest.ARROW.setColorScale(1, 1, 0, 1, 1)
            MinimapDemoQuest.ARROW.flattenStrong()

        MinimapDemoObject.__init__(self, 'quest', worldNode, MinimapDemoQuest.ICON)
        self.outOfRangeGeom = NodePath('outOfRange')
        arrow = MinimapDemoQuest.ARROW.copyTo(self.outOfRangeGeom)
        arrow.setPosHpr(1.10, 0, 0, 0, 0, 90)


    def _addedToMap(self, map):
        self.mapGeom.setScale(250)


    def _updateOnMap(self, map):
        localAvatar.guiMgr.radarGui.updateOutOfRange(map, self, self.outOfRangeGeom)


    def _removedFromMap(self, map):
        self.outOfRangeGeom.detachNode()
