# Generated by Django 3.2.16 on 2022-11-21 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20221121_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingPlaceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=True, verbose_name='Отрытое')),
                ('is_near_exit', models.BooleanField(default=False, verbose_name='Рядом с выездом')),
                ('is_for_disabled', models.BooleanField(default=False, verbose_name='Место для инвалидов')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Свободно'), (1, 'Занято')], default=0, verbose_name='Статус')),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='main.parking')),
                ('place_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places', to='main.parkingplacetype')),
            ],
        ),
    ]
