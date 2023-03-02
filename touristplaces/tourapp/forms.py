from django import forms
from .models import spots

class spot_edit(forms.ModelForm):
    class Meta:
        model= spots
        fields= ['name','known','desc','thb']