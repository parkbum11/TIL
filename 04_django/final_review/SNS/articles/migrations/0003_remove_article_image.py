# Generated by Django 2.2.6 on 2019-11-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]