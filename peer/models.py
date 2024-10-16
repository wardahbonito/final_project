from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.TextField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=50)
    student_course=models.CharField(max_length=50, default='Unknown')

class Admin(models.Model):
    admin_id=models.AutoField(primary_key=True)  
    admin_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=10)
    password=models.TextField(max_length=10, default=None)
    admin_role=models.CharField(max_length=10)

class Event(models.Model):
    event_id=models.CharField(max_length=10)
    event_name=models.CharField(max_length=15)
    event_location=models.CharField(max_length=20, default=None)
    event_date=models.DateField(max_length=30, default=None)
    
class Registration(models.Model):
    registration_id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    registration_date=models.DateField(max_length=10)
    event_id=models.ForeignKey(Event, on_delete=models.CASCADE, default=1)

class Fill(models.Model):
    fill_id=models.AutoField(primary_key=True)
    fill_name=models.CharField(max_length=10)
    
