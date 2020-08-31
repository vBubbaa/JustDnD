from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True, max_length=200)
