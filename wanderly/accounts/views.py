from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from wanderly.accounts.forms import AppUserCreationForm

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    model=UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')


class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'
