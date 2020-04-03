from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
import requests as rq

webdriver = webdriver.Chrome()
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(20)
print("working")
username = webdriver.find_element_by_name('username')
username.send_keys('username')
password = webdriver.find_element_by_name('password')
password.send_keys('password')

button_login = webdriver.find_element_by_class_name("y3zKF")
button_login.click()
sleep(10)
notification = webdriver.find_element_by_class_name("HoLwm")
notification.click()
sleep(2)
webdriver.get('https://www.instagram.com/virat.kohli/')
sleep(10)

soup = BeautifulSoup(webdriver.page_source, 'html.parser')
# print(soup)

allimages = soup.select('img')
print(allimages)
imglink = []
for img in allimages:

    imglink.append(img["src"])


# os.mkdir("pixabay")
print(imglink)

for index, img_link in enumerate(imglink):

    if img_link:
        print(img_link)
        if not rq.get(img_link):
            pass
        else:
            img_data = rq.get(img_link).content
            print(img_link)
            with open("insta/" + str(index + 1) + ".jpg", 'wb+') as f:
                f.write(img_data)

    else:
        f.close()
        print("Images Downloaded")
        break
