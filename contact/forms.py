from django.forms import ModelForm
from contact.models import Submitted


class ContactForm(ModelForm):

    class Meta:
        model = Submitted
        fields = "__all__"
