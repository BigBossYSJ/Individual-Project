# import library:
import smtplib
import ssl
import getpass
from socket import gaierror

# define port,server,login and password:
port = 465
smtp_server = "smtp.gmail.com"
login = input("\nPlease enter your gmail : ") # enter your mail
password = getpass.getpass("\nPlease enter your password : ") # enter your password

# specify who the sender and the receiver:
sender = "hahakerol@gmail.com"
receiver = input("\nPlease enter the receiver gmail : ")

# type any message to send to the receiver:
message = input("\nPlease enter the message that you want to send : ")

try:
    # smtp credentials:
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, receiver, message)

    # tell whether the message is successfully sent or have any error:
    print('\nMessage is successfully send to the receiver!\n')
except (gaierror, ConnectionRefusedError):
    print('\nFailed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('\nFailed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('\nSMTP error occurred: ' + str(e))

