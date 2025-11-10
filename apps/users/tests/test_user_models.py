import pytest
from django.core.exceptions import ValidationError
from apps.users.models import User

@pytest.mark.django_db
def test_create_user():
    # Create a regular user
    user = User.objects.create_user(
        email="alice@example.com",
        user_name="Alice",
        password="password123",
        role="client"
    )

    # Check that the user was saved successfully
    assert user.pk is not None  # ID is assigned
    assert user.email == "alice@example.com"
    assert user.user_name == "Alice"
    assert user.role == "client"
    assert user.is_active is True
    assert user.is_staff is False

    # Check that the password is hashed and valid
    assert user.check_password("password123")


@pytest.mark.django_db
def test_create_superuser():
    # Create a superuser
    superuser = User.objects.create_superuser(
        email="admin@example.com",
        user_name="Admin",
        password="adminpass"
    )

    # Check fields
    assert superuser.pk is not None
    assert superuser.email == "admin@example.com"
    assert superuser.user_name == "Admin"
    assert superuser.role == "admin"
    assert superuser.is_staff is True
    assert superuser.is_superuser is True
    assert superuser.is_active is True
    assert superuser.check_password("adminpass")


@pytest.mark.django_db
def test_user_role_validation():
    # Creating user with invalid role should raise ValidationError
    with pytest.raises(ValidationError):
        User.objects.create_user(
            email="bob@example.com",
            user_name="Bob",
            password="password123",
            role="invalid_role"
        )
