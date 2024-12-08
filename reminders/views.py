from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required 
from .models import Task 
from garden.models import Garden, Plant 
from .forms import TaskForm

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.garden = Garden.objects.get(user=request.user)
            task.save()
            return redirect('view_tasks')
    else:
        form = TaskForm()
    return render(request, 'reminders/add_task.html', {'form': form})

@login_required
def view_tasks(request):
    tasks = Task.objects.filter(garden__user=request.user)
    return render(request, 'reminders/view_tasks.html', {'tasks': tasks})

@login_required 
def update_task_status(request, task_id): 
    task = Task.objects.get(id=task_id) 
    if task.garden.user == request.user: 
        task.is_completed = not task.is_completed 
        task.save() 
    return redirect('view_tasks')