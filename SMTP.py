#import library:
import smtplib
import ssl
import getpass
from socket import gaierror

#define port,server,login and password:
port = 465 
smtp_server = "smtp.gmail.com"
login = input("Please enter your gmail : ") # enter your mail
password = getpass.getpass("Please enter your password : ") # enter your password

# specify who the sender and the receiver
sender = "hahakerol@gmail.com"
receiver = "hahakerol@gmail.com"

# type any message to send to the receiver
message = f"""\
Subject: mic drop 321 sila makan jambu batu
To: {receiver}
From: {sender}

Kita push github duluuuuu. Alhamdulillah syukur nikmat tuhan."""

try:
    #smtp credentials
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, receiver, message)

    # tell whether the message is successfully sent or have any error 
    print('Message is successfully send to the receiver')
except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))
