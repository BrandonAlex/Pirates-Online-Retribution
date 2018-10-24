from panda3d.core import Camera, Vec3, lookAt
from pirates.pirate import ShipCamera
from pirates.ship import ShipGlobals

CamParams = ShipCamera.ShipCamera.ParamSet
ShipModelClass2CameraParams = {
    ShipGlobals.INTERCEPTORL1: CamParams(idealDistance = 270.0, autoFaceForward = True, minDistance = 100.0, maxDistance = 535.0, lookAtOffset = Vec3(0, 0, 40)),
    ShipGlobals.INTERCEPTORL2: CamParams(idealDistance = 550.0, autoFaceForward = True, minDistance = 200.0, maxDistance = 985.0, lookAtOffset = Vec3(0, 0, 60)),
    ShipGlobals.INTERCEPTORL3: CamParams(idealDistance = 600.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 1300.0, lookAtOffset = Vec3(0, 0, 80)),
    ShipGlobals.MERCHANTL1: CamParams(idealDistance = 350.0, autoFaceForward = True, minDistance = 150.0, maxDistance = 820.0, lookAtOffset = Vec3(0, 0, 40)),
    ShipGlobals.MERCHANTL2: CamParams(idealDistance = 600.0, autoFaceForward = True, minDistance = 200.0, maxDistance = 1185.0, lookAtOffset = Vec3(0, 0, 60)),
    ShipGlobals.MERCHANTL3: CamParams(idealDistance = 700.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 1625.0, lookAtOffset = Vec3(0, 0, 80)),
    ShipGlobals.WARSHIPL1: CamParams(idealDistance = 350.0, autoFaceForward = True, minDistance = 150.0, maxDistance = 800.0, lookAtOffset = Vec3(0, 0, 40)),
    ShipGlobals.WARSHIPL2: CamParams(idealDistance = 600.0, autoFaceForward = True, minDistance = 200.0, maxDistance = 1285.0, lookAtOffset = Vec3(0, 0, 60)),
    ShipGlobals.WARSHIPL3: CamParams(idealDistance = 700.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 1650.0, lookAtOffset = Vec3(0, 0, 80)),
    ShipGlobals.SHIP_OF_THE_LINE: CamParams(idealDistance = 1000.0, autoFaceForward = True, minDistance = 300.0, maxDistance = 2500.0, lookAtOffset = Vec3(0, 0, 50)),
    ShipGlobals.BLACK_PEARL: CamParams(idealDistance = 600.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 1680.0, lookAtOffset = Vec3(0, 0, 50)),
    ShipGlobals.QUEEN_ANNES_REVENGE: CamParams(idealDistance = 600.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 1300.0, lookAtOffset = Vec3(0, 0, 80)),
    ShipGlobals.GOLIATH: CamParams(idealDistance = 600.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 2775.0, lookAtOffset = Vec3(0, 0, 50)),
    ShipGlobals.SKEL_WARSHIPL3: CamParams(idealDistance = 600.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 1545.0, lookAtOffset = Vec3(0, 0, 80)),
    ShipGlobals.SKEL_INTERCEPTORL3: CamParams(idealDistance = 550.0, autoFaceForward = True, minDistance = 250.0, maxDistance = 1330.0, lookAtOffset = Vec3(0, 0, 80)) }
del CamParams
