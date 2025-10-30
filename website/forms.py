from django import forms
from contact.models import Submitted


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea())


class SubmitForm(forms.ModelForm):
    # last_name = forms.CharField(max_length=255)

    class Meta:
        model = Submitted
        fields = "__all__"
        # fields = ["name", "subject"]
        # exclude = ["email"]
