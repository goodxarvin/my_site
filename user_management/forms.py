from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class GenderSignUpForm(SignupForm):
    gender_choices = [
        ("m", 'male'),
        ("f", "female")
    ]
    gender = forms.ChoiceField(choices=gender_choices, label='gender')

    def save(self, request):
        user = super().save(request)
        user.gender = self.cleaned_data["gender"]
        user.save()
        return user
