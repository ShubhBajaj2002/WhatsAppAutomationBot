from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from config import CHROME_PROFILE_PATH

try:
    if sys.argv[1]:
        with open(sys.argv[1], 'r', encoding='utf8') as f:
            contacts = [names.strip() for names in f.readlines()]
except IndexError:
    print('Please provide contacts in .txt as the first argument')
    exit()



with open('message.txt', 'r', encoding='utf8') as f:
    msg = f.read()

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

browser = webdriver.Chrome(options=options)

browser.get('https://web.whatsapp.com/')
browser.maximize_window()


for name in contacts:
    search_box = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]'))
    )
    time.sleep(5)
    search_box.clear()
    search_box.send_keys(name)

    time.sleep(3)
    
    search_box.send_keys(Keys.ENTER)

    time.sleep(3)

    msgbox = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msgbox.send_keys(msg)
    msgbox.send_keys(Keys.ENTER)

    try:
        if sys.argv[2]:
            attachment_box = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div')
            attachment_box.click()
            time.sleep(1)
            img_box = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
            img_box.send_keys(sys.argv[2])
            time.sleep(1)
            click_box = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')
            click_box.click()
            time.sleep(3)
    except IndexError:
        pass


time.sleep(10)
