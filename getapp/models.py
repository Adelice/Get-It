from django.db import models
# from django.contrib.auth.models import User
# Create your models here

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    product_image = models.ImageField(upload_to = 'images/')
    

    def __str__(self):
        return self.name

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()
    @classmethod
    def search_by_name(cls,search_term):
        product = cls.objects.filter(name__icontains=search_term)
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
      
