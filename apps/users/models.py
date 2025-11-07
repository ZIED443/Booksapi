from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None, role="client", **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, role=role, **extra_fields)
        user.set_password(password)
        user.full_clean() 
        user.save()
        return user

    def create_superuser(self, email, user_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, user_name, password, role="admin", **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("client", "Client"),
        ("worker", "Worker"),
        ("admin", "Admin"),
    )

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="client")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    def clean(self):
        if self.role not in dict(self.ROLE_CHOICES):
            raise ValidationError({"role": "Invalid role"})
        super().clean()

    def __str__(self):
        return f"{self.user_name} ({self.email})"
