from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reservation

@receiver(post_save, sender=Reservation)
def send_reservation_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Reservation Confirmed",
            f"Hello {instance.user.user_name}, you reserved '{instance.book.name}' "
            f"from {instance.start_date} to {instance.end_date}.",
            "noreply@library.com",
            [instance.user.email],
        )
