set arg1 = %1
git config --global --add safe.directory %arg1%
git add .
git commit -m "autocommit!"
git push -u origin main
pause