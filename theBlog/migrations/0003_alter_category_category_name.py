# Generated by Django 3.2.7 on 2021-10-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
