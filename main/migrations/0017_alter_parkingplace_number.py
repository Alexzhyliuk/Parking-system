# Generated by Django 3.2.16 on 2022-12-01 15:47

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20221201_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingplace',
            name='number',
            field=models.IntegerField(default=main.models.get_last_number),
        ),
    ]
