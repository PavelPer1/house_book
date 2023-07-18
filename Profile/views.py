from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from django.db.models import Q

from .settings import *

from .models import FavoritesUser
from Exchange.models import Books, Exchange
from Profile.forms import RegisterForm, CreateUserForm, ExchangeForm, FavoritesAdd


@login_required
def login_view(request):
    return render(request, 'profile1.html')


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create_profile')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def get_user_books(request):
    name_books = []
    for i in Books.objects.all():
        if str(i.user) == str(request.user.username):
            name_books += [i]
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
        avatar = request.POST.get('avatar')

        book = Books(name=name_books,
                     author=author_books,
                     genre=genre_books,
                     description=description_books,
                     status=status_books,
                     user_id=request.user.id,
                     avatar=avatar
                     )
        book.save()
        return redirect('my-books')

    return render(request, 'books/add_books.html')


class CreateProfile(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        # Associate the profile with the current user
        form.instance.user = self.request.user
        return super().form_valid(form)


def get_katalog(request):
    search_query = request.GET.get('search', '')

    if search_query:
        books = Books.objects.filter(Q(name__icontains=search_query) | Q(author__icontains=search_query) |
                                     Q(genre__icontains=search_query))
    else:
        books = Books.objects.all()

    books = [i for i in books if i.user != request.user]

    paginator = Paginator(books, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'katalog/katalog.html', {'page_obj': page_obj})


def get_favorites(request):
    books = []
    for i in FavoritesUser.objects.all():
        if str(i.user) == str(request.user.username):
            books += [i]
    context = {
        'name_books': books
    }
    return render(request, 'favorites.html', context)


def get_book(request, path):
    context = {
        'my_book': Books.objects.filter(user_id=request.user.id),
        'book': Books.objects.get(id=path)
    }
    if request.method == 'POST' and 'add_fav' in request.POST:
        try:
            favorite = FavoritesUser.objects.get(user=request.user, book_id=int(path))
            # Если объект уже существует, вы можете добавить соответствующую логику обработки здесь
            print('Object already exists')
        except FavoritesUser.DoesNotExist:
            favorite = FavoritesUser(user_id=request.user.id, book_id=int(path))
            favorite.save()
            return redirect('favorites')
            print('Object added to favorites')
    ex = Exchange(
        one_book_id=int(path),
        status=f'{request.user.id}'
    )
    ex.save()
    return render(request, 'books/book.html', context)


def get_ex(request):
    content = {
        'name_books': Books.objects.filter(user_id=request.user.id)
    }
    if request.method == "POST":
        for j in Books.objects.all():
            if str(j.id) in request.POST:
                book_id = j.id
        for i in Exchange.objects.all():
            try:
                if int(i.status) == request.user.id:
                    exchange_two = i.id
            except:
                pass
        exch = Exchange.objects.get(id=exchange_two)
        exch.status = 'В процессе'
        exch.save(update_fields=["status", "two_book"])
        exch1 = Exchange.objects.get(id=exchange_two)
        exch1.two_book_id = int(book_id)
        exch1.save(update_fields=["two_book"])
        for f in Exchange.objects.all():
            if f.status != 'В процессе':
                f.delete()
    return render(request, 'books/exchange_books.html', content)






