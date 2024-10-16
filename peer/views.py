from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Admin, Registration, Event
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def register(request):
    mystudent = Student.objects.all().values()
    dict = {
        'mystudent': mystudent
    }

    if request.method == 'POST':
        c_student_name = request.POST['name']
        c_student_email = request.POST['email']
        c_student_password = request.POST['password']
        c_phone_number = request.POST['phone']
        c_student_course = request.POST['course']

        data = Student(student_name=c_student_name, email=c_student_email, password=c_student_password, phone_number=c_phone_number,student_course=c_student_course)
        data.save()
        
    return render(request, 'register.html', dict)

def man_stud(request):
    students = Student.objects.all()
    context = {
        'students':students,
    }

    return render(request, 'man_stud.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email') #ni ambik dari yang input name contoh:<input type='text' name='EMAIL'> jangan ikut bold just nak tunjuk je
        password = request.POST.get('password')

        student = search(Student, email)
        admin = search(Admin, email)
        #register = search(Registration, email)


        if student:
            if student.password == password:
                request.session['user_type'] = 'user' # ni declare user type je tukar ikut user type website 
                request.session['user_id'] = student.student_id  
                return redirect('welcome-user')
            else:
                messages.error(request, "Password is incorrect.")
        #elif register:
            #if register.password == password:
             #   request.session['user_type'] = 'staff'
              #  request.session['user_id'] = register.registeration_id
                #return redirect('staffmenu')
            #else:
             #   messages.error(request, "Password is incorrect.")
        elif admin:
            if admin.password == password:
                request.session['user_type'] = 'admin'
                request.session['user_id'] = admin.admin_id
                return redirect('admin_page')
            else:
                messages.error(request, "Password is incorrect.")
        else:
            messages.error(request, "Email not found. Please sign up first.")

    
    return render(request, 'login.html')

def search(model, email):
    try:
        return model.objects.get(email=email)
    except model.DoesNotExist:
        return None

def welcome_user(request):
    return render(request, 'welcome-user.html')

def fill(request):
    return render(request, 'fill.html')

def learn_more(request):
    return render(request, 'learn_more.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def admin_page(request):
    students = Student.objects.all()
    context = {
        'students':students,
    }
    return render(request, 'admin_page.html',context)

def list(request):
    mystudent = Student.objects.all().values()
    myevent = Event.objects.all().values()

    dict = {
        'mystudent':mystudent,
        'myevent' :myevent,
    }

    if request.method == 'POST':
        c_student_name = request.POST['name']
        c_phone_number = request.POST['phone']
        c_email = request.POST['email']
        c_student_course = request.POST['course']
        c_event_id = request.POST['event']

        data = Student (student_name=c_student_name, phone_number=c_phone_number, email = c_email, student_course=c_student_course)
        dataa = Event (event_id=c_event_id)
        data.save()
        dataa.save()
    return render(request, 'list.html', dict)

def add(request):

    return render(request, 'add.html')

def delete_student(request, student_id):
    data = Student.objects.get(student_id=student_id)
    data.delete()

    return HttpResponseRedirect(reverse('man_stud'))
