from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView

from wanderly.trips.forms import CreateTripForm, SearchForm
from wanderly.trips.models import Trip


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = CreateTripForm
    success_url = reverse_lazy('all-trips')
    template_name = 'trips/create-trip.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TripsView(LoginRequiredMixin, ListView, FormView):
    model = Trip
    form_class = SearchForm
    paginate_by = 3
    success_url = reverse_lazy('all-trips')
    context_object_name = 'trips'
    template_name = 'trips/trip-list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(
            user=self.request.user,
        )

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(
                name__icontains=query,
            )

        return queryset



