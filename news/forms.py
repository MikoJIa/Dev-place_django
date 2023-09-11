from django import forms
from news.models import Category, News
import re
from django.core.exceptions import ValidationError


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

