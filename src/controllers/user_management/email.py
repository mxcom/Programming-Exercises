import keyring
import pyotp
import smtplib


def gen_key():
    return pyotp.random_base32()


def generate_code(key: str):
    totp = pyotp.TOTP(key)
    return totp.now()


def verify_code(key: str, code: str):
    totp = pyotp.TOTP(key)
    return totp.verify(code)


def send_mail(mail : str):
    try:
        usr = keyring.get_credential(service_name="email_login", username=None).username,
        passwrd = keyring.get_credential(service_name="email_login", username=None).password,
        mail_txt = 'Your 2FA code is:\n' + str(generate_code) + '\n'
        subject = 'Your 2FA code.'
        MAIL_FROM = 'progex@gmx.de'
        RCPT_TO = mail
        DATA = 'From:%s\nTo:%s\nSubject:%s\n\n'.format(MAIL_FROM, RCPT_TO, subject, mail_txt)

        server = smtplib.SMTP('smtpserver', 25) # exchange port with real port
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(usr, passwrd)
        server.sendmail(MAIL_FROM, RCPT_TO, DATA)
        server.quit()
    except Exception as e:
        print(e)
