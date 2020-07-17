#There is mailing to Client
import smtplib
def sending_mail(mailToo,mailSubjectt,mailBodyy):
    mailFrom = "CarFactory"
    mailTo = mailToo
    mailSubject = mailSubjectt
    mailBody = mailBodyy

    message = '''From: {}
Subject: {}
{}
'''.format(mailFrom, mailSubject, mailBody)
    newsletter_email = "aaa@op.pl"
    newsletter_password = "sda"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.login(newsletter_email,newsletter_password)
        server.sendmail(newsletter_email,mailTo,message)
        server.close()
        print(f"Mail wysłano do {mailTo}")
    except Exception as e:
        print(e)

