# Generated by Django 5.0.2 on 2024-02-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aset', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aset',
            options={'ordering': ['-title']},
        ),
        migrations.AddField(
            model_name='aset',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='aset',
            index=models.Index(fields=['-title'], name='aset_aset_title_a9cbdf_idx'),
        ),
    ]
