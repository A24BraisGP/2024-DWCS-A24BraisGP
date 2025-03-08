# Generated by Django 4.2.19 on 2025-03-06 12:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=350)),
                ('number_of_years', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=150)),
                ('picture', models.ImageField(upload_to='alumni')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('year_of_birth', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2010)])),
                ('finished_degree', models.BooleanField(default=False)),
                ('degree', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.degree')),
            ],
        ),
    ]
