from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug= models.SlugField(unique=True)

class DigitalProduct(Product):
    class Meta:
        proxy = True