#!/bin/sh
cd ..

export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
export DYLD_FRAMEWORK_PATH="Frameworks"

echo "Welcome to Pirates Online Retribution!"
read -p "Username: " LOGIN_COOKIE
read -p "Password: " PASSWORD
read -p "GameServer IP: " SERVER_IP

export PIRATES_USERNAME=$LOGIN_COOKIE
export USER_PASS=$PASSWORD
export GAME_SERVER=$SERVER_IP

echo "=============================="
echo "Success!"
echo "Launching Pirates Online Retribution!"
echo "Username: $LOGIN_COOKIE"
echo "Password: $PASSWORD"
echo "Gameserver: $GAME_SERVER"
echo "Welcome to the best POTCO Remake Ever! :)"
echo "=============================="

ppython -m pirates.piratesbase.PiratesStart
