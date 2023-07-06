from django.shortcuts import render


def get_main(request):
    return render(request, 'index.html')
