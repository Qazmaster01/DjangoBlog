# Generated by Django 5.0.2 on 2024-02-23 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aset', '0005_category_aset_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aset',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aset.category'),
        ),
    ]
