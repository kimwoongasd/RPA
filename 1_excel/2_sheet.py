from tkinter import W
from openpyxl import Workbook

wb = Workbook()

# 새로운 sheet 기본 이름으로 생성
ws = wb.create_sheet()

# 타이틀 이름 변경
ws.title = 'Mysheet'

# RGB 형태로 값을 넣어주면 sheet 색상 변경
ws.sheet_properties.tabColor = 'ff66ff'

# 주어진 이름으로 sheet 생성
ws_1 = wb.create_sheet('Yoursheet')

wb.save('sample.xlsx')
wb.close()
