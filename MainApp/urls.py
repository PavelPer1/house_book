from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_main, name='index'),
    
    path('whome', go_who, name='who'),

    path('help', go_help, name='helpme'),

    path('whom', go_whom, name='whomme'),
]
