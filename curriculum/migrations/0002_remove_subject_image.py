# Generated by Django 3.2.6 on 2021-08-07 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='image',
        ),
    ]
