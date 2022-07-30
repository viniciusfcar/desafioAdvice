from pyexpat import model
from django import forms
from .models import Carro

class FormCarro(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['cor', 'modelo']