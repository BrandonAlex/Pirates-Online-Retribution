@echo off
title Starting POR...

start start-mongo-server.bat
start start-astron-cluster.bat
start start-uberdog-server.bat
start start-ai-server.bat
start start-game.bat