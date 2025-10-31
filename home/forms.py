from django.forms import ModelForm
from home.models import NewsLetter


class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"


