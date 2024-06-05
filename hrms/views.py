from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models  import User, Department,Kin, Attendance, Leave, Recruitment, Break
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from .forms import RegistrationForm,LoginForm,EmployeeForm,KinForm,DepartmentForm,AttendanceForm, LeaveForm, RecruitmentForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from datetime import datetime, date,timedelta
from django.shortcuts import  HttpResponse
import csv
import requests
import json
import os
import openpyxl
from django.conf import settings


if len(Attendance.objects.values())==0:
    for i in User.objects.all():
            new = Attendance()
            new.staff = i
            new.status = "ABSENT"
            new.date = date.today()

            new.save()
elif Attendance.objects.values().last()['date'] != date.today() :
    for i in User.objects.all():
        new = Attendance()
        new.staff = i
        new.status = "ABSENT"
        new.date = date.today()
        new.save()
if len(Break.objects.values())==0:
    for i in User.objects.all():
            new = Break()
            new.staff = i
            # new.status = "ABSENT"
            new.date = date.today()

            new.save()
elif Break.objects.values().last()['date'] != date.today() :
    for i in User.objects.all():
        new = Break()
        new.staff = i
        # new.status = "ABSENT"
        new.date = date.today()
        new.save()


# Create your views here.
class Index(TemplateView):
   template_name = 'hrms/home/home.html'

#   Authentication
class Register (CreateView):
    model = get_user_model()
    form_class  = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')
    
class Login_View(LoginView):
    model = get_user_model()
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'

    def get_success_url(self):
        url = resolve_url('hrms:dashboard')
        return url

class Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:login',permanent=True)
    

 # Main Board   
class Dashboard(LoginRequiredMixin,ListView,):
    template_name = 'hrms/dashboard/index.html'
    login_url = 'hrms:login'
    model = User
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = User.objects.all().filter(is_superuser = 0).count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.filter(is_superuser = 1).count()
        context['workers'] = User.objects.order_by('-id').filter(is_superuser=0)
        return context
    # def get_twh(emp_id):
        # a12 = Attendance.objects.get(pk = self.kwargs['pk'])
        # a11 = super().get_twh(**kwargs)
        # a12 = Attendance.objects.get(id = emp_id)
        # a11['twh'] = a12
        # print(a12)
        # pds = User.objects.get(Q(staff__id=self.kwargs['pk']))
        # q = Attendance.objects.filter(staff=pds)
        # print(pds)
# def get_employee_name(request,id):
#     a1 = Attendance.objects.get(pk=staff_id)
#     a1.twh = twh
#     a1.save()
#     return HttpResponse('aadfdfadsfasdfadsfadsfasdsdf')
# def display_employee(request, staff_id):
#     employee = Attendance.objects.get(pk=staff_id)
#     value = employee.value
#     context = {
#         'employee': employee,
#         'value': value
#     }
#     return HttpResponse('faeffewff')
#     print(context)

    # attendance = Attendance.objects.filter(staff_id=id).last()
        # # if attendance:
    # a1 = attendance.twh
        # print(a2)
    # a1 = Attendance.objects.values(id).last()['twh']
    # print(a1)
        # time_object = datetime.strptime(a2, "%H:%M:%S.%f")
        # time_integer = int(time_object.strftime("%H%M%S"))
        # print(time_integer)
        # if time_integer >= 0:
        #     print('done')
        # else:
        #     print('ND')  
        # if id == 2:
    # return HttpResponse('<h1> hello guyz </h1>')
        # else:
        #     return HttpResponse('gfafwe')

class Employee_New(CreateView):
    model = get_user_model() 
    form_class = EmployeeForm  
    template_name = 'hrms/employee/create.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    success_url = reverse_lazy('hrms:dashboard')
    
    
    
class Employee_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/employee/index.html'
    model = get_user_model()
    login_url = 'hrms:login'
    context_object_name = 'employees'
    paginate_by  = 5
    
class Employee_View(LoginRequiredMixin,DetailView):
    queryset = User.objects.select_related('department')
    template_name = 'hrms/employee/single.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context
        
class Employee_Update(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'hrms/employee/edit.html'
    form_class = EmployeeForm
    login_url = 'hrms:login'
    
    
class Employee_Delete(LoginRequiredMixin,DeleteView):
    pass

class Employee_Kin_Add (LoginRequiredMixin,CreateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_add.html'
    login_url = 'hrms:login'
   

    def get_context_data(self):
        context = super().get_context_data()
        if 'id' in self.kwargs:
            emp = User.objects.get(pk=self.kwargs['id'])
            context['emp'] = emp
            return context
        else:
            return context

class Employee_Kin_Update(LoginRequiredMixin,UpdateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_update.html'
    login_url = 'hrms:login'

    def get_initial(self):
        initial = super(Employee_Kin_Update,self).get_initial()
        
        if 'id' in self.kwargs:
            emp =  User.objects.get(pk=self.kwargs['id'])
            initial['employee'] = emp.pk
            
            return initial

#Department views

class Department_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = User.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Department_New (LoginRequiredMixin,CreateView):
    model = Department
    template_name = 'hrms/department/create.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'

class Department_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')

#Attendance View

class Attendance_New (LoginRequiredMixin,CreateView):
    model = Attendance
    form_class = AttendanceForm
    login_url = 'hrms:login'
    template_name = 'hrms/attendance/create.html'
    success_url = reverse_lazy('hrms:attendance_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.localdate()
        pstaff = Attendance.objects.all()


        context['present_staffers'] = pstaff
        # for i in pstaff:
        #     if i.last and i.first:
        #         print(i.wh)



        return context

class Attendance_Out(LoginRequiredMixin,View):
    login_url = 'hrms:login'

    def get(self, request,*args, **kwargs):
       user = Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(date=timezone.localdate()))
       user.last_out = datetime.now()
       user.last = datetime.now()

       user.save()
       user = Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(date=timezone.localdate()))
       user.wh = user.last - user.first
       dt = datetime.strptime(user.TBT, "%H:%M:%S.%f")
       total_sec = dt.hour*3600 + dt.minute*60 + dt.second  # total seconds calculation
       td = timedelta(seconds=total_sec)     
       user.twh = (user.last - user.first) - td
        
       user.save()


       return redirect('hrms:attendance_new')
    


class LeaveNew (LoginRequiredMixin,CreateView, ListView):
    model = Leave
    template_name = 'hrms/leave/create.html'
    form_class = LeaveForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:leave_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leaves"] = Leave.objects.all()
        return context

class Payroll(LoginRequiredMixin, ListView,):
    model = User
    template_name = 'hrms/payroll/index.html'
    login_url = 'hrms:login'
    context_object_name = 'stfpay'
   
    # def salary():
    #     print('start')
    #     # staff_id = request.get['pk']
    #     staff_id = 3
    #     user = User.objects.get(id=staff_id)
    #     print(user)

    #     salary = float(user.salary)
    #     print(salary)

    #     if salary == 0:
    #         sal_per_day = 0
    #     else:    
    #         sal_per_day = salary / 25

    #     is_present = Attendance.objects.filter(staff=staff_id)
    #     print(is_present[0].status)

    #     count = 0
        
    #     for i in range(len(is_present)):
    #         if is_present[i].status == "PRESENT":
    #             count += 1

    #     print(count)
    #     total_sal = sal_per_day * count
    #     print(total_sal)
        
    # salary()
class RecruitmentNew (CreateView):
    model = Recruitment
    template_name = 'hrms/recruitment/index.html'
    form_class = RecruitmentForm
    success_url = reverse_lazy('hrms:recruitment')

class RecruitmentAll(LoginRequiredMixin,ListView):
    model = Recruitment
    login_url = 'hrms:login'
    template_name = 'hrms/recruitment/all.html'
    context_object_name = 'recruit'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = requests.get("https://script.googleusercontent.com/macros/echo?user_content_key=U7MEkkhMUwRt3KrET5iL0gkmCzyTKb52PDnjuHi5NlOd6rnzrq2X1PR2zYe1bU9ABXrJRDGw99sDlPhxj3_Khl1HOBbG4P1pm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnAi2aJZGbP2FVRDstJrcUxI3al7Y5mCrv9NHX_PRqzx2tabxNITQD8yd8VLn0xbjSPAFzgbcuN1KEwOFBTjDbW4zpm50RqvrZA&lib=ME2YbkWRlb0EHiAseivp7PHA-nDy3ldf7").json()
        # print(data)
        
        newdata = []
        for i in data:
            newdata.append({"first":i['First Name'],"last": i['Last Name'],"mobile": i['Mobile Number'],"email": i['Personal Email ID'] , "Qualification":i['Qualification'],"Experience":i['Fresher/Experience ']})
        # print(newdata)
        context['data'] = newdata
        return context

class RecruitmentDelete (LoginRequiredMixin,View):
    login_url = 'hrms:login'
    def get (self, request,pk):
     form_app = Recruitment.objects.get(pk=pk)
     form_app.delete()
     return redirect('hrms:recruitmentall', permanent=True)

class Pay(LoginRequiredMixin,ListView):
    model = User
    template_name = 'hrms/payroll/index.html'
    context_object_name = 'emps'
    login_url = 'hrms:login'

class Report(LoginRequiredMixin,ListView):
    model = Attendance
    template_name = 'hrms/attendance/report/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.localdate()
        pstaff = Attendance.objects.all()
        context['present_staffers'] = pstaff
        return context
# break     
class Break_new(LoginRequiredMixin,ListView):
    model = Break
    template_name = 'hrms/Breaks/break.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.localdate()


        pstaff = Break.objects.all()


        context['present_staffers'] = pstaff
        return context

class Break_in(LoginRequiredMixin,View):
   
    
    def get(self, request,*args, **kwargs):
        user=Break.objects.get(Q(staff__id=self.kwargs['pk']) & Q(date=timezone.localdate()))
        user.break_in = datetime.now()
        user.bi = datetime.now()
        print(user.staff.first_name)
        user.save()
        return redirect('hrms:break')
    
class Attendance_In(LoginRequiredMixin,View):
    login_url = 'hrms:login'

    def get(self, request,*args, **kwargs):
       user=Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(date=timezone.localdate()))
       user.first_in = datetime.now()
       user.first = datetime.now()

       user.status="PRESENT"
       user.save()
       return redirect('hrms:attendance_new')
class Break_out(LoginRequiredMixin,View):


    def get(self, request,*args, **kwargs):
        user=Break.objects.get(Q(staff__id=self.kwargs['pk']) & Q(date=timezone.localdate()))
        user.break_out = datetime.now()  
        user.bo = datetime.now()
        user.save()


        user = Break.objects.get(Q(staff__id=self.kwargs['pk']) & Q(date=timezone.localdate()))
        print(user.bo)
        print(user.bi)
        user.TBT = user.bo - user.bi
        bt =  user.bo - user.bi
        user.save()
        

        user = Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(date=timezone.localdate()))
        print(bt)
        user.TBT = str(datetime.strptime(user.TBT, "%H:%M:%S.%f") +  bt)[11:]
        user.save()


        
        return redirect('hrms:break')

def export_table_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance.csv"'

    # Get the data from the table
    data = Attendance.objects.all()

    # Write the data to the CSV file
    writer = csv.writer(response)
    writer.writerow(['date' , 'first_in' , 'last_out' , 'status' , 'staff' , 'first' , 'last' , 'wh' , 'TBT'])
    for row in data:
        writer.writerow([row.date, row.first_in, row.last_out , row.status , row.staff , row.first , row.last , row.wh , row.TBT])

    return response








###################


def import_api_data_to_excel(request):
    api_url = 'https://script.googleusercontent.com/macros/echo?user_content_key=U7MEkkhMUwRt3KrET5iL0gkmCzyTKb52PDnjuHi5NlOd6rnzrq2X1PR2zYe1bU9ABXrJRDGw99sDlPhxj3_Khl1HOBbG4P1pm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnAi2aJZGbP2FVRDstJrcUxI3al7Y5mCrv9NHX_PRqzx2tabxNITQD8yd8VLn0xbjSPAFzgbcuN1KEwOFBTjDbW4zpm50RqvrZA&lib=ME2YbkWRlb0EHiAseivp7PHA-nDy3ldf7'
  

    response = requests.get(api_url)
    data = response.json()  # Assuming the API returns JSON data

    # Create a new Excel workbook and get the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write headers to the first row of the sheet
    headers = ['First Name', 'Last Name', 'Mobile Number' , 'Personal Email ID' , 'Qualification' ,'Qualification (Course Name)', 'Fresher/Experience ' , 'Date Of Birth ', 'Gender ' , 'Father Name' ,'Aadhaar Card Number' , 'Present Address' , 'permanent Address','Area Name ','Pin code','Language ','Last Company Name & Designation ','Last Salary (Monthly)','Are You the Single Earner In your Family ? ' , 'Current City Name ', 'State ', 'Are You From Village or City?' , 'How did you Know About Us?','Write source Name ']  # Replace with your column names
    sheet.append(headers)

    # Write data to subsequent rows
    for item in data:
        row = [item['First Name'], item['Last Name'], item['Mobile Number'] , item['Personal Email ID'], item['Qualification'],item['Qualification (Course Name)'], item['Fresher/Experience '], item['Date Of Birth '],item['Gender '], item['Father Name'] , item['Aadhaar Card Number'], item['Present Address'], item['permanent Address'],item['Area Name '],item['Pin code'],item['Language '],item['Last Company Name & Designation '], item['Last Salary (Monthly)'], item['Are You the Single Earner In your Family ? '],item['Current City Name '],item['State '],item['Are You From Village or City?'],item['How did you Know About Us?'],item['Write source Name '] ]  # Replace with your field names
        sheet.append(row)

    # Save the workbook
    file_path = os.path.join(settings.MEDIA_ROOT, 'mydata.xlsx')  # Replace with the desired file path
   
    workbook.save(file_path)

    # Return the Excel file as a download response
    with open(file_path, 'rb') as excel_file:
        response = HttpResponse(content=excel_file.read())
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response['Content-Disposition'] = 'attachment; filename=mydata.xlsx'

    return response

# class ButtonPressView(View):
#     def post(self, request):
#         # if 'button_press' in request.POST:
#         #     button_press = ButtonPress.objects.create()
#         #     button_press.save()
#         #     return render(request, 'index.html')
#         return render(request, 'a2.html')
