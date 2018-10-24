@echo off

title POR Game

echo Choose your connection method!
echo.
echo #1 - Localhost
echo #2 - Custom
echo.

:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    set POR_GAMESERVER=127.0.0.1
) else if %INPUT%==2 (
    echo.
    set /P POR_GAMESERVER=Gameserver: 
) else (
	goto selection
)

echo.
set /P POR_PLAYCOOKIE=Username: 
echo.

echo ===============================
echo Starting POR...
echo Username: %POR_PLAYCOOKIE%
echo Gameserver: %POR_GAMESERVER%
echo ===============================

cd ../

:main
"C:\Panda3D-1.10.0\python\ppython.exe" -m pirates.piratesbase.PiratesStartDev

pause
goto main