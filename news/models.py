from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime
from django.urls import reverse



# id, title, content, created_at, update_at, photo, is_published

class News(models.Model):
    objects = None
    title = models.CharField(verbose_name="title", max_length=150)
    content = models.TextField(verbose_name="text", blank=True)
    created_at = models.DateTimeField(verbose_name="data", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="up_data", auto_now=True)
    photo = models.ImageField(verbose_name="photo", upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(verbose_name="published", default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')
    slug = models.SlugField(max_length=155, unique=True, db_index=True, verbose_name='URL', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='имя котегории')
    slug = models.SlugField(max_length=155, unique=True, db_index=True,
                            verbose_name='URL', null=True)

    class Mate:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
