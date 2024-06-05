from django.urls import path
from . import views
from .views import import_api_data_to_excel
app_name = 'hrms'
urlpatterns = [

# Authentication Routes
    path('ad', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='reg'),
    path('', views.Login_View.as_view(), name='login'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    # path('dashboard/<int:id>', views.get_employee_name, name='dashboard'),

# Employee Routes
    path('dashboard/employee/', views.Employee_All.as_view(), name='employee_all'),
    path('dashboard/employee/new/', views.Employee_New.as_view(), name='employee_new'),
    path('dashboard/employee/<int:pk>/view/', views.Employee_View.as_view(), name='employee_view'),
    path('dashboard/employee/<int:pk>/update/', views.Employee_Update.as_view(), name='employee_update'),
    path('dashboard/employee/<int:pk>/delete/', views.Employee_Delete.as_view(), name='employee_delete'),
    path('dashboard/employee/<int:id>/kin/add/', views.Employee_Kin_Add.as_view(), name='kin_add'),
    # path('dashboard/button-press/', ButtonPressView.as_view(), name='button_press'),
    path('dashboard/employee/<int:id>/kin/<int:pk>/update/', views.Employee_Kin_Update.as_view(), name='kin_update'),

#Department Routes
    path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
    path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),

#Attendance Routes
    path('dashboard/attendance/in/', views.Attendance_New.as_view(), name='attendance_new'),
    path('dashboard/attendance/<int:pk>/out/', views.Attendance_Out.as_view(), name='attendance_out'),
    path('dashboard/attendance/<int:pk>/in/', views.Attendance_In.as_view(), name='attendance_in'),

#Leave Routes

    path("dashboard/leave/new/", views.LeaveNew.as_view(), name="leave_new"),

#Recruitment

    path("recruitment/",views.RecruitmentNew.as_view(), name="recruitment"),
    path("recruitment/all/",views.RecruitmentAll.as_view(), name="recruitmentall"),
    path("recruitment/<int:pk>/delete/", views.RecruitmentDelete.as_view(), name="recruitmentdelete"),

#Payroll
    path("employee/pay/",views.Pay.as_view(), name="payroll"),


#report
    path('dashboard/report/in/', views.Report.as_view(), name='report'),
#Break
    path('dashboard/break/in/', views.Break_new.as_view(), name='break'),
    path('dashboard/break/<int:pk>/in/', views.Break_in.as_view(), name='break_in'),
    path('dashboard/break/<int:pk>/out/', views.Break_out.as_view(), name='break_out'),

        # export to csv 
path('export-csv/', views.export_table_to_csv, name='export_table_to_csv'),

path('export-data/', import_api_data_to_excel, name='import_api_data_to_excel'),


]