# 첨부파일로 전송
import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()

send_email = os.getenv("SECRET_ID")
send_pwd = os.getenv("SECRET_PASS")

recv_email = "@naver.com"

# SMTP 연결
smtp = smtplib.SMTP("smtp.naver.com", 587)
smtp.ehlo()
smtp.starttls()

# 로그인
smtp.login(send_email, send_pwd)

# 메일 객체 생성
msg = MIMEMultipart()

msg['Subject'] = "모니터 탐지"
msg['From'] = send_email
msg['To'] = recv_email

# 메일 본문
text = "<b>탐지되었습니다.</b>"

content_part = MIMEText(text, 'html')
msg.attach(content_part)

# 첨부파일
etc_file_path = r'uploads/1.txt'

with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())

    etc_part.add_header(
        'Content-Disposition',
        'attachment',
        filename=os.path.basename(etc_file_path)
    )

    msg.attach(etc_part)

# 메일 전송
smtp.sendmail(send_email, recv_email, msg.as_string())

smtp.quit()