from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField()