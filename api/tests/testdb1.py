
import pytest
from django.utils import timezone
from ..models import  User, Auhor, Book, Bookreservation

@pytest.mark.django_db
def test_custom_user_create_user():
    user = User.objects.create_user(
        password="testpassword",
        email="test@example.com",
        user_name="testuser",
    )
    assert user.email == "test@example.com"
    assert user.user_name == "testuser"
    assert user.is_staff is False
    assert user.is_active is True
    assert user.check_password("testpassword")

@pytest.mark.django_db
def test_custom_user_create_superuser():
    user = User.objects.create_superuser(
        password="superpassword",
        email="super@example.com",
        user_name="superuser",
    )
    assert user.email == "super@example.com"
    assert user.user_name == "superuser"
    assert user.is_staff is True
    assert user.is_superuser is True
    assert user.is_active is True
    assert user.check_password("superpassword")

@pytest.mark.django_db
def test_user_str_representation():
    user = User.objects.create(
        email="user@example.com",
        user_name="testuser",
    )
    assert str(user) == "user@example.com"

@pytest.mark.django_db
def test_author_model():
    author = Auhor.objects.create(
        name="Test Author",
        birthday=timezone.now(),
    )
    assert author.name == "Test Author"

@pytest.mark.django_db
def test_book_model():
    author = Auhor.objects.create(
        name="Test Author",
        birthday=timezone.now(),
    )
    book = Book.objects.create(
        author=author,
        date_release=timezone.now(),
        name="Test Book",
    )
    assert book.name == "Test Book"
    assert book.author == author

@pytest.mark.django_db
def test_bookreservation_model():
    user = User.objects.create(
        email="user@example.com",
        user_name="testuser",
    )
    author = Auhor.objects.create(
        name="Test Author",
        birthday=timezone.now(),
    )
    book = Book.objects.create(
        author=author,
        date_release=timezone.now(),
        name="Test Book",
    )
    reservation = Bookreservation.objects.create(
        user=user,
        book=book,
        date1=timezone.now(),
        date2=timezone.now(),
    )
    assert reservation.user == user
    assert reservation.book == book
