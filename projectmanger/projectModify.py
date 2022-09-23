import subprocess
import os

def is_mod_project(folder):
    curPath = os.getcwd()
    os.chdir(folder)
    
    data = subprocess.check_output(['git', 'diff'])
    cmdContent = str(data).split('\\n')
    isModify = False
    for cmd in cmdContent:
        #TODO: +++가 포함되면 업데이트된 정보가 있는것
        check = '+++' in cmd
        if check == True:
            isModify = True
            break
    
    os.chdir(curPath)
    return  isModify

