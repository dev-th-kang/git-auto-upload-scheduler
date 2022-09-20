@echo off
cd %1
git config --global --add safe.directory %1
git add .
git commit -m "autocommit test!"
git push -u origin main