# Generated by Django 4.2.17 on 2024-12-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('long_description', models.TextField(max_length=150)),
                ('photo', models.ImageField(upload_to='courses/images')),
            ],
        ),
    ]
