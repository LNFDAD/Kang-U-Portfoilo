import smtplib
import time
from email.mime.text import MIMEText
print("Made By Kangyoo - 매일보내기 ")
print("지금부터 정보를 입력해주세요. ( 이상한거 아닙니당!! ) \n---------------------------------")
name = input("이메일을 입력해주세요.  : ")
password = input("비밀번호를 입력해주세요.  : ")
name2 = input("누구에게 보낼건지 정해주세요.  : ")
subjectt = input("제목을 정해주세요  : ")
msggg = input("내용을 입력해주세요.  : ")
a = input("몇 번 반복하실지 입력해주세요.  : ")
x=0
print("---------------------------------")
s = smtplib.SMTP('smtp.gmail.com', 587)
 
s.starttls()

s.login(name , password)
 
msg = MIMEText(msggg)
msg['Subject'] = subjectt
i = 0  
while str(i) < str(a):
    time.sleep(5)
    s.sendmail(name , name2 , msg.as_string())
    i += 1  
    print(i , "번째 매일 전송완료. \n---------------------------------")
print("이상으로 메일보내기를 마칩니다.")
s.quit()