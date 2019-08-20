from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)