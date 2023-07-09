from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile', login_view, name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('my-books', get_user_books, name='my-books'),
    path('add-books', add_books, name='add-books'),
    path('login/', LoginUser.as_view(), name='login')
]
