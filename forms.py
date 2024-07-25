from django import forms
from .models import Product, ProductImage, ProductSpecification, ProductSustainability

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'availability', 'description']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']

class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = ['product', 'specifications']

class ProductSustainabilityForm(forms.ModelForm):
    class Meta:
        model = ProductSustainability
        fields = ['product', 'sustainability_info']
