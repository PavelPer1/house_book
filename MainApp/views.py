from django.shortcuts import render


def get_main(request):
    return render(request, 'index.html')

def get_who(request):
    return render(request, 'who.html')


def get_dliakogo(request):
    return render(request, 'dliakogo.html')


def get_help(request):
    return render(request, 'help.html')

