from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Trip(models.Model):
    name = models.CharField(
        max_length=21,
    )

    description = models.TextField(
        max_length=51,
        blank=True,
        null=True,
    )

    start_date = models.DateField()

    end_date = models.DateField()

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    is_published = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='trips',
    )
