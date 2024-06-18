from django.shortcuts import render, redirect
from .models import Level
from django.contrib import messages

def index_level(request):
    level = Level.objects.all()
    
    context = {
        'level': level
    }
    
    return render(request, 'level/index.html', context)

def create_level(request):
    return render(request, 'level/create.html')

def store_level(request):
    level = request.POST.get('level')
    Level.objects.create(level=level)
    messages.success(request, 'Level Successfully saved!')
    return redirect('/level')

def index_student(request):
    return render(request, 'students/index.html')

def create_user(request):
    return render(request, 'students/create.html')