# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User, Task

def login(request):
    if request.method == 'POST':
        # Handle login form submission
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, {'error': 'Invalid email or password.'})
    else:
        # Render login form
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        # Handle registration form submission
        name = request.POST['name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        address = request.POST['address']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        user = User.objects.create(name=name, email=email, mobile_number=mobile_number, password=password, address=address, latitude=latitude, longitude=longitude)
        return redirect('login')
    else:
        # Render registration form
        return render(request, 'register.html')

@login_required
def dashboard(request):
    assigned_tasks = request.user.assigned_tasks.all()
    context = {
        'assigned_tasks': assigned_tasks,
    }
    return render(request, 'dashboard.html', context)

@login_required
def task_scheduler(request):
    if request.method == 'POST':
        # Handle task form submission
        name = request.POST['name']
        date_time
