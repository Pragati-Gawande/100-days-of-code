import smtplib

to = input("Enter the email of recipent:  ")

content = input("Enter the content for mail: ")

def sendEmail(to, content):
    server = smptlib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sernderemail@gmail.com', '')
    server.sendermail('', to, content)
    server.close()

sendEmail(to,content)    