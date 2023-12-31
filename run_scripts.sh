#!/bin/bash

echo Running seed generator...
python seedgenerator.py
echo Seed generator completed.

echo Running TokenGuard...
python TokenGuard.py
echo TokenGuard completed.

echo Running Balance checker...
python Balance.py
echo Balance checker completed.

echo All scripts executed.
