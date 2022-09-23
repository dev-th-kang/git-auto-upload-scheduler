@echo off
cd %1
git config --global --add safe.directory %1
git add .
git commit -m "파일 정리 및 이후 세부사항 정리"
git push -u origin main