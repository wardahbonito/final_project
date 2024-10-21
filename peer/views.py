from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Admin, Registration, Event, Fill
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
        messages.success(request,"Success")
        
    return render(request, 'register.html', dict)

def man_stud(request):
    students = Student.objects.all()
    
    if request.method == 'GET':
        c_student_name = request.GET.get('c_student_name')
        if c_student_name:
            students = Student.objects.filter(student_name=c_student_name)
    
    context = {
        'students': students,
    }
    return render(request, 'man_stud.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email') #ni ambik dari yang input name contoh:<input type='text' name='EMAIL'> jangan ikut bold just nak tunjuk je
        password = request.POST.get('password')

        student = search(Student, email)
        admin = search(Admin, email)

        if student:
            if student.password == password:
                request.session['user_type'] = 'user' # ni declare user type je tukar ikut user type website 
                request.session['user_id'] = student.student_id  
                return redirect('welcome-user')
            else:
                messages.error(request, "Password is incorrect.")

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
    student = request.user
    context = {
        'student': student
    }
    return render(request, 'welcome-user.html', context)

def fill(request):

    if request.method == 'POST':
        c_fill_name = request.POST['name']
        c_fill_phone = request.POST['phone']
        c_fill_email = request.POST['email']
        c_fill_course = request.POST['course']
        c_event_id = request.POST['event']
        
        myevent = Event.objects.get(event_id=c_event_id) 
        
        data = Fill (
            fill_name=c_fill_name,
            fill_phone=c_fill_phone,
            fill_email=c_fill_email,
            fill_course=c_fill_course,
            event_id=myevent 
        )
        
        data.save()  

        return redirect('fill')

    return render(request, 'fill.html')

def list(request):

    fill = Fill.objects.all()
    if request.method == 'GET':
        c_fill_name = request.GET.get('c_fill_name')
        if c_fill_name:
            fill = Fill.objects.filter(fill_name=c_fill_name)

    context = {
        'fill' : fill,
    }

    return render(request, 'list.html', context)

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

def add(request):

    event = Event.objects.all().values()
    context = {
        'event':event
    }

    if request.method == 'PUT':
        c_event_id = request.POST['id']
        c_event_name = request.POST['name']
        c_event_location = request.POST['location']
        c_event_date = request.POST['date']

        data = Event(event_id=c_event_id, event_name=c_event_name, event_location=c_event_location, event_date=c_event_date)
        data.save()

    return render(request, 'add.html', context)

def delete_student(request, student_id):
    data = Student.objects.get(student_id=student_id)
    data.delete()

    return HttpResponseRedirect(reverse('man_stud'))

def stud_profile(request):
    user_id = request.session.get('user_id')
    mystudent = Student.objects.get(student_id=user_id)
    
    # Access the attributes from the mystudent object
    ids = mystudent.student_id
    name = mystudent.student_name
    email = mystudent.email
    phone = mystudent.phone_number
    course = mystudent.student_course
    
    context = {
        'ids': ids,
        'name': name,
        'email': email,
        'phone': phone,
        'course': course,
    }

    return render(request, 'stud_profile.html', context)

def stud_admin(request):
    user_id = request.session.get('user_id')
    myadmin = Admin.objects.get(admin_id=user_id)
    
    # Access the attributes from the mystudent object
    ids = myadmin.admin_id
    name = myadmin.admin_name
    email = myadmin.email
    password = myadmin.password
    
    context = {
        'ids': ids,
        'name': name,
        'email': email,
        'password': password,
    }

    return render(request, 'stud_admin.html', context)


def event(request):
    events = Event.objects.all().values()
    if request.method == 'GET':
        c_event_name = request.GET.get('c_event_name')
        if c_event_name:
            events = Event.objects.filter(event_name=c_event_name)
    
    context = {
        'event': events
    }
    return render(request, 'event.html', context)


def delete_event(request,event_id):
    data = Event.objects.get(event_id=event_id)
    data.delete()

    return HttpResponseRedirect(reverse('add'))

def update_event(request, event_id):
    data = Event.objects.get(event_id=event_id)
    dict = {
        'data' : data
    }

    return render(request, 'update_event.html', dict)

def save_update_event(request, event_id):
    c_event_name = request.POST['event_name']
    c_event_location = request.POST['event_location']
    c_event_date = request.POST['event_date']

    data = Event.objects.get(event_id=event_id)
    data.event_name = c_event_name
    data.event_location = c_event_location
    data.event_date = c_event_date
    data.save()

    return HttpResponseRedirect (reverse("add"))

def edit_profile_s(request):
    user_id = request.session.get('user_id')
    data = Student.objects.get(student_id=user_id)
    context = {
        'data':data,
    }
    return render(request, "edit_profile_s.html",context)

def save_update_profile(request, student_id):
    c_student_name = request.POST['student_name']
    c_email = request.POST['email']
    c_phone_number = request.POST['phone_number']
    c_student_course = request.POST['student_course']

    data = Student.objects.get(student_id=student_id)
    data.student_name = c_student_name
    data.email = c_email
    data.phone_number = c_phone_number
    data.student_course = c_student_course
    data.save()

    return HttpResponseRedirect(reverse("stud_profile"))

def delete_list(request, fill_id):
    data = Fill.objects.get(fill_id=fill_id)
    data.delete()

    return HttpResponseRedirect(reverse('fill'))
