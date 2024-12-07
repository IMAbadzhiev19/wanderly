import random

from django.views.generic import TemplateView

from wanderly.trips.models import Trip


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trips = Trip.objects.filter(is_published=True)

        if self.request.user.is_authenticated:
            trips = trips.exclude(user=self.request.user)

        context['random_trip'] = random.choice(trips) if trips.exists() else None

        return context
