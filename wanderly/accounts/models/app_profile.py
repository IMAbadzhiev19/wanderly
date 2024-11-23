from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    image = CloudinaryField(
        'image',
        default='https://res.cloudinary.com/dfgp2jwi3/image/upload/v1732391607/default-profile-img.jpg',
        null=True,
        blank=True,
    )
