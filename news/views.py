from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import NewsForm
from .models import *


def index(request):  # любая функция должна принимать аргумент
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',

    }
    return render(request,
                  f'news/index.html', context)
    # news = News.objects.all()
    # res = '<h1>Список новостей</h1>'
    # for i in news:
    #     res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p></div>\n<hr>\n'
    # return HttpResponse(res)


def get_category(request, category_slug):
    # category = get_object_or_404(Category, slug=category_slug)
    category = Category.objects.get(slug=category_slug)
    news = News.objects.filter(category=category)

    context = {
        'news': news,
        'category': category
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_slug):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, slug=news_slug)
    context = {
        'news_item': news_item
    }
    return render(request, 'news/view_news.html', context)


def add_news(request):
    global form
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    context = {
        'form': form
    }
    return render(request, 'news/add_news.html', context)