from django.db import models
import random
from django.urls import reverse
from django.utils import timezone
import time
from django.contrib.auth.models import AbstractUser
from datetime import datetime,time


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hrms:dept_detail", kwargs={"pk": self.pk})
    
class BD(models.Model):
    Details = (('tea','TEA'), ('lunch', 'LUNCH'),('bio', 'BIO'),('other', 'OTHER'))
    detail = models.CharField(choices=Details, max_length=15 ,default=False)
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    thumb = models.ImageField()
    # GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    # gender = models.CharField(choices=GENDER, max_length=15 ,default=False)
    Gender = models.CharField(max_length=20) 
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    address = models.TextField(max_length=100, default='')
    Designation = models.CharField(max_length=20 ,null=True, blank=True)
    Date_of_joining = models.DateField(verbose_name='Select a date', help_text='Please choose a date.',null=True, blank=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    salary = models.CharField(max_length=16)      
    def __str__(self):
        return self.first_name
        
    def get_absolute_url(self):
        return reverse("hrms:employee_view", kwargs={"pk": self.pk})




class Kin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    occupation = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    employee = models.OneToOneField(User,on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.first_name+'-'+self.last_name
    
    def get_absolute_url(self):
        return reverse("hrms:employee_view",kwargs={'pk':self.employee.pk})
    

class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField(null=True)
    last_out = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first = models.DateTimeField(null=True)
    last = models.DateTimeField(null=True)
    wh = models.CharField(null=True, max_length=50)
    TBT = models.CharField(default='00:00:00.000', max_length=50)
    twh = models.CharField(null=True, max_length=50)

    
    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)

class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start

class Recruitment(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    position = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name +' - '+self.position
#break

class Break(models.Model):
    date = models.DateField(auto_now_add=True)
    break_in = models.TimeField(null=True)
    break_out = models.TimeField(null=True)
    TBT = models.CharField(null=True, max_length=50, default='00:00:00.00')
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bi = models.DateTimeField(null=True)
    bo = models.DateTimeField(null=True)
    # STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    # status = models.CharField(choices=STATUS, max_length=15 )
    # def __str__(self):
    #         return self.first_name +' - '+self.last_name

