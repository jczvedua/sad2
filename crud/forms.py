from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        model = Item
        fields = ['name', 'price']

    def __str__(self):
        return self.name
