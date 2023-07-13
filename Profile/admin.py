from django.contrib import admin

from Profile.models import Profile, FavoritesUser

admin.site.register(Profile)
admin.site.register(FavoritesUser)
