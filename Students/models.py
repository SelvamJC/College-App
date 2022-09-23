from django.db import models

class Departments(models.Model):
    ID = models.AutoField(primary_key=True)
    Department_ID = models.IntegerField()
    Departments = models.CharField(max_length=150)

class Students(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    EnRoll_ID = models.IntegerField()
    Department_Name = models.CharField(max_length=150)
    Email = models.EmailField()
    Gender = models.CharField(max_length=30)
    Date_Of_Joining = models.DateField()
    Address = models.CharField(max_length=200)
    Photo_Name = models.ImageField(upload_to = 'images', blank = True)
    Documents_Name = models.FileField(upload_to='documents' , blank=True)

