from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.task.Task import Task
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals
from otp.uberdog.RejectCode import RejectCode
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import SocialPage
from pirates.piratesgui import PiratesGuiGlobals
from pirates.uberdog import UberDogGlobals
from pirates.battle.DistributedBattleNPC import DistributedBattleNPC
from pirates.piratesgui.RequestButton import RequestButton

class PVPInviterButton(RequestButton):
    
    def __init__(self, text, command):
        RequestButton.__init__(self, text, command)
        self.initialiseoptions(PVPInviterButton)



class PVPInviter(SocialPage.SocialPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('PVPInviter')
    
    def __init__(self, avId, avName):
        SocialPage.SocialPage.__init__(self, 'PVPInviter')
        self.initialiseoptions(PVPInviter)
        self.setPos(-0.59999999999999998, 0, 0.46999999999999997)
        self.avId = avId
        self.avName = avName
        self.avDisableName = 'disable-%s' % avId
        self.fsm = ClassicFSM.ClassicFSM('PVPInviter', [
            State.State('off', self.enterOff, self.exitOff),
            State.State('begin', self.enterBegin, self.exitBegin),
            State.State('inBattle', self.enterInBattle, self.exitInBattle),
            State.State('notYet', self.enterNotYet, self.exitNotYet),
            State.State('checkAvailability', self.enterCheckAvailability, self.exitCheckAvailability),
            State.State('notAvailable', self.enterNotAvailable, self.exitNotAvailable),
            State.State('notAcceptingChallenges', self.enterNotAcceptingChallenges, self.exitNotAcceptingChallenges),
            State.State('wentAway', self.enterWentAway, self.exitWentAway),
            State.State('alreadyChallenging', self.enterAlreadyChallenging, self.exitAlreadyChallenging),
            State.State('alreadyInvited', self.enterAlreadyInvited, self.exitAlreadyInvited),
            State.State('askingNPC', self.enterAskingNPC, self.exitAskingNPC),
            State.State('endChallenge', self.enterEndChallenge, self.exitEndChallenge),
            State.State('challengeNoMore', self.enterChallengeNoMore, self.exitChallengeNoMore),
            State.State('self', self.enterSelf, self.exitSelf),
            State.State('ignored', self.enterIgnored, self.exitIgnored),
            State.State('asking', self.enterAsking, self.exitAsking),
            State.State('yes', self.enterYes, self.exitYes),
            State.State('no', self.enterNo, self.exitNo),
            State.State('otherInBattle', self.enterOtherInBattle, self.exitOtherInBattle),
            State.State('maybe', self.enterMaybe, self.exitMaybe),
            State.State('down', self.enterDown, self.exitDown),
            State.State('cancel', self.enterCancel, self.exitCancel)], 'off', 'off')
        guiMain = loader.loadModel('models/gui/gui_main')
        self.box = OnscreenImage(parent = self, pos = (0.25, 0, 0.27500000000000002), image = guiMain.find('**/general_frame_e'), scale = 0.25)
        self.title = DirectLabel(parent = self, relief = None, text = PLocalizer.PVPInviterTitle, text_scale = PiratesGuiGlobals.TextScaleExtraLarge, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_font = PiratesGlobals.getPirateOutlineFont(), pos = (0.25, 0, 0.41999999999999998), image = None, image_scale = 0.25)
        self.message = DirectLabel(parent = self, relief = None, text = '', text_scale = PiratesGuiGlobals.TextScaleLarge, text_align = TextNode.ACenter, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, text_wordwrap = 11, pos = (0.25, 0, 0.32500000000000001), textMayChange = 1)
        self.context = None
        self.bOk = PVPInviterButton(text = OTPLocalizer.DialogOK, command = self._PVPInviter__handleOk)
        self.bOk.reparentTo(self)
        self.bOk.setPos(0.20000000000000001, 0, 0.050000000000000003)
        self.bOk.hide()
        self.bCancel = PVPInviterButton(text = OTPLocalizer.DialogCancel, command = self._PVPInviter__handleCancel)
        self.bCancel.reparentTo(self)
        self.bCancel.setPos(0.20000000000000001, 0, 0.050000000000000003)
        self.bCancel.hide()
        self.bStop = PVPInviterButton(text = 'Stop', command = self._PVPInviter__handleStop)
        self.bStop.reparentTo(self)
        self.bStop.setPos(0.20000000000000001, 0, 0.14999999999999999)
        self.bStop.hide()
        self.bYes = PVPInviterButton(text = OTPLocalizer.DialogYes, command = self._PVPInviter__handleYes)
        self.bYes.reparentTo(self)
        self.bYes.setPos(0.10000000000000001, 0, 0.050000000000000003)
        self.bYes.hide()
        self.bNo = PVPInviterButton(text = OTPLocalizer.DialogNo, command = self._PVPInviter__handleNo)
        self.bNo.reparentTo(self)
        self.bNo.setPos(0.29999999999999999, 0, 0.050000000000000003)
        self.bNo.hide()
        self.fsm.enterInitialState()
        self.fsm.request('begin')

    
    def destroy(self):
        if hasattr(self, 'destroyed'):
            return None
        
        self.destroyed = 1
        self.fsm.request('cancel')
        del self.fsm
        SocialPage.SocialPage.destroy(self)

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterBegin(self):
        myId = base.localAvatar.doId
        self.accept(self.avDisableName, self._PVPInviter__handleDisableAvatar)
        if self.avId == myId:
            self.fsm.request('self')
        else:
            self.fsm.request('notYet')

    
    def exitBegin(self):
        self.ignore(self.avDisableName)

    
    def enterSendChallenge(self):
        pass

    
    def exitSendChallenge(self):
        pass

    
    def enterInBattle(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        self['text_pos'] = (0.0, 0.20000000000000001)
        self.bCancel.show()
        self.bCancel.setPos(0.0, 0.0, -0.16)

    
    def exitInBattle(self):
        self.bCancel.hide()

    
    def enterNotYet(self):
        self.accept(self.avDisableName, self._PVPInviter__handleDisableAvatar)
        self.message['text'] = PLocalizer.PVPInviterNotYet % self.avName
        self.bYes.show()
        self.bNo.show()

    
    def exitNotYet(self):
        self.ignore(self.avDisableName)
        self.bYes.hide()
        self.bNo.hide()

    
    def enterCheckAvailability(self):
        self.accept(self.avDisableName, self._PVPInviter__handleDisableAvatar)
        avatar = base.cr.doId2do.get(self.avId)
        if not avatar:
            self.fsm.request('wentAway')
            return None
        
        if isinstance(avatar, DistributedBattleNPC):
            self.fsm.request('askingNPC')
            return None
        
        base.cr.pvpManager.sendRequestChallenge(self.avId)
        self.message['text'] = PLocalizer.PVPInviterCheckAvailability % self.avName
        self.accept(PiratesGlobals.PVPAcceptEvent, self._PVPInviter__challengeAccepted)
        self.accept(PiratesGlobals.PVPRejectEvent, self._PVPInviter__challengeRejected)
        self.bCancel.show()

    
    def _PVPInviter__challengeAccepted(self, avIds):
        if self.avId in avIds:
            self.fsm.request('yes')
        

    
    def exitCheckAvailability(self):
        self.ignore(self.avDisableName)
        self.ignore('challengeConsidering')
        self.ignore('challengeResponse')
        self.ignore(PiratesGlobals.PVPAcceptEvent)
        self.ignore(PiratesGlobals.PVPRejectEvent)
        self.bCancel.hide()

    
    def enterNotAvailable(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        self.context = None
        self.bOk.show()

    
    def exitNotAvailable(self):
        self.bOk.hide()

    
    def enterNotAcceptingChallenges(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        self.context = None
        self.bOk.show()

    
    def exitNotAcceptingChallenges(self):
        self.bOk.hide()

    
    def enterWentAway(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        if self.context != None:
            self.context = None
        
        self.bOk.show()

    
    def exitWentAway(self):
        self.bOk.hide()

    
    def enterAlreadyChallenging(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        self['text_pos'] = (0.0, 0.20000000000000001)
        self.context = None
        self.bStop.show()
        self.bCancel.show()

    
    def exitAlreadyChallenging(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bStop.hide()
        self.bCancel.hide()

    
    def enterAlreadyInvited(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        self['text_pos'] = (0.0, 0.20000000000000001)
        self.context = None
        self.bStop.show()
        self.bCancel.show()

    
    def exitAlreadyInvited(self):
        self.message['text'] = ''
        self['text_pos'] = (0.0, 0.13)
        self.bStop.hide()
        self.bCancel.hide()

    
    def enterAskingNPC(self):
        self.message['text'] = PLocalizer.PVPInviterAskingNPC % self.avName
        taskMgr.doMethodLater(2.0, self.npcReplies, 'npcChallenge')
        self.bCancel.show()

    
    def exitAskingNPC(self):
        taskMgr.remove('npcChallenge')
        self.bCancel.hide()

    
    def npcReplies(self, task):
        self.fsm.request('no')
        return Task.done

    
    def enterEndChallenge(self):
        self.message['text'] = PLocalizer.PVPInviterEndChallenge % self.avName
        self.context = None
        self.bYes.show()
        self.bNo.show()

    
    def exitEndChallenge(self):
        self.bYes.hide()
        self.bNo.hide()

    
    def enterChallengeNoMore(self):
        self.message['text'] = PLocalizer.PVPInviterChallengeNoMore % self.avName
        self.bOk.show()
        if not base.cr.doId2do.has_key(self.avId):
            messenger.send(self.avDisableName)
        

    
    def exitChallengeNoMore(self):
        self.bOk.hide()

    
    def enterSelf(self):
        self.message['text'] = PLocalizer.PVPInviterSelf
        self.context = None
        self.bOk.show()

    
    def exitSelf(self):
        self.bOk.hide()

    
    def enterIgnored(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        self.context = None
        self.bOk.show()

    
    def exitIgnored(self):
        self.bOk.hide()

    
    def enterAsking(self):
        self.accept(self.avDisableName, self._PVPInviter__handleDisableAvatar)
        self.message['text'] = PLocalizer.PVPInviterAsking % self.avName
        self.accept('challengeResponse', self._PVPInviter__challengeResponse)
        self.accept(PiratesGlobals.PVPAcceptEvent, self._PVPInviter__challengeAccepted)
        self.bCancel.show()

    
    def exitAsking(self):
        self.ignore(self.avDisableName)
        self.ignore('challengeResponse')
        self.ignore(PiratesGlobals.PVPAcceptEvent)
        self.bCancel.hide()

    
    def enterYes(self):
        self.message['text'] = PLocalizer.PVPInviterSaidYes % self.avName
        self.context = None
        self.bOk.show()

    
    def exitYes(self):
        self.bOk.hide()

    
    def enterNo(self):
        self.message['text'] = PLocalizer.PVPInviterSaidNo % self.avName
        self.context = None
        self.bOk.show()

    
    def exitNo(self):
        self.bOk.hide()

    
    def enterOtherInBattle(self):
        self.message['text'] = PLocalizer.PVPInviterBusy % self.avName
        self.context = None
        self.bOk.show()

    
    def exitOtherInBattle(self):
        self.bOk.hide()

    
    def enterMaybe(self):
        self.message['text'] = PLocalizer.PVPInviterMaybe % self.avName
        self.context = None
        self.bOk.show()

    
    def exitMaybe(self):
        self.bOk.hide()

    
    def enterDown(self):
        self.message['text'] = PLocalizer.PVPInviterDown
        self.context = None
        self.bOk.show()

    
    def exitDown(self):
        self.bOk.hide()

    
    def enterCancel(self):
        if self.context != None:
            self.context = None
        
        self.fsm.request('off')

    
    def exitCancel(self):
        pass

    
    def _PVPInviter__handleOk(self):
        self.destroy()

    
    def _PVPInviter__handleCancel(self):
        self.destroy()

    
    def _PVPInviter__handleStop(self):
        self.fsm.request('endChallenge')

    
    def _PVPInviter__handleYes(self):
        if self.fsm.getCurrentState().getName() == 'notYet':
            localAvatar.guiMgr.showLookoutPanel()
            localAvatar.guiMgr.lookoutPage.displayLookout(gameType = PiratesGlobals.GAME_TYPE_PVP, gameStyle = PiratesGlobals.GAME_STYLE_TEAM_BATTLE, inviteOptions = [
                PiratesGlobals.LOOKOUT_INVITE_CREW], additionalAvs = [
                self.avId])
            self._PVPInviter__handleOk()
        elif self.fsm.getCurrentState().getName() == 'endChallenge':
            self.fsm.request('challengeNoMore')
        else:
            self.destroy()

    
    def _PVPInviter__handleNo(self):
        self.destroy()

    
    def _PVPInviter__challengeConsidering(self, yesNoAlready, context):
        if yesNoAlready == 1:
            self.context = context
            self.fsm.request('asking')
        elif yesNoAlready == 0:
            self.fsm.request('notAvailable')
        elif yesNoAlready == 2:
            self.fsm.request('alreadyChallenging')
        elif yesNoAlready == 3:
            self.fsm.request('self')
        elif yesNoAlready == 4:
            self.fsm.request('ignored')
        elif yesNoAlready == 6:
            self.fsm.request('notAcceptingChallenges')
        elif yesNoAlready == 10:
            self.fsm.request('no')
        elif yesNoAlready == 13:
            self.fsm.request('otherInBattle')
        else:
            self.notify.warning('Got unexpected response to challengeConsidering: %s' % yesNoAlready)
            self.fsm.request('maybe')

    
    def _PVPInviter__challengeRejected(self, avId, reason):
        if reason == RejectCode.INVITEE_NOT_ONLINE:
            self.fsm.request('notAvailable')
        elif reason == RejectCode.ALREADY_INVITED:
            self.fsm.request('alreadyInvited')
        elif reason == RejectCode.ALREADY_CHALLENGED:
            self.fsm.request('alreadyChallenging')
        elif reason == RejectCode.PVP_IN_BATTLE:
            self.fsm.request('inBattle')
        elif reason == RejectCode.PVP_OTHER_IN_BATTLE:
            self.fsm.request('otherInBattle')
        elif reason == RejectCode.INVITATION_DECLINED:
            self.fsm.request('no')
        else:
            self.notify.warning('challengeRejectInvite: %s unknown reason: %s.' % (avId, reason))

    
    def _PVPInviter__challengeResponse(self, yesNoMaybe, context):
        if self.context != context:
            self.notify.warning('Unexpected change of context from %s to %s.' % (self.context, context))
            self.context = context
        
        if yesNoMaybe == 1:
            self.fsm.request('yes')
        elif yesNoMaybe == 0:
            self.fsm.request('no')
        elif yesNoMaybe == 3:
            self.fsm.request('otherInBattle')
        else:
            self.notify.warning('Got unexpected response to challengeResponse: %s' % yesNoMaybe)
            self.fsm.request('maybe')

    
    def _PVPInviter__handleDisableAvatar(self):
        self.fsm.request('wentAway')


