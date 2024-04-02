from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()

    def __str__(self):
        return self.username



class Animal(models.Model):
    DOG = "Dog"
    CAT = "Cat"
    BEAR = "Bear"
    RODENT = "Rodent"
    AVAILABLE = "AVAILABLE"
    ADOPTED = "ADOPTED"

    ANIMAL_TYPE_CHOICES = [
        (DOG, "Dog"),
        (CAT, "Cat"),
        (BEAR, "Bear"),
        (RODENT, "Rodent"),
    ]

    ADOPTION_STATUS_CHOICES = [
        (AVAILABLE, "AVAILABLE"),
        (ADOPTED, "ADOPTED"),
    ]

    animal_type = models.CharField(
        max_length=10,
        choices=ANIMAL_TYPE_CHOICES,
        default=DOG,
    )
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    neutered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    weight = models.CharField(max_length=20)
    adoption_status = models.CharField(
        max_length=10,
        choices=ADOPTION_STATUS_CHOICES,
        default=AVAILABLE,
    )
    temperament = models.CharField(max_length=100)
    likes = models.CharField(max_length=100)
    fee = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_images", default=None)
