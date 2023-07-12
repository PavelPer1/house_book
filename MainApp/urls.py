from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_main, name='index'),
    path('who/', get_who, name='who'),
    path('dliakogo/', get_dliakogo, name='dliakogo'),
    path('help/', get_help, name='help')
]

