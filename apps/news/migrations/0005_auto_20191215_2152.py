# Generated by Django 2.2.6 on 2019-12-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_url',
            field=models.URLField(max_length=250),
        ),
    ]
