# Generated by Django 3.0.2 on 2020-01-30 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0014_auto_20200129_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='date',
            new_name='datetime',
        ),
    ]
