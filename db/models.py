from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    # likes = models.IntegerField()