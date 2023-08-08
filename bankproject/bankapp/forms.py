from django import forms
from .models import BankForm

class BankFormForm(forms.ModelForm):

    class Meta:
        model = BankForm
        fields = '__all__'
        widgets ={
            'gender': forms.RadioSelect,
            'material': forms.RadioSelect
        }



