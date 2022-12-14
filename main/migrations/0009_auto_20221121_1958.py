# Generated by Django 3.2.16 on 2022-11-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20221121_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingplacetype',
            name='is_cover',
            field=models.BooleanField(default=False, verbose_name='Крытое'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='is_cover',
            field=models.BooleanField(default=False, verbose_name='Крытое'),
        ),
        migrations.AlterField(
            model_name='parkingplacetype',
            name='is_open',
            field=models.BooleanField(default=True, verbose_name='Открытое'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='is_open',
            field=models.BooleanField(default=False, verbose_name='Открытое'),
        ),
    ]
