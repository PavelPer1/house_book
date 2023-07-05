from django.urls import path, include
from .views import login_view, RegisterView

urlpatterns = [
    path('profile', login_view, name='profile'),
    path('register', RegisterView.as_view(), name='register')
]
