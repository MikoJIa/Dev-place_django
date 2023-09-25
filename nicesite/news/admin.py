from django.contrib import admin
from news.models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Mets:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id',
                    'title',
                    'category',
                    'slug',
                    'get_photo',
                    'created_at',
                    'updated_at',
                    'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title', )}
    fields = ('title', 'category',
              'content',
              'photo', 'get_photo',
              'is_published', 'created_at',
              'updated_at', 'slug',)
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=75>')
        else:
            return 'Нет фото'

    get_photo.short_description = 'Изображение'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'