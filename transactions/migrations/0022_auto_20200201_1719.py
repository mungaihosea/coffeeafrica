# Generated by Django 3.0.2 on 2020-02-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0021_auto_20200201_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='humidity',
            field=models.CharField(default='Not Provided', max_length=12),
        ),
        migrations.AlterField(
            model_name='auction',
            name='soil_ph',
            field=models.CharField(default='Not Provided', max_length=12),
        ),
    ]
