from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import City, Street, Shop
from .forms import ShopForm, SearchShopForm
from datetime import datetime, time

# Create your views here.

def main_menu(request):
    return render(request, 'shop/main.html')


def cities_list(request):
    cities=City.objects.all()
    return render(request, 'shop/cities_list.html', {'cities':cities})

def shop_list(request):
    shop_list=Shop.objects.all()
    return render(request, 'shop/shop_list.html', {'shop_list':shop_list})

class CityDetailView(View):
    def get(self, request, city_id):
        city=get_object_or_404(City, id=city_id)
        streets=Street.objects.filter(city=city)
        return render(request, 'shop/city_detail.html',context={'city':city, 'streets':streets})
    
class ShopDetailView(View):
    def get(self, request, shop_id):
        shop=get_object_or_404(Shop, id=shop_id)
      
        return render(request, 'shop/shop_detail.html',context={'shop':shop})
    

class ShopCreate(View):

    def get(self,request):
        form=ShopForm()
        return render(request, 'shop/shop_create.html', context={'form':form})
    def post(self, request):
        bound_form=ShopForm(request.POST)
        if bound_form.is_valid():
            new_shop=bound_form.save()
            return redirect(new_shop)
        return  render(request, 'shop/shop_create.html', context={'form':bound_form})

class SearchShop(View):

    def get(self,request):
        query_city=[]
        query_st=[]
        r=''
        if request.GET:
            bound_form=SearchShopForm(request.GET)
            if bound_form['shop_city'].value()[0]:
                query_city=bound_form['shop_city'].value()
            else:
                for city in City.objects.all():
                    query_city.append(city)
            if bound_form['shop_street'].value()[0]:
                query_st=bound_form['shop_street'].value()
            else:
                for st in Street.objects.all():
                    query_st.append(st)

            if len(bound_form['work_status'].value())>1 or not bound_form['work_status'].value():
                shps=Shop.objects.filter(shop_city__in=query_city,shop_street__in=query_st)
                return render(request, 'shop/shop_list.html',context={'shop_list':shps})
            elif request.GET['work_status']=='Открыто':
                shps=Shop.objects.filter(shop_city__in=query_city,shop_street__in=query_st,
                                     shop_began_work__range=(time(0,0,0),time(datetime.now().time().hour,0,0)),
                                     shop_end_work__range=(time(datetime.now().time().hour,0,0),time(23,59,59)))
                return render(request, 'shop/shop_list.html',context={'shop_list':shps})
            elif request.GET['work_status']=='Закрыто':
                
                shps=Shop.objects.filter(shop_city__in=query_city,shop_street__in=query_st,
                                     shop_end_work__range=(time(0,0,0),time(datetime.now().time().hour,0,0)))
                return render(request, 'shop/shop_list.html',context={'shop_list':shps})
        else:
            
            form=SearchShopForm()
        return render(request, 'shop/shop_search.html', context={'form':form})
                        
                     
        
