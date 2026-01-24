from decimal import Decimal
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
import os


User=settings.AUTH_USER_MODEL

def upload_image_path(filepath):
     base_name = os.path.basename(filepath)
     name, ext = os.path.splitext(base_name)
     return name, ext

class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    description = models.TextField()
    prize = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured= models.BooleanField(default=False)
    active= models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    is_digital= models.BooleanField(default=False)
    slug= models.SlugField(unique=True)

    def get_absolute_url(self):
        return f"/products/products/{self.slug}"

    def get_edit_url(self):
            return f"/products/my-products/{self.slug}"
    
    def get_delete_url(self):
        return f"/products/my-products/{self.slug}/delete"     

class DigitalProduct(Product):
    class Meta:
        proxy = True
