from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
service = Service('/chromedriver')
browser = webdriver.Chrome(service=service)

browser.get("")


# 카페 메뉴 찾기
elem = browser.find_element_by_link_text('카페')

# 속성 가져오기
elem.get_attribute('href')
elem.get_attribute('class')

# 클릭
elem.click()

# 뒤로 가기
browser.back()

# 앞으로 가기
browser.forward()

# 새로고침
browser.refresh()

# 뒤로 가기
browser.back()

# 검색창 찾기 (개발자 도구 이용)
elem = browser.find_element(By.ID, 'query')

# 글자 입력하기
elem.send_keys('나도코딩')

# enter 치기

elem.send_keys(Keys.ENTER)

# a 태그 찾기
elem = browser.find_element(By.TAG_NAME, 'a')
elem.get_attribute('href')

# a 태그 모두 찾기
elems = browser.find_elements(By.TAG_NAME, 'a')
for e in elems:
    e.get_attribute('href')

# 다음으로 이동
browser.get('')

# 검색창 찾기
elem = browser.find_element(By.NAME, 'q')

# 글자 입력하기
elem.send_keys("나도코딩")

# 글자 지우기
elem.clear()

# 글자 입력하기
elem.send_keys("나도코딩")

# 검색 버튼 찾기
elem = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[2]')

# 클릭하기
elem.click()

# 스크린샷 찍기
browser.save_screenshot('daum.png')

# 페이지 소스 보기
browser.page_source

# 브라우저 종료
browser.close() # 현재 탭 닫기
browser.quit() # 브라우저 종료하기