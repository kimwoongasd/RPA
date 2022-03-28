import pyautogui
import time
import pyperclip

# 그림판 실행
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.hotkey("enter")

time.sleep(1)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

if w.isActive == False:
    w.activate()

if w.isMaximized == False:
    w.maximize()

time.sleep(1)

# 상당 텍스트 기능을 찾아서 흰 영역 아무 곳에다가 글자 입력
txt_img = pyautogui.locateOnScreen("quiz_txt.png")
pyautogui.click(txt_img)

pyautogui.moveTo(23, 176, duration=2)
pyautogui.leftClick()

pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

# 5초 대기 후 그림판 종료
pyautogui.countdown(5)
pyautogui.hotkey("alt", "f4")
time.sleep(1)
pyautogui.press("n")
