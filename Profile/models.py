from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    class Meta:
    	# Используем параметры related_query_name, чтобы задать альтернативные имена для обратных связей с группами и правами пользователя
        # Здесь используем "custom_user_groups" и "custom_user_permissions" в качестве альтернативных имен
    	default_related_name = 'custom_users'
    	swappable = 'AUTH_USER_MODEL'
    	app_label = 'auth'


