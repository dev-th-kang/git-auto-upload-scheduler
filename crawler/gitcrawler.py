import schedule
from getpass import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time


def crawling(user_id):
    nowDate = datetime.today().strftime("%Y-%m-%d")
    yesterDate = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")

    url = 'https://github.com/' + user_id
    response = requests.get(url)

    if response.status_code == 200 :
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        commitContents = soup.select("g>rect.ContributionCalendar-day")
        commitCount = 0
        todayUpdateInfo = False
        commitData = dict()
        for c in commitContents:
            if str(c["data-date"]) == nowDate:
                {}
                commitCount = c["data-count"]
                todayUpdateInfo = True
                break
            if str(c["data-date"]) == yesterDate:
                commitCount = c["data-count"]



        # result
        if todayUpdateInfo == False: 
            print("Today info is not updated")
            
        elif int(commitCount) > 0 and todayUpdateInfo == True:
            print("commit good!")
            
        else:
            print("nop")
        return todayUpdateInfo
    else :
        print(response.status_code)