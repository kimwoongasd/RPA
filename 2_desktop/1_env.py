import pyautogui

# 현재 화면의 스크린 사이즈 가져옴
size = pyautogui.size()
print(size) # 가로 세로 크기 알 수 있음
# size[0] : width size[1] : height