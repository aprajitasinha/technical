from django import forms
from .models import GeeksModel
class GeeksForm(forms.ModelForm):
    
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel

        # specify fields to be used
        fields = [
            "title",
            "description",
        ]