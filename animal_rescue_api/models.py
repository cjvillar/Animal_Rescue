from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.

class Animal(models.Model):
    DOG = 'Dog'
    CAT = 'Cat'
    BEAR = 'Bear'
    RODENT = 'Rodent'
    AVAILABLE = 'AVAILABLE'
    ADOPTED = 'ADOPTED'

    ANIMAL_TYPE_CHOICES = [
        (DOG,'Dog'),
        (CAT,'Cat'),
        (BEAR,'Bear'),
        (RODENT,'Rodent'),
    ]

    ADOPTION_STATUS_CHOICES =[
        (AVAILABLE,'AVAILABLE'),
        (ADOPTED,'ADOPTED'),

    ]

    animal_type = models.CharField(
        max_length=10,
        choices=ANIMAL_TYPE_CHOICES,
        default=DOG,
    )
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    neutred = models.BooleanField(default=False)
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
    image = models.ImageField(upload_to='profile_images', default=None)




