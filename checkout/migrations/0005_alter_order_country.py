# Generated by Django 5.0.4 on 2024-05-01 18:06

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]