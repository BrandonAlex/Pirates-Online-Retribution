@echo off

rem Read the contents of the PYTHON_PATH file into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH


set /P LOGIN_COOKIE="Username: " || ^
set LOGIN_COOKIE=dev
set TLOPO_GAMESERVER=104.251.215.54
set TLOPO_PLAYCOOKIE=%LOGIN_COOKIE%

%PYTHON_PATH% -m _start.py game -wx
pause
