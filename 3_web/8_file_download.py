from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 다운로드한 파일을 지정한 경로에 저장
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\USER21R16\Desktop\RPA'})

service = Service('chromedriver')
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

# 다운로드 링크 클릭
elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

browser.switch_to.default_content()

time.sleep(3)
browser.quit()
