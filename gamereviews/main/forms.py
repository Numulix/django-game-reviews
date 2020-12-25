from django import forms
from .models import *

# Forma za dodavanje igrice
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'release_year', 'company', 'description', 'image']