# Generated by Django 3.0.2 on 2020-02-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0030_order_arrived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
