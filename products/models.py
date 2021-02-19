from django.db import models

# Create your models here.
class Product(models.Model):
    product_shape = models.CharField(max_length=30)
    product_size = models.FloatField()
    product_location = models.CharField(max_length=30)
    product_price = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)

