from django.shortcuts import render
from django.http import HttpResponse

AUTHOR = {
    'Имя': 'Иван',
    'Отчество': 'Петрович',
    'Фамилия': 'Иванов',
    'телефон': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
    }

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
    # text = """
    # <a href = "/">Домой</a>
    # <br>
    # <h1>Список товаров</h1><br>
    # """
    # for item in lst_items:
    #     text += f"<p><b>{item['id']}</b> <a href = '/items/item/{item['id']}'>{item['name']}</a></p>"
    # return HttpResponse(text)
    
    return render(request, 'items.html')

def item_info(request, item_id: int):
    lst_items = [
   {"id": 1, "name": "Кроссовки adidas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]
    
    # context = {
    #     'item': lst_items
    # }


    # flag = 0
    for item in lst_items:
        if item_id == item['id']:
            context = item
    #         <a href = "/items/">Назад к списку товаров</a>
    #         <br>
    #         <br>
    #         <table bordercolor='black' align='center' rules='all'>
    #             <tr>
    #                 <td><i>Наименование</i>:</td> 
    #                 <td>{item['name']}</td>
    #             </tr>
    #             </tr>
    #                 <td><i>Количество</i>:</td>
    #                 <td> {item['quantity']}</td>
    #             </tr>
    #         </table>
    #         """
    #     else:
    #         flag += 1

    # if flag == len(lst_items):
    #     text = f"""
    #     <h2>Товар с id={item_id} не найден</h2>"""

    return render(request, "item.html", context)





