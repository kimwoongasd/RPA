import smtplib
from acount import *
from email.message import EmailMessage

# 메시지객체 만들기
msg = EmailMessage()

msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = EMAIL_ADDRESS # 받는 사람

# 여러명에게 메일 보낼 떄
# msg["To"] = EMAIL_ADDRESS, 'nadocoding', "somsom"

# 리스트 형태일떄
# to_list = ["nadocoding", "somsom", "test"]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "nadocoding"

# 비밀참조
# msg["Bc"] = "nadocoding"

msg.set_content("테슽트 본문입니다") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결 잘 되는지 확인
    smtp.starttls() # 암호화
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg) # 메일 보내기
