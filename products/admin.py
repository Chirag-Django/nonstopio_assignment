from django.contrib import admin
from .models import Product, Recommendation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_shape','product_size','product_location','product_price']

class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['id','product_id','get_user']

    def get_user(self, obj):
        return obj.user_id.pk


admin.site.register(Product, ProductAdmin)
admin.site.register(Recommendation,RecommendationAdmin)

