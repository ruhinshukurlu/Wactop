import smtplib


def sendemail(email, text):
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("kamilgarib@gmail.com", "realpassword")
    subject = "Wactop"
    message = 'Subject:{}\n\n{}'.format(subject, text)
    mail.sendmail("kamilgarib@gmail.com", email, message)
    mail.quit()

