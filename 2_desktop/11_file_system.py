import os
import time
import datetime
import fnmatch

# # 현재 작업 공간
# print(os.getcwd())

# # RPA로 작업공간 이동
# os.chdir("2_desktop")
# print(os.getcwd())

# # 부모 폴더로 이동
# os.chdir("..")
# print(os.getcwd())

# os.chdir("../..")
# print(os.getcwd())

# # 절대경로로 이동
# os.chdir("c:/")
# print(os.getcwd())

# 파일 경로 만들기
# 절대 경로 생성
# file_path = os.path.join(os.getcwd(), "file_test.txt")
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\USER21R16 \Desktop\RPA\my_file.txt"))

# 파일 정보 가져오기
# 파일의 생성 날짜
# ctime = os.path.getctime("sample_insert.xlsx")
# # print(ctime)
# # # 날짜 정보를 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime('sample_insert.xlsx')
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접글 날자
# atime = os.path.getatime('sample_insert.xlsx')
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 크기
# size = os.path.getsize('sample_insert.xlsx')
# print(size) # 바잍트 단위로 파일크기 출력

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("2_desktop")) # 주어진 폴더에서 모든 폴더 파일 목록 가져오기

# 파일 목록 가져오기(하위 폴더 모두 포함)
# 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# res = os.walk(".") # . : 현재 폴더
# print(res)
# for root, dirs, files in res:
#     print(root, dirs, files)

# 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# res = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         res.append(os.path.join(root, name))
# print(res)

# *.xlsx, *.txt 등 찾으려면?
pattern = "*.png" # .py로 끝나는 모든 파일
res = []
for root, dirs, files in os.walk("."):
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            res.append(os.path.join(root, file))
print(res)
