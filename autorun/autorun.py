import os
import json
def readjson():
    with open('data/folderinfo.json', 'r') as f:
        json_data = json.load(f)
        
    print("!")
    return json_data


def autorun():
    json_data = readjson()
    folderData = json_data["folder"]
    folderDataKeys = list(json_data["folder"].keys())
    # for k in folderDataKeys:
    #     cmd = "test.bat " + folderData[k]
    #     os.system(cmd)
    cmd = "autocommit.bat " + folderData['1']
    os.system(cmd)

#autorun()