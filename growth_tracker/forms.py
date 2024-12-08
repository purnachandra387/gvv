from django import forms
from .models import PlantGrowthLog
from garden.models import Plant

class PlantGrowthLogForm(forms.ModelForm):
    class Meta:
        model = PlantGrowthLog
        fields = ['plant', 'date', 'observation', 'photo']