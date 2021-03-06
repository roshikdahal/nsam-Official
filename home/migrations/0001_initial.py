# Generated by Django 3.1 on 2020-08-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('Heading', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='home/image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
