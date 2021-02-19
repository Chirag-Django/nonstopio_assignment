from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_shape','product_size','product_location','product_price']

admin.site.register(Product, ProductAdmin)