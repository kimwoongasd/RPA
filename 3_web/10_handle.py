from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# handle
# 새 브라우저가 열리면 그 브라우저로 이동해 자동화 도와줌

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')

# 현재 윈도우 핸들 정보
curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

# 모든 핸들 정보
handels = browser.window_handles 
for handle in handels:
    print(handle)
    # 각 핸들로 이동
    browser.switch_to.window(handle)
    # 이동한 핸들 (브라우저) 타이틀 출력
    print(browser.title)
    print()
# 새로 이동된 브라우저에서 자동화 작업


# 현재 브라우저 종료
print("현재 핸들 닫기")
print(browser.title)
browser.close()

# 이전 핸들로 돌아오가
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

# 브라우저 컨트롤 가능한지 확인
time.sleep(5)
browser.get("")


time.sleep(5)
browser.quit()