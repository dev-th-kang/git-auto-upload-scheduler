import schedule
from getpass import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time

def crawling(user_id):
    nowDate = datetime.today().strftime("%Y-%m-%d")
    yesterDate = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
    print(yesterDate)

    url = 'https://github.com/' + user_id
    print(url)
    response = requests.get(url)

    if response.status_code == 200 :
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        commitData = soup.select("g>rect.ContributionCalendar-day")
        commitCount = 0;
        todayUpdateInfo = False
        
        for c in commitData:
            if str(c["data-date"]) == nowDate:
                commitCount = c["data-count"]
                todayUpdateInfo = True
                break
            
            elif str(c["data-date"]) == yesterDate:
                commitCount = c["data-count"]
                break

        if todayUpdateInfo == False: 
            print("Today info is not updated")
            
        elif int(commitCount) > 0 and todayUpdateInfo == True:
            print("commit good!")
            
        else:
            print("nop")
        return todayUpdateInfo
    else :
        print(response.status_code)