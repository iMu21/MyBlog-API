# Generated by Django 3.2.7 on 2021-11-13 03:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0005_auto_20211113_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]