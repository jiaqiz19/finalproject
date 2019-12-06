from django import forms
from .models import Sq

class SquirrelForm(forms.ModelForm):
    class Meta:
        model = Sq
        fields = '__all__'
