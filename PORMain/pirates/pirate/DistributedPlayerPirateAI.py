from panda3d.core import Datagram, Point3
from otp.ai.MagicWordGlobal import *
from otp.avatar.DistributedPlayerAI import DistributedPlayerAI
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from pirates.uberdog.PirateInventoryAI import PirateInventoryAI
from pirates.uberdog.UberDogGlobals import *
from pirates.inventory import ItemConstants, ItemGlobals
from pirates.reputation import RepChart
from pirates.battle import WeaponGlobals
from pirates.battle.DistributedBattleAvatarAI import *
from pirates.inventory import ItemGlobals
import random
import math

class DummyInventory(PirateInventoryAI):
    doId = 0

    def __init__(self, air):
        air.dclassesByName['DummyInventory'] = air.dclassesByName['PirateInventoryAI']
        PirateInventoryAI.__init__(self, air)

    def sendUpdate(self, *args):
        return

    def sendUpdateToChannel(self, *args):
        return

class DistributedPlayerPirateAI(DistributedBattleAvatarAI, DistributedPlayerAI):
    avatarType = AvatarTypes.Player

    def __init__(self, air):
        DistributedBattleAvatarAI.__init__(self, air)
        DistributedPlayerAI.__init__(self, air)

        self.inventory = DummyInventory(air)
        self.levelBuff = {}
        self.penaltyStartTime = 0
        self.gameState = ''

        self.returnLocation = ''
        self.jailCell = None
        self.underArrest = 0
        self.inventoryId = 0
        self.founder = False
        self.allegiance = 0
        self.gmNametag = ('', '')
        self.defaultShard = 0

    def announceGenerate(self):
        DistributedBattleAvatarAI.announceGenerate(self)
        DistributedPlayerAI.announceGenerate(self)

        if config.GetBool('want-auto-founder', False) and not self.getFounder():
            self.b_setFounder(True)
        
        if self.defaultShard != self.air.districtId:
            self.b_setDefaultShard(self.air.districtId)
        
        taskMgr.doMethodLater(10, self.__healthTask, self.taskName('healthTask'))

    def getInventory(self):
        return self.inventory

    def gotInventory(self):
        self.repChanged()
    
    def b_setInventoryId(self, inventoryId):
        self.setInventoryId(inventoryId)
        self.d_setInventoryId(inventoryId)
    
    def d_setInventoryId(self, inventoryId):
        self.sendUpdate('setInventoryId', [inventoryId])
    
    def setInventoryId(self, inventoryId):
        self.inventoryId = inventoryId
    
    def getInventoryId(self):
        return self.inventoryId
    
    def b_setFounder(self, founder):
        self.setFounder(founder)
        self.d_setFounder(founder)
    
    def d_setFounder(self, founder):
        self.sendUpdate('setFounder', [founder])
    
    def setFounder(self, founder):
        self.founder = founder
    
    def getFounder(self):
        return self.founder
    
    def b_setAllegiance(self, allegiance):
        self.setAllegiance(allegiance)
        self.d_setAllegiance(allegiance)
    
    def d_setAllegiance(self, allegiance):
        self.sendUpdate('setAllegiance', [allegiance])
    
    def setAllegiance(self, allegiance):
        self.allegiance = allegiance
    
    def getAllegiance(self):
        return self.allegiance
    
    def b_setGMNametag(self, color, string):
        self.setGMNametag(color, string)
        self.d_setGMNametag(color, string)
    
    def d_setGMNametag(self, color, string):
        self.sendUpdate('setGMNametag', [color, string])
    
    def setGMNametag(self, color, string):
        self.gmNametag = (color, string)
    
    def getGMNametag(self):
        return self.gmNametag
    
    def b_setDefaultShard(self, defaultShard):
        self.d_setDefaultShard(defaultShard)
        self.setDefaultShard(defaultShard)

    def d_setDefaultShard(self, defaultShard):
        self.sendUpdate('setDefaultShard', [defaultShard])

    def setDefaultShard(self, defaultShard):
        self.defaultShard = defaultShard

    def getDefaultShard(self):
        return self.defaultShard
    
    def repChanged(self):
        newLevel = self.calcLevel()
        levelChanged = newLevel != self.level
        if levelChanged:
            self.b_setLevel(self.calcLevel())

        # TO DO: Endurance bonus
        maxHp = 250
        mana = 50

        for i in xrange(InventoryType.begin_Accumulator, InventoryType.end_Accumulator):
            newLevel = self.calcLevel(i)
            oldLevel = self.levelBuff.get(i, 0)
            if oldLevel and oldLevel != newLevel:
                self.sendUpdate('levelUpMsg', [i, newLevel, 0])
                earnedUnspent, earnedSkill = RepChart.getLevelUpSkills(i, newLevel)
                for eu in earnedUnspent:
                    self.inventory.addStackItem(eu)

                for es in earnedSkill:
                    self.inventory.addStackItem(es)

            self.levelBuff[i] = newLevel
            maxHp += RepChart.getHpGain(i) * (newLevel - 1)
            mana += RepChart.getManaGain(i) * (newLevel - 1)

            if not oldLevel:
                # Ensure they have level 0 and 1 skills
                for es in RepChart.getLevelUpSkills(i, 0)[1] + RepChart.getLevelUpSkills(i, 1)[1]:
                    if not self.inventory.getStackQuantity(es):
                        self.inventory.addStackItem(es)

        self.b_setMaxHp(maxHp)
        self.b_setMaxMojo(mana)

        if levelChanged:
            self.fillHpMeter()

    def addDeathPenalty(self, force=False):
        duration = 5

        if (10 < self.level < 50) or force:
            self.inventory.setStackQuantity(InventoryType.Vitae_Level, 12)
            self.inventory.setStackQuantity(InventoryType.Vitae_Cost, duration)
            self.inventory.setStackQuantity(InventoryType.Vitae_Left, duration)

            self.penaltyStartTime = globalClock.getRealTime()

        self.fillHpMeter()

    def removeDeathPenalty(self):
        self.penaltyStartTime = 0
        self.inventory.setStackQuantity(InventoryType.Vitae_Level, 0)
        self.inventory.setStackQuantity(InventoryType.Vitae_Cost, 0)
        self.inventory.setStackQuantity(InventoryType.Vitae_Left, 0)

    def hasDeathPenalty(self):
        return self.inventory.getStackQuantity(InventoryType.Vitae_Level)

    def calcHpAndMojoLimit(self, hp=None, mojo=None, fill=False):
        mult = .75 if self.hasDeathPenalty() else 1
        hpLimit = self.maxHp * mult
        mojoLimit = self.maxMojo * mult

        if hp is None:
            hp = self.hp

        if mojo is None:
            mojo = self.mojo

        hp = min(hp, hpLimit)
        mojo = min(mojo, mojoLimit)

        if fill:
            hp = hpLimit
            mojo = mojoLimit

        return (hp, mojo)

    def fillHpMeter(self):
        hp, mojo = self.calcHpAndMojoLimit(fill=True)
        self.b_setHp(hp, 1)
        self.b_setMojo(mojo)

    def setHp(self, hp, *args):
        hp, _ = self.calcHpAndMojoLimit(hp=hp)
        DistributedBattleAvatarAI.setHp(self, hp, *args)

    def setMojo(self, mojo):
        _, mojo = self.calcHpAndMojoLimit(mojo=mojo)
        DistributedBattleAvatarAI.setMojo(self, mojo)

    def __healthTask(self, task):
        if self.gameState in ('Battle', 'Injured', 'Death'):
            return task.again

        if self.hasDeathPenalty():
            duration = self.inventory.getStackQuantity(InventoryType.Vitae_Cost) * 60
            elapsed = globalClock.getRealTime() - self.penaltyStartTime
            left = math.ceil(int(duration - elapsed) / 60)

            if left <= 0:
                self.removeDeathPenalty()

            elif left != self.inventory.getStackQuantity(InventoryType.Vitae_Left):
                self.inventory.setStackQuantity(InventoryType.Vitae_Left, left)

        else:
            mult = random.randint(6, 13) / 2.0 + .5
            tp = int(self.level * mult)
            self.toonUp(tp)

            # Toon up mojo
            mojo = self.mojo + tp
            self.b_setMojo(mojo)

        return task.again

    def delete(self):
        self.inventory = DummyInventory(self.air)
        taskMgr.remove(self.taskName('healthTask'))

        DistributedBattleAvatarAI.delete(self)
        DistributedPlayerAI.delete(self)

    def calcLevel(self, rep=InventoryType.OverallRep):
        return self.inventory.getCategoryLevel(rep)

    def requestCurrentWeapon(self, currentWeapon, isWeaponDrawn):
        weapons = (x[1] for x in self.inventory.getWeapons().values())
        reason = ItemConstants.REASON_NONE
        msg = ''

        if currentWeapon not in weapons:
            msg = 'tried to use weapon they don\'t own!'
            reason = ItemConstants.REASON_INVENTORY

        else:
            canUse, reason = self.canUseItem((InventoryType.ItemTypeWeapon, currentWeapon))
            if not canUse:
                msg = 'tried to use weapon they cannot!'

        if reason != ItemConstants.REASON_NONE:
            msg += ' weapons = %r, requested = %d, reason = %d' % (weapons, currentWeapon, reason)
            self.notify.warning(msg)
            self.air.writeServerEvent('suspicious', self.doId, issue=msg)
            return

        self.b_setCurrentWeapon(currentWeapon, isWeaponDrawn)

    def canUseItem(self, itemTuple):
        canUse = 1
        reason = ItemConstants.REASON_NONE
        itemCat, itemId = itemTuple

        if itemCat == InventoryType.ItemTypeClothing:
            pass

            ''' TO DO
            gender = self.style.getGender()
            if gender == 'm' and ItemGlobals.getMaleModelId(itemId) == -1:
                canUse = 0
                reason = ItemConstants.REASON_GENDER

            elif gender == 'f' and ItemGlobals.getFemaleModelId(itemId) == -1:
                canUse = 0
                reason = ItemConstants.REASON_GENDER
            '''

        elif itemCat in (InventoryType.ItemTypeWeapon, InventoryType.ItemTypeCharm):
            reqs = self.inventory.getItemRequirements(itemId)
            if reqs == None or filter(lambda x: reqs[x][1] == False, reqs):
                return 0, ItemConstants.REASON_LEVEL

        return (canUse, reason)

    def requestTargetedSkill(self, skillId, ammoSkillId, clientResult, targetId, areaIdList,
                             timestamp, pos, charge):
        pos = Point3(pos)
        self.attemptUseTargetedSkill(skillId, ammoSkillId, clientResult, targetId, areaIdList,
                                     timestamp, pos, charge)

    def spendSkillPoint(self, skillId):
        if 0 < self.inventory.getStackQuantity(skillId) < 5:
            up = self.getUnspent(WeaponGlobals.getRepId(skillId))
            if self.inventory.getStackQuantity(up):
                self.inventory.addStackItem(skillId)
                self.inventory.addStackItem(up, -1)
                self.sendUpdate('spentSkillPoint', [skillId])

    def getUnspent(self, rep):
        if rep == InventoryType.CutlassRep:
            return InventoryType.UnspentCutlass
        elif rep == InventoryType.DaggerRep:
            return InventoryType.UnspentDagger
        elif rep == InventoryType.PistolRep:
            return InventoryType.UnspentPistol
        elif rep == InventoryType.GrenadeRep:
            return InventoryType.UnspentGrenade
        elif rep == InventoryType.DollRep:
            return InventoryType.UnspentDoll
        elif rep == InventoryType.WandRep:
            return InventoryType.UnspentWand
        elif rep == InventoryType.SailingRep:
            return InventoryType.UnspentSailing
        else:
            return InventoryType.UnspentCannon

    def setGameState(self, state, *args):
        self.gameState = state

        if state == 'ThrownInJail':
            world = self.getWorld()
            if world and self.jailCell:
                x, y, z = self.jailCell.getPos()
                h = self.jailCell.getH()
                world.sendUpdateToAvatarId(self.doId, 'setSpawnInfo', [x, y, z, h, 0, []])

    def requestReturnLocation(self, doId):
        obj = self.air.doId2do.get(doId)
        if hasattr(obj, 'getUniqueId'):
            returnLocation = obj.getUniqueId()
            self.b_setReturnLocation(returnLocation)

    def setReturnLocation(self, location):
        self.returnLocation = location

    def d_setReturnLocation(self, location):
        self.sendUpdate('setReturnLocation', [location])

    def b_setReturnLocation(self, location):
        self.setReturnLocation(location)
        self.d_setReturnLocation(location)

    def getReturnLocation(self):
        return self.returnLocation

    def requestGotoJailWhileInjured(self):
        messenger.send('sendAvToJail', [self])

    def setUnderArrest(self, flag):
        self.underArrest = flag

    def d_setUnderArrest(self, flag):
        self.sendUpdate('setUnderArrest', [flag])

    def b_setUnderArrest(self, flag):
        self.setUnderArrest(flag)
        self.d_setUnderArrest(flag)

    def getUnderArrest(self):
        return self.underArrest

    def setStatus(self, todo0):
        pass

    def enterAreaSphere(self, todo0, todo1):
        pass

    def requestRegionUpdate(self, todo0):
        pass

    def leaveAreaSphere(self, todo0, todo1):
        pass

    def requestInteraction(self, avId, interactType, instant):
        pass

    def submitErrorLog(self, errorString):
        pass

    def setCrewIconIndicator(self, iconId):
        pass

    def requestBadgeIcon(self, titleId, rank):
        pass

    def requestShipBadgeIcon(self, titleId, rank):
        pass

    def setAFK(self, isAFK):
        pass

    def setInInvasion(self, inInvasion):
        pass

    def setActiveShipId(self, shipId):
        pass

    def requestExit(self):
        pass

    def setAuraActivated(self, todo0):
        pass

    def requestKill(self, variable):
        pass

@magicWord(CATEGORY_GAME_DEVELOPER)
def suicide(reason = "kindergarten is elsewhere."):
    """ Kick yourself from the game server. """
    av = spellbook.getInvoker()
    dg = PyDatagram()
    dg.addServerHeader(av.GetPuppetConnectionChannel(av.doId), simbase.air.ourChannel, CLIENTAGENT_EJECT)
    dg.addString(reason)
    dg.addUint16(155)
    simbase.air.send(dg)
    return "Kicked %s from the game." % av

@magicWord(CATEGORY_ADMINISTRATION)
def system(text):
    """Send a whisper to the whole district (system), un-prefixed."""
    air = spellbook.getInvoker().air
    air.systemMsgAll(text)
    return "Sent system message '%s' to all pirates in the district." % text

@magicWord(CATEGORY_ADMINISTRATION)
def sysadmin(text):
    """Send a whisper to the whole district, prefixed with 'ADMIN:'."""
    air = spellbook.getInvoker().air
    text = 'ADMIN: ' + text # Prefix text with "ADMIN".
    air.systemMsgAll(text)
    return "Sent system message '%s' to all pirates in the district." % text

@magicWord(CATEGORY_ADMINISTRATION)
def sysname(text):
    """Send a whisper to the whole district, prefixed with 'ADMIN Name:'."""
    air = spellbook.getInvoker().air
    text = 'ADMIN ' + spellbook.getInvoker().getName() + ': ' + text # Prepend text with "ADMIN ", then the Invoker's pirate name.
    air.systemMsgAll(text)
    return "Sent system message '%s' to all pirates in the district." % text

@magicWord(CATEGORY_ADMINISTRATION)
def update(reason="for an update"):
    """Send a whisper to the whole gameserver, prefixed with 'ADMIN Name:'."""
    air = spellbook.getInvoker().air
    text = "ADMIN: Ahoy, maties! Pirates Online Retribution will be closing momentarily " + reason + "." # Maintenance text
    air.systemMsgAll(text)
    return "Sent maintenance warning message to all pirates in the gameserver!"

@magicWord(CATEGORY_STAFF, types=[int])
def hp(value=-1):
    av = spellbook.getTarget()
    if value < 0:
        value = av.getMaxHp()

    value = min(value, av.getMaxHp())
    av.b_setHp(value)

@magicWord(CATEGORY_STAFF, types=[int])
def mojo(value=-1):
    av = spellbook.getTarget()
    if value < 0:
        value = av.getMaxMojo()

    value = min(value, av.getMaxMojo())
    av.b_setMojo(value)

@magicWord(CATEGORY_GAME_MASTER)
def groggy():
    av = spellbook.getTarget()
    av.addDeathPenalty(True)

@magicWord(CATEGORY_GAME_MASTER)
def rmgroggy():
    av = spellbook.getTarget()
    av.removeDeathPenalty()
    av.fillHpMeter()

@magicWord(CATEGORY_ADMINISTRATION, types=[int])
def rep(amount):
    av = spellbook.getInvoker()
    repId = ItemGlobals.getItemRepId(av.currentWeaponId)
    if not repId:
        return 'Pick the weapon you want to add reputation to!'

    av.inventory.addReputation(repId, amount)

@magicWord(CATEGORY_GAME_MASTER)
def founder():
    av = spellbook.getTarget()
    av.b_setFounder(not av.getFounder())
    
    if av.getFounder():
        return 'Enabled founder status!'
    else:
        return 'Disabled founder status!'

@magicWord(CATEGORY_GAME_MASTER, types=[str])
def allegiance(side=None):
    allegiances = ['pirate', 'spanish', 'french']
    side = side.lower()
    
    if side not in allegiances:
        return 'Your side can only be pirate, spanish or french!'
    
    av = spellbook.getTarget()
    av.b_setAllegiance(allegiances.index(side))
    return 'Your allegiance has been set!'

@magicWord(CATEGORY_GAME_MASTER, types=[str, str])
def gm(color=None, tag=None):
    av = spellbook.getTarget()
    
    if not color:
        av.b_setGMNametag('', '')
        return 'Cleared GM nametag!'
    elif color not in ('gold', 'red', 'green', 'blue'):
        return 'Color must be gold, red, green or blue!'
    elif not tag:
        return 'You must specify a tag!'
    else:
        av.b_setGMNametag(color, tag)
        return 'GM nametag set!'