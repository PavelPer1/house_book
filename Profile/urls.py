from django.conf.urls.static import static
from django.urls import path, include

from House_books import settings
from .views import *

urlpatterns = [
    path('profile', login_view, name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('my-books', get_user_books, name='my-books'),
    path('add-books', add_books, name='add-books'),
    path('login/', LoginUser.as_view(), name='login'),
    path('create_profile', CreateProfile.as_view(), name='create_profile'),
    path('katalog/', get_katalog, name='katalog'),
    path('favorites', get_favorites, name='favorites'),
    path('book/<path>', get_book, name='book')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
