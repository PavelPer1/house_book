from django.shortcuts import render

from Exchange.models import Exchange


def get_exchange(request):
    for f in Exchange.objects.all():
        if f.status != 'В процессе':
            f.delete()
    exchange = []
    for i in Exchange.objects.all():
        if i.one_book.user_id == request.user.id or i.two_book.user_id == request.user.id:
            exchange += [i]
    context = {
        'exchange': exchange
    }
    return render(request, 'exchange.html', context)
