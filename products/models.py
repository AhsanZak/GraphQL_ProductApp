from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="product_category")
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name="product_brand")
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING, related_name="product_type")

    def __str__(self):
        return self.name
