# Generated by Django 3.2.8 on 2022-06-20 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_article_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleoftheweek',
            options={'verbose_name_plural': 'Article of the week'},
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 22, 4, 32, 631228)),
        ),
    ]