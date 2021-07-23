from django.shortcuts import render, redirect
from .form import employeeForm

from . models import Employee
from . form import employeeForm
# Create your views here.


def emp(request):
    if request.method == "POST":
        form = employeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = employeeForm()

    return render(request, 'index.html', {'form': form})

    #return render(request, 'index.html')


def show(request):
    employee = Employee.objects.all()
    return render(request, "show.html", {'employee': employee})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = employeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

