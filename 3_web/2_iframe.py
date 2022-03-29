from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

# frame 전환
browser.switch_to.frame('iframeResult')

# iframe 안에 또 다른 html이 있기떄문에 전환해 주지 않으면 오류
elem = browser.find_element(By.XPATH, '//*[@id="html"]')

elem.click()

# 다시 원래 frame(문서)로 전환
# 상위로 빠져 나옴
browser.switch_to.default_content()

time.sleep(5)

browser.quit()