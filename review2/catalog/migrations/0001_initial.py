# Generated by Django 4.2.20 on 2025-03-07 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField(blank=True)),
                ('picture', models.ImageField(upload_to='products')),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
        ),
    ]
