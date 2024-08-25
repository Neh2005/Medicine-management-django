from django import forms
from .models import MedicalProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = MedicalProduct
        fields = ['name','description','price','stock']