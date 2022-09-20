
git config --global --add safe.directory %1
git add .
git commit -m "autocommit!"
git push -u origin main
pause