# Generated by Django 4.1.3 on 2023-03-28 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoCows', '0004_alter_borncows_id_son'),
    ]

    operations = [
        migrations.AddField(
            model_name='cows',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
