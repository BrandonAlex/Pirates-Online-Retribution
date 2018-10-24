@echo off

rem Default Values
set BASE_CHANNEL=401000000
set MAX_CHANNELS=999999
set STATE_SERVER=4002
set ASTRON_IP=127.0.0.1:6669
set EVENT_LOGGER_IP=127.0.0.1:6668

rem Read the contents of PYTHON_PATH into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

echo ==============================
echo Starting Pirates Online UberDOG server...
echo Python Path: %PYTHON_PATH%
echo Base Channel: %BASE_CHANNEL%
echo Max Channels: %MAX_CHANNELS%
echo State Server: %STATE_SERVER%
echo Astron IP: %ASTRON_IP%
echo Event Logger IP: %EVENT_LOGGER_IP%
echo ==============================

:main
%PYTHON_PATH% -m pirates.uberdog.ServiceStart --base-channel %BASE_CHANNEL% --max-channels %MAX_CHANNELS% --state-server %STATE_SERVER% --astron-ip %ASTRON_IP% --event-logger-ip %EVENT_LOGGER_IP%
pause