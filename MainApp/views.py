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
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    <br>
    <href>About</href>

    """
    return HttpResponse(text)

def about(request):
    text = ''
    for k, v in AUTHOR.items():
        text += f'<i>{k}: {v}</i><br>'
    return HttpResponse(text)

