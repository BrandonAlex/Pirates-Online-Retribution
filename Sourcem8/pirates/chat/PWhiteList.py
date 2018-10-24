import os
import datetime
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import AppRunnerGlobal
from otp.chat.WhiteList import WhiteList
from direct.directnotify import DirectNotifyGlobal

class PWhiteList(WhiteList):
    RedownloadTaskName = 'RedownloadWhitelistTask'
    WhitelistBaseDir = config.GetString('whitelist-base-dir', '')
    WhitelistStageDir = config.GetString('whitelist-stage-dir', 'whitelist')
    WhitelistOverHttp = config.GetBool('whitelist-over-http', False)
    WhitelistFileName = config.GetString('whitelist-filename', 'pwhitelist.txt')

    def __init__(self):
        self.notify = DirectNotifyGlobal.directNotify.newCategory('PWhiteList')
        vfs = VirtualFileSystem.getGlobalPtr()
        filename = Filename('pwhitelist.txt')
        searchPath = DSearchPath()
        searchPath.appendDirectory(Filename('/phase_4/etc'))
        if __debug__:
            searchPath.appendDirectory(Filename('resources/phase_4/etc'))
        found = vfs.resolveFilename(filename, searchPath)
        if not found:
            self.notify.info("Couldn't find whitelist data file!")
        data = vfs.readFile(filename, 1)
        lines = data.split('\n')
        WhiteList.__init__(self, lines)
        if self.WhitelistOverHttp:
            self.redownloadWhitelist()

    def unload(self):
        self.removeDownloadingTextTask()
