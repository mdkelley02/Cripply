from selenium import webdriver
from time import sleep
from random import randint
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.idahostatesman.com/sports/high-school/article256047062.html"

ROLE = '[role="button"]'
SCRIPT_LITERAL = f"return document.querySelector('beop-widget').shadowRoot.querySelectorAll('{ROLE}')[6].click()"

times_ran = 0
while True:
    print(times_ran)
    driver = webdriver.Firefox()
    driver.get(URL)
    element = driver.execute_script(SCRIPT_LITERAL)
    sleep(2)
    times_ran += 1
    driver.close()

# driver.close()


# number_of_votes = 0
# while number_of_votes < 2000:
#     driver = webdriver.Firefox()
#     driver.get(URL)
#     sleep(2)
#     element = driver.execute_script(SCRIPT_LITERAL)
#     driver.close()
#     number_of_votes += 1




