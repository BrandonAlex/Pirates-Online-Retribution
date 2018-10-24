@echo off
cd ..

rem Read the contents of the PYTHON_PATH file into %PYTHON_PATH%:

set /P PYTHON_PATH=<PYTHON_PATH


set TLOPO_PLAYCOOKIE=patcotts
set TLOPO_GAMESERVER=tlopo.servegame.com
python -m main

echo ==============================
echo Starting Pirates Online...
echo Python: %PYTHON_PATH%

echo Username: %LOGIN_COOKIE%

echo Gameserver: %TLOPO_GAMESERVER%
echo ==============================

%PYTHON_PATH% -m main
pause
