from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books")
    date_release = models.DateField(null=True, blank=True)
    total_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    @property
    def available_copies(self):
        """
        Returns the number of copies available for reservation.
        This is calculated as total_copies minus active reservations.
        """
        from apps.reservation.models import Reservation
        active_reservations = Reservation.objects.filter(
            book=self,
            end_date__gte=timezone.now()
        ).count()
        return max(self.total_copies - active_reservations, 0)

    def clean(self):
        if self.total_copies < 1:
            raise ValidationError({"total_copies": "There must be at least 1 copy of the book"})
        super().clean()
