#!/bin/sh
cd ..

read -p "Username: " LOGIN_COOKIE

export PIRATES_USERNAME=$LOGIN_COOKIE
export GAME_SERVER=127.0.0.1

echo "==============================="
echo "Starting Pirates Online..."
echo "Username: $LOGIN_COOKIE"
echo "Gameserver: $GAME_SERVER"
echo "==============================="

/usr/bin/python2 -m pirates.piratesbase.PiratesStart