from selenium import webdriver
from time import sleep
from random import randint
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
import time

TEXT=[]

f = open("insults.txt", "rt")
for line in f:
    TEXT.append(line)
f.close()


URL = "https://onyolo.com/m/P9ARaPeBjA?w=i%E2%80%99m%20bored,%20entertain%20me&sc_ewa_page_id=74065D11-E13F-4120-857A-8219B43D8262&sc_ewa=1"




for _ in range(100):
    driver = webdriver.Firefox()
    driver.get(URL)
    text_box = driver.find_element_by_xpath('//*[@id="text"]')
    text_box.click()
    text_box.send_keys(TEXT[randint(0,len(TEXT))])
    submit_button = driver.find_element_by_xpath('//*[@id="send-button"]')
    submit_button.click()
    driver.close()



