from django.shortcuts import render,HttpResponse
from .models import Employee,Role
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        emp_id = int(request.POST['emp_id'])
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        salary = int(request.POST['salary'])
        phone = str(request.POST['phone'])
        print("emp id", emp_id)
        roleName = request.POST['role']
        role = Role(name= roleName)
        role.save()
        new_emp = Employee(emp_id=emp_id, first_name=first_name, last_name=last_name, gender=gender, salary=salary, role=role, phone=phone)
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif request.method =='GET':

         return render(request, 'add_emp.html')
    else:

         return HttpResponse("An Exception Occured! Employee has not been added")
def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(emp_id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter a valid emp id")
    emps = Employee.objects.all()
    context = {
       'emps' : emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) |Q(last_name__icontains = name))
        if role:
            emps = emps.filter(role__name__icontains = role)
        context = {
            'emps':emps
        }
        return render(request, 'view_all_emp.html',context)
    elif request.method =='GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')
