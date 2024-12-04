from django.db import models

from wanderly.trips.models import Trip


class Itinerary(models.Model):
    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    trip = models.ForeignKey(
        to=Trip,
        on_delete=models.CASCADE,
        related_name='itineraries',
    )
