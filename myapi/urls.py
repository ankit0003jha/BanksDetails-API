from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from .import views

#urlpatterns=[

 #   path('', views.index, name='index'),
    
    
#]

urlpatterns = [

    
     
     path('api/branches/autocomplete/', views.Autocomplete_API, name='Autocomplete_API'),
     path('api/branches/', views.Search_API, name='Search_API'),
     path('api/branch/q=<query>/limit=<lim>/offset=<off>', views.Dynamic_url_API, name='Dynamic_url_API'),
     path('', views.index, name='index'),
     path('search/' , views.search, name='search'),


     
 ]