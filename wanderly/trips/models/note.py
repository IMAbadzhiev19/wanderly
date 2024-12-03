from django.contrib.auth import get_user_model
from django.db import models

from wanderly.trips.choices import NoteCategoryChoices

UserModel = get_user_model()

class Note(models.Model):
    category = models.CharField(
        choices=NoteCategoryChoices,
    )

    content = models.TextField(
        max_length=71,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='notes',
    )

    trip = models.ForeignKey(
        to='trips.Trip',
        on_delete=models.CASCADE,
        related_name='notes',
        null=True,
        blank=True,
    )
