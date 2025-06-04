from celery import shared_task
from django.core.mail import send_mail


@shared_task(name='email_celery')
def send_feedback_email_task(email, message):
    send_mail(
        subject="Fikr-mulohaza",
        message=message,
        from_email=email,
        recipient_list=["admin@example.com"],
        fail_silently=False,
    )
