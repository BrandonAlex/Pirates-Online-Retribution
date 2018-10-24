from direct.directnotify.DirectNotifyGlobal import directNotify
from pirates.reputation.DistributedReputationAvatarAI import *
from pirates.pirate.AvatarType import AvatarType
from pirates.pirate import AvatarTypes
from pirates.inventory import ItemGlobals

from WeaponBaseAI import WeaponBaseAI
from BattleRandom import BattleRandom
from Teamable import Teamable

import WeaponGlobals

class DistributedBattleAvatarAI(Teamable, DistributedReputationAvatarAI, WeaponBaseAI):
    notify = directNotify.newCategory('DistributedBattleAvatarAI')
    avatarType = AvatarTypes.AnyAvatar
    isNpc = False
    zombie = False

    def __init__(self, air):
        DistributedReputationAvatarAI.__init__(self, air)
        WeaponBaseAI.__init__(self, air)
        Teamable.__init__(self)
        self.level = 0
        self.mojo = 0
        self.maxMojo = 0
        self.currentWeaponId = 0
        self.isWeaponDrawn = 0
        self.currentAmmo = 0
        self.currentCharm = 0
        self.shipId = 0
        self.inInvasion = False
        self.skillEffects = []

        self.enemySkills = {}

    def announceGenerate(self):
        DistributedReputationAvatarAI.announceGenerate(self)
        self.battleRandom = BattleRandom(self.doId)

    def getHp(self):
        return [self.hp, 1]

    def setLevel(self, level):
        self.level = level

    def d_setLevel(self, level):
        self.sendUpdate('setLevel', [level])

    def b_setLevel(self, level):
        self.setLevel(level)
        self.d_setLevel(level)

    def getLevel(self):
        return self.level

    def setHp(self, hp, quietly=0):
        DistributedAvatarAI.setHp(self, hp)

    def d_setHp(self, hp, quietly=0):
        self.sendUpdate('setHp', [hp, quietly])

    def b_setHp(self, hp, quietly=0):
        self.setHp(hp) # This might be modified by DPPAI (groggy)
        self.d_setHp(self.hp, quietly)

    def setMojo(self, mojo):
        self.mojo = mojo

    def d_setMojo(self, mojo):
        self.sendUpdate('setMojo', [mojo])

    def b_setMojo(self, mojo):
        self.setMojo(mojo) # This might be modified by DPPAI (groggy)
        self.d_setMojo(self.mojo)

    def getMojo(self):
        return self.mojo

    def setMaxMojo(self, maxMojo):
        self.maxMojo = maxMojo

    def d_setMaxMojo(self, maxMojo):
        self.sendUpdate('setMaxMojo', [maxMojo])

    def b_setMaxMojo(self, maxMojo):
        self.setMaxMojo(maxMojo)
        self.d_setMaxMojo(maxMojo)

    def getMaxMojo(self):
        return self.maxMojo

    def setAvatarType(self, avatarType):
        self.avatarType = AvatarType.fromTuple(avatarType)

    def getAvatarType(self):
        return self.avatarType.asTuple()

    def isBoss(self):
        return self.avatarType.isA(AvatarTypes.BossType)

    def setCurrentWeapon(self, currentWeapon, isWeaponDrawn):
        self.currentWeaponId = currentWeapon
        self.isWeaponDrawn = isWeaponDrawn

    def d_setCurrentWeapon(self, currentWeapon, isWeaponDrawn):
        self.sendUpdate('setCurrentWeapon', [currentWeapon, isWeaponDrawn])

    def b_setCurrentWeapon(self, currentWeapon, isWeaponDrawn):
        self.setCurrentWeapon(currentWeapon, isWeaponDrawn)
        self.d_setCurrentWeapon(currentWeapon, isWeaponDrawn)

    def getCurrentWeapon(self):
        return [self.currentWeaponId, self.isWeaponDrawn]

    def setCurrentAmmo(self, currentAmmo):
        self.currentAmmo = currentAmmo

    def d_setCurrentAmmo(self, currentAmmo):
        self.sendUpdate('setCurrentAmmo', [currentAmmo])

    def b_setCurrentAmmo(self, currentAmmo):
        self.setCurrentAmmo(currentAmmo)
        self.d_setCurrentAmmo(currentAmmo)

    def getCurrentAmmo(self):
        return self.currentAmmo

    def setCurrentCharm(self, currentCharm):
        self.currentCharm = currentCharm

    def d_setCurrentCharm(self, currentCharm):
        self.sendUpdate('setCurrentCharm', [currentCharm])

    def b_setCurrentCharm(self, currentCharm):
        self.setCurrentCharm(currentCharm)
        self.d_setCurrentCharm(currentCharm)

    def getCurrentCharm(self):
        return self.currentCharm

    def setShipId(self, shipId):
        self.shipId = shipId

    def d_setShipId(self, shipId):
        self.sendUpdate('setShipId', [shipId])

    def b_setShipId(self, shipId):
        self.setShipId(shipId)
        self.d_setShipId(shipId)

    def getShipId(self):
        return self.shipId

    def setInInvasion(self, inInvasion):
        self.inInvasion = inInvasion

    def d_setInInvasion(self, inInvasion):
        self.sendUpdate('setInInvasion', [inInvasion])

    def b_setInInvasion(self, inInvasion):
        self.setInInvasion(inInvasion)
        self.d_setInInvasion(inInvasion)

    def getInInvasion(self):
        return self.inInvasion

    def isInInvasion(self):
        return self.getInInvasion()

    def addSkillEffect(self, effectId, attacker=0):
        # TO DO
        timestamp = 0
        duration = 0
        timeLeft = 0
        recur = 0
        data = [0]

        self.skillEffects.append([effectId, attacker, timestamp, duration, timeLeft, recur, data])
        self.sendUpdate('setSkillEffects', [self.skillEffects])
        # TO DO: expire task

    def removeSkillEffect(self, effectId, attacker=0):
        newEffectList = []
        for buff in self.skillEffects:
            if buff[0] == effectId:
                if (not attacker) or buff[1] == attacker:
                    continue

            newEffectList.append(buff)

        self.skillEffects = newEffectList
        self.sendUpdate('setSkillEffects', [self.skillEffects])
        # TO DO: expire task

    def getSkillEffects(self):
        # Extremely hackful
        if not hasattr(self, 'battleRandom'):
            return self.skillEffects

        buffIds = set()
        for buff in self.skillEffects:
            buffIds.add(buff[0])

        return buffIds

    def getSkillRankBonus(self, skillId):
        upgradeAmt = WeaponGlobals.getAttackUpgrade(skillId)
        realSkillId = WeaponGlobals.getLinkedSkillId(skillId)
        if not realSkillId:
            realSkillId = skillId

        rank = self.getSkillRank(realSkillId)
        if WeaponGlobals.getSkillTrack(skillId) != WeaponGlobals.PASSIVE_SKILL_INDEX:
            rank -= 1

        statBonus = 0
        if rank > 5:
            statBonus = 5 * upgradeAmt
            statBonus += (rank - 5) * (upgradeAmt / 2.0)
        else:
            statBonus = rank * upgradeAmt
        return statBonus


    def getSkillRank(self, skillId):
        if self.isNpc:
            return 0

        skillLvl = 0
        inv = self.getInventory()
        if inv:
            skillLvl = max(0, inv.getStackQuantity(skillId) - 1)
            skillLvl += ItemGlobals.getWeaponBoosts(self.currentWeaponId, skillId)
            skillLvl += ItemGlobals.getWeaponBoosts(self.getCurrentCharm(), skillId)

        return skillLvl

    def sethasGhostPowers(self, powers):
        pass