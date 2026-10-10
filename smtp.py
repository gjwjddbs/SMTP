import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
send_email = os.getenv("SECRET_ID")
send_pwd = os.getenv("SECRET_PASS")
recv_email = "@naver.com"

smtp_name="smtp.naver.com"
smtp_port = 587

text = "이메일 보내기 테스트" #메일 내용

msg = MIMEText(text,'plain','utf-8')
msg['Subject']="이메일 테스트" #메일 제목
msg['From'] = send_email #송신 이메일
msg['To'] = recv_email #수신 이메일

email_string = msg.as_string()
print(email_string)

s = smtplib.SMTP(smtp_name,smtp_port)
s.starttls() #tls 보안 활성화
s.login(send_email,send_pwd) #smtp 서버 로그인
s.sendmail(send_email,recv_email,email_string) 
s.quit()
