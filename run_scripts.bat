@echo off

echo Running seed generator...
start /wait cmd /c "python seedgenerator.py"
echo Seed generator completed.

echo Running TokenGuard...
start /wait cmd /c "python TokenGuard.py"
echo TokenGuard completed.

echo Running Balance checker...
start /wait cmd /c "python Balance.py"
echo Balance checker completed.

echo All scripts executed.
pause
