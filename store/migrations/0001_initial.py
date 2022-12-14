# Generated by Django 4.1.1 on 2022-09-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('quantity', models.SmallIntegerField()),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
