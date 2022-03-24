from openpyxl import load_workbook

wb = load_workbook("sample2.xlsx")
ws = wb.active

# 8번쨰 줄 데이터 삭제
# ws.delete_rows(8)

# 8번쨰 줄부터 3줄 삭제
# ws.delete_rows(8, 3)

# 2열 삭제
# ws.delete_cols(2)

# 2열부터 총 2개 삭제
ws.delete_cols(2, 2)

wb.save('sample_del.xlsx')
wb.close()