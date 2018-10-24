@echo off

set /P LOGIN_COOKIE="Username: " || ^
set LOGIN_COOKIE=dev
set TLOPO_GAMESERVER=25.77.104.45
set TLOPO_PLAYCOOKIE=%LOGIN_COOKIE%

rem Read the contents of the PYTHON_PATH file into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

echo ==============================
echo Starting Pirates Online...
echo Python: %PYTHON_PATH%
echo Username: %LOGIN_COOKIE%
echo Gameserver: %TLOPO_GAMESERVER%
echo ==============================

:main
%PYTHON_PATH% -m main
pause

echo Restarting Pirates Online...
goto main

#107.170.142.53