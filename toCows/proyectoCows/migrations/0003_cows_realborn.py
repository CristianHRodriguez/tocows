# Generated by Django 4.1.3 on 2023-03-25 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoCows', '0002_alter_borncows_id_son_alter_borncows_pregnant'),
    ]

    operations = [
        migrations.AddField(
            model_name='cows',
            name='realBorn',
            field=models.DateField(default=datetime.date.today),
        ),
    ]