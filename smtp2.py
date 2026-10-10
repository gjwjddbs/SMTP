# uploads 경로 내 중요 정보 탐지 시 자동으로 이메일 전송
import os
import re
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

def mail_sender(file_path,line):
    load_dotenv()
    send_email = os.getenv("SECRET_ID")
    send_pwd = os.getenv("SECRET_PASS")
    recv_email = "@naver.com" #수신 이메일

    smtp_name = "smtp.naver.com"
    smtp_port = 587

    text = f"중요 정보 탐지 {file_path} : 라인 {line}"
    
    msg = MIMEText(text,'plain','utf-8')
    msg['Subject'] = f"{file_path} 내 중요 정보 탐지"
    msg['From'] = send_email
    msg['To'] = recv_email

    email_string = msg.as_string()
    print(email_string)

    s = smtplib.SMTP(smtp_name,smtp_port)
    s.starttls()
    s.login(send_email,send_pwd)
    s.sendmail(send_email,recv_email,email_string)
    s.quit()

dir_path = 'uploads' #업로드된 파일 경로
all_files = os.listdir(dir_path)

txt_files=[]

# .txt 파일이 있으면 추가
for file in all_files:
    if file.endswith(".txt"):
        txt_files.append(file)

# .txt 파일 내 주석, 주민등록번호 탐지
for filename in txt_files:
    file_path = os.path.join(dir_path,filename)
    with open(file_path,'r',encoding='urf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            # 주석 탐지
            if line.startswith("#") or line.startswith("//"):
                print(f"주석 {file_path} {index+1} 라인 탐지 : {line.strip()}")
                mail_sender(file_path,line)
            # 주민등록번호 탐지
            if re.search(r'\d{6}\s*[-]\s*\d{7}',line):
                print(f"주민등록번호 {file_path} {index+1} 라인 탐지 : {line.strip()}")
                mail_sender(file_path,line)