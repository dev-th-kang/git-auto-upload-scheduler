##project가 있는 폴더가 수정됬는지 여부 판단
##git init 이 되어있는 작업폴더여야함.
import subprocess
 
data = subprocess.check_output(['git', 'diff'])
l = str(data).split('\\n')
isCheck = False
for c in l:
    check = '+++' in c
    if check == True:
        isCheck = True
        break
print(isCheck)