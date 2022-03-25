import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 22,8 81,178,243 #51B2F3

# RGB값 가져오기
pixel = pyautogui.pixel(22, 8)
print(pixel)

# RGB 값이 같은지 확인 True or False
print(pyautogui.pixelMatchesColor(22, 8, (81,178,244)))