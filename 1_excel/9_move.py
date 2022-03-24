from openpyxl import load_workbook

wb = load_workbook("sample2.xlsx")
ws = wb.active

# b1 부터 c11 까지 데이터를 행 0 열 1칸씩 옮긴다
# ws.move_range("B1:C11", rows=0, cols=1)

# 덮어쓰기 가능
ws.move_range("C1:C11", rows=5, cols=-1)

wb.save("sample2_move.xlsx")
wb.close()