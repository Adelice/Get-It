from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def welcome(request):
    return render(request, 'all-products/index.html')


def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_products = Product.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"products": searched_product})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-products/search.html',{"message":message}) 