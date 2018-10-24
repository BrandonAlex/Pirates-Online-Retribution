@echo off

title POR Game
set POR_GAMESERVER=104.251.215.54

set /P POR_PLAYCOOKIE=Username: 
echo.

echo ===============================
echo Starting POR...
echo Username: %POR_PLAYCOOKIE%
echo ===============================

:main
"%~dp0\engine\python\ppython" -m pirates.piratesbase.PiratesStart
pause
goto main