from django.db import models

from wanderly.trips.choices import ActivityChoices


class Activity(models.Model):
    name = models.CharField(
        max_length=21,
    )

    description = models.TextField(
        max_length=51,
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    location = models.CharField(
        max_length=51,
        blank=True,
        null=True,
    )

    category = models.CharField(
        choices=ActivityChoices
    )

    itinerary = models.ForeignKey(
        to='trips.Itinerary',
        on_delete=models.CASCADE,
        related_name='activities',
    )
