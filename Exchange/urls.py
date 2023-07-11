from django.urls import path, include
from .views import *

urlpatterns = [
    path('exchange', get_exchange, name='exchange')
]