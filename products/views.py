from django.shortcuts import render
from .models import Product
from django.http import Http404

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'all_products':products})

def productDetails(request,id):
    global message
    try:
        product_details = Product.objects.get(pk=id)
        message = None
        if product_details is None:
            message = "Product Not Found"
    except Product.DoesNotExist:
        raise Http404("Product Doesnot Exists")
    return render(request,'product_details.html',{'product_details': product_details,'message': message})
