from django.conf import settings
from django.core.mail import send_mail



def send_order_email(order_email):
    try:
        subject = 'A new Product'
        message = f'Hi Admin, a new order from {order_email}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail( subject, message, email_from, recipient_list )
        print(f"{order_email} order email sent")
    except Exception as e:
        print(e.args)
