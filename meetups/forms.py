from django import forms
from .models import Participant


class MeetupRegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['firstName', 'lastName', 'email']
