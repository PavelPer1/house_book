from django.contrib.auth.models import User
from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='media/', null=True)


class Exchange(models.Model):
    one_book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, related_name='exchange')
    two_book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, related_name='two_book')
    date = models.DateField()
    status = models.CharField(max_length=50)