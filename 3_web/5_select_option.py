from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame('iframeResult')

time.sleep(2)
# cars에 해당하는 element를 팢고 내부에 있는 2번쨰 옵션 선택
# option[1] : 1번쨰 옵션 
# option[2] : 2번쨰 옵션 
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[3]')
# elem.click()

# 텍스트 값을 통해서 값 선택
# 옵션 중에서 텍스트가 Opel인 값을 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Opel"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Op")]')
elem.click()

time.sleep(5)

browser.quit()