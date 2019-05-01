from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url


urlpatterns=[
     url(r'^$', views.home, name='home'),
     url(r'^store/(\d+)', views.single_store, name='single_store'),
     # url(r'^location/(\d+)',views.location,name = 'location')
     
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
