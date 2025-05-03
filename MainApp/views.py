from django.shortcuts import render
from django.http import HttpResponse

AUTHOR = {
    'Имя': 'Иван',
    'Отчество': 'Петрович',
    'Фамилия': 'Иванов',
    'телефон': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
    }

lst_items = [
   {"id": 1, "name": "Кроссовки adidas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]
   

def home(request):
    context = {
        "name": "Иванов Иван Ивынович",
        "email": "example@mail.ru"
    }
    return render(request, "index.html",context)

def about(request):
    text = """
    <a href = "/">Домой</a>
    <br>
    <h1>Информация</h1>
    <br>
    """
    for k, v in AUTHOR.items():
        text += f'{k}: <b>{v}</b><br>'
    return HttpResponse(text)


def items(request):
    
    context = {
        'items': lst_items
    }
    
    return render(request, 'items.html', context)

def item_info(request, item_id: int):

    for item in lst_items:
        if item_id == item['id']:
            context = item


    return render(request, "item.html", context)





