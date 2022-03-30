import smtplib
from acount import *

# 이메일 보내기
# smtplib.SMTP("smtp.메일주소", 포트번호)
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    
    subject = "test email" # 메일 제목
    body = "mail body" # 메일 본문
    
    # 아래 형식대로 해야 제목 줄바꿈 후 본문 해야 구분해준다
    msg = f"Subject: {subject}\n{body}"
    
    # 발신자, 수신자, 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
