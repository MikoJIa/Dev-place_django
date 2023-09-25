from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


def send_email_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],
                             form.cleaned_data['content'],
                             'popovn022@gmail.com',
                             ['kolya_popov_86@tut.by'],
                             fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('contact_form')
            else:
                messages.error(request, 'Ошибка отправки')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'news/page_contact_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'news/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'news/login.html', context)


def test(request):
    object = ['miwa1',
              'vasya2', 'petya3', 'miwa4',
              'vasya5', 'petya6', 'miwa7']

    paginator = Paginator(object, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {
        'page_obj': page_objects
    }
    return render(request, 'news/test.html', context)


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')

        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


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


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    #  allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        return News.objects.filter(category=category, is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(slug=self.kwargs['category_slug']))
        return context

# def get_category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     # category = Category.objects.get(slug=category_slug)
#     news = News.objects.filter(category=category)
#
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, 'news/category.html', context)


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'
    slug_url_kwarg = 'news_slug'


# def view_news(request, news_slug):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, slug=news_slug)
#     context = {
#         'news_item': news_item
#     }
#     return render(request, 'news/view_news.html', context)


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #  success_url = reverse_lazy('home')
    #login_url = 'home'
    raise_exception = True


#
# def add_news(request):
#     global form
#     if request.method == 'POST':
#         form = NewsForm(request.POST)  # если у нас запрос POST
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #news = News.objects.create(**form.cleaned_data)  # мы передаём в нашу базу данных распакованные данные
#             news = form.save()
#             return redirect(news) #  после создания новости переносит нас на страницу наше новости
#     else:
#         form = NewsForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'news/add_news.html', context)


def pageNotFound404(request, exception):
    return render(request, 'page404.html', status=404)
