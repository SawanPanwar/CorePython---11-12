import smtplib
import traceback


gmail_user = 'email'
gmail_password = 'password'

sent_from = gmail_user
to = ['sandeepratnawat1106@gmail.com']
subject = 'This is my first Python Message'
body = 'Hi, What is going on'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, body)
    server.close()
    print('Email sent!')

except:
    traceback.print_exc()
