from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView, DeleteView, UpdateView

from wanderly.trips.forms import CreateTripForm, SearchForm, TripEditForm, CreateNoteForm, ExpenseCreateForm, \
    ItineraryCreateForm
from wanderly.trips.models import Trip, Note, Expense, Itinerary


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
        context['is_owner'] = self.request.user == trip.user

        return context


class TripEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Trip
    template_name = 'trips/edit-trip.html'
    form_class = TripEditForm

    def get_success_url(self):
        return reverse_lazy(
            'trip-details',
            kwargs={'pk': self.kwargs['pk']}
        )

    def test_func(self):
        trip = Trip.objects.get(pk=self.kwargs['pk'])
        return self.request.user == trip.user


class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy('all-trips')

    def test_func(self):
        trip = Trip.objects.get(pk=self.kwargs['pk'])
        return self.request.user == trip.user


class NoteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Note
    form_class = CreateNoteForm
    template_name = 'trips/create-note.html'

    def get_success_url(self):
        return reverse_lazy(
            'trip-details',
            kwargs={'pk': self.kwargs['pk']},
        )

    def form_valid(self, form):
        trip = Trip.objects.get(pk=self.kwargs['pk'])

        form.instance.user = self.request.user
        form.instance.trip = trip

        return super().form_valid(form)

    def test_func(self):
        trip = Trip.objects.get(pk=self.kwargs['pk'])
        return self.request.user == trip.user


class ExpenseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Expense
    form_class = ExpenseCreateForm
    template_name = 'trips/create-expense.html'

    def get_success_url(self):
        return reverse_lazy(
            'trip-details',
            kwargs={'pk': self.kwargs['pk']},
        )

    def form_valid(self, form):
        trip = Trip.objects.get(pk=self.kwargs['pk'])

        form.instance.trip = trip

        return super().form_valid(form)

    def test_func(self):
        trip = Trip.objects.get(pk=self.kwargs['pk'])
        return self.request.user == trip.user


class ItineraryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Itinerary
    form_class = ItineraryCreateForm
    template_name = 'trips/create-itinerary.html'

    def get_success_url(self):
        return reverse_lazy(
            'trip-details',
            kwargs={'pk': self.kwargs['pk']},
        )

    def form_valid(self, form):
        trip = Trip.objects.get(pk=self.kwargs['pk'])

        form.instance.trip = trip

        return super().form_valid(form)

    def test_func(self):
        trip = Trip.objects.get(pk=self.kwargs['pk'])
        return self.request.user == trip.user


class ItineraryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Itinerary

    def get_success_url(self):
        return reverse_lazy(
            'trip-details',
            kwargs={'pk': self.kwargs['pk']},
        )

    def test_func(self):
        trip = Trip.objects.get(pk=self.kwargs['pk'])
        return self.request.user == trip.user
