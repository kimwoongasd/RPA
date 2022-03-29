from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame('iframeResult')

# 전체 선택이 안되어 있을떄

ch_1 = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')
ch_2 = browser.find_element(By.XPATH, '//*[@id="vehicle2"]')
ch_3 = browser.find_element(By.XPATH, '//*[@id="vehicle3"]')

if ch_1.is_selected() == False and ch_2.is_selected() == False and ch_3.is_selected() == False:
    ch_1.click()
    print('1번선택')

else:
    print('선택되어있음')
    
time.sleep(3)

if ch_1.is_selected() == False and ch_2.is_selected() == False and ch_3.is_selected() == False:
    ch_1.click()
    print('1번선택')

else:
    print('선택되어있음')
    
browser.switch_to.default_content()


    