from blog.models import Post
from django.utils.text import slugify

ps = Post.objects.all()

for p in ps:
     