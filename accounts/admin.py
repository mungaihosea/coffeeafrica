from django.contrib import admin
from .models import SellerFactory, Buyer, SellerFactoryEmployee
from django.contrib.auth.models import User

# admin.site.register(User)
admin.site.register(SellerFactory)
admin.site.register(SellerFactoryEmployee)
admin.site.register(Buyer)