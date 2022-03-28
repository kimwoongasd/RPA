from curses import window
import pyautogui
import time
import pyperclip
import sys

def txt_write(txt):
    pyperclip.copy(txt)
    pyautogui.hotkey("ctrl", "v")
    
# 그림판 실행
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

time.sleep(1)

w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]

if w.isActive == False:
    w.activate()

if w.isMaximized == False:
    w.maximize()

time.sleep(1)

# 상당 텍스트 기능을 찾아서 흰 영역 아무 곳에다가 글자 입력
txt_img = pyautogui.locateOnScreen("quiz_txt.png")
if txt_img:
    pyautogui.click(txt_img)

else:
    sys.exit()
    
pyautogui.moveTo(23, 176, duration=2)
pyautogui.leftClick()

# txt_write("참 잘했어요")
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

# 5초 대기 후 그림판 종료
pyautogui.sleep(5)

# 종료
# window.close()
pyautogui.hotkey("alt", "f4")
time.sleep(1)
pyautogui.press("n")
