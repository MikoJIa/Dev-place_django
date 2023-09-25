from django import forms
from news.models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст письма',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(label='Пароль',
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердить пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form_control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r"\b[A-Za-z]", title):
            raise ValidationError('числа не допустимы')
        return title



# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label=' Название новости',
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Контекст новости', required=False,
#                               widget=forms.Textarea(attrs={'class': 'form-control', 'row': 5}))
#     is_published = forms.BooleanField(label='Публиковать?', initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория', empty_label='Выберите категорию',
#                                       widget=forms.Select(attrs={'class': 'form-select'}))

