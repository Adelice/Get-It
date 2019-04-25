from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length =30)
    product_image=models.ImageField(upload_to = 'images/')
    price=models.IntegerField()

    def __str__(self):
        return self.name
        
    def save_product(self):
        self.save() 

class SuperMarket(models.Model):
    market_name= models.CharField(max_length =30)
    market_image = models.ImageField(upload_to = 'images/')
    market_location = models.CharField(max_length =50)
    product = models.ForeignKey(Product)



class Location (models.Model): 
    name = models.CharField(max_length=30)
    supermarkerk = models.ForeignKey(SuperMarket)

    def __str__(self):
        return self.name 

    def save_location(self):
        self.save()

# class Payment(models.Model):
#     name = models.CharField(max_length=30)
#     product = models.ForeignKey(Product)

#     def __str__(self):
#         return self.name

#     def save_payment(self):
#         self.save()


