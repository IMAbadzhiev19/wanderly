from django import forms
from django.forms.models import ModelForm

from wanderly.trips.models import Trip, Note, Expense


class CreateTripForm(ModelForm):
    class Meta:
        model = Trip
        exclude = ('user', )

        labels = {
            'is_published': 'Public',
        }

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 2,
                    'style': 'resize: none;',
                }
            ),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TripEditForm(ModelForm):
    class Meta:
        model = Trip
        exclude = ('user', )

        labels = {
            'is_published': 'Public',
        }

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 2,
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


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ('user', 'trip', )

        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
            })
        }


class ExpenseCreateForm(ModelForm):
    class Meta:
        model = Expense
        exclude = ('trip', )
