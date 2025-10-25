from django.db import models


class Submitted(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=60)
    email = models.EmailField()
    messsage = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
