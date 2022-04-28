import smtplib
from acount import *
from random import *
from email.message import EmailMessage
from imap_tools import MailBox
from openpyxl import Workbook

names = ["유재석", "박명수", "하하", "이광수", "김종국"]
winner = []

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    # 신청자 메일 5개 보내기
    for name in names:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        phone = randint(1000, 9999)
        msg.set_content(f"{name}/{str(phone)}")
        smtp.send_message(msg)

lst = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 30-Mar-2022)'):
        if "파이썬 특강 신청합니다." in msg.subject:
            lst.append((msg, index, msg.text[:3], msg.text[4:]))
            index += 1

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    wait = 1
    for x in lst:
        index, nickname, phone = x[1:]
        msg = EmailMessage()
        # 선정 안내 메일 보내기 (선착순 3명)
        if index < 4:
            msg["Subject"] = "파이썬 특강 안내 [선정]"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = x[0].from_
            msg.set_content(f"{nickname}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {index}번)")
            smtp.send_message(msg)
                
            # 당첨자 추가
            winner.append({"number" : index, "name" : nickname, "phone" : phone})
            
        # 탈락자 안내 메일 보내기
        else:
            msg["Subject"] = "파이썬 특강 안내 [탈락]"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = x[0].from_
            msg.set_content(f"{nickname}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {wait}번)")
            wait += 1
            smtp.send_message(msg)
                

# 당첨자 xlsx파일 만들기
wb = Workbook()
ws = wb.active
        
ws.append(["순번", "이름", "전화번호"])
for file in winner:
    ws.append(list(file.values()))
            
wb.save("winner_list.xlsx")
wb.close()