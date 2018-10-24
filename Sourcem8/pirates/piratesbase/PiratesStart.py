import PiratesLogger
import os
print "TLOPO_GAMESERVER = %s" % os.environ.get('TLOPO_GAMESERVER', 'None')
print "TLOPO_PLAYCOOKIE = %s" % os.environ.get('TLOPO_PLAYCOOKIE', 'None')
from panda3d.core import *
if __debug__:
    loadPrcFile('config/general.prc')
    loadPrcFile('config/dev.prc')

    if os.path.isfile('config/personal.prc'):
        loadPrcFile('config/personal.prc')

    if os.path.isfile('config/local.prc'):
        loadPrcFile('config/local.prc')

# Right now Windows computers cannot handle the power of nice quality icons
# Macs can. Suck my icon you PC scum. -mfwass
import sys
if sys.platform == 'darwin':
    quality = 500
else:
    quality = 256
loadPrcFileData('', 'icon-filename resources/phase_3/etc/icon%s.ico' % quality)

import PiratesPreloader
print 'PiratesStart: Starting the game.'
import __builtin__

class game:
    name = 'pirates'
    process = 'client'

__builtin__.game = game()
import __builtin__

import CMotionTrail
__builtin__.CMotionTrail = CMotionTrail.CMotionTrail

from pirates.launcher.PiratesLauncher import PiratesLauncher
launcher = PiratesLauncher()
__builtin__.launcher = launcher

from direct.gui import DirectGuiGlobals
import PiratesGlobals
DirectGuiGlobals.setDefaultFontFunc(PiratesGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
import PiratesBase
PiratesBase.PiratesBase()
from direct.showbase.ShowBaseGlobal import *
if base.config.GetBool('want-preloader', 0):
    base.preloader = PiratesPreloader.PiratesPreloader()

if base.win == None:
    print 'Unable to open window; aborting.'
    sys.exit()

launcher.setPandaErrorCode(0)
base.sfxPlayer.setCutoffDistance(500.0)

from pirates.piratesgui.PDialog import PDialog
PDialog(text='Pre-initialise PDialog').hide()

from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx
rolloverSound = loadSfx(SoundGlobals.SFX_GUI_ROLLOVER_01)
rolloverSound.setVolume(0.5)
DirectGuiGlobals.setDefaultRolloverSound(rolloverSound)
clickSound = loadSfx(SoundGlobals.SFX_GUI_CLICK_01)
DirectGuiGlobals.setDefaultClickSound(clickSound)
clearColor = Vec4(0.0, 0.0, 0.0, 1.0)
base.win.setClearColor(clearColor)
from pirates.shader.Hdr import *
hdr = Hdr()
from pirates.seapatch.Reflection import Reflection
Reflection.initialize(render)
serverVersion = base.config.GetString('server-version', 'no_version_set')
print 'serverVersion: ', serverVersion
from pirates.distributed import PiratesClientRepository
cr = PiratesClientRepository.PiratesClientRepository(serverVersion, launcher)
base.initNametagGlobals()
base.startShow(cr)
if base.config.GetBool('want-portal-cull', 0):
    base.cam.node().setCullCenter(base.camera)
    base.graphicsEngine.setPortalCull(1)

def _doExit(*args):
    print ':TaskManager: TaskManager.destroy()'
    os._exit(1)

taskMgr.destroy = _doExit

if base.options:
    base.options.options_to_config()
    base.options.setRuntimeOptions()
    try:
        base.run()
    finally:
        os._exit(0)
