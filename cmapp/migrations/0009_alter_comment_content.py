# Generated by Django 5.0.4 on 2024-05-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmapp', '0008_comment_delete_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]
