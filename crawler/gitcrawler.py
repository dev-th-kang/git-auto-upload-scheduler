import schedule
from getpass import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from projectmanger import folderManger
import time

PATH = './data/commitdata.json'
def createMsg(commitCount, todayUpdateInfo):
    # result
    if todayUpdateInfo == False: 
        print("Today info is not updated")
        
    elif int(commitCount) > 0 and todayUpdateInfo == True:
        commitData[user_id][nowDate]={"commit":True}
        print(commitData)
        folderManger.writejson(PATH,commitData)

    return todayUpdateInfo



def crawling(user_id,unConditionCrawl):
    nowDate = datetime.today().strftime("%Y-%m-%d")
    yesterDate = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
    commitData = folderManger.readjson(PATH);
    
    # TODO: unConditionCrawl이 False 일 때 :이미 올라가있으면 크롤링을 굳이 안함
    if unConditionCrawl == False and nowDate in commitData[user_id].keys():
        print("commit good!")
        return True

    # TODO: unConditionCrawl이 True일때 :이미 올라가있더라도 크롤링 진행
    url = 'https://github.com/' + user_id
    response = requests.get(url)

    if response.status_code == 200 :
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        commitContents = soup.select("g>rect.ContributionCalendar-day")
        commitCount = 0
        todayUpdateInfo = False
        #commitData = dict()
        for c in commitContents:
            if str(c["data-date"]) == nowDate:
                commitCount = c["data-count"]
                todayUpdateInfo = True
                break
            if str(c["data-date"]) == yesterDate:
                commitCount = c["data-count"]

        return createMsg(commitCount,todayUpdateInfo)

        
    else :
        print(response.status_code)
    