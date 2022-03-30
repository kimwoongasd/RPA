import smtplib
from acount import *
from email.message import EmailMessage

# 메시지 객체 생성
msg = EmailMessage()

msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 이
msg["To"] = EMAIL_ADDRESS # 받는 이

msg.set_content("다운로드 하세요") # 본문

# 첨부파일 추가
# msg.add_attachment()
# 메인, 서브 type은 mime type 구글 검색 후 알맞게 입력
# 이미지 파일
with open('run.png', "rb") as f:
    # add_attachment 인자(파일의 내용, 메인타입, 서브타입, 파일명)
    msg.add_attachment(f.read(), maintype="image", subtype='png', filename=f.name)

# pdf 파일
with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

# 엑셀파일
with open("scores.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="vnd.ms-excel", filename=f.name)


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 암호화
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)