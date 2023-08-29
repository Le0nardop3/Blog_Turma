# Generated by Django 4.2.2 on 2023-08-01 19:00

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Publicado em')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
        ),
    ]
