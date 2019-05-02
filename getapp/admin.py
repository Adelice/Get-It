from django.contrib import admin

# Register your models here.

from .models import Store,Product,Supermarket,Location

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Supermarket)
admin.site.register(Location)