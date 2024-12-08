from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Garden, Plant
from .forms import GardenForm

@login_required
def plan_garden(request):
    recommended_plants = None
    if request.method == 'POST':
        form = GardenForm(request.POST)
        soil_type = request.POST.get('soil_type')
        if form.is_valid():
            garden = form.save(commit = False)
            garden.user = request.user
            garden.save()
            form.save_m2m()
            return redirect('garden_detail', pk = garden.pk)
        # Recommend plants based on soil type 
        if soil_type: 
            recommended_plants = Plant.objects.filter(optimal_soil__icontains=soil_type)
    else:
        form = GardenForm()
        soil_type = request.GET.get('soil_type', '')
        recommended_plants = Plant.objects.filter(optimal_soil__icontains=soil_type) if soil_type else None
    plants = Plant.objects.all()
    return render(request, 'garden/plan.html', {'form': form, 'plants': plants,'recommended_plants': recommended_plants})

def garden_detail(request, pk): 
    garden = get_object_or_404(Garden, pk=pk) 
    return render(request, 'garden/garden_detail.html', {'garden': garden})