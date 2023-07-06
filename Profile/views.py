from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render
from reportlab.lib.randomtext import objects

from Exchange.models import Books
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


def get_user_books(request):
    name_books = []
    for i in Books.objects.all():
        name_books += [i.name]
    content = {
        'name_books': name_books
    }
    return render(request, 'user_books.html', content)