# Generated by Django 5.0.2 on 2025-01-13 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
