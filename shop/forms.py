from django import forms
from django.forms import widgets, fields

from .models import Shop

class ShopForm(forms.ModelForm):


    class Meta:
    
        model=Shop
        fields=['name','shop_city','shop_street', 'shop_house_num','shop_began_work','shop_end_work','shop_info']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'shop_city':forms.Select(attrs={'class':'form-control','empty_value':True}),
            'shop_street':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'shop_house_num':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'shop_began_work':forms.TimeInput(attrs={'class':'form-control', 'empty_value':True, 'type':'time'}),
            'shop_end_work':forms.TimeInput(attrs={'class':'form-control', 'empty_value':True, 'type':'time'}),
            'shop_info':forms.Textarea(attrs={'class':'form-control', 'empty_value':True})

            }

class SearchShopForm(forms.ModelForm):



    work_status=forms.MultipleChoiceField(choices=(('Открыто','Открыто'),('Закрыто','Закрыто')),widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control', 'empty_value':True}))
    class Meta:

        
       

        model=Shop
        fields=['shop_city','shop_street']

        widgets={
          
            'shop_city':forms.SelectMultiple(attrs={'class':'form-control','empty_value':True}),
            'shop_street':forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True})
            }   
