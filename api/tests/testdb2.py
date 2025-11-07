from django.test import TestCase
from ..models import  User, Auhor, Book, Bookreservation
from factories import  UserFactory, AuhorFactory, BookFactory, BookreservationFactory


class UserTestCase(TestCase):
    def test_user_creation(self):
        user = UserFactory()
        self.assertTrue(isinstance(user, User))
        self.assertTrue(user.email)
        self.assertTrue(user.user_name)
        self.assertTrue(user.check_password('password'))
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertEqual(user.sex, 'male')

class AuthorTestCase(TestCase):
    def test_author_creation(self):
        author = AuhorFactory()
        self.assertTrue(isinstance(author, Auhor))
        self.assertTrue(author.name)
        self.assertTrue(author.birthday)

class BookTestCase(TestCase):
    def test_book_creation(self):
        book = BookFactory()
        self.assertTrue(isinstance(book, Book))
        self.assertTrue(book.name)
        self.assertTrue(book.author)
        self.assertTrue(book.date_release)

class BookReservationTestCase(TestCase):
    def test_book_reservation_creation(self):
        reservation = BookreservationFactory()
        self.assertTrue(isinstance(reservation, Bookreservation))
        self.assertTrue(reservation.user)
        self.assertTrue(reservation.book)
        self.assertTrue(reservation.date1)
        self.assertTrue(reservation.date2)
