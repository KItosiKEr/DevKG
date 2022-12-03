from email import message
import smtplib
# from email.mime.text import MIMEText

def send_mail(message):
    sender = ""
    password = ""

    server = smtplib.SMTP("smtp.gmail.com", 2525)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)
        return "message send"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password pls"

def main():
    message = input("ввуди текст")
    print(send_mail(message=message))

if __name__ == "__main__":
    main()


