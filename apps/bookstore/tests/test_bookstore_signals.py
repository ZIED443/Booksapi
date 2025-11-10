import pytest
from django.core import mail
from apps.bookstore.models import Author, Book

@pytest.mark.django_db
def test_notify_new_author_signal_sends_email():
    Author.objects.create(name="Ernest Hemingway")
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert "New Author Added" in email.subject
    assert "Ernest Hemingway" in email.body
    assert email.to == ["admin@library.com"]


@pytest.mark.django_db
def test_notify_new_book_signal_sends_email():
    author = Author.objects.create(name="Dan Brown")
    mail.outbox = []  # reset
    Book.objects.create(name="The Da Vinci Code", author=author)
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert "New Book Added" in email.subject
    assert "The Da Vinci Code" in email.body
    assert "Dan Brown" in email.body
