from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Author, Book

@receiver(post_save, sender=Author)
def notify_new_author(sender, instance, created, **kwargs):
    if created:
      
        send_mail(
            "New Author Added",
            f"Author '{instance.name}' has been added to the system.",
            "noreply@library.com",
            ["admin@library.com"],  # change to admin email
        )

@receiver(post_save, sender=Book)
def notify_new_book(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "New Book Added",
            f"Book '{instance.name}' by {instance.author.name if instance.author else 'Unknown'} added.",
            "noreply@library.com",
            ["admin@library.com"],
        )
