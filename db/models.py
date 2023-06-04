from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    pwd = models.CharField(max_length = 50)