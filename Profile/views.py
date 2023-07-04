from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@login_required
def login_view(request):
    return render(request, 'profile.html')
