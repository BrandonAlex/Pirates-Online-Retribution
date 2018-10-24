from panda3d.core import lookAt
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.FSM import FSM
from direct.distributed.GridParent import GridParent
from direct.distributed.ClockDelta import *
from pirates.battle.DistributedBattleAvatarAI import *
from pirates.piratesbase import PiratesGlobals
from pirates.battle import WeaponGlobals
from pirates.battle import EnemyGlobals

import random

class DistributedBattleNPCAI(DistributedBattleAvatarAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleNPCAI')
    isNpc = True

    def __init__(self, spawner):
        self.spawner = spawner
        DistributedBattleAvatarAI.__init__(self, spawner.air)
        FSM.__init__(self, 'DistributedBattleNPCAI')
        self.spawnPos = (0, 0, 0)
        self.spawnPosIndex = ''
        self.associatedQuests = []

        self.animSet = 'default'
        self.noticeAnim1 = ''
        self.noticeAnim2 = ''
        self.greetingAnim = ''

        self.collisionMode = PiratesGlobals.COLL_MODE_ALL
        self.initZ = 0
        self.uniqueId = ''

        self.enemies = set()

    def setLevel(self, level):
        if not level:
            level = EnemyGlobals.getRandomEnemyLevel(self.avatarType)
        DistributedBattleAvatarAI.setLevel(self, level)
        maxHp = EnemyGlobals.getMonsterHp(level)
        self.setHp(maxHp)
        self.setMaxHp(maxHp)

    def announceGenerate(self):
        DistributedBattleAvatarAI.announceGenerate(self)
        self.demand('Spawn')

        self.skills = EnemyGlobals.getEnemySkills(self.avatarType, self.level)
        self.weapons = EnemyGlobals.getEnemyWeapons(self.avatarType, self.level)

        self.mainWeapon = self.weapons.keys()[0]
        if self.mainWeapon > 1:
            self.b_setCurrentWeapon(self.mainWeapon, 0)

    def enterSpawn(self):
        self.sendUpdate('setSpawnIn', [globalClockDelta.getRealNetworkTime(bits=32)])
        self.addSkillEffect(WeaponGlobals.C_SPAWN)
        taskMgr.doMethodLater(8, self.__removeSpawn, self.uniqueName('spawned'))

    def __removeSpawn(self, task):
        self.removeSkillEffect(WeaponGlobals.C_SPAWN)
        self.demand(self.getStartState())
        return task.done

    def exitSpawn(self):
        taskMgr.remove(self.uniqueName('spawned'))
        self.d_updateSmPos()

    def delete(self):
        self.demand('Off')
        DistributedBattleAvatarAI.delete(self)

    def setSpawnPos(self, spawnPos):
        self.spawnPos = spawnPos

    def getSpawnPos(self):
        return self.spawnPos

    def getSpawnPosIndex(self):
        # This seems related to quests, return uniqueId for now
        return self.getUniqueId()

    def setAssociatedQuests(self, associatedQuests):
        self.associatedQuests = associatedQuests

    def getAssociatedQuests(self):
        return self.associatedQuests

    def setActorAnims(self, animSet, noticeAnim1, noticeAnim2, greetingAnim):
        self.animSet = animSet
        self.noticeAnim1 = noticeAnim1
        self.noticeAnim2 = noticeAnim2
        self.greetingAnim = greetingAnim

    def getActorAnims(self):
        return [self.animSet, self.noticeAnim1, self.noticeAnim2, self.greetingAnim]

    def setCollisionMode(self, collisionMode):
        self.collisionMode = collisionMode

    def getCollisionMode(self):
        return self.collisionMode

    def setUniqueId(self, uniqueId):
        self.uniqueId = uniqueId

    def setAvatarType(self, avatarType):
        DistributedBattleAvatarAI.setAvatarType(self, avatarType)
        self.setName(self.avatarType.getName())

    def getUniqueId(self):
        return self.uniqueId

    # setInitZ is not used by client
    def setInitZ(self, initZ):
        self.initZ = initZ

    def getInitZ(self):
        return self.initZ

    def posControlledByIsland(self):
        area = self.getParentObj()

        cell = GridParent.getCellOrigin(area, self.zoneId)
        pos = self.getPos()
        self.reparentTo(cell)
        self.setPos(area, pos)

        self.d_updateSmPos()
        return False

    def d_updateSmPos(self):
        x, y, z, h, p, r = list(self.getPos()) + list(self.getHpr())
        self.sendUpdate('setSmPosHpr', [x, y, z, h, p, r, 0])

    def enterBattle(self):
        self.sendUpdate('setIsAlarmed', [1, self.getAggroRadius()])
        self.waitForNextBattleTask()
        if self.mainWeapon > 1:
            self.b_setCurrentWeapon(self.mainWeapon, 1)

    def waitForNextBattleTask(self):
        dt = random.random() * 6 + .15
        dt -= self.getLevel() / 25.0
        dt = max(.3, dt)
        taskMgr.doMethodLater(dt, self.__battleTask, self.taskName('battleTask'))

    def __battleTask(self, task):
        remove = set()
        for enemy in self.enemies:
            av = self.air.doId2do.get(enemy)
            if not av:
                remove.add(enemy)
                continue

            if av.hp <= 0:
                remove.add(enemy)
                continue

            if av.getLocation() != self.getLocation():
                remove.add(enemy)
                continue

            if (self.getPos() - av.getPos()).length() > EnemyGlobals.CALL_FOR_HELP_DISTANCE:
                remove.add(enemy)
                continue

        for r in remove:
            self.removeEnemy(r)

        if not self.enemies:
            self.demand('Idle')
            return task.done

        target, = random.sample(self.enemies, 1)
        av = self.air.doId2do[target]

        skillId = random.choice(self.skills.keys())
        ammoSkillId = 0 # TO DO
        pos = self.getPos() - av.getPos()
        self.lookAt(av)
        self.d_updateSmPos()
        result = self.attemptUseTargetedSkill(skillId, ammoSkillId, 0, av.doId, [],
                                              globalClockDelta.getRealNetworkTime(bits=32),
                                              pos, 0)

        if result == WeaponGlobals.RESULT_OUT_OF_RANGE and not ammoSkillId:
            self.removeEnemy(av.doId)

        self.waitForNextBattleTask()
        return task.done

    def getMonsterDmg(self):
        return EnemyGlobals.getMonsterDmg(self.level)

    def exitBattle(self):
        self.sendUpdate('setIsAlarmed', [0, 0])
        taskMgr.remove(self.taskName('battleTask'))

        if self.mainWeapon > 1:
            self.b_setCurrentWeapon(self.mainWeapon, 0)

    # TO DO:
    # boardVehicle(uint32) broadcast ram
    # setChat(string, uint8) broadcast ownsend
    # requestAnimSet(string) broadcast

    def handleInteract(self, avId, interactType, instant):
        if interactType == PiratesGlobals.INTERACT_TYPE_HOSTILE:
            self.enemies.add(avId)
            if self.state not in ('Battle', 'Death'):
                self.demand('Battle')

            av = self.air.doId2do.get(avId)
            if av:
                av.sendUpdate('setCurrentTarget', [0])

        return IGNORE

    def requestHostilize(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.handleInteract(avId, PiratesGlobals.INTERACT_TYPE_HOSTILE, 0)

    def requestExit(self):
        avId = self.air.getAvatarIdFromSender()
        self.removeEnemy(avId)

    def removeEnemy(self, avId):
        if avId in self.enemies:
            self.enemies.remove(avId)
            av = self.air.doId2do.get(avId)
            if av:
                av.sendUpdate('setCurrentTarget', [0])

    def enterAmbush(self):
        self.sendUpdate('setAmbush', [1])

    def ambushIntroDone(self):
        if self.state == 'Ambush':
            self.demand('Battle')

    def died(self):
        self.demand('Death')

    def enterDeath(self):
        def doDeath(task):
            self.spawner.died()
            self.applyRewards()
            self.requestDelete()
            return task.done

        taskMgr.doMethodLater(5, doDeath, self.taskName('death'))

    def applyRewards(self):
        multiplier = random.randint(6, 12) / 1.2
        for avId, skills in self.enemySkills.items():
            av = self.air.doId2do.get(avId)
            if not av:
                continue

            repId2rep = {}
            for repId, skillId, ammoSkillId in skills:
                amount = int(self.level * WeaponGlobals.getAttackReputation(skillId, ammoSkillId) * multiplier)
                repId2rep[repId] = repId2rep.get(repId, 0) + amount

            for repId, amount in repId2rep.items():
                while amount > 125:
                    amount = int(amount / 1.173)
                av.inventory.addReputation(repId, amount)

            av.repChanged()

    def exitDeath(self):
        taskMgr.remove(self.taskName('death'))

    def demand(self, state, *args):
        FSM.demand(self, state, *args)
        self.sendUpdate('setGameState', [state, globalClockDelta.getRealNetworkTime()])

    @staticmethod
    def makeFromObjectKey(cls, spawner, uid, avType, data):
        if cls is None:
            cls = DistributedBattleNPCAI

        obj = cls(spawner)

        x, y, z = data.get('Pos', (0, 0, 0))
        h, p, r = data.get('Hpr', (0, 0, 0))
        pos = (x, y, z)
        hpr = (h, p, r)

        obj.setSpawnPos(pos)
        obj.setPos(pos)
        obj.setHpr(hpr)

        animSet = data.get('AnimSet', 'default')
        noticeAnim1 = data.get('Notice Animation 1', '')
        noticeAnim2 = data.get('Notice Animation 2', '')
        greetingAnim = data.get('Greeting Animation', '')

        obj.setAvatarType(avType)
        obj.setUniqueId(uid)
        obj.setActorAnims(animSet, noticeAnim1, noticeAnim2, greetingAnim)
        try:
            obj.setIsGhost(int(data['GhostFX']))
        except:
            # some objects don't have GhostFX declared in their data.
            obj.setIsGhost(0)
        try:
            obj.setGhostColor(int(data['GhostColor']))
        except:
            obj.setGhostColor(None)
        if 'Level' in data:
            obj.setLevel(int(data['Level']))

        if 'Aggro Radius' in data:
            obj.setAggroRadius(int(float(data['Aggro Radius'])))

        if 'Start State' in data:
            obj.setStartState(data['Start State'])

        return obj
