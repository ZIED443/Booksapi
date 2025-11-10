import pytest
from django.core import mail
from apps.users.models import User

@pytest.mark.django_db
def test_send_welcome_email_signal():
    # Reset mail outbox to start fresh
    mail.outbox = []

    # Create a new user (triggers post_save signal)
    user = User.objects.create_user(
        email="alice@example.com",
        user_name="Alice",
        password="password123"
    )

    # Check that a welcome email was sent
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert email.subject == "Welcome to our platform"
    assert f"Hello {user.user_name}" in email.body
    assert email.to == [user.email]
