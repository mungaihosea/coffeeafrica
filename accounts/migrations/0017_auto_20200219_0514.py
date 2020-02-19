# Generated by Django 3.0.3 on 2020-02-19 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200219_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerfactoryemployee',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sellerfactoryemployee',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='sellerfactoryemployee',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sellerfactoryemployee',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]