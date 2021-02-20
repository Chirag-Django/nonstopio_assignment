from django.urls import path
from .views import product_list,product_details,index,search_products,top_ten_list,user_search_based_recommendation

urlpatterns = [
    path('',index,name='home'),
    path('product_list/',product_list,name='product_list'),
    path('product_details/<int:id>/',product_details,name='product_details'),
    path('search/',search_products,name='search_products'),
    path('top_ten_list/',top_ten_list,name='top_ten_list'),
    path('user_recommendations/<int:id>/',user_search_based_recommendation,name='user_recommendations'),
]