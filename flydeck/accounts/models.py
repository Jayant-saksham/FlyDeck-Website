from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class StudentProfile(models.Model):
    """
    Model to store additional profile information for students.

    This model extends the custom user model to include fields like profile image,
    biography, phone number, and birth year.

    Attributes:
        user (CustomUser): The user associated with this profile.
        image (ImageField): Profile image of the student.
        bio (TextField): Short biography of the student.
        phone_number (CharField): Contact phone number of the student.
        birth_year (PositiveIntegerField): Birth year of the student.
    """
    BIRTH_YEAR_CHOICES = [(year, year) for year in range(1920, 2023)]  # Example range
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    birth_year = models.PositiveIntegerField(choices=BIRTH_YEAR_CHOICES, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.email)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.user.email
