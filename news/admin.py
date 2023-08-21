from django.contrib import admin
from news.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'category',
                    'slug',
                    'created_at',
                    'updated_at',
                    'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)