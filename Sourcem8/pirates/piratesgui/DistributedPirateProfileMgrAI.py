from direct.distributed import DistributedObjectAI


'''
dclass DistributedPirateProfileMgr : DistributedObject {
  requestAvatar(uint32, uint32) airecv clsend;
  setAvatarInfo(HumanDNA, uint32, string, uint8, uint16, uint16, uint16, uint16, uint32, bool, bool, uint32);
  receiveAvatarInfo(HumanDNA, uint32, string, uint8, uint16, uint16, uint16, uint16, uint32, bool, bool);
  setAvatarSkillLevels(uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint32);
  receiveAvatarSkillLevels(uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8);
  setAvatarShipInfo(bool, bool, bool, uint32);
  receiveAvatarShipInfo(bool, bool, bool);
  receiveAvatarOnlineInfo(string, string, uint8, uint8);
  receiveAvatarChatPermissions(uint8);
};
'''

class DistributedPirateProfileMgrAI(DistributedObjectAI.DistributedObjectAI):

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectAI.DistributedObjectAI.announceGenerate(self)

    def disable(self):
        DistributedObjectAI.DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.DistributedObjectAI.disable(self)

    def requestAvatar(self, avId):
        self.sendUpdate('requestAvatar', [
            avId,
            localAvatar.getDoId()])

    def setAvatarInfo(self, AvatarInfo):
        pass

    def d_setAvatarInfo(self, AvatarInfo):
        pass

    def b_setAvatarInfo(self, AvatarInfo):
        pass
    
    def receiveAvatarInfo(self, dna, guildId, guildName, founder, hp, maxHp, voodoo, maxVoodoo, shardId, disableButtons, showGoTo):
        messenger.send('avatarInfoRetrieved', [
            dna,
            guildId,
            guildName,
            founder,
            hp,
            maxHp,
            voodoo,
            maxVoodoo,
            shardId,
            disableButtons,
            showGoTo])

    def setAvatarSkillLevels(self, AvatarSkillLevels):
        pass

    def d_setAvatarSkillLevels(self, AvatarSkillLevels):
        pass

    def b_setAvatarSkillLevels(self, AvatarSkillLevels):
        pass

    def receiveAvatarSkillLevels(self, level, cannon, sailing, cutlass, pistol, doll, dagger, grenade, staff, potions, fishing):
        messenger.send('avatarSkillLevelsRetrieved', [
            level,
            cannon,
            sailing,
            cutlass,
            pistol,
            doll,
            dagger,
            grenade,
            staff,
            potions,
            fishing])


    def setAvatarShipInfo(self, AvatarShipInfo):
        pass

    def d_setAvatarShipInfo(self, setAvatarShipInfo):
        pass

    def b_setAvatarShipInfo(self, setAvatarShipInfo):
        pass

    def receiveAvatarShipInfo(self, guildState, crewState, friendState):
        messenger.send('avatarShipInfoRetrieved', [
            guildState,
            crewState,
            friendState])

    def receiveAvatarOnlineInfo(self, islandName, locationName, siege, profileIcon):
        messenger.send('avatarOnlineInfoRetrieved', [
            islandName,
            locationName,
            siege,
            profileIcon])

    def receiveAvatarChatPermissions(self, chatPermission):
        messenger.send('avatarChatPermissionsRetrieved', [
            chatPermission]) 
