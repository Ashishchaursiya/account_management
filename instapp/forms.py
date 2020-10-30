from django import forms
from .models import Customer
class customerRegister(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','phone','product','credit','due']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','min':'10'}),
            'product':forms.TextInput(attrs={'class':'form-control'}),
            'credit':forms.NumberInput(attrs={'class':'form-control'}),
            'due':forms.NumberInput(attrs={'class':'form-control'}),
            
            
            
            
        }