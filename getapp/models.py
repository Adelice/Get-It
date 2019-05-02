# Create your models here.
from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

class Store(models.Model):
    store_pic = models.ImageField(upload_to='stores/', blank=True, verbose_name="logo/picture")
    store_name = models.CharField(max_length=30, verbose_name="store")
    store_location = models.CharField(max_length=30, verbose_name="location name")
    store_address = models.CharField(max_length=200, verbose_name="Address")
    store_city = models.CharField(max_length=30, verbose_name="city")
   
    # delivery_area = models.ManyToManyField(Zipcode)

    def __str__(self):
        return str(self.store_name) + " (" + str(self.store_location) + ")"

    class Meta:
        ordering = ['store_name','store_city', 'store_location']
    @classmethod
    def get_store_by_id(cls, id):
        store = cls.objects.get(pk=id)
        return store 
    @classmethod
    def get_all_store(cls):
        store= Store.objects.all()
        return store 
class Category(models.Model):
    name = models.CharField(max_length =30) 
    def __str__(self):
        return self.category    
class Product(models.Model):
    product_pic = models.ImageField(upload_to='products/', blank=True,null=True, verbose_name="product picture")
    product_name = models.CharField(max_length=60, verbose_name="product")
    product_price =models.IntegerField( default=0, verbose_name="price")
    product_store = models.ManyToManyField(Store, verbose_name="availability(ies) in store(s)") 

    class Meta:
        ordering = ['product_name']
    @classmethod
    def get_product_by_id(cls, id):
       product = cls.objects.get(pk=id)
       return product
    @classmethod
    def get_all_product(cls):
        product= Product.objects.all()
        return product 
    @classmethod
    def get_store_product(cls, store):
        products = Product.objects.filter(store__pk =store)
        return products 





