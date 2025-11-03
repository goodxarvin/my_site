from django.forms import ModelForm
from blog.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "subject", "comment_content"]
