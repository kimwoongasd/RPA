from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get('')

# 상품 입력
product = ""
search = browser.find_element(By.XPATH, '//*[@id="autocompleteWrapper"]/input[1]')
search.send_keys(product)

time.sleep(1)

# 검색 클릭
browser.find_element(By.XPATH, '//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤
# 지정한 위치로 스크롤 내리기
# 모니터 해상도 높이에 따라 값이 다를 수 있음
# browser.execute_script('window.scrollTo(0, 1080)')
# browser.execute_script('window.scrollTo(0, 2080)')

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 동적 페이지에 대해서 마지막까지 스크롤 반복
prev_h = browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

while True:
    # 스크롤 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    
    # 현재 문서 높이 저장
    cur_h = browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 높이 변화 없다면 반복문 탈출
    if cur_h == prev_h:
        break
    
    prev_h = cur_h

# 맨위로 스크롤 올리기
browser.execute_script("window.scrollTo(0, 0)")

time.sleep(5)
browser.quit()
