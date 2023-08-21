from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):  # любая функция должна принимать аргумент
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request,
                  f'news/index.html', context)
    # news = News.objects.all()
    # res = '<h1>Список новостей</h1>'
    # for i in news:
    #     res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p></div>\n<hr>\n'
    # return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
