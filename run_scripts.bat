@echo off

:run_scripts
echo Running seed generator...
start /B python seedgenerator.py
echo Seed generator completed.

echo Running TokenGuard...
start /B python TokenGuard.py
echo TokenGuard completed.

echo Running Balance checker...
start /B python Balance.py
set "errorlevel="

REM Check the error level to determine if Balance checker found something
if not %errorlevel% == 0 (
    echo Balance checker completed with a result.
    goto end
)

echo Balance checker did not find anything.

REM Add a delay (optional)
timeout /t 10 /nobreak >nul

REM Go back to run the scripts again
goto run_scripts

:end
echo All scripts executed.

REM Add any cleanup or final actions here
