from django.contrib import admin
from .models import Category, Brand, ProductType, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(Product)
