from django.shortcuts import render

from Students.models import Departments, Students
from Students.serializers import DepartmentSerializer, StudentSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class DepartmentView(APIView):

    def get(self, request, format = None):
        department = Departments.objects.all()
        department_serializer = DepartmentSerializer(department, many = True)
        return Response({ 'department':department_serializer.data})


    def post(self,request, format=None):
        department_serializer =DepartmentSerializer(data=request.data)
        if department_serializer.is_valid():
            department_serializer.save()
            return Response({'msg':'Uploaded Successfully...','department':department_serializer.data})
        return Response(department_serializer.errors)    
             
    def put(self, request,id, format=None):
        department = Departments.objects.get(ID=id)
        department_serializer = DepartmentSerializer(department,data=request.data)  
        if department_serializer.is_valid():
            department_serializer.save()
            return Response({'msg':'Updated Successfully...','department':department_serializer.data})
        return Response(department_serializer.errors)      

    def delete(self, request,id, format=None):
        department = Departments.objects.get(ID=id)     
        department.delete()
        return Response({'msg':'Deleteded Successfully...'})

class StudentView(APIView):

    def get(self, request, format = None):
        student = Students.objects.all()
        student_serializer = StudentSerializer(student, many = True)
        return Response({'student':student_serializer.data})


    def post(self,request, format=None):
        student_serializer =StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg':'Uploaded Successfully...','student':student_serializer.data})
        return Response(student_serializer.errors)    
                          
    def put(self, request,id, format=None):
        student = Students.objects.get(ID=id)
        student_serializer = StudentSerializer(student,data=request.data)  
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg':'Updated Successfully...','department':student_serializer.data})
        return Response(student_serializer.errors)          

    def delete(self, request,id, format=None):
        student = Students.objects.get(ID=id)     
        student.delete()
        return Response({'msg':'Deleteded Successfully...'})                       