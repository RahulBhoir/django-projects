from django.db import models
from django.contrib.auth.models import User


class PasswordSafe(models.Model):
    site_name = models.TextField()
    username = models.TextField()
    password = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
