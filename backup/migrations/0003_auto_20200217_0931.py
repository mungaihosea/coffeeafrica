# Generated by Django 3.0.2 on 2020-02-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0002_auto_20200216_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backorder',
            name='date_placed',
            field=models.DateTimeField(null=True),
        ),
    ]
