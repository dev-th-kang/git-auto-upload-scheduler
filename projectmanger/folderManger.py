import json

def readjson(path):
    with open(path, 'r') as f:
        json_data = json.load(f)
    return json_data

def writejson(path,json_data):
    with open(path,'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent="\t")

def fmanagement():
    json_data = readjson()
    print(json_data)
    cnt =len(json_data["folder"])
    json_data = add_folderlocation(cnt, json_data)
    print(json_data)
    writejson('./data/folderinfo.json',json_data)
