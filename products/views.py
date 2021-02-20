from django.shortcuts import render
from .models import Product, Recommendation
from django.http import Http404
import pandas as pd
from collections import OrderedDict

def index(request):
    return render(request,'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'all_products':products})

#COLLABARATIVE RECOMMENDATION

def top_ten_list(request):
    products = Recommendation.objects.all()
    temp_list = []
    title = 'TOP TEN SEARCHES!!!'
    for record in products:
        tup = (record.product_id.pk,record.user_id.pk)
        temp_list.append(tup)
    df = pd.DataFrame(temp_list)
    duplicate_users_and_products = df.pivot_table(index=[0, 1], aggfunc='size')
    duplicates_counter_dict = duplicate_users_and_products.to_dict()
    sorted_values = sorted(duplicates_counter_dict.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in duplicates_counter_dict.keys():
            if duplicates_counter_dict[k] == i:
                sorted_dict[k] = duplicates_counter_dict[k]
    top_item_pk = list()
    print(top_item_pk)
    for k, v in sorted_dict.items():
        top_item_pk.append(k[0])
    top_item_pk = list(OrderedDict.fromkeys(top_item_pk))
    top_ten_item_pk = top_item_pk[:10]
    products = Product.objects.filter(id__in=top_ten_item_pk)
    objects = dict([(obj.id, obj) for obj in products])
    sorted_objects = [objects[id] for id in top_ten_item_pk]
    print(sorted_objects)
    return render(request,'product_list.html',{'title':title,'all_products':sorted_objects})

#CONTENT BASED RECOMMENDATIONS
def user_search_based_recommendation(request,id):
    products = Recommendation.objects.all()
    temp_list = []
    sorted_objects = []
    message = ''
    title = 'Your Favorite Searches!!!'
    for record in products:
        if record.user_id.pk == id:
            tup = (record.product_id.pk,record.user_id.pk)
            temp_list.append(tup)
    if temp_list:
        df = pd.DataFrame(temp_list)
        duplicate_users_and_products = df.pivot_table(index=[0, 1], aggfunc='size')
        duplicates_counter_dict = duplicate_users_and_products.to_dict()
        print(duplicates_counter_dict)
        sorted_values = sorted(duplicates_counter_dict.values(), reverse=True)
        sorted_dict = {}
        for i in sorted_values:
            for k in duplicates_counter_dict.keys():
                if duplicates_counter_dict[k] == i:
                    sorted_dict[k] = duplicates_counter_dict[k]
        top_item_pk = list()
        for k, v in sorted_dict.items():
            top_item_pk.append(k[0])
        top_item_pk = list(OrderedDict.fromkeys(top_item_pk))
        top_ten_item_pk = top_item_pk[:10]
        products = Product.objects.filter(id__in=top_ten_item_pk)
        objects = dict([(obj.id, obj) for obj in products])
        sorted_objects = [objects[id] for id in top_ten_item_pk]
    else:
        message = "You Didn't Explore Different Products Yet!!"
    return render(request, 'product_list.html',{'message':message,'all_products':sorted_objects,'title':title})


def product_details(request,id):
    global message
    try:
        product_details = Product.objects.get(pk=id)
        message = None
        if product_details is None:
            message = "Product Not Found"
    except Product.DoesNotExist:
        raise Http404("Product Doesnot Exists")
    return render(request,'product_details.html',{'product_details': product_details,'message': message})

def search_products(request):
    search_product = request.GET.get('q')
    try:
        int(search_product)
    except:
        message = "PLEASE ENTER ID OF PRODUCT"
    else:
        search_product = int(search_product)
        products = Product.objects.filter(id=search_product)
        product = products.first()
        if request.user.is_authenticated:
            user = request.user
            Recommendation.objects.create(user_id=user,product_id=product)
        return render(request,'product_list.html',{'all_products':products})
    return render(request, 'product_list.html',{'message': message})
