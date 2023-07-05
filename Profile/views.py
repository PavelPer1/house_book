from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from Profile.forms import RegisterForm


@login_required
def login_view(request):
    return render(request, 'profile.html')


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
