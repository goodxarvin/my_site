from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class GenderSignUpForm(forms.Form):
    GENDER_CHOICES = (
        ("", "select gender"),
        ("M", 'male'),
        ("F", "female")
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, required=False, label="Gender")

    def signup(self, request, user):
        gender = self.cleaned_data.get('gender')
        if gender:
            user.gender = gender
            user.save()
        return user
