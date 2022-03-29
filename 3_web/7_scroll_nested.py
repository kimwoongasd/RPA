from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(3)

# 특정 영역 스크롤
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[62]')

# 1. ActionChain
# 찾은 element를 이용해서 element가 보일떄 까지 스크롤 내림
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 2.
# 함수가 아니라 () 쓰지 마세요
xy = elem.location_once_scrolled_into_view
print(type(xy))
print(xy)

elem.click()

time.sleep(2)
browser.quit()
