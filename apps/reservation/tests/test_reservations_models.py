import pytest
from django.core.exceptions import ValidationError
from django.core import mail
from django.utils import timezone
from apps.users.models import User
from apps.bookstore.models import Book, Author
from apps.reservation.models import Reservation

@pytest.mark.django_db
def test_reservation_str():
    user = User.objects.create(user_name="Alice", email="alice@example.com")
    author = Author.objects.create(name="J.K. Rowling")
    book = Book.objects.create(name="Harry Potter", author=author, total_copies=3)
    start = timezone.now()
    end = start + timezone.timedelta(days=1)
    reservation = Reservation.objects.create(user=user, book=book, start_date=start, end_date=end)
    expected_str = f"{user.user_name} reserved {book.name} from {start} to {end}"
    assert str(reservation) == expected_str

@pytest.mark.django_db
def test_clean_end_date_validation():
    user = User.objects.create(user_name="Bob", email="bob@example.com")
    author = Author.objects.create(name="George Orwell")
    book = Book.objects.create(name="1984", author=author)
    start = timezone.now()
    end = start - timezone.timedelta(hours=1)  # invalid: end before start
    reservation = Reservation(user=user, book=book, start_date=start, end_date=end)
    with pytest.raises(ValidationError) as exc:
        reservation.clean()
    assert "end_date" in exc.value.message_dict

@pytest.mark.django_db
def test_overlapping_reservation_validation():
    user = User.objects.create(user_name="Charlie", email="charlie@example.com")
    author = Author.objects.create(name="Agatha Christie")
    book = Book.objects.create(name="Murder on the Orient Express", author=author)
    start1 = timezone.now()
    end1 = start1 + timezone.timedelta(days=2)
    Reservation.objects.create(user=user, book=book, start_date=start1, end_date=end1)

    # overlapping reservation
    start2 = start1 + timezone.timedelta(days=1)
    end2 = start2 + timezone.timedelta(days=2)
    overlapping = Reservation(user=user, book=book, start_date=start2, end_date=end2)
    with pytest.raises(ValidationError) as exc:
        overlapping.clean()
    assert "book" in exc.value.message_dict


