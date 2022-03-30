from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 사이트 들어가기
service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get('https://www.w3schools.com')
browser.maximize_window()

# 메뉴클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

time.sleep(2)

# how to 클릭
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[10]').click()

time.sleep(2)

# content form 메뉴 클릭
# xpath는 메뉴가 추가되거나 없어지면 값이 변할 수 있어 text를 사용
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]')

# 특정 영역 스크롤
xy = elem.location_once_scrolled_into_view
time.sleep(2)
elem.click()

# 값 입력
first_name = '나도'
last_name = '코딩'
country = 'Canada'
subject = '퀴즈 완료하였습니다.'

time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
# select-option 이기 떄문에 text를 씀
browser.find_element(By.XPATH, f'//*[@id="country"]/option[text()="{country}"]').click()
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)

# 제출 클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

# 브라우저 종료
time.sleep(5)
browser.quit()