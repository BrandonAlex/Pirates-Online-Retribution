#!/bin/sh
cd ..

read -p "Username: " LOGIN_COOKIE
read -p "Gameserver: " LOGIN_SERVER

export TLOPO_PLAYCOOKIE=$LOGIN_COOKIE
export TLOPO_GAMESERVER=$LOGIN_SERVER

echo "=============================="
echo "Starting Pirates Online..."
echo "Username: $LOGIN_COOKIE"
echo "Gameserver: $LOGIN_SERVER"
echo "=============================="

/usr/bin/python2 -m main
