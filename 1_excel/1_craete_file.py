from openpyxl import Workbook

# 새 워크북 생성
wb = Workbook()

# 현재 활성화된 sheet를 가져옴
ws = wb.active

# 시트 이름 변경
ws.title = 'Nadosheet'

# 워크북 저장
wb.save("sample.xlsx")
wb.close()