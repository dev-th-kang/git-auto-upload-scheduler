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
    
    os.chdir(curPath)
    return  isModify

#ismodify('D:\Progamming\project\git-auto-upload-scheduler')