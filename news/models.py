from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime



# id, title, content, created_at, update_at, photo, is_published

class News(models.Model):
    objects = None
    title = models.CharField("title", max_length=150)
    content = models.TextField("text", blank=True)
    created_at = models.DateTimeField("data", auto_now_add=True)
    updated_at = models.DateTimeField("up_data", auto_now=True)
    photo = models.ImageField("photo", upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    # id = models.IntegerField("id", )

    def __str__(self):
        return self.title


