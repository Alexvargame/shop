from django.urls import path
from .views import *

urlpatterns = [
 
    path('',main_menu, name='main_menu_url'),
    path('cities/',cities_list, name='cities_list_url'),
    path('shop_list/',shop_list, name='shop_list_url'),
    path('shop_list/create',ShopCreate.as_view(), name='shop_create_url'),
    path('shop_list/search',SearchShop.as_view(), name='shop_search_url'),
    path('cities/<int:city_id>',CityDetailView.as_view(), name='city_detail_url'),
    path('shop_list/<int:shop_id>',ShopDetailView.as_view(), name='shop_detail_url'),
    
]
