from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import NewProductForm
from .models import Product
# Create your views here.

def welcome(request):
    return render(request, 'all-products/index.html')


def product(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
        return redirect('welcome')

    else:
        form = NewProductForm()
    return render(request, 'product.html', {"form": form})

def search_results(request):

    if 'product_name' in request.GET and request.GET["product_name"]:
        search_term = request.GET.get("product_name")
        searched_products = Product.search_by_name(search_term)
        message = f"{search_term}"
       
        return render(request, 'all-products/search.html',{"message":message,"products": searched_products})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-products/search.html',{"message":message}) 