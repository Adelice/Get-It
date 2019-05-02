from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Store,Product


@login_required(login_url='/accounts/login/')
def home(request):
    store = Store.get_all_store()  

    return render(request, 'index.html',{'store':store})

def single_store(request,store):
    # store=Store.object.get(id=id)
    # product=Product.object.filter(store_id=id).all()
    # products = Product.objects.filter(store_id=)
    
    print(store)

    selected_store = Store.objects.filter(id = store)

    products = Product.objects.filter(id = store)
  
    return render(request, 'item.html', {'products':products ,' selected_store': selected_store})
   