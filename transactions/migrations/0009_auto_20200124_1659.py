# Generated by Django 3.0.2 on 2020-01-24 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_sellerfactory_factory_logo'),
        ('transactions', '0008_order_date_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Buyer'),
        ),
    ]