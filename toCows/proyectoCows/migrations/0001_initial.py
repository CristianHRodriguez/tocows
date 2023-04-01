# Generated by Django 4.1.3 on 2023-03-21 00:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberC', models.IntegerField()),
                ('nameC', models.CharField(max_length=45)),
                ('breedC', models.CharField(max_length=45)),
                ('momC', models.IntegerField()),
                ('dadC', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.TextField()),
                ('id_cowP', models.ForeignKey(db_column='numCowP', on_delete=django.db.models.deletion.CASCADE, related_name='numVacasP', to='proyectoCows.cows')),
            ],
        ),
        migrations.CreateModel(
            name='BornCows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateMonta', models.DateField(default=datetime.date.today)),
                ('id_son', models.IntegerField()),
                ('pregnant', models.BooleanField(default=True)),
                ('id_cowB', models.ForeignKey(db_column='numCowB', on_delete=django.db.models.deletion.CASCADE, related_name='numVacasB', to='proyectoCows.cows')),
            ],
        ),
    ]
