from django.shortcuts import render
from django.http import Http404
from employees.models import Employee


def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)


def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        raise Http404("Employee not found")

    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)
