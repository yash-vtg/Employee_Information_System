from django.shortcuts import render,redirect
from . models import Employee
from django.contrib import messages

# Create your views here.


def index(req):
    emp=Employee.objects.all()
    empdict={"emp":emp}
    return render(req,"index.html",empdict)


def regsave(request):
    empid=request.POST['empid']
    empname=request.POST['empname']
    department=request.POST['department']
    designation=request.POST['designation']
    salary=request.POST['salary']
    sv=Employee(empid=empid,empname=empname,department=department,designation=designation,salary=salary)
    sv.save()
    return redirect('index')

def empreg(request):
    return render(request,"empreg.html")

def empedit(request, id):
    try:
        sv = Employee.objects.get(empid=id)
    except Employee.DoesNotExist:
        messages.error(request, "Employee not found.")
        return redirect('index.html')
    if request.method == 'POST':
        empname = request.POST.get('empname')
        designation = request.POST.get('designation')
        if empname and designation:
            Employee.objects.filter(empid=id).update(empname=empname, designation=designation)
            messages.success(request, "Employee updated successfully.")
        else:
            messages.error(request, "Please fill in all fields.")
    return render(request,'empedit.html',{'sv':sv})