from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import string
from selenium.webdriver.common.keys import Keys
import time
import names
import requests
import json
import math
import base64
import hashlib
import datetime
from json import dumps
import urllib

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-dev-shm-usage')

months = ['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']


with open("emails.txt","r") as f:
    mails = f.readlines()
    mail = random.choice(mails)
    
driver1 = webdriver.Chrome(options=chrome_options)
driver1.get("https://discord.com/register")
email_box = driver1.find_element_by_name("email")
email_box.send_keys(mail)
id_box = driver1.find_element_by_name("username")
name = names.get_first_name()
id_box.send_keys(name)
pass_box = driver1.find_element_by_name("password")
pass_box.send_keys(''.join(random.choice(string.ascii_uppercase + string.digits)
                                                  for i in range(10 )))
date = random.randint(1970, 2002)
selection_month = random.choice(months)
selection_day = random.randint(1,28)
enter_month = driver1.find_element_by_id("react-select-2-input")
enter_month.send_keys(selection_month, Keys.ENTER)
enter_day = driver1.find_element_by_id("react-select-3-input")
enter_day.send_keys(selection_day, Keys.ENTER)
enter_year = driver1.find_element_by_id("react-select-4-input")
enter_year.send_keys(date, Keys.ENTER)
submit = driver1.find_element_by_class_name("button-3k0cO7.button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeLarge-1vSeWK.fullWidth-1orjjo.grow-q77ONN")

discord_login = driver1.current_url
submit.click()
with open('proxy.txt','r') as proxyfile:
      ProxyPool = proxyfile.read().split("\n")
      ProxyPool = random.choice(ProxyPool)
      print(ProxyPool)

while True:
  if discord_login != driver1.current_url:
    print("Account Created")
    token = driver1.execute_script('''
    var req = webpackJson.push([
        [], {
            extra_id: (e, t, r) => e.exports = r
        },
        [
            ["extra_id"]
        ]
    ]);
    for (let e in req.c)
        if (req.c.hasOwnProperty(e)) {
            let t = req.c[e].exports;
            if (t && t.__esModule && t.default)
                for (let e in t.default) "getToken" === e && (token = t.default.getToken())
        }
    return token;   
                ''')
    print(f"{token} - {name}")

    with open("accoount.txt","a") as file:
      file.write(f"{token} - {name}\n")

    break
