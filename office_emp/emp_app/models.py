from django.db import models
from django.contrib import admin

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name
class Employee(models.Model):
    emp_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30, null = False)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.TextField(max_length=50,blank=True,null=True)
    def __str__(self):
        return "%s %s "%(self.first_name,self.last_name )
