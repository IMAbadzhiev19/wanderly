from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView, DeleteView

from wanderly.trips.forms import CreateTripForm, SearchForm
from wanderly.trips.models import Trip, Itinerary, Note, Expense


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


class TripDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'trips/details.html'
    model = Trip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        trip = self.object
        itineraries = Itinerary.objects.filter(trip=trip)
        notes = Note.objects.filter(trip=trip)

        context['itineraries'] = itineraries
        context['notes'] = notes
        context['expenses'] = Expense.objects.filter(trip=trip)

        # Handle pagination for itineraries
        itineraries_paginator = Paginator(itineraries, 3)
        itineraries_page_number = self.request.GET.get('itinerary_page')
        itineraries_page_obj = itineraries_paginator.get_page(itineraries_page_number)

        # Handle pagination for notes
        notes_paginator = Paginator(notes, 1)
        notes_page_number = self.request.GET.get('notes_page')
        notes_page_obj = notes_paginator.get_page(notes_page_number)

        context['itineraries_page_obj'] = itineraries_page_obj
        context['notes_page_obj'] = notes_page_obj

        return context


class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy('all-trips')

    def test_func(self):
        trip = Trip.objects.get(pk=self.kwargs['pk'])
        return self.request.user == trip.user

