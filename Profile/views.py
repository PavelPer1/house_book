from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render
from .settings import *
from reportlab.lib.randomtext import objects

from Exchange.models import Books
from Profile.forms import RegisterForm


@login_required
def login_view(request):
    return render(request, 'profile.html')


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def get_user_books(request):
    name_books = []
    for i in Books.objects.all():
        print(i.user, request.user.username)
        if str(i.user) == str(request.user.username):
            name_books += [i.name]
    content = {
        'name_books': name_books
    }
    return render(request, 'books/user_books.html', content)


def add_books(request):
    if request.method == "POST":
        name_books = request.POST.get('name')
        author_books = request.POST.get('author')
        genre_books = request.POST.get('genre')
        description_books = request.POST.get('description')
        status_books = True

        book = Books(name=name_books,
                     author=author_books,
                     genre=genre_books,
                     description=description_books,
                     status=status_books,
                     )
        book.save()
    return render(request, 'books/add_books.html')