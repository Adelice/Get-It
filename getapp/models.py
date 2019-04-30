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

