import os
import time
import datetime
import fnmatch
import shutil

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
# pattern = "*.png" # .py로 끝나는 모든 파일
# res = []
# for root, dirs, files in os.walk("."):
#     for file in files:
#         if fnmatch.fnmatch(file, pattern):
#             res.append(os.path.join(root, file))
# print(res)

# 주어진 경로가 파일인지 폴더인지?
# print(os.path.isfile('sample_insert.xlsx'))
# print(os.path.isdir('sample_insert.xlsx'))

# print(os.path.isfile('2_desktop'))
# print(os.path.isdir('2_desktop'))

# # 지정된 경로에 해당하는 파일 / 폴더가 없다면? 
# print(os.path.isfile('2_deskto')) # False 출력

# 주어진 경로가 존재하는지
# if os.path.exists('2_desktop'):
#     print('존재')
# else:
#     print("파일 없음")

# 파일 만들기
# open("new_file.txt", "a").close() # 빈파일 생성

# 파일명 변경
# os.rename("new_file.txt", "rename_file.txt")

# 파일 삭제
# os.remove("rename_file.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준
# os.mkdir("c:/Users/USER21R1") # 절대경로 기준

# 하위 폴더를 가지는 폴더 만들기
# os.makedirs("new_folder/a/b/c")

# 폴더명 변경
# os.rename("new_folder", "news_folder")

# 폴더 지우기 : 폴더 안이 비어있지 않으면 오류
# os.rmdir("news_folder") # 폴더 안이 비었을 때만 삭제 가능

# 폴더 안이 비어 있지 않아도 완전 삭제가능
# shutil.rmtree("news_folder")

# 파일 복사하기
# shutil.copy("scores.xlsx", "test_folder")
# # 파일을 폴더 안에 새로운 파일 이름으로 복사하기
# shutil.copy("scores.xlsx", "test_folder/copied_scores.xlsx")

# 원본 파일 경로, 대상 파일 경로
# shutil.copyfile("scores.xlsx", "test_folder/copied_scores2.xlsx")

# copy, copyfile : 메타정보 복사 x
# copy2 : 메타정보 복가 o
# 메타정보 : 그 파일 정보 그대로 ex) 만든 날짜까지
# shutil.copy2("scores.xlsx", "test_folder/copy2.xlsx")

# 폴더 복사
# 하위 폴더도 복사
# shutil.copytree("test_folder", "test_folder2")

# 폴더 이동
# shutil.move("test_folder", "test_folder2")
# 폴더명이 변경되는 효과
# shutil.move("test_folder", "test_folder_rename")