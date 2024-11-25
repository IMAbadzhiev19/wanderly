from django.urls import path

from wanderly.common.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]