# Generated by Django 3.0.2 on 2020-01-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200121_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]