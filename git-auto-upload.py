import schedule
from getpass import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import configparser
from crawler import gitCrawler
from autorun import autoRun

#TODO: read config.ini 
config = configparser.ConfigParser()
config.readfp(open('config.ini'))

def autoLoad():
    if gitCrawler.crawling(config["GIT_INFO"]["userName"]) == False:
        autoRun.autorun()
        print("notcrawling")

schedule.every(1).day.at(config["AUTORUN_SETTING"]["timeCycle"]).do(autoLoad)

while True:
    schedule.run_pending()
    time.sleep(1)
