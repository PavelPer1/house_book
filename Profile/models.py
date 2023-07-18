from django.contrib.auth.models import User
from django.db import models
from Exchange.models import Books


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='media/')
    email = models.EmailField(max_length=250)
    number = models.CharField(max_length=50)
    fio = models.CharField(max_length=100, null=True)


class FavoritesUser(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

