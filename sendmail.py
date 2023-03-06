import smtplib

SERVER = "smtp.qq.com"

FROM = "example@qq.com"
TO = ["luckyguy@RenyiMail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = f"""\
From: {FROM}
To: {','.join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

# Send the mail

sender = smtplib.SMTP_SSL(SERVER,port=465) # pay attention the SSL 
username="example@qq.com"   # for qq mail, must be the same as FROM 
password="somesixteenchars"  # authorization code from tencent, generally not the same as your login password  
sender.login(username, password)
sender.sendmail(FROM, TO, message)
sender.quit()
