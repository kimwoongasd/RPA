import smtplib
from acount import *
from random import *
from email.message import EmailMessage
from imap_tools import MailBox
from openpyxl import Workbook


names = ["유재석", "박명수", "하하", "이광수", "김종국"]

# 당첨자 리스트
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
        

    mailbox = MailBox("imap.gmail.com", 993)
    mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
        
    
    count = 1
    wait = 1

    # 특정 날짜 이후로 검색
    for mail in mailbox.fetch('(SENTSINCE 30-Mar-2022)', reverse=False):
        msg = EmailMessage()
        
        try:
        # 이름과 전화번호 분리
            nickname, number = mail.text.strip().split("/")

            # 선정 안내 메일 보내기 (선착순 3명)
            if "신청" in mail.subject and count < 4:
                msg["Subject"] = "파이썬 특강 안내 [선정]"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = EMAIL_ADDRESS
                msg.set_content(f"{nickname}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {count}번)")
                # msg.set_content(f"{mail.text[:3]}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {count}번)")
                smtp.send_message(msg)
                
                # 당첨자 추가
                winner.append({"number" : count, "name" : nickname, "phone" : number})
                count += 1
            
            # 탈락자 안내 메일 보내기
            elif "신청" in mail.subject:
                msg["Subject"] = "파이썬 특강 안내 [탈락]"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = EMAIL_ADDRESS
                msg.set_content(f"{nickname}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {wait}번)")
                # msg.set_content(f"{mail.text[:3]}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {wait}번)")
                wait += 1
                smtp.send_message(msg)
                
        except:
            continue

        # 당첨자 xlsx파일 만들기
        wb = Workbook()
        ws = wb.active
        
        ws.append(["순번", "이름", "전화번호"])
        for file in winner:
            ws.append(list(file.values()))
            
        wb.save("winner_list.xlsx")
        wb.close()