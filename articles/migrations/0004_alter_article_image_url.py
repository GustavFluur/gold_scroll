# Generated by Django 3.2.22 on 2023-11-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.URLField(blank=True, max_length=9999, null=True),
        ),
    ]
