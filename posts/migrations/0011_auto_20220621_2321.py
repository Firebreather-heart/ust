# Generated by Django 3.2.8 on 2022-06-21 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20220621_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleprime',
            name='imgIllustration',
            field=models.FileField(default='media/logo.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 23, 21, 21, 727598)),
        ),
        migrations.AlterField(
            model_name='articleprime',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 23, 21, 21, 728597)),
        ),
    ]
