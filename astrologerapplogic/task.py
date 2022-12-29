from django.conf import settings
from django.core.mail import send_mail

def Sending_Emails(email_handle):
    subject = 'Welcome to Asltrologer Website'
    message = 'Hi  thank you for registering in  Asltrologer Website, Go to this site to create your free kundali  :)'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_handle,]
    flag = send_mail(subject, message, email_from, recipient_list)
    if flag:
        return True
    else:
        return False