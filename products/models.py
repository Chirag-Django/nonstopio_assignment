from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_shape = models.CharField(max_length=30)
    product_size = models.FloatField()
    product_location = models.CharField(max_length=30)
    product_price = models.DecimalField(max_digits=19, decimal_places=2,default=0.00)

    def __str__(self):
        return str(self.id)


class Recommendation(models.Model):
    user_id = models.ForeignKey(User, related_name='user_id',on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='product_id',on_delete=models.CASCADE)



