# Generated by Django 4.2.16 on 2024-11-15 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
    ]