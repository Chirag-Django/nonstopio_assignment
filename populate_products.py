import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'nonstop.settings')
import django
django.setup()


from faker import Faker
from products.models import Product
from random import *

fake = Faker()

def random_size_gen():
    num = str()
    for i in range(2):
        num += str(randint(0,9))
    return num

def random_price_gen():
    num = str()
    for i in range(3):
        num += str(randint(0,9))
    return num

def populate(n):
    for i in range(n):
        fsize = float(random_size_gen())
        fshape = fake.random_element(elements=('Square','Circle', 'Sphere', 'Cube')) + str(int(fsize))
        fprice = float(random_price_gen())
        flocation = fake.random_element(elements=('Pune', 'Mumbai', 'Bangalore', 'Hyderabad','Delhi'))
        product_record = Product.objects.get_or_create(product_shape=fshape,product_size=fsize,product_location=flocation,product_price=fprice)

populate(25)

