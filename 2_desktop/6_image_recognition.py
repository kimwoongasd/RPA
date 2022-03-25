import pyautogui

# # 이미지 파일과 같은 이미지를 화면에서 찾는다
# file_menu = pyautogui.locateOnScreen("file_menu.png")

# # 중간 부분 클릭
# pyautogui.click(file_menu)


# close_icon = pyautogui.locateOnScreen('close_icon.png')
# pyautogui.moveTo(close_icon)

# 못찾는다면 None출력
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# check_box = pyautogui.locateAllOnScreen("check_box.png")

# for i in check_box:
#     pyautogui.click(i)

ch = pyautogui.locateOnScreen("check_box.png")
pyautogui.click(ch)