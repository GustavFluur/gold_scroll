# Generated by Django 3.2.22 on 2023-11-25 19:35

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
