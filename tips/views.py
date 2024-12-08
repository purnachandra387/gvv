from django.shortcuts import render
from .models import GardeningTip

def view_tips(request):
    tips = GardeningTip.objects.all()
    return render(request, 'tips/view_tips.html', {'tips': tips})
