from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request, 'view_all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept= int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        emps = Employee.objects.all()
        context = {
            'emps':emps
        }
        print(context)
        return redirect('all_emp')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An error occured!")
    

def rem_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect('all_emp')
        except:
            return HttpResponse("goooo")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'view_all_emp.html',context)

def fil_emp(request):
    if request.method == "GET":
        search_result = request.GET['search']
        
        emps = Employee.objects.all()
        if Q:
            emps = emps.filter(Q(first_name__icontains = search_result) | Q(last_name__icontains = search_result) | Q(dept__name__icontains = search_result) | Q(dept__location__icontains = search_result) | Q(role__name__icontains = search_result))
        context = {
        'emps' : emps
        }
        return render(request, 'view_all_emp.html',context)
    elif request.method=='POST':
        return render(request,'filter_emp.html')  
    else:
        return HttpResponse("An error occured!")
        
    
def edit_emp(request, emp_id = 0):
     emp = Employee.objects.get(id=emp_id)
     context = {
         'emp': emp,
     }
     return render(request, 'edit_emp.html', context)


def update_emp(request, emp_id=0):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept= int(request.POST['dept'])
        role = int(request.POST['role'])
        emp = Employee(id=emp_id, first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        emp.save()
        return redirect('all_emp')
    return redirect(request, 'view_all_emp.html')