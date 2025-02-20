from django import forms
from .models import Product





class ProductInputForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = '__all__'

class ProductDeleteForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = 'id',

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'stock']
