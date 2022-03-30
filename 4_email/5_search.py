from imap_tools import MailBox
from acount import *

# mailbox = MailBox('imap.gmail.com', 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()


# 위 3줄 코드를 한줄로
# 로그아웃 필요없음
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # limit 없다면 전체 메일 가져오기 
    # for msg in mailbox.fetch():
    #     print(f'[{msg.from_}] {msg.subject}')
        
    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)', limit=10, reverse=True):
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM email)', limit=5, reverse=True):
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 어떤 글자를 포함하는 메일 (제목, 본문)
    # for msg in mailbox.fetch('(TEXT "test email")', limit=1, reverse=True):
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 어떤 글자를 포함하는 메일 (제목)
    # 한글 x
    # for msg in mailbox.fetch('(SUBJECT "test email")'):
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 한글로 검색 방법
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print(f'[{msg.from_}] {msg.subject}')
    
    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)',limit=5, reverse=True):
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 30-Mar-2022)',limit=5, reverse=True):
    #     print(f'[{msg.from_}] {msg.subject}')
        
    # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(ON 30-Mar-2022 SUBJECT "test email")',limit=5, reverse=True):
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 둘 중 하나 조건이라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 30-Mar-2022 SUBJECT "test email")',limit=5, reverse=True):
        print(f'[{msg.from_}] {msg.subject}')
    
    # imap tools 에서 더 자세한 사용법 나옴
        
        