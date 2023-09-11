from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<slug:category_slug>/', get_category, name='category'),
    path('news/<slug:news_slug>/', view_news, name='view_news'),
    path('add-news/', add_news, name='add_news'),
]