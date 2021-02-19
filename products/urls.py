from django.urls import path
from .views import product_list,product_details,index,search_products

urlpatterns = [
    path('home/',index,name='home'),
    path('product_list/',product_list,name='product_list'),
    path('product_details/<int:id>/',product_details,name='product_details'),
    path('search/',search_products,name='search_products'),
]