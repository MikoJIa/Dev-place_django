# Generated by Django 4.2.4 on 2023-08-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ["id"],
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
        migrations.AlterField(
            model_name="news",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="published"),
        ),
        migrations.AlterField(
            model_name="news",
            name="photo",
            field=models.ImageField(
                blank=True, upload_to="photos/%Y/%m/%d", verbose_name="photo"
            ),
        ),
    ]
