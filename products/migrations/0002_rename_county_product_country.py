# Generated by Django 5.0.4 on 2024-04-19 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='county',
            new_name='country',
        ),
    ]
