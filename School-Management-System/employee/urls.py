from django.urls import path
from . import views

urlpatterns = [
    path('allemployees', views.employee_list, name='employee_list'),
    path('registration', views.create_employee, name='create_employee'),
]

