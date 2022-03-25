from openpyxl import Workbook
from openpyxl import load_workbook

wb = Workbook()
ws = wb.active

ws.append(["학번", "출석", "퀴즈1", "퀴즈2", "중간고사", "기말고사", "프로잭트"])
scores = [(1,10,8,5,14,26,12),
(2,7,3,7,15,24,18),
(3,9,5,8,8,12,4),
(4,7,8,7,17,21,18),
(5,7,8,7,16,25,15),
(6,3,5,8,8,17,0),
(7,4,9,10,16,27,18),
(8,6,6,6,15,19,17),
(9,10,10,9,19,30,19),
(10,9,8,8,20,25,20)]

for s in scores:
    ws.append(s)

for row in ws.rows:
    for cell in row:
        if cell.column == 4 and cell.row != 1:
            cell.value = 10

ws["H1"] = '총점'
for i in range(2, 12):
    ws[f"H{i}"] = f"=SUM(B{i}:G{i})"

wb.save('scores.xlsx')
wb.close()

wb = load_workbook('scores.xlsx', data_only=True)
ws = wb.active
    
ws["I1"] = "성적"
for i in range(2, 12):
    if ws[f"B{i}"].value >= 5:
        if int(ws[f"H{i}"].value) >= 90:
            ws[f"I{i}"] = 'A'
            
        if int(ws[f"H{i}"].value) >= 80:
            ws[f"I{i}"] = 'B'
            
        if int(ws[f"H{i}"].value) >= 70:
            ws[f"I{i}"] = 'C'
            
        else:
            ws[f"I{i}"] = 'D'
    else:
        ws[f"I{i}"] = 'F'

        
wb.save('scores.xlsx')
wb.close()