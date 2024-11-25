from django.urls import path

from wanderly.accounts.views import AppUserRegisterView

urlpatterns = [
    path('register/', AppUserRegisterView.as_view() , name='register'),
]