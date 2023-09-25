from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<slug:category_slug>/', NewsByCategory.as_view(), name='category'),
    path('news/<slug:news_slug>/', ViewNews.as_view(), name='view_news'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
    path('test/', test, name='test'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact-form/', send_email_contact_form, name='contact_form')
]