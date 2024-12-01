from django import forms
from django.forms.models import ModelForm

from wanderly.trips.models import Trip


class CreateTripForm(ModelForm):
    class Meta:
        model = Trip
        exclude = ('user', )

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 1,
                    'style': 'resize: none;',
                }
            ),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }




class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=21,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...',
            }
        )
    )
