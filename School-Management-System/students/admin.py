from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StudentClassInfo)
admin.site.register(StudentSectionInfo)
admin.site.register(StudentShiftInfo)
admin.site.register(StudentInfo)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'status', 'date']
admin.site.register(Attendance, AttendanceAdmin)

