# Generated by Django 3.1 on 2020-08-12 06:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationAwarness',
            fields=[
                ('eduId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('picture', models.ImageField(blank=True, default='', null=True, upload_to='EducationAwarness/picture')),
                ('date_And_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_And_time'],
            },
        ),
        migrations.CreateModel(
            name='PublicHealth',
            fields=[
                ('healthId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_And_time', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, default='', null=True, upload_to='PublicHealth/picture')),
            ],
            options={
                'ordering': ['date_And_time'],
            },
        ),
        migrations.CreateModel(
            name='wildlife',
            fields=[
                ('disId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_And_time', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, default='', null=True, upload_to='wildlife/picture')),
            ],
            options={
                'ordering': ['date_And_time'],
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('workshopId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_And_time', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, default='', null=True, upload_to='Workshop/picture')),
            ],
            options={
                'ordering': ['date_And_time'],
            },
        ),
    ]
