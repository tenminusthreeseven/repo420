from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='employee_home'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),  # Correct function name
]
