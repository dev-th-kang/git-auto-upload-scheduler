import os
import json
from projectmanger import projectModify
from projectmanger import folderManger

updateFolderList = list()
def autorun(): 
    json_data = folderManger.readjson('./data/folderinfo.json')
    folerKeys = json_data['folder'].keys()
    folerInfo = json_data['folder']


    for k in folerKeys:
        if projectModify.is_mod_project(folerInfo[k]) == True:
            updateFolderList.append(folerInfo[k])

    # 수정된 폴더 리스트   
    for updatefolder in updateFolderList: 
        cmd = "autocommit.bat " + updatefolder
        os.system(cmd)
    
    updateFolderList.clear()