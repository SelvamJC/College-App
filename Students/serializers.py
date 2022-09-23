from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Students.models import Departments, Students

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'          