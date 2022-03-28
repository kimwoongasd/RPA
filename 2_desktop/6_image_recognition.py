import pyautogui
import time
import sys

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
# run = pyautogui.locateOnScreen('run.png', confidence=0.7)
# pyautogui.moveTo(run)

# 자동화 대상이 바로 보여지지 않는 경우
file_menu_notepad = pyautogui.locateOnScreen('note_menu.png')
# if file_menu_notepad:
#     pyautogui.moveTo(file_menu_notepad)
# else:
#     print("발견 실패")

# 1. 계속 기다리기
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen('note_menu.png')
# pyautogui.moveTo(file_menu_notepad)

# 일정 시간동안 기다리기
# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = pyautogui.locateOnScreen('note_menu.png')
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen('note_menu.png')
#     end = time.time() # 종료 시간 설정
    
#     if end - start > timeout: # 10초 초과하면 종료
#         print("시간종료")
#         sys.exit()
    
# pyautogui.moveTo(file_menu_notepad)

# 함수로 만들기
def find_target(img_file, timeout = 30):
    start = time.time() 
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    
    else:
        print(f'{timeout}초 초과, {img_file} 파일을 찾지 못했습니다')
        
my_click('note_menu.png', 10)