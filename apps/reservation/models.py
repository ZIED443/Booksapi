# apps/reservation/models.py
from django.db import models
from django.utils import timezone
from apps.users.models import User
from django.core.exceptions import ValidationError

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    book = models.ForeignKey("bookstore.Book", on_delete=models.CASCADE, related_name="reservations")  
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


    def clean(self):
        # 1. End date must be after start date
        if self.end_date <= self.start_date:
            raise ValidationError({"end_date": "End date must be after start date"})
        # 3. Check overlapping reservations for the same book
        overlapping = Reservation.objects.filter(
            book=self.book,
            end_date__gte=self.start_date,
            start_date__lte=self.end_date
        ).exclude(pk=self.pk)
        if overlapping.exists():
            raise ValidationError({"book": "This book is already reserved for the selected period"})

        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.user_name} reserved {self.book.name} from {self.start_date} to {self.end_date}"
