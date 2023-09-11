from django.db import models
from django.urls import reverse
from unidecode import unidecode
from django.utils.text import slugify

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

    def save(self, *args, **kwargs):
        if not self.slug:
            # Используем unidecode для преобразования русского текста в ASCII
            ascii_title = unidecode(self.title)
            self.slug = slugify(ascii_title)
        super().save(*args, **kwargs)


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

