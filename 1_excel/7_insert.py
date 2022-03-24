from openpyxl import load_workbook

wb = load_workbook('sample2.xlsx')
ws = wb.active

# 8번쨰 줄이 비워짐
# ws.insert_rows(8)

# 8번쨰부터 5번쨰 빈줄이 생김
ws.insert_rows(8, 5)

wb.save('sample_insert.xlsx')

# B번쨰 열이 비워짐
# ws.insert_cols(2)
# B번째 열부터 3칸 비워짐
ws.insert_cols(2, 3)

wb.save('sample_insert_col.xlsx')
wb.close()