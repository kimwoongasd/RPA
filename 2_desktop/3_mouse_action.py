import pyautogui

# 3초 대기
pyautogui.sleep(3)
# print(pyautogui.position())

# 좌표를 클릭
# pyautogui.click(67, 15, duration=1)

# pyautogui.click()

# 드래그 드랍등 할떄 활용
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()

# clicks 클릭 횟수
# pyautogui.click(clicks=2)

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태

# pyautogui.moveTo(400, 400)
# pyautogui.mouseUp() # 마우스 버튼 떈 상태

# pyautogui.rightClick() # 우클릭
# pyautogui.middleClick() # 휠 클릭

# pyautogui.moveTo(666, 368)
# drag 상대좌표(현재 기준 이동)
# 너무 빨라 수행이 안될떄는 duration을 설정해준다
# pyautogui.drag(200, 200, duration=0.25)

# 절대좌표
# pyautogui.dragTo(800, 500, duration=0.25)

# 양수 : 위방향, 음수 : 아래방향
pyautogui.scroll(-500)