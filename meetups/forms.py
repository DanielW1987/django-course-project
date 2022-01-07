from django import forms


# class MeetupRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['firstName', 'lastName', 'email']

class MeetupRegistrationForm(forms.Form):
    firstName = forms.CharField(max_length=50, min_length=3, label='Your first name')
    lastName = forms.CharField(max_length=50, label='Your last name')
    email = forms.EmailField(label='Your email')
