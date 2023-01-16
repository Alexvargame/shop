from django.db import models
from django.shortcuts import reverse

# Create your models here.


class City(models.Model):
    name=models.CharField("Город", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Город"
        verbose_name_plural="Города"

    def get_absolute_url(self):
            return reverse('city_detail_url', kwargs={'city_id':self.id})




class Street(models.Model):
    name=models.CharField("Улица", max_length=50)
    city=models.ForeignKey(City,verbose_name="Город", on_delete=models.CASCADE,null =True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Улица"
        verbose_name_plural="Улицы"

    def get_absolute_url(self):
            return reverse('street_detail_url', kwargs={'street_id':self.id})
    
class Shop(models.Model):

    name=models.CharField("Название", max_length=50)
    shop_city=models.ForeignKey(City, verbose_name="Город", on_delete=models.CASCADE, null=True)
    shop_street=models.ForeignKey(Street, verbose_name="Улица", on_delete=models.CASCADE, null=True)
    shop_house_num=models.CharField("Дом", max_length=70,default='', blank=True,null=True)
    shop_began_work=models.TimeField()
    shop_end_work=models.TimeField()
    shop_info=models.TextField(default='',blank=True,null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Магазин"
        verbose_name_plural="Магазины"

    def get_absolute_url(self):
            return reverse('shop_detail_url', kwargs={'shop_id':self.id})

