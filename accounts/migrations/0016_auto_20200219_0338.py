# Generated by Django 3.0.3 on 2020-02-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_sellerfactory_factory_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='use_case',
            field=models.TextField(null=True),
        ),
    ]