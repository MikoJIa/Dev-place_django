from django.shortcuts import render
from django.http import HttpResponse


def index(request): # любая функция должна принимать аргумент
    return HttpResponse('Hello world')


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')



