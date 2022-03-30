from django.forms import ModelForm
from .models import  AddStock

class AddStockRegister(ModelForm):
    class Meta:
        model = AddStock
        fields = ['productsName', 'productsCategory', 'productsQuantity', 'productsPrice']