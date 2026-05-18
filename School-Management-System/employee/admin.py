from django.contrib import admin
from .models import OfficialInfo, PersonalInfo

# Register your models here.
admin.site.register(OfficialInfo)
admin.site.register(PersonalInfo)

