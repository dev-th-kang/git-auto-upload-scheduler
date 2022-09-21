##project가 있는 폴더가 수정됬는지 여부 판단
##git init 이 되어있는 작업폴더여야함.
import subprocess
import os
def isfoldermodify(folder):
    curPath = os.getcwd()
    os.chdir(folder)
    data = subprocess.check_output(['git', 'diff'])
    cmdInfo = str(data).split('\\n')
    isModify = False
    for cmd in cmdInfo:
        check = '+++' in cmd
        if check == True:
            isModify = True
            break
    print(isModify)
    os.chdir(curPath)
    return  isModify

#ismodify('D:\Progamming\project\git-auto-upload-scheduler')