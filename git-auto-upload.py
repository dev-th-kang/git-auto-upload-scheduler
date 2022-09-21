import schedule
from getpass import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
from crawler import gitcrawler
from fmanagement import fmanagement
from autorun import autorun

def autoLoad():
    if gitcrawler.crawling(user_id) == False:
        #autorun.autorun()
        print("notcrawling")
    
user_id = "dev-th-kang"
timeCycleStandard = "22:42"
schedule.every(1).day.at(timeCycleStandard).do(autoLoad)

while True:
    schedule.run_pending()
    time.sleep(1)
