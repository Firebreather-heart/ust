# Generated by Django 3.2.8 on 2022-06-16 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220616_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 20, 45, 25, 997497)),
        ),
        migrations.AlterField(
            model_name='article',
            name='imgIllustration',
            field=models.FileField(default='media/logo.jpg', upload_to='media/'),
        ),
    ]
