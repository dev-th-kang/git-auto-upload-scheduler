import subprocess
import os


""" TODO: git diff 를 활용해서 branch의 내용과 다르게 수정이 되어있으면,
    수정된 부분을 올리게 된다."""

def is_mod_project(folder):
    curPath = os.getcwd()
    os.chdir(folder)
    
    data = subprocess.check_output(['git', 'diff'])
    cmdContent = str(data).split('\\n')
    isModify = False
    for cmd in cmdContent:
        check = '+++' in cmd
        if check == True:
            isModify = True
            break
    
    os.chdir(curPath)
    return  isModify

