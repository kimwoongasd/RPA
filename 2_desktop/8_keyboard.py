import pyautogui
import pyperclip

# 메모장 1개 띄운 상태에서 가져옴
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("1235")
# # 글 입력하는 속도 조절가능
# pyautogui.write("nadocoding", interval=1)

# left : 방향키 왼쪽, right : 오른쪽, enter = 엔터
# automate the boring stuff with python 에서 공부 가능
# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "L", "A", "enter"], interval=0.25)

# 특수 문자
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 ctrl + a
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# pyautogui.hotkey("ctrl", "a")

# 한글처리 pip install pyperclip
# 글자를 클립보드에 저장 : ctrl + c
pyperclip.copy("나도 코딩")
pyautogui.hotkey("ctrl", "v")