from django.db import models


class Submitted(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.name}: {self.subject}"
