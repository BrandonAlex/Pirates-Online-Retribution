from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
REPORT_PLAYER = 'REPORT_PLAYER'
ReportFoulLanguage = 'MODERATION_FOUL_LANGUAGE'
ReportPersonalInfo = 'MODERATION_PERSONAL_INFO'
ReportRudeBehavior = 'MODERATION_RUDE_BEHAVIOR'
ReportBadName = 'MODERATION_BAD_NAME'
ReportHacking = 'MODERATION_HACKING'

class CentralLogger(DistributedObjectGlobal):
    PlayersReportedThisSession = {}

    def hasReportedPlayer(self, targetAvId):
        return targetAvId in self.PlayersReportedThisSession

    def reportPlayer(self, category, targetAvId, description = 'None'):
        if self.hasReportedPlayer(targetAvId):
            return False
        self.PlayersReportedThisSession[targetAvId] = 1
        self.sendUpdate('sendMessage', [category,
         REPORT_PLAYER,
         targetAvId])
        return True

    def writeClientEvent(self, eventString):
        self.sendUpdate('sendMessage', ['ClientEvent',
         eventString,
         0])
