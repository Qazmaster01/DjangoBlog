# Generated by Django 5.0.2 on 2024-02-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aset', '0002_alter_aset_options_aset_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aset',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
