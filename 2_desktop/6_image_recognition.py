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

# locateAllOnScreen : 2개이상 이미지가 같을떄
# check_box = pyautogui.locateAllOnScreen("check_box.png")

# for i in check_box:
#     pyautogui.click(i)

# 한개만
# ch = pyautogui.locateOnScreen("check_box.png")
# pyautogui.click(ch)


# 속도 개선
# 1. GrayScale : 컬러 이미지를 흑백으로 전환(30퍼센트 정도 개선된 속도)
# 단 정확도가 떨어질 수 있다

# close_icon = pyautogui.locateOnScreen('close_icon.png', grayscale=True)
# pyautogui.moveTo(close_icon)

# # 2. 범위 지정
# 759,644
# 954,840
# close_icon = pyautogui.locateOnScreen('close_icon.png', region=(759, 644, 954 - 759, 840 - 644))
# pyautogui.moveTo(close_icon)

# 정확도 조정
# 기본 값 0.999
# 몇 퍼센트 이상 일치하면 찾는다
run = pyautogui.locateOnScreen('run.png', confidence=0.7)
pyautogui.moveTo(run)