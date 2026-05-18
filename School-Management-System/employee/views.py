from django.shortcuts import render
from .models import *

# Create your views here.
def employee_list(request):
    official_info = OfficialInfo.objects.all()
    context = {
        "official_info": official_info
    }
    return render(request, "employee/employee_list.html", context)


def create_employee(request):
    personal_info = PersonalInfo.objects.all()
    context = {
        "personal_info": personal_info
    }
    return render(request, "employee/registration.html", context)


