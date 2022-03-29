from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service('chromedriver')
browser = webdriver.Chrome(service=service)
browser.get('')
time.sleep(2)

start_port = ''
arrive_port = ''

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/b').click()
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input').send_keys(start_port)
time.sleep(1)
browser.find_element(By.CLASS_NAME, 'autocomplete_search_item__2WRSw').click()

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input').send_keys(arrive_port)
time.sleep(1)
browser.find_element(By.CLASS_NAME, 'autocomplete_search_item__2WRSw').click()


m = 2
w = 5
d = 5
diff = 5
# 가는 날 
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
browser.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{m}]/table/tbody/tr[{w}]/td[{d}]/button/b').click()

d += diff - 1
if d > 7:
    d -= 7
    w += 1
    if w > 5:
        w = 1
        m += 1
time.sleep(1)

# 오늘날
try:
    browser.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{m}]/table/tbody/tr[{w}]/td[{d}]/button/b').click()
except:
    w += 1
    browser.find_element(By.XPATH, f'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[{m}]/table/tbody/tr[{w}]/td[{d}]/button/b').click()
    
# 검색 클릭
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()

# 로딩시간 대기
# 페이지가 변경되서 결과 안나옴
try:
    elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div/button')))
    time.sleep(5)
    print(elem.tetxt)

except:
    print("결과 검색 없음")

time.sleep(5)
# browser.quit()