import schedule
from getpass import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
from gitcrawler import crawler
#user_pw = getpass("git_pw : ")

def autoLoad():
    print(crawler.crawling(user_id))
    
# 특정시간 실행

#user_id = input("git_id : ")
user_id = "dev-th-kang"
schedule.every(1).day.at("00:33").do(autoLoad)

while True:
    schedule.run_pending()
    time.sleep(1)
