from django.contrib import admin

from Students.models import Departments, Students


admin.site.register(Departments)
admin.site.register(Students)
# @admin.register(Departments)
# class DepartmentsModelAdmin(admin.ModelAdmin):
#     list_display = [
#          'ID', 
#     'Department_ID', 
#     'Departments' 
#     ]

# @admin.register(Students)    
# class StudentsModelAdmin(admin.ModelAdmin):
#     list_display = [
#         'ID','Name','EnRoll_ID','Department_Name','Email','Gender','Date_Of_Joining','Address','Photo_Name','Documents_Name'
#     ]