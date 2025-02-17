# Generated by Django 4.2.19 on 2025-02-17 10:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('hardware', models.CharField(max_length=25)),
                ('cover_art', models.ImageField(null=True, upload_to='covers')),
                ('recommended_age', models.IntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(18)])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50, null=True)),
                ('date', models.DateField()),
                ('logo', models.ImageField(null=True, upload_to='logos')),
                ('participants', models.JSONField(blank=True, default=list, null=True)),
                ('slug', models.SlugField(blank=True, default='')),
                ('description', models.TextField(max_length=400, null=True)),
                ('games', models.ManyToManyField(to='events.games')),
            ],
        ),
    ]
