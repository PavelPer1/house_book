from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='media/')
    email = models.EmailField(max_length=250)
    number = models.CharField(max_length=50)

