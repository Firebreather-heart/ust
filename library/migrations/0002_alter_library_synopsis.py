# Generated by Django 3.2.8 on 2022-06-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='synopsis',
            field=models.CharField(blank=True, default='unavailable', max_length=1000, null=True),
        ),
    ]