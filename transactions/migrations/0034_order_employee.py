# Generated by Django 3.0.2 on 2020-02-17 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_sellerfactory_factory_bio'),
        ('transactions', '0033_remove_order_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.SellerFactoryEmployee'),
        ),
    ]