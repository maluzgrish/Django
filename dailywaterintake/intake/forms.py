from django import forms
from .models import Waterintake

class WaterintakeForm(forms.ModelForm):
    class Meta:
        model = Waterintake
        fields = ['quantity']