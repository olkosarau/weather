# Generated by Django 3.2.6 on 2021-08-23 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_city_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='temp',
        ),
    ]
