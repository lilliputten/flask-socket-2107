#!/bin/sh
# @desc Initialize python venv
# @changed 2020.10.23, 23:41

if uname | grep -q "CYGWIN"; then
  cmd /C "util-venv-init.cmd"
else
  # Global system requirements...
  pip install setuptools virtualenv
  # Create venv...
  python -m virtualenv -p "C:\Python39\python.exe" .venv3
  # Activate venv
  . ./.venv3/Scripts/activate
  # For windows: call .venv/Scripts/activate
  # Install project dependencies...
  pip install -r requirements-dev.txt
  # User info...
  echo "Use next command to activate venv: '. ./.venv/Scripts/activate'"
fi
