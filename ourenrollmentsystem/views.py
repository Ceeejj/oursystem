from django.shortcuts import render, redirect
from .models import Level, Students
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
    messages.success(request, 'Year Level Successfully saved!')
    return redirect('/level')

def index_student(request):
    students = Students.objects.all()
    
    context = {
        'students': students
    }
    return render(request, 'students/log_in.html', context)

def create_user(request):
    level = Level.objects.all()
    
    context = {
        'level':level
    }
    return render(request, 'students/create.html', context)

def login_view(request):
    
    return redirect(request, 'students/log_in.html')

def store_students(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    gender = request.POST.get('gender')
    program = request.POST.get('program')
    levelId = request.POST.get('level_id')
    studentId = request.POST.get('username')
    
    Students.objects.create(first_name=firstName, middle_name=middleName, last_name=lastName,age=age, birth_date=birthDate,gender=gender,program=program,level_id=levelId,username=studentId )
    messages.success(request, 'Your information was saved!')
    return redirect('/students')

def show_info(request, user_id):
    students = Students.objects.get(pk=user_id)
    
    context = {
        'students' : students,
    }
    
    return render(request, 'students/show.html', context)

def update_students(request, level_id):
    students = Students.objects.get(pk=level_id)
    
    context = {
        'students' : students,
    }
    
    return render(request, 'students/update.html', context)

def edit_student(request, level_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    gender = request.POST.get('gender')
    program = request.POST.get('program')
    levelId = request.POST.get('level_id')
    studentId = request.POST.get('username')
    
    Students.objects.filter(pk=level_id).update(first_name=firstName, middle_name=middleName, last_name=lastName, age=age, birth_date=birthDate,gender=gender,program=program,level_id=levelId,username=studentId)
    messages.success(request, 'Your officially enrolled this year.')
    
    return redirect('/students')


    
    
    