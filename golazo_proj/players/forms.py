from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'current_club', 'value', 'country', 'goals', 'assists', 'age', 'photo']