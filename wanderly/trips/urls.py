from django.urls import path

from wanderly.trips.views import TripsView, TripCreateView

urlpatterns = [
    path('', TripsView.as_view(), name='all-trips'),
    path('add/', TripCreateView.as_view(), name='trip-create'),
]