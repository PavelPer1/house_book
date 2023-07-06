from django.urls import path, include
from .views import login_view, RegisterView, get_user_books

urlpatterns = [
    path('profile', login_view, name='profile'),
    path('register', RegisterView.as_view(), name='register'),
    path('my-books', get_user_books, name='my-books')
]
