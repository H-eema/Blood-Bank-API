import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.core.validators import RegexValidator


# user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


# custom user model with necessary fields
class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True)
    facility_name = models.CharField(
        unique=True,
        max_length=250,
    )
    phone_num1 = models.CharField(
        max_length=13,
        validators=[RegexValidator("^0093\d{9}")],
    )
    phone_num2 = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        validators=[RegexValidator("^0093\d{9}")],
    )
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # the manager to interact with the model
    objects = CustomUserManager()

    # which field is used for loging in
    USERNAME_FIELD = "username"

    # required fields when creating an instance
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
