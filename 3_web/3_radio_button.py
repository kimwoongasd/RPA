from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
    
else:
    print("선택됨")
    
time.sleep(5)

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
    
else:
    print("선택됨")