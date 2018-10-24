#!/bin/sh
cd ..

export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
export DYLD_FRAMEWORK_PATH="Frameworks"

read -p "Username: " LOGIN_COOKIE
read -p "Gameserver: " LOGIN_SERVER

export TLOPO_PLAYCOOKIE=$LOGIN_COOKIE
export TLOPO_GAMESERVER=$LOGIN_SERVER

echo "=============================="
echo "Starting Pirates Online..."
echo "Username: $LOGIN_COOKIE"
echo "Gameserver: $LOGIN_SERVER"
echo "=============================="

ppython -m main
