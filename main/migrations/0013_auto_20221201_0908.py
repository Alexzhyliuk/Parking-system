# Generated by Django 3.2.16 on 2022-12-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20221201_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingplacetype',
            name='is_open',
            field=models.IntegerField(choices=[(0, 'Открытое'), (1, 'Крытое')], default=0, verbose_name='Открытое-закрытое'),
        ),
        migrations.AlterField(
            model_name='parkingplacetype',
            name='location',
            field=models.IntegerField(blank=True, choices=[(0, 'Рядом с выездом'), (1, 'Рядом со входом')], null=True, verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='is_open',
            field=models.IntegerField(blank=True, choices=[(0, 'Открытое'), (1, 'Крытое')], default=0, null=True, verbose_name='Открытое-закрытое'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='location',
            field=models.IntegerField(blank=True, choices=[(0, 'Рядом с выездом'), (1, 'Рядом со входом')], null=True, verbose_name='Расположение'),
        ),
    ]
