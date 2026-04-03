from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128) 