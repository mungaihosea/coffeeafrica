# Generated by Django 3.0.2 on 2020-02-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0027_auto_20200202_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_of_shipping',
            field=models.DateField(verbose_name='2020-01-01'),
        ),
    ]
