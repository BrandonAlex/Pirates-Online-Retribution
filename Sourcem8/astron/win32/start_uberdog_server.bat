@echo off
cd ../..

rem Read the contents of PYTHON_PATH into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

echo ==============================
echo Starting Pirates Online UberDOG server...
echo Python: %PYTHON_PATH%
echo ==============================

:main
%PYTHON_PATH% -m pirates.uberdog.ServiceStart
pause

goto main
