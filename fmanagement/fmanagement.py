import json

def readjson():
    with open('./data/folderinfo.json', 'r') as f:
        json_data = json.load(f)
    return json_data
    
def add_folderlocation(cnt, json_data):
    while True:
        cnt = cnt+1
        folder = str(input("project folder location INPUT (0:finish): "))
        # 0을 입력받으면 입력 정지
        if folder == "0":
            break
        else:
            json_data["folder"][cnt] = folder
    return json_data

def writejson(json_data):
    with open('./data/folderinfo.json','w', encoding='utf-8') as f:
        json.dump(json_data, f, indent="\t")

def fmanagement():
    json_data = readjson()
    print(json_data)
    cnt =len(json_data["folder"])
    json_data = add_folderlocation(cnt, json_data)
    print(json_data)
    writejson(json_data)