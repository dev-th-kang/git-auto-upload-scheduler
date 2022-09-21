import schedule
from getpass import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
from gitcrawler import crawler
from fmanagement import fmanagement
from autorun import autorun
#user_pw = getpass("git_pw : ")

def autoLoad():
    if crawler.crawling(user_id) == False:
        autorun.autorun()
    
# 특정시간 실행

# 초기set
#fmanagement.fmanagement()
#autoLoad()

user_id = "dev-th-kang"
#user_id = input("git_id : ")
schedule.every(1).day.at("22:23").do(autoLoad)

while True:
    schedule.run_pending()
    time.sleep(1)
