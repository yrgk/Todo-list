# Generated by Django 4.2.4 on 2023-08-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('day_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
