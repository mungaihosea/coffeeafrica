# Generated by Django 3.0.2 on 2020-01-21 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_remove_buyer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='email',
            new_name='company_email',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='account_active',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='user',
        ),
        migrations.CreateModel(
            name='SellerEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_active', models.BooleanField(default=False)),
                ('profile_picture', models.ImageField(null=True, upload_to='')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('factory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Seller')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]