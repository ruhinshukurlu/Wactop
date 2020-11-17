import smtplib
from django.core.mail import send_mail, EmailMultiAlternatives
from Wactop.settings import EMAIL_HOST_USER

def sendemail(email, text):
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("kamilgarib@gmail.com", "realpassword")
    subject = "Wactop"
    message = 'Subject:{}\n\n{}'.format(subject, text)
    mail.sendmail("kamilgarib@gmail.com", email, message)
    mail.quit()


def sendMail(subject,text_content, html_content):
    
    msg = EmailMultiAlternatives(subject,text_content, EMAIL_HOST_USER, ['sara.axmedova98@gmail.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()