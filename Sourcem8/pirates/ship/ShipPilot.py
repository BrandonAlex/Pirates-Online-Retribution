from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.InputStateGlobal import inputState
from direct.task.Task import Task
from direct.controls.PhysicsWalker import PhysicsWalker
import math

class ShipPilot(PhysicsWalker):
    notify = directNotify.newCategory('ShipPilot')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    MAX_STRAIGHT_SAIL_BONUS = 2.1
    STRAIGHT_SAIL_BONUS_TIME = 18.0
    REVERSE_STRAIGHT_SAIL_BONUS_TIME = -8.0
    TURNING_BONUS_REDUCTION = 3.0

    def __init__(self, gravity = -32.174, standableGround = 0.707, hardLandingForce = 16.0):
        PhysicsWalker.__init__(self, gravity, standableGround, hardLandingForce)
        self._ShipPilot__speed = 0.0
        self._ShipPilot__rotationSpeed = 0.0
        self._ShipPilot__slideSpeed = 0.0
        self._ShipPilot__vel = Vec3(0.0)
        self.currentTurning = 0.0
        self.ship = None
        self.pusher = None
        self.straightHeading = 0
        self.cNodePath = None


    def setWalkSpeed(self, forward, jump, reverse, rotate):
        PhysicsWalker.setWalkSpeed(self, forward, 0, reverse, rotate)


    def setWallBitMask(self, bitMask):
        self.wallBitmask = bitMask


    def adjustWallBitMask(self, oldMask, newMask):
        self.wallBitmask = self.wallBitmask & ~oldMask
        self.wallBitmask |= newMask
        if self.cNodePath and not self.cNodePath.isEmpty():
            self.cNodePath.node().setFromCollideMask(self.wallBitmask)



    def setFloorBitMask(self, bitMask):
        self.floorBitmask = bitMask


    def setShip(self, ship):
        self.setAvatar(ship)


    def setAvatar(self, ship):
        if ship is None:
            if self.ship is not None and base.controlForce.getPhysicsObject() == self.ship.node().getPhysicsObject():
                base.controlForce.clearPhysicsObject()
                base.controlForce.setVector(Vec3(0))

            self.takedownPhysics()
            self.setCollisionsActive(0)
            self.ship = ship
        else:
            base.controlForce.setPhysicsObject(ship.node().getPhysicsObject())
            self.ship = ship
            self.setupPhysics(ship)
            self.setCollisionsActive(1)


    def initializeCollisions(self, collisionTraverser, cRootNodePath, bow, stern, starboard, port):
        self.cTrav = collisionTraverser
        self.cRootNodePath = cRootNodePath
        self.bowPos = bow.getPos(cRootNodePath)
        self.sternPos = stern.getPos(cRootNodePath)
        self.starboardPos = starboard.getPos(cRootNodePath)
        self.portPos = port.getPos(cRootNodePath)


    def setupCollisions(self):
        if self.pusher:
            return None

        self.pusher = CollisionHandlerPusher()
        self.pusher.setInPattern('enter%in')
        self.pusher.setOutPattern('exit%in')
        sRadius = abs(self.portPos - self.starboardPos[0] / 2.0)
        cNode = CollisionNode('SP.cNode')
        frontPos = self.bowPos[1] + sRadius
        rearPos = self.sternPos[1] - sRadius
        cBowSphere = CollisionSphere(0.0, frontPos, 0.0, sRadius)
        cSternSphere = CollisionSphere(0.0, rearPos, 0.0, sRadius)
        midSphereRadius = max(sRadius, (rearPos - frontPos - sRadius * 2) / 2)
        cMidSphere = CollisionSphere(0.0, frontPos + (rearPos - frontPos) / 2, 0.0, midSphereRadius)
        cNode.addSolid(cBowSphere)
        cNode.addSolid(cMidSphere)
        cNode.addSolid(cSternSphere)
        shipIColRoot = self.ship.getInteractCollisionRoot()
        self.cNodePath = shipIColRoot.attachNewNode(cNode)
        shipLen = abs(self.sternPos[1] - self.bowPos[1])
        self.cNodePath.setScale(1, 1, 1)
        self.pusher.addCollider(self.cNodePath, self.shipNodePath)
        self.pusher.setHorizontal(True)
        self.ship.getWallCollisions().stash()


    def setCollisionsActive(self, active = 1):
        if active:
            self.setupCollis
