from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("img.png")

# 선택 위치에 img.png 이미지를 삽임
ws.add_image(img, "C3")

wb.save("sample_img.xlsx")
wb.close()