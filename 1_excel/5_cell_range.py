from openpyxl import Workbook
from random import *
from openpyxl.utils.cell import coordinate_from_string

wb = Workbook()
ws = wb.active

# 1줄씩 데이터 넣기
ws.append(['번호', '영어', '수학'])

for i in range(1, 11):
    ws.append([i, randint(0, 100), randint(0, 100)])

# 영어 column만 가져오기
# col_b = ws["B"]
# for cell in col_b:
#     print(cell.value)

# 영어 수학 column 가져오기
# col_range = ws["B:C"]
# for cols in col_range:
#     for cell in cols:
#         print(cell.value)

# 1번쨰 row만 가져오기
# row_title = ws["1"]
# for i in row_title:
#     print(i.value)

# 2 ~ 6 번쨰 row만 가져오기
rows_range = ws["2:6"]
for i in rows_range:
    for x in i:
        # print(x.value, end=' ')
        # print(x.coordinate, end=' ') # cell의 좌표정보를 가져온다
        xy = coordinate_from_string(x.coordinate) # row와 column 를 분리
        # print(xy, end=' ')
        print(xy[0], end='')
        print(xy[1], end=' ')
    print()
  
wb.save('sample2.xlsx')
wb.close()