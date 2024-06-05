from django.contrib import admin
from .models import User,Department,Attendance,Kin,Break
# Register your models here.
admin.site.register([User,Department,Attendance,Kin, Break,])
