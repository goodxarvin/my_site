from django.forms import ModelForm
from contact.models import Submitted
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Submitted
        fields = "__all__"
