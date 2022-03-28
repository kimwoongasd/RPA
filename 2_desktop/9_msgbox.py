import pyautogui

# 자동화 프로그램 종료
# ctrl + alt + del

# pyautogui.countdown(3)
# print('자동화 시작')

# pyautogui.alert("자동화 수행에 실패", "경고") # 확인 버튼만 있는 팝업

# res = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
# print(res)

# 사용자 입력
# res = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
# print(res)

# 비밀번호
res = pyautogui.password("암호를 입력하세요")
print(res)