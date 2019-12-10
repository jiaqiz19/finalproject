from django import forms
from .models import Sq
# from Paul's note
class SquirrelForm(forms.ModelForm):
    class Meta:
        model = Sq
        fields = '__all__'
