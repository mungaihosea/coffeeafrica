from django.db import models
from django.contrib.auth.models import User as user_model

User = user_model


class SellerFactory(models.Model):
    date_created = models.DateField(auto_now_add=True, null=True)
    factory_name = models.CharField(max_length=30)
    company_email = models.EmailField()
    phone = models.CharField(max_length=20)
    region = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    trade_license = models.FileField(null=True, blank=True)
    rating = models.IntegerField(null=True)
    factory_logo = models.ImageField(null=True)
    googlemap = models.TextField(null=True)
    factory_bio = models.TextField(default="No bio")

    def __str__(self):
        return self.factory_name


class SellerFactoryEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    factory = models.ForeignKey(SellerFactory, on_delete = models.CASCADE)
    country = models.CharField(max_length = 30 , null = True)
    address = models.TextField(null = True)
    profile_picture = models.ImageField(null = True)
    phone = models.IntegerField(null = True)

    def __str__(self):
        return self.user.username


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length = 30, null = True)
    address = models.TextField(null = True)
    profile_picture = models.ImageField(null = True)
    phone = models.IntegerField(null = True)
    use_case = models.TextField(null = True)

    def __str__(self):
        return self.user.username

