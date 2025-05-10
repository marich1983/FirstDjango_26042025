from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.exceptions import ObjectDoesNotExist

AUTHOR = {
    'Имя': 'Иван',
    'Отчество': 'Петрович',
    'Фамилия': 'Иванов',
    'телефон': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
    }
   

def home(request):
    context = {
        "name": "Иванов Иван Иванович",
        "email": "example@mail.ru"
    }
    return render(request, "index.html",context)

def about(request):
    context = {
        'author': AUTHOR
    }
    return render(request, 'about.html', context)

def items(request):
    
    context = {
        'items': models.Item.objects.all()
    }
    
    return render(request, 'items.html', context)

def item_info(request, item_id: int):
    try:
        item = models.Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, 'errors.html', {'error': f'Товар с id {item_id} не найден'})
    else:
        context = {
            "item": item
            }
        return render(request, "item.html", context)
    






