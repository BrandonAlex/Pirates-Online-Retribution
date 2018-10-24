from direct.directnotify import DirectNotifyGlobal
import os

class PiratesLauncher:
    notify = DirectNotifyGlobal.directNotify.newCategory('PiratesLauncher')

    def __init__(self):
        self.setServerVersion('tlopo-' + config.GetString('server-version', 'dev'))

    def getGameServer(self):
        return self.getValue('TLOPO_GAMESERVER', '127.0.0.1')

    def setServerVersion(self, version):
        self.version = version

    def getServerVersion(self):
        return self.version

    def setPandaErrorCode(self, code):
        pass

    def getValue(self, key, default=None):
        return os.environ.get(key, default)

    def setValue(self, key, value):
        os.environ[key] = str(value)

    def isTestServer(self):
        return False
