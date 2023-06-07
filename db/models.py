from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    pwd = models.CharField(max_length = 50)


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length = 500)
    # likes = models.IntegerField()