from django.urls import path, include

from wanderly.trips.views import TripsView, TripCreateView, TripDetailsView, TripDeleteView, TripEditView, \
    NoteCreateView, ExpenseCreateView

urlpatterns = [
    path('', TripsView.as_view(), name='all-trips'),
    path('add/', TripCreateView.as_view(), name='trip-create'),
    path('<int:pk>/', include([
        path('', TripDetailsView.as_view(), name='trip-details'),
        path('delete/', TripDeleteView.as_view(), name='trip-delete'),
        path('edit/', TripEditView.as_view(), name='trip-edit'),
        path('add-note/', NoteCreateView.as_view(), name='note-create'),
        path('add-expense/', ExpenseCreateView.as_view(), name='expense-create'),
    ])),
]