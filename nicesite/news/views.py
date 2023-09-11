from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .forms import NewsForm
from .models import *
from django.views.generic import ListView


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

# def index(request):  # любая функция должна принимать аргумент
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#
#     }
#     return render(request,
#                   f'news/index.html', context)
    # news = News.objects.all()
    # res = '<h1>Список новостей</h1>'
    # for i in news:
    #     res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p></div>\n<hr>\n'
    # return HttpResponse(res)


def get_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    # category = Category.objects.get(slug=category_slug)
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
        form = NewsForm(request.POST)  # еслт у нас запрос POST
        if form.is_valid():
            #print(form.cleaned_data)
            #news = News.objects.create(**form.cleaned_data)  # мы передаём в нашу базу данных распакованные данные
            news = form.save()
            return redirect(news) #  после создания новости переносит нас на страницу наше новости
    else:
        form = NewsForm()
    context = {
        'form': form
    }
    return render(request, 'news/add_news.html', context)


def pageNotFound404(request, exception):
    return render(request, 'page404.html', status=404)
