from panda3d.core import CollideMask, NodePath, Point3, Vec3, Vec4
import random
from direct.interval.IntervalGlobal import *
from direct.distributed import DistributedObject
from direct.distributed import DistributedCartesianGrid
from direct.showbase.PythonUtil import report
from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import TODGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals, RadarGui
from pirates.world.LocationConstants import LocationIds, getLocationList
from pirates.world import DistributedIsland
from pirates.world import DistributedGameArea
from pirates.world import GridAreaBuilder
from pirates.world import WorldGlobals
from pirates.map.Minimap import InteriorMap
from pirates.map.Mappable import MappableGrid
from otp.otpbase import OTPRender

class DistributedGAInterior(DistributedGameArea.DistributedGameArea, DistributedCartesianGrid.DistributedCartesianGrid, MappableGrid):
    notify = directNotify.newCategory('DistributedGAInterior')

    def __init__(self, cr):
        DistributedGameArea.DistributedGameArea.__init__(self, cr)
        DistributedCartesianGrid.DistributedCartesianGrid.__init__(self, cr)
        MappableGrid.__init__(self)
        self.intervals = []
        self.fadeInTrack = None
        self.autoFadeIn = True
        self.musicName = None
        self.buildingInterior = False

    def setBuildingInterior(self, buildingInterior):
        self.buildingInterior = buildingInterior

    def announceGenerate(self):
        DistributedGameArea.DistributedGameArea.announceGenerate(self)
        DistributedCartesianGrid.DistributedCartesianGrid.announceGenerate(self)
        if not base.cr.activeWorld.worldGrid:
            base.cr.activeWorld.setWorldGrid(self)

        self.loadModel()
        for obj in self.geom.findAllMatches('**/=ignore-lighting'):
            obj.setLightOff(1000)

        doorPlanes = self.geom.findAllMatches('**/door_collision_planar_*;+s')
        doorPlanes.stash()
        self.startProcessVisibility(base.localAvatar)
        base.worldCreator.registerSpecialNodes(self, self.uniqueId)
        self.builder.loadObjects()
        self.enableFloors()
        self.loadConnectors()
        self.initBlockers(self)
        self.startCustomEffects()
        self.builder.resumeSFX()
        self.closeSfx = loadSfx(SoundGlobals.SFX_DOOR_SLAM)

        if self.buildingInterior:
            self.setZ(100)

    def disable(self):
        self.stopCustomEffects()
        self.builder.pauseSFX()
        self.unloadConnectors()
        if self.fadeInTrack:
            self.fadeInTrack.pause()

        self.fadeInTrack = None
        self.ignoreAll()
        DistributedGameArea.DistributedGameArea.disable(self)
        DistributedCartesianGrid.DistributedCartesianGrid.disable(self)
        del self.closeSfx

    def delete(self):
        del self.coll
        self.geom.remove_node()
        if self.modelPath != 'models/buildings/navy_jail_interior':
            self.stopProcessVisibility()
            self.handleExitGameArea(None)

        self.fadeOutSoundAndMusic()
        self.disableFloors()
        for anim in self.intervals:
            if anim:
                anim.pause()
                del anim
                continue

        self.intervals = []
        DistributedGameArea.DistributedGameArea.delete(self)
        DistributedCartesianGrid.DistributedCartesianGrid.delete(self)

    def isGridParent(self):
        return 1

    def addObjectToGrid(self, av):
        DistributedCartesianGrid.DistributedCartesianGrid.addObjectToGrid(self, av)
        if av.isLocal():
            self.updateAvReturnLocation(av)

    def setLinks(self, links):
        DistributedGameArea.DistributedGameArea.setLinks(self, links)
        self.loadConnectors()

    def setConnectorId(self, connectorId):
        self.connectorId = connectorId

    def enableFloors(self):
        floorName = 'floor_interior'
        self.uniqueFloorName = self.uniqueName(floorName)
        collNodes = self.findAllMatches('**/+CollisionNode')
        for collNode in collNodes:
            curMask = collNode.node().getIntoCollideMask()
            if curMask.hasBitsInCommon(PiratesGlobals.FloorBitmask):
                collNode.setName(self.uniqueFloorName)
                self.setupCannonballLandColl(collNode, PiratesGlobals.TargetBitmask | curMask, 0)

        self.accept('enterFloor' + self.uniqueFloorName, self.handleEnterGameArea)
        self.accept('exitFloor' + self.uniqueFloorName, self.handleExitGameArea)

    def disableFloors(self):
        if self.uniqueFloorName:
            self.ignore('enterFloor' + self.uniqueFloorName)
            self.ignore('exitFloor' + self.uniqueFloorName)

    def handleEnterGameArea(self, collEntry):
        localAvatar.interior = self
        self.addObjectToGrid(localAvatar)
        if self.buildingInterior:
            localAvatar.setInterest(self.doId, 2709, ['ga-interior'])
        DistributedGameArea.DistributedGameArea.handleEnterGameArea(self, collEntry)

    def setLocation(self, parentId, zoneId, teleport = 0):
        DistributedObject.DistributedObject.setLocation(self, parentId, zoneId)
        self.reparentTo(render)

    def getZoneFromXYZ(self, *args):
        if self.buildingInterior:
            return 2709

        return DistributedCartesianGrid.DistributedCartesianGrid.getZoneFromXYZ(self, *args)

    def handleExitGameArea(self, collEntry):
        if collEntry:
            return None

        self.removeObjectFromGrid(localAvatar)
        self.stopProcessVisibility()
        localAvatar.interior = None
        localAvatar.clearInterestNamed(None, ['ga-interior'])
        DistributedGameArea.DistributedGameArea.handleExitGameArea(self, collEntry)

    def loadModelParts(self):
        if self.modelPath.startswith('models/islands/pir_m_are_isl_'):
            self.geom = loader.loadModel(self.modelPath)
            return None

        modelBaseName = self.modelPath.split('_zero')[0]
        terrainModel = loader.loadModel(modelBaseName + '_terrain', okMissing = True)
        if terrainModel:
            self.geom = terrainModel
        else:
            self.geom = loader.loadModel(self.modelPath)
            return None
        terrainDetailModel = loader.loadModel(modelBaseName + '_terrain_detail', okMissing = True)
        if terrainDetailModel:
            self.notify.debug('loading _terrain_detail')
            terrainDetailModel.getChild(0).reparentTo(self.geom)

        pierModel = loader.loadModel(modelBaseName + 'pier', okMissing = True)
        if pierModel:
            self.notify.debug('loading pier')
            pierModel.getChild(0).reparentTo(self.geom)

        fortModel = loader.loadModel(modelBaseName + '_fort', okMissing = True)
        if fortModel:
            self.notify.debug('loading _fort')
            fortModel.getChild(0).reparentTo(self.geom)

        logModel = loader.loadModel(modelBaseName + '_logs', okMissing = True)
        if logModel:
            self.notify.debug('loading _logs')
            logModel.getChild(0).reparentTo(self.geom)

        vegeWallModel = loader.loadModel(modelBaseName + '_nat_wall', okMissing = True)
        if vegeWallModel:
            self.notify.debug('loading _nat_wall')
            vegeWallModel.getChild(0).reparentTo(self.geom)

        vegModel = loader.loadModel(modelBaseName + '_veg', okMissing = True)
        if vegModel:
            self.notify.debug('loading _veg')
            vegModel.getChild(0).reparentTo(self.geom)

        rockModel = loader.loadModel(modelBaseName + '_rocks', okMissing = True)
        if rockModel:
            self.notify.debug('loading _rocks')
            rockModel.getChild(0).reparentTo(self.geom)

        mapNode = self.getMapNode()
        if mapNode and not mapNode.isEmpty():
            mapNode.hide()

    def loadModel(self):
        if 'interior' not in self.modelPath:
            self.loadModelParts()
        else:
            self.geom = loader.loadModel(self.modelPath)
        self.geom.findAllMatches('**/door_hole*').setColorScale(Vec4(0, 0, 0, 1))
        self.geom.reparentTo(self)
        self.geom.hide(OTPRender.MainCameraBitmask)
        self.geom.showThrough(OTPRender.EnviroCameraBitmask)
        coll = self.geom.findAllMatches('**/+CollisionNode')
        self.coll = coll
        locatorNodes = self.geom.findAllMatches('**/portal_interior_*')
        locatorNodes.wrtReparentTo(self)
        self.locatorNodes = locatorNodes
        self.portalNodes = self.geom.findAllMatches('**/portal_[0-9]')
        self.initBlockers(self.geom)

    def setName(self, name):
        self.name = name

    def getTeam(self):
        return PiratesGlobals.ISLAND_TEAM

    def updateAvReturnLocation(self, av):
        if 'Jail' in self.dclass.getName():
            av.d_requestReturnLocation(self.doId)

    def enterInteriorFromDoor(self, doorIndex):
        base.cr.loadingScreen.showTarget(self.uniqueId)
        base.cr.loadingScreen.show()
        doorIndexStr = ''
        if doorIndex > 0:
            doorIndexStr = '_' + str(doorIndex + 1)

        self.doorLeftStr = '**/door_left' + doorIndexStr
        self.doorRightStr = '**/door_right' + doorIndexStr
        self.doorLocatorStr = '**/door_locator' + doorIndexStr
        doorLeft = self.geom.find(self.doorLeftStr)
        doorRight = self.geom.find(self.doorRightStr)
        self.openDoorIval = Parallel()
        self.closeDoorIval = Parallel()
        self.tOpen = 0.5
        if not doorLeft.isEmpty():
            self.openDoorIval.append(LerpHprInterval(doorLeft, self.tOpen, Vec3(-90, 0, 0)))
            self.closeDoorIval.append(LerpHprInterval(doorLeft, self.tOpen, Vec3(0, 0, 0)))

        if not doorRight.isEmpty():
            self.openDoorIval.append(LerpHprInterval(doorRight, self.tOpen, Vec3(90, 0, 0)))
            self.closeDoorIval.append(LerpHprInterval(doorRight, self.tOpen, Vec3(0, 0, 0)))

        doorLocator = self.geom.find(self.doorLocatorStr)
        if doorLocator.isEmpty():
            doorLocator = self.geom.find(self.doorLeftStr)
            if doorLocator.isEmpty():
                doorLocator = self.geom.find(self.doorRightStr)

        localAvatar.reparentTo(doorLocator)
        localAvatar.setPos(0, 10, 0)
        localAvatar.setHpr(0, 0, 0)
        localAvatar.wrtReparentTo(self)
        localAvatar.setP(0)
        localAvatar.setR(0)
        localAvatar.setScale(1)
        self.handleEnterGameArea(None)
        base.loadingScreen.tick()
        messenger.send('doorToInteriorFadeIn', [
            self.uniqueId])
        base.loadingScreen.tick()
        if self.autoFadeIn:
            fadeInFunc = Func(base.transitions.fadeIn, self.tOpen)
            playerStateFunc = Func(localAvatar.gameFSM.request, 'LandRoam')
        else:

            def Nothing():
                pass

            fadeInFunc = Func(Nothing)
        if self.autoFadeIn:
            sf = Sequence(Func(self.requestDoorInteract), fadeInFunc, self.openDoorIval, self.closeDoorIval, Func(self.closeSfx.play), Func(self.requestPlayerStateFunc))
        else:
            sf = Sequence(Func(self.requestDoorInteract), fadeInFunc, self.openDoorIval, self.closeDoorIval, Func(self.requestPlayerStateFunc))
        self.fadeInTrack = sf
        self.fadeInTrack.start()
        base.cr.loadingScreen.hide()

    def requestPlayerStateFunc(self):
        if localAvatar.getGameState() in [
            'Injured']:
            return None

        if self.autoFadeIn:
            localAvatar.gameFSM.request('LandRoam')

    def requestDoorInteract(self):
        if localAvatar.getGameState() in [
            'Injured']:
            return None

        localAvatar.gameFSM.request('DoorInteract')

    def handleChildArrive(self, childObj, zoneId):
        DistributedGameArea.DistributedGameArea.handleChildArrive(self, childObj, zoneId)
        if childObj.isLocal():
            self.updateAvReturnLocation(childObj)
            self.builder.checkForHolidayObjects()
            self.requestSoundAndMusic()
            if not self.footstepSound:
                localAvatar.setAreaFootstep('Wood')

            self.setupMinimap()
            if self.minimap and localAvatar.getMinimapObject():
                self.minimap.addObject(localAvatar.getMinimapObject())
                localAvatar.guiMgr.setMinimap(self.minimap)

    def handleChildLeave(self, childObj, zoneId):
        DistributedGameArea.DistributedGameArea.handleChildLeave(self, childObj, zoneId)
        if childObj.isLocal():
            localAvatar.guiMgr.clearMinimap(self.minimap)
            self.destroyMinimap()
            self.fadeOutSoundAndMusic()

    def loadConnectors(self):
        if 'interior' in self.modelPath and 'fortCharles_zero' in self.modelPath and 'kingshead_zero' in self.modelPath or 'pir_m_bld_int_tavernA_oneDoor' in self.modelPath:
            return None

        DistributedGameArea.DistributedGameArea.loadConnectors(self)

    def unloadConnectors(self):
        if 'interior' in self.modelPath and 'fortCharles_zero' in self.modelPath and 'kingshead_zero' in self.modelPath or 'pir_m_bld_int_tavernA_oneDoor' in self.modelPath:
            return None

        DistributedGameArea.DistributedGameArea.unloadConnectors(self)

    def setAutoFadeInOnEnter(self, autoFadeIn):
        self.autoFadeIn = autoFadeIn

    def getTeleportDestPosH(self, index = 0):
        pt = self._getTunnelSpawnPos(index)
        if pt == None:
            pt = self._getDoorSpawnPos(index)

        return (pt[0], pt[1], pt[2], 0)

    def _getDoorSpawnPos(self, index = 0):
        doorIndexStr = ''
        if index > 0:
            index = '_' + str(index + 1)

        doorLocatorStr = '**/door_locator' + doorIndexStr
        doorLocator = self.find(doorLocatorStr)
        if doorLocator.isEmpty():
            doorLocator = self.find(self.doorLeftStr)
            if doorLocator.isEmpty():
                doorLocator = self.find(self.doorRightStr)

        return self.getRelativePoint(doorLocator, Point3(0, 10, 0))

    def turnOn(self, av=None):
        self.unstash()

        if self.buildingInterior:
            av = None

        DistributedGameArea.DistributedGameArea.turnOn(self, av)
        DistributedCartesianGrid.DistributedCartesianGrid.turnOn(self, av)

    def turnOff(self):
        DistributedGameArea.DistributedGameArea.turnOff(self)
        DistributedCartesianGrid.DistributedCartesianGrid.turnOff(self)
        self.stash()

    def getLevel(self):
        return 1

    def handleLowTerrainDetail(self):
        grids = self.findAllMatches('**/Grid-*')
        for dl in self.builder.dynamicLights:
            if dl.type != 0:
                for gi in xrange(0, grids.getNumPaths()):
                    geomParent = grids[gi].getChild(0)
                    geomParent.setLightOff(dl.lightNodePath)
                    for ci in xrange(0, geomParent.getNumChildren()):
                        geoms = geomParent.getChild(ci)
                        geoms.setLightOff(dl.lightNodePath)

    def requestSoundAndMusic(self):
        self.ambientName = SoundGlobals.getAmbientFromStr(self.modelPath)
        if not self.ambientName == SoundGlobals.AMBIENT_JUNGLE and self.ambientName == SoundGlobals.AMBIENT_CAVE or self.ambientName == SoundGlobals.AMBIENT_SWAMP:
            base.ambientMgr.requestFadeIn(self.ambientName, finalVolume = PiratesGlobals.DEFAULT_AMBIENT_VOLUME)

        if self.musicName:
            base.musicMgr.requestFadeOut(self.musicName)
            self.musicName = None

        if self.uniqueId == LocationIds.RAMBLESHACK_INSIDE and localAvatar.getTutorialState() < 2:
            self.musicName = SoundGlobals.MUSIC_COMBAT_A
            base.musicMgr.request(self.musicName, priority = 1, volume = 0.3)
        elif 'tavern' in self.modelPath:
            self.musicName = random.choice((SoundGlobals.MUSIC_TAVERN_A, SoundGlobals.MUSIC_TAVERN_B, SoundGlobals.MUSIC_TAVERN_C))
            base.musicMgr.request(self.musicName, priority = 1, volume = 0.5)

    def fadeOutSoundAndMusic(self):
        if hasattr(self, 'ambientName'):
            if not self.ambientName == SoundGlobals.AMBIENT_JUNGLE and self.ambientName == SoundGlobals.AMBIENT_CAVE:
                pass
            if not (self.ambientName == SoundGlobals.AMBIENT_SWAMP):
                base.ambientMgr.requestFadeOut(self.ambientName)

        if self.musicName:
            base.musicMgr.requestFadeOut(self.musicName)
            self.musicName = None

    def setupMinimap(self):
        if not (self.minimap) and self.getMapNode():
            self.minimap = InteriorMap(self)

    def destroyMinimap(self):
        if self.minimap:
            self.minimap.destroy()
            self.minimap = None

    def getGridParameters(self):
        return (self.cellWidth, self.viewingRadius)

    def getTunnelNodes(self):
        return self.locatorNodes

    def isInInvasion(self):
        return False

    def getArmorScale(self):
        return 1.0
