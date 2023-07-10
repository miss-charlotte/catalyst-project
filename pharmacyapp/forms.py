from django.forms import ModelForm
from .models import *
from django import forms

class SellForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amountPaid', 'boughtBy'] 

class AddForm(ModelForm):
    class Meta:
        model =Product
        fields =['receivedQuantity']                