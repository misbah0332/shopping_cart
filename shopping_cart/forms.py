from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  
        # fields = ('name', 'description', 'price', 'image') 
        # labels = {
        #     'fullname': 'Full Name',
        #     'emp_code': 'Employee Code',
        #     'mobile': 'Mobile Number',
        #     'position' : 'Position'
        # }
