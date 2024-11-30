from django.db import models

from wanderly.trips.choices import CategoryChoices


class Expense(models.Model):
    category = models.CharField(
        choices=CategoryChoices,
    )

    description = models.TextField(
        max_length=51,
        blank=True,
        null=True,
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    trip = models.ForeignKey(
        to='trips.Trip',
        on_delete=models.CASCADE,
        related_name='expenses',
    )
