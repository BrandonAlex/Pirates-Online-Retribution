from pirates.quest.QuestConstants import NPCIds
from pirates.quest.QuestPrereq import *
from pirates.quest.DialogProcess import *
from pirates.battle import WeaponGlobals
from pirates.audio import SoundGlobals
from pirates.piratesbase import EmoteGlobals as EG
DialogDict = {
    NPCIds.JACK: {
        'rc.1visitJack.after': {
            0: (NPCDialog(textId = 0), StepChoice(choices = (1, 2))),
            1: (PlayerDialog(textId = 1), NPCDialog(textId = 3), ShowGivenQuest(), ExitDialog()),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 4), ShowGivenQuest(), ExitDialog()) } },
    NPCIds.EDWARD_BRITTLE: {
        'rc.edwardBrittle.intro': {
            0: (Prereq(prereq = [
                HasQuest('rc.3bTalkToEdward')]), NPCDialog(textId = 0, prereq = [
                WithinTimeOfDay(timeFrom = 6, timeTo = 20)]), NPCDialog(textId = 13, prereq = [
                WithinTimeOfDay(timeFrom = 20, timeTo = 6)]), StepChoice(choices = (1, 2, 3))),
            1: (PlayerDialog(textId = 1, prereq = [
                WithinTimeOfDay(timeFrom = 6, timeTo = 20)]), PlayerDialog(textId = 14, prereq = [
                WithinTimeOfDay(timeFrom = 20, timeTo = 6)]), PlayerDrawPistolAndAim(delayCleanup = True, prereq = [
                WithinTimeOfDay(timeFrom = 6, timeTo = 20)]), NPCDialog(textId = 4), StepChoice(choices = (4, 5, 6))),
            2: (PlayerDialog(textId = 2, prereq = [
                WithinTimeOfDay(timeFrom = 6, timeTo = 20)]), PlayerDialog(textId = 15, prereq = [
                WithinTimeOfDay(timeFrom = 20, timeTo = 6)]), NPCDialog(textId = 4), StepChoice(choices = (4, 5, 6))),
            3: (PlayerDialog(textId = 3, prereq = [
                WithinTimeOfDay(timeFrom = 6, timeTo = 20)]), PlayerDialog(textId = 16, prereq = [
                WithinTimeOfDay(timeFrom = 20, timeTo = 6)]), ExitDialog()),
            4: (PlayerDialog(textId = 5), NPCDialog(textId = 8), PlayerHidePistol(), StepChoice(choices = (5, 7))),
            5: (PlayerDialog(textId = 6), NPCDialog(textId = 10), PlayerHidePistol(), StepChoice(choices = (8, 6))),
            6: (PlayerDialog(textId = 7), PlayerHidePistol(), Delay(duration = 0.5), ExitDialog()),
            7: (PlayerDialog(textId = 9), ExitDialog()),
            8: (PlayerDialog(textId = 11), NPCDialog(textId = 12), AdvanceQuest(questId = 'rc.3bTalkToEdward'), AssignQuest(questId = 'rc.ghosts.helpAllGhosts'), NPCDialog(textId = 17, prereq = [
                NotCompleted(questIds = [
                    'RavensCoveTotem'])]), OfferQuest(questId = 'rct.findHiddenPieces', prereq = [
                NotCompleted(questIds = [
                    'RavensCoveTotem'])]), ExitDialog()) },
        'rc.GhostsOfRavensCove.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), ShowGivenQuest(), ExitDialog()) },
        'RavensCoveTotem.before': {
            0: (NPCDialog(textId = 0, prereq = [
                NotCompleted(questIds = [
                    'RavensCoveTotem']),
                DidQuest('rc.3bTalkToEdward')]), OfferQuest(questId = 'rct.findHiddenPieces'), ExitDialog()) },
        'RavensCoveTotem.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), ExitDialog()) } },
    NPCIds.THOMAS_FISHMEISTER: {
        'rc.ghosts.fishmeister.catchFish.intro': {
            0: (NPCDialog(textId = 0, prereq = [
                HasQuest('rc.ghosts.helpAllGhosts'),
                NotCompleted('rc.ghosts.ThomasFishmeister')]), StepChoice(choices = (1, 2))),
            1: (PlayerDialog(textId = 1), NPCDialog(textId = 3), OfferQuest(questId = 'rc.ghosts.fishmeister.catchFish'), ExitDialog()),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 4), OfferQuest(questId = 'rc.ghosts.fishmeister.catchFish'), ExitDialog()) },
        'rc.ghosts.fishmeister.catchFish.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), ExitDialog()) } },
    NPCIds.MADAM_ZIGANA: {
        'rc.ghosts.zigana.brewPotions.intro': {
            0: (NPCDialog(textId = 0, prereq = [
                HasQuest('rc.ghosts.helpAllGhosts'),
                NotCompleted('rc.ghosts.MadamZigana')]), StepChoice(choices = (1, 2, 3))),
            1: (PlayerDialog(textId = 1), OfferQuest(questId = 'rc.ghosts.zigana.brewPotions'), ExitDialog()),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 4), StepChoice(choices = (4, 5))),
            3: (PlayerDialog(textId = 3), NPCDialog(textId = 5), OfferQuest(questId = 'rc.ghosts.zigana.brewPotions'), ExitDialog()),
            4: (PlayerDialog(textId = 6), OfferQuest(questId = 'rc.ghosts.zigana.brewPotions'), ExitDialog()),
            5: (PlayerDialog(textId = 7), ExitDialog()) },
        'rc.ghosts.zigana.brewPotions.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), ExitDialog()) } },
    NPCIds.WIDOW_THREADBARREN: {
        'rc.ghosts.threadbarren.RetrieveSails.intro': {
            0: (NPCDialog(textId = 0, prereq = [
                HasQuest('rc.ghosts.helpAllGhosts'),
                NotCompleted('rc.ghosts.WidowThreadbarren')]), StepChoice(choices = (1, 2, 3))),
            1: (PlayerDialog(textId = 1), NPCDialog(textId = 4), OfferQuest(questId = 'rc.ghosts.threadbarren.RetrieveSails'), ExitDialog()),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 5), OfferQuest(questId = 'rc.ghosts.threadbarren.RetrieveSails'), ExitDialog()),
            3: (PlayerDialog(textId = 3), ExitDialog()) },
        'rc.ghosts.threadbarren.RetrieveSails.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), ExitDialog()) } },
    NPCIds.SENOR_FANTIFICO: {
        'rc.ghosts.fantifico.visitTiaDalma.intro': {
            0: (NPCDialog(textId = 0, prereq = [
                HasQuest('rc.ghosts.helpAllGhosts'),
                NotCompleted('rc.ghosts.SenorFantifico')]), StepChoice(choices = (1, 2, 3))),
            1: (PlayerDialog(textId = 1), NPCDialog(textId = 4), OfferQuest(questId = 'rc.ghosts.fantifico.visitTiaDalma'), ExitDialog()),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 5), OfferQuest(questId = 'rc.ghosts.fantifico.visitTiaDalma'), ExitDialog()),
            3: (PlayerDialog(textId = 3), OfferQuest(questId = 'rc.ghosts.fantifico.visitTiaDalma'), ExitDialog()) },
        'rc.ghosts.fantifico.deliverPotion.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), PlayNPCEmote(emoteId = EG.EMOTE_DRINKPOTION), Delay(duration = 2.0), StepChoice(choices = (1, 2, 3))),
            1: (PlayerDialog(textId = 1), PlayCombatEffectOnNPC(effectId = WeaponGlobals.VFX_CLEANSE), FadeOutGhost(), PlaySfx(sfxId = SoundGlobals.SFX_SKILL_CLEANSE), Delay(duration = 1.0), SwitchVisualModeNPC(mode = 'chickenFantifico', skipHide = True), StepChoice(choices = (4, 5, 6))),
            2: (PlayerDialog(textId = 2), PlayCombatEffectOnNPC(effectId = WeaponGlobals.VFX_CLEANSE), FadeOutGhost(), PlaySfx(sfxId = SoundGlobals.SFX_SKILL_CLEANSE), Delay(duration = 1.0), SwitchVisualModeNPC(mode = 'chickenFantifico', skipHide = True), StepChoice(choices = (4, 5, 6))),
            3: (PlayerDialog(textId = 3), PlayCombatEffectOnNPC(effectId = WeaponGlobals.VFX_CLEANSE), FadeOutGhost(), PlaySfx(sfxId = SoundGlobals.SFX_SKILL_CLEANSE), Delay(duration = 1.0), SwitchVisualModeNPC(mode = 'chickenFantifico', skipHide = True), StepChoice(choices = (4, 5, 6))),
            4: (PlayerDialog(textId = 4), ExitDialog()),
            5: (PlayerDialog(textId = 5), ExitDialog()),
            6: (PlayerDialog(textId = 6), ExitDialog()) } },
    NPCIds.KUDGEL: { },
    NPCIds.EL_PATRON: { },
    NPCIds.BEN_CLUBHEART: {
        'rc.ghosts.clubhearts.disguise.intro': {
            0: (NPCDialog(textId = 0, prereq = [
                HasQuest('rc.ghosts.helpAllGhosts'),
                NotCompleted('rc.ghosts.TheClubhearts')]), StepChoice(choices = (1, 2))),
            1: (PlayerDialog(textId = 1), OfferQuest(questId = 'rc.ghosts.clubhearts.disguise'), ExitDialog()),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 3), OfferQuest(questId = 'rc.ghosts.clubhearts.disguise'), ExitDialog()) },
        'rc.ghosts.clubhearts.undeadPoker.after': {
            0: (ShowRewards(), PlayNPCEmote(emoteId = EG.EMOTE_CELEBRATE, npcId = NPCIds.SANDIE_CLUBHEART), NPCDialog(textId = 0), HideRewards(), ExitDialog()) } },
    NPCIds.SANDIE_CLUBHEART: { },
    NPCIds.DR_BELLROG: {
        'rc.talkToBellrog.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), StepChoice(choices = (1, 2, 3))),
            1: (PlayerDrawPistolAndAim(delayCleanup = True), PlayerDialog(textId = 1), NPCDialog(textId = 4), StepChoice(choices = (4, 5))),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 5), ShowGivenQuest(), ExitDialog()),
            3: (PlayerDialog(textId = 3), NPCDialog(textId = 6), ShowGivenQuest(), ExitDialog()),
            4: (PlayerHidePistol(), PlayerDialog(textId = 7), NPCDialog(textId = 6), ShowGivenQuest(), ExitDialog()),
            5: (PlayerDialog(textId = 8), NPCDialog(textId = 6), ShowGivenQuest(), ExitDialog()) },
        'rc.le.1findJournals.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), NPCDialog(textId = 1), ShowGivenQuest(), ExitDialog()) },
        'rc.le.2LureGhosts.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), NPCDialog(textId = 1), ShowGivenQuest(), ExitDialog()) },
        'rc.le.3defendTraitor.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), NPCDialog(textId = 1), ShowGivenQuest(), ExitDialog()) },
        'rc.le.4DowsingRodParts.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), NPCDialog(textId = 1), ShowGivenQuest(), ExitDialog()) },
        'rc.le.5useDowsingRod.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), NPCDialog(textId = 1), ShowGivenQuest(), ExitDialog()) },
        'rc.le.6getLastIdol.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), PlayerDialog(textId = 1), NPCDialog(textId = 2), ExitDialog(), MakeNPCHostile(npcId = NPCIds.KUDGEL)) },
        'rc.le.7defeatKudgel.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), NPCDialog(textId = 1), ShowGivenQuest(), ExitDialog()) } },
    NPCIds.TIA_DALMA: {
        'rc.ghosts.fantifico.visitTiaDalma.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), StepChoice(choices = (1, 2))),
            1: (PlayerDialog(textId = 1), NPCDialog(textId = 3), ShowGivenQuest(), ExitDialog()),
            2: (PlayerDialog(textId = 2), NPCDialog(textId = 3), ShowGivenQuest(), ExitDialog()) },
        'rc.ghosts.fantifico.PotionIngredients.after': {
            0: (ShowRewards(), NPCDialog(textId = 0), HideRewards(), PlayerDialog(textId = 1), NPCDialog(textId = 2), ExitDialog()) } },
    NPCIds.SKELETON_POKER_BOUNCER: {
        'rc.ghosts.clubhearts.disguise.after': {
            0: (NPCDialog(textId = 0, prereq = [
                HasQuest('rc.ghosts.clubhearts.disguise')]), StepChoice(choices = (1, 2))),
            1: (PlayerDialog(textId = 1), NPCDialog(textId = 3, prereq = [
                IsGender('m'),
                RequiresItemEquipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemEquipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemEquipped(ItemGlobals.F44_DUBLOON_BREECHES)]), AdvanceQuest(questId = 'rc.ghosts.clubhearts.disguise', prereq = [
                IsGender('m'),
                RequiresItemEquipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemEquipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemEquipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 4, prereq = [
                IsGender('f'),
                RequiresItemEquipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemEquipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemEquipped(ItemGlobals.FOREST_KNEE_BOOTS)]), AdvanceQuest(questId = 'rc.ghosts.clubhearts.disguise', prereq = [
                IsGender('f'),
                RequiresItemEquipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemEquipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemEquipped(ItemGlobals.FOREST_KNEE_BOOTS)]), NPCDialog(textId = 5, prereq = [
                IsGender('m'),
                RequiresItemUnequipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemUnequipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemUnequipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 5, prereq = [
                IsGender('f'),
                RequiresItemUnequipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemUnequipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemUnequipped(ItemGlobals.FOREST_KNEE_BOOTS)]), NPCDialog(textId = 6, prereq = [
                IsGender('m'),
                RequiresItemUnequipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemEquipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemEquipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 7, prereq = [
                IsGender('m'),
                RequiresItemUnequipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemUnequipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemEquipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 8, prereq = [
                IsGender('m'),
                RequiresItemUnequipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemEquipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemUnequipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 9, prereq = [
                IsGender('m'),
                RequiresItemEquipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemUnequipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemEquipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 10, prereq = [
                IsGender('m'),
                RequiresItemEquipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemUnequipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemUnequipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 11, prereq = [
                IsGender('m'),
                RequiresItemEquipped(ItemGlobals.STRAW_EXPLORER_HAT),
                RequiresItemEquipped(ItemGlobals.FLAP_LONG_SLEEVE),
                RequiresItemUnequipped(ItemGlobals.F44_DUBLOON_BREECHES)]), NPCDialog(textId = 12, prereq = [
                IsGender('f'),
                RequiresItemUnequipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemEquipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemEquipped(ItemGlobals.FOREST_KNEE_BOOTS)]), NPCDialog(textId = 13, prereq = [
                IsGender('f'),
                RequiresItemUnequipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemUnequipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemEquipped(ItemGlobals.FOREST_KNEE_BOOTS)]), NPCDialog(textId = 14, prereq = [
                IsGender('f'),
                RequiresItemUnequipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemEquipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemUnequipped(ItemGlobals.FOREST_KNEE_BOOTS)]), NPCDialog(textId = 15, prereq = [
                IsGender('f'),
                RequiresItemEquipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemUnequipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemEquipped(ItemGlobals.FOREST_KNEE_BOOTS)]), NPCDialog(textId = 16, prereq = [
                IsGender('f'),
                RequiresItemEquipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemUnequipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemUnequipped(ItemGlobals.FOREST_KNEE_BOOTS)]), NPCDialog(textId = 17, prereq = [
                IsGender('f'),
                RequiresItemEquipped(ItemGlobals.WOODLAND_TOP),
                RequiresItemEquipped(ItemGlobals.CANDYBOX_SKIRT),
                RequiresItemUnequipped(ItemGlobals.FOREST_KNEE_BOOTS)]), ExitDialog()),
            2: (PlayerDialog(textId = 2), ExitDialog()) } } }
