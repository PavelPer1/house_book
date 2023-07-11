from django.shortcuts import render


def get_main(request):
    return render(request, 'index.html')
    
def go_who(request):
    return render(request, 'who.html')

def go_help(request):
    return render(request, 'help.html')

def go_whom(request):
    return render(request, 'dliakogo.html')
