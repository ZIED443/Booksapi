import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.bookstore.models import Author, Book
from apps.reservation.models import Reservation

@pytest.mark.django_db
def test_author_str():
    author = Author.objects.create(name="George Orwell")
    assert str(author) == "George Orwell"


@pytest.mark.django_db
def test_book_str():
    author = Author.objects.create(name="J.K. Rowling")
    book = Book.objects.create(name="Harry Potter", author=author)
    assert str(book) == "Harry Potter"
    assert book.author.name == "J.K. Rowling"


@pytest.mark.django_db
def test_book_validation():
    author = Author.objects.create(name="Victor Hugo")
    book = Book(name="Les Misérables", author=author, total_copies=0)
    # total_copies < 1 should raise a ValidationError
    with pytest.raises(ValidationError):
        book.clean()


@pytest.mark.django_db
def test_available_copies(monkeypatch):
    """
    Simulates having active reservations.
    """
    author = Author.objects.create(name="Agatha Christie")
    book = Book.objects.create(name="Murder on the Orient Express", author=author, total_copies=3)

    # Mock Reservation.objects.filter().count() to simulate 2 active reservations
    class MockQuerySet:
        def count(self):
            return 2

    # Correctly patch the Reservation model in the reservation app
    monkeypatch.setattr(Reservation.objects, "filter", lambda **kwargs: MockQuerySet())

    assert book.available_copies == 1  # 3 total - 2 active = 1 available