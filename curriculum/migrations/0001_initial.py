# Generated by Django 3.2.5 on 2021-07-11 17:36

import curriculum.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_Id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=curriculum.models.renameImagesFiles, verbose_name='Subject image')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='curriculum.standard')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Chapter n.')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=curriculum.models.renameImagesFiles, verbose_name='Video')),
                ('ppt', models.FileField(blank=True, null=True, upload_to=curriculum.models.renameImagesFiles, verbose_name='Presentation')),
                ('notes', models.FileField(blank=True, null=True, upload_to=curriculum.models.renameImagesFiles, verbose_name='Notes')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='curriculum.subject')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]