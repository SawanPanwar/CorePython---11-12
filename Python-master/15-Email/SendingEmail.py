# Example of Sending Email by Gmail Account
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#


import smtplib
connection = smtplib.SMTP('smtp.gmail.com' , 587)
connection.ehlo()
connection.starttls()
connection.login('email' , 'password')
connection.sendmail('skpanwar25@gmail.com' , 'sandeepratnawat1106@gmail.com' , 'Subject : This is the Subject \n\n Hello User')
connection.quit()


