@echo off
title POR OTP
cd "../astron"

:main
astrond --loglevel info config/cluster.yml
goto main
