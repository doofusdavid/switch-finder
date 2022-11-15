import re
import time
import smtplib
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pushover import init, Client

def stock_check(url, device):
    """Checks url for 'sold out!' substring in buy-now-bar-con"""
    soup = BeautifulSoup(url.content, "html.parser") #Need to use lxml parser
    stock = soup.select('button#product-addtocart-button') #Check the html tags for sold out/coming soon info.
    if stock:
        notify_user(device)

def notify_user(device):
    """Sends push notification to user"""
    init('aigkghzu8edzqp1bikhahpfvrw7ex9')
    client = Client('udmwmhh7k59p92bb6vdq4v7b67k5n2')
    client.send_message("{0} SWITCH IN STOCK".format(device), title="Switch Finder", sound="magic", device=device)

if __name__ == "__main__":

    devices = {'oledWhite': "https://store.nintendo.com/nintendo-switch-oled-model-white-set.html",
    'oledNeonBlue': "https://store.nintendo.com/nintendo-switch-oled-model-neon-blue-neon-red-set.html",
    'liteBlue': "https://store.nintendo.com/nintendo-switch-lite-blue.html" }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
               'Content-Type': 'text/html'}

    url = requests.get("https://store.nintendo.com/nintendo-switch-lite-blue.html", headers=headers)
    soup = BeautifulSoup(url.content, "html.parser") #Need to use lxml parser

    for device in devices:
        url = requests.get(devices[device], headers=headers)
        stock_check(url, device)
        time.sleep(1)


