# Generated by Django 4.1.3 on 2023-03-21 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoCows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borncows',
            name='id_son',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='borncows',
            name='pregnant',
            field=models.BooleanField(default=True, null=True),
        ),
    ]