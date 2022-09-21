import os
import json
from fmanagement import checkfolder
from fmanagement import fmanagement

updateFolderList = list()
def autorun(): 
    json_data = fmanagement.readjson()
    folerKeys = json_data['folder'].keys()
    folerInfo = json_data['folder']


    for k in folerKeys:
        if checkfolder.isfoldermodify(folerInfo[k]) == True:
            updateFolderList.append(folerInfo[k])

    # 수정된 폴더 리스트   
    for updatefolder in updateFolderList: 
        cmd = "autocommit.bat " + updatefolder
        os.system(cmd)
    updateFolderList.clear()

    #cmd = "autocommit.bat " + folderData['1']
    #os.system(cmd)

#autorun()