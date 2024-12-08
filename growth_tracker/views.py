from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PlantGrowthLog
from .forms import PlantGrowthLogForm

@login_required
def plant_growth_log_list(request):
    logs = PlantGrowthLog.objects.all()
    return render(request, 'growth_tracker/plant_growth_log_list.html', {'logs': logs})

@login_required
def add_plant_growth_log(request):
    if request.method == 'POST':
        form = PlantGrowthLogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant_growth_log_list')
    else:
        form = PlantGrowthLogForm()
    return render(request, 'growth_tracker/add_plant_growth_log.html', {'form': form})