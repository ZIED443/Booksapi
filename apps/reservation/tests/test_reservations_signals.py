import pytest
from django.core import mail
from django.utils import timezone
from apps.users.models import User
from apps.bookstore.models import Book, Author
from apps.reservation.models import Reservation

@pytest.mark.django_db
def test_reservation_signal_sends_email():
    user = User.objects.create(user_name="Dave", email="dave@example.com")
    author = Author.objects.create(name="Victor Hugo")
    book = Book.objects.create(name="Les Misérables", author=author, total_copies=3)
    start = timezone.now()
    end = start + timezone.timedelta(days=1)

    # Reset mail outbox to ignore emails from Author/Book signals
    mail.outbox = []

    Reservation.objects.create(user=user, book=book, start_date=start, end_date=end)

    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert email.to == [user.email]
    assert "reserved" in email.body
