# Generated by Django 5.0.4 on 2024-05-14 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='voter',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='voter',
        ),
    ]