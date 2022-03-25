import pyautogui

# pyautogui.mouseInfo()

# 마우스를 모퉁이에 가져가도 안멈춤
# pyautogui.FAILSAFE = False

# 모든 동작에 1초씩 sleep 적용
pyautogui.PAUSE = 1 

# 중간에 멈추고 싶다면 4모퉁이 중에 한곳에 가져가면 멈춤
for i in range(10):
    pyautogui.move(100, 100)
    