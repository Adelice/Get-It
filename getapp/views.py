

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Store


@login_required(login_url='/accounts/login/')
def home(request):
    store = Store.get_all_store()  

    return render(request, 'index.html',{'store':store})

# class StoreView(View):
   
#     template_name = 'index.html'

#     def get(self, request, zipcode, store_id):
#         try:
#             store = Store.objects.get(pk=store_id)
#         except: # if the user try to access a non-existent store page
#             messages.error(self.request,
#                            "The store you're looking for doesn't exist.",
#                            fail_silently=True,
#                            )
#             return redirect('grocerystore:start', zipcode=zipcode)

#         try: # check if the chosen store delivers the chosen zipcode
#             zipcode_obj = Zipcode.objects.get(zipcode=int(zipcode))
#             if zipcode_obj not in store.delivery_area.all():
#                 messages.error(self.request,
#                                "The store you're looking for doesn't deliver "\
#                                "the area you've chosen.",
#                                fail_silently=True,
#                                )
#                 return redirect('grocerystore:start', zipcode=zipcode)

#         except:
#             # if there aren't any stores that deliver the chosen zipcode area
#             messages.error(self.request, "There's no store available in the area "\
#                                          "you've chosen.", fail_silently=True)
#             return redirect('grocerystore:start', zipcode=zipcode)

#         all_categories = {}
#         # = {'category1': [subcat1, ..., subcatN], 'category2': [subcat1, ..., subcatN], etc.}

#         for category in ProductCategory.objects.all():
#             for subcat in category.productsubcategory_set.all():
#                 # a category shouldn't be displayed if the store has nothing in stock for it
#                 if Availability.objects.filter(store=store)\
#                                        .filter(product__product_category=subcat):
#                     try:
#                         all_categories[category].append(subcat)
#                     except KeyError:
#                         all_categories[category] = [subcat]

#         context = {}
#         context['all_categories'] = all_categories
#         context['store'] = store
#         context['store_id'] = store_id
#         context['zipcode'] = zipcode
#         available_stores = Store.objects.filter(delivery_area__zipcode=zipcode)
#         if len(available_stores) > 0:
#             context['available_stores'] = available_stores

#         if self.request.user.is_authenticated:
#             user = self.request.user
#             user_orders = Order.objects.filter(data__user__user_pk=user.pk)\
#                           .filter(data__store__store_pk=store_id)
#             if user_orders:
#                 context['purchases_here'] = True

#         return render(self.request, 'grocerystore/store.html', context=context)
