from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465   ##ip통신상의 채널과 같은 역할로써 데이터 섞이지 않게
SMTP_USER = 'kt01099343122@gmail.com' ## 이메일주소
SMTP_PASSWORD = 'hlrswcymnlhmjjvl'

def send_mail(name, recvs, cc, hidden_cc, contents, attachment=False):
    msg = MIMEMultipart('alternative')

    if attachment:
        msg=MIMEMultipart('mixed')

    msg['From'] = SMTP_USER
    msg['To'] = recvs
    msg['CC'] = cc
    msg['Subject']  = name + '님, 메일이 도착했습니다.'

    text = MIMEText(contents)
    msg.attach(text)

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application','octet-stream')
        f = open(attachment,'rb')
        file_contents = f.read()
        file_data.set_payload(file_contents)
        encoders.encode_base64(file_data)

        from os.path import basename
        filename = basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment',filename=filename)

        msg.attach(file_data)


    targets = ','.join((recvs, cc, hidden_cc))
    smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    print('login')
    smtp.sendmail(SMTP_USER, targets.split(','),
                  msg.as_string())
    smtp.close()
send_mail('kt01099343122@gmail.com','scolpigemail@gmail.com', '', '', '할수있음','ju_jit_su.jpg')