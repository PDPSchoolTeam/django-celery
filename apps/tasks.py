from celery import shared_task
from django.core.mail import send_mail


@shared_task(name="msg")
def send_feedback_email_task(email, message):
    send_mail(
        subject="hi",
        message=message,
        from_email="admin@gmail.com",
        recipient_list=[email],
        fail_silently=False,
    )
