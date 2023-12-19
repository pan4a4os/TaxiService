from celery import shared_task
from django.core.mail import EmailMessage


@shared_task()
def send_notification_to_email(subject: str, message: str, recipient_list: tuple[str]) -> None:
    """Селері завдання, яке відповідає за надсилання повідомлення на електрону пошту користувача."""

    email_message = EmailMessage(subject=subject, body=message, to=recipient_list)
    email_message.send()
