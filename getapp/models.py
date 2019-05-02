from django.db import models
# from django.contrib.auth.models import User
# Create your models here
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

class Product(models.Model):
    product_pic = models.ImageField(upload_to='images/', blank=True,null=True, verbose_name="product picture")
    product_name = models.CharField(max_length=60, verbose_name="product",null=True)
    product_price =models.IntegerField( default=0, verbose_name="price")
    product_store = models.ManyToManyField(Store, verbose_name="availability(ies) in store(s)") 
    
    class Meta:
        ordering = ['product_name']

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()
    @classmethod
    def search_by_name(cls,search_term):
        product = cls.objects.filter(product_name__icontains=search_term)
        return product
    
class Supermarket(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    product=models.ForeignKey(Product)
    def __str__(self):
        return self.name

    def save_supermarket(self):
        self.save() 
    def delete_supermarket(self):
        self.delete() 


class Location(models.Model):
    name = models.CharField(max_length =30)
    supermaket=models.ForeignKey(Supermarket)
    def __str__(self):
        return self.name

    def save_location(self):
        self.save() 
    def delete_location(self):
        self.delete() 
      
