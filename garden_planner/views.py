from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from users.forms import UserRegisterForm  # Ensure this import is here


def home(request):
    context = { 'user': request.user }
    return render(request, 'home/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def garden_planning(request):
    # Your garden planning view logic here
    return render(request, 'garden_planning.html')

@login_required
def plant_growth_log_list(request):
    # Your plant growth log list view logic here
    return render(request, 'plant_growth_log_list.html')

@login_required
def add_task(request):
    # Your add task view logic here
    return render(request, 'add_task.html')

@login_required
def view_tasks(request):
    # Your view tasks view logic here
    return render(request, 'view_tasks.html')

@login_required
def community_forum(request):
    # Your community forum view logic here
    return render(request, 'community_forum.html')

@login_required
def gardening_tips(request):
    # Your gardening tips view logic here
    return render(request, 'gardening_tips.html')