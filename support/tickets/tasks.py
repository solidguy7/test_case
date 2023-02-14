from celery import shared_task
from django.core.mail import send_mail
from .models import Ticket

@shared_task
def ticket_created(ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    subject = f'New ticket {ticket.id}'
    message = f'Dear support, please answer {ticket.sender}'
    mail_sent = send_mail(subject, message, 'ouremail@gmail.com', 'support_manager@gmail.com')
    return mail_sent
