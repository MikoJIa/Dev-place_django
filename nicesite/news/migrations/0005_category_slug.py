# Generated by Django 4.2.4 on 2023-09-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_news_slug_alter_news_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                max_length=155, null=True, unique=True, verbose_name="URL"
            ),
        ),
    ]
