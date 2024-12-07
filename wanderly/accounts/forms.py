from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from wanderly.accounts.models import Profile
from wanderly.mixins import PlaceholderMixin

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', )


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = "__all__"


class ProfileEditForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(),
        }

    def save(self, commit=True):
        instance = super().save(commit=commit)

        profile = Profile.objects.get(pk=instance.pk)

        profile.image = f"https://res.cloudinary.com/dfgp2jwi3/image/upload/v1732391607/{instance.image}.png"
        profile.save()

        return instance
