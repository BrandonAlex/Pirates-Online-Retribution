import argparse
from panda3d.core import ConfigVariableString
from panda3d.core import loadPrcFileData
from panda3d.core import loadPrcFile

CmdArgsParse = argparse.ArgumentParser()
CmdArgsParse.add_argument('--base-channel', help="The base channel that the server will use.")
CmdArgsParse.add_argument('--max-channels', help="The number of channels the server is able to use.")
CmdArgsParse.add_argument('--state-server', help="The control channel of this AI's designated State Server.")
CmdArgsParse.add_argument('--astron-ip', help="The IP address of the Astron Message Director to connect to.")
CmdArgsParse.add_argument('--event-logger-ip', help="The IP address of the Astron event logger.")
CmdArgsParse.add_argument('--district-name', help="The name of the district.")
CmdArgsParse.add_argument('config', nargs='*', default=['config/general.prc'], help="PRC file(s) to load.")

Args = CmdArgsParse.parse_args()

if Args.config:
	loadPrcFile(Args.config[0])

localconfig = ''
if Args.base_channel:
	localconfig += 'air-base-channel %s\n' % Args.base_channel
if Args.max_channels:
	localconfig += 'air-channel-allocation %s\n' % Args.max_channels
if Args.state_server:
	localconfig += 'air-stateserver %s\n' % Args.state_server
if Args.district_name:
	localconfig += 'district-name %s\n' % Args.district_name
if Args.astron_ip:
	localconfig += 'air-connect %s\n' % Args.astron_ip
if Args.event_logger_ip:
	localconfig += 'eventlog-host %s\n' % Args.event_logger_ip
loadPrcFileData('Command-line', localconfig)

class game:
    name = 'pirates'
    process = 'server'
__builtins__.game = game

from otp.ai.AIBaseGlobal import *

from pirates.ai.PiratesAIRepository import PiratesAIRepository
simbase.air = PiratesAIRepository(config.GetInt('air-base-channel', 401000000),
                                   config.GetInt('air-stateserver', 4002),
                                   config.GetString('district-name', 'Uncharted Waters'))
host = config.GetString('air-connect', '127.0.0.1')
port = 6669
if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)
simbase.air.connect(host, port)

try:
    run()
except SystemExit:
    raise
except Exception:
    info = PythonUtil.describeException()
    simbase.air.writeServerEvent('ai-exception', simbase.air.getAvatarIdFromSender(), simbase.air.getAccountIdFromSender(), info)
    raise