@echo off

Start start_astron.bat

rem Read the contents of the PYTHON_PATH file into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

start %PYTHON_PATH% -m _start.py uberdog
start %PYTHON_PATH% -m _start.py ai

set LOGIN_COOKIE="Username:test2"
set LOGIN_COOKIE=dev
set TLOPO_GAMESERVER=127.0.0.1
set TLOPO_PLAYCOOKIE=%LOGIN_COOKIE%

%PYTHON_PATH% -m _start.py game
pause
