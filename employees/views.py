from django.shortcuts import render
from employees.models import Employee

def home(request):
    employees = Employee.objects.all()  # Fixed variable name
    context = {
        'employees': employees,
    }
    print(employees)  # This will print the QuerySet to the console
    return render(request, 'home.html', context)
