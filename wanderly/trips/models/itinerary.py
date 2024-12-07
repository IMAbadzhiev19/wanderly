from django.db import models


class Itinerary(models.Model):
    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    trip = models.ForeignKey(
        to='trips.Trip',
        on_delete=models.CASCADE,
        related_name='itineraries',
    )
