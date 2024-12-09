from django.urls import path, include

from wanderly.trips.views import TripsView, TripCreateView, TripDetailsView, TripDeleteView, TripEditView, \
    NoteCreateView, ExpenseCreateView, ItineraryCreateView, ItineraryDeleteView, ItineraryDetailsView, \
    ActivityCreateView

urlpatterns = [
    path('', TripsView.as_view(), name='all-trips'),
    path('add/', TripCreateView.as_view(), name='trip-create'),
    path('<int:pk>/', include([
        path('', TripDetailsView.as_view(), name='trip-details'),
        path('delete/', TripDeleteView.as_view(), name='trip-delete'),
        path('edit/', TripEditView.as_view(), name='trip-edit'),
        path('add-note/', NoteCreateView.as_view(), name='note-create'),
        path('add-expense/', ExpenseCreateView.as_view(), name='expense-create'),
        path('create-itinerary/', ItineraryCreateView.as_view(), name='itinerary-create'),
        path('delete-itinerary/<int:i_id>/', ItineraryDeleteView.as_view(), name='itinerary-delete'),
        path('itinerary-details/<int:i_id>/', include([
            path('', ItineraryDetailsView.as_view(), name='itinerary-details'),
            path('create-activity', ActivityCreateView.as_view(), name='create-activity'),
        ])),
    ])),
]