from django.contrib import admin
from .models import Department,Student,Lecturer


class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','depname','depintake']
admin.site.register(Department,DepartmentAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','stuname','sturollno','stuaddress','stumarks','department']
admin.site.register(Student,StudentAdmin)

class LecturerAdmin(admin.ModelAdmin):
    list_display=['id','lecname','lecsal','lecsub','written_by']
admin.site.register(Lecturer,LecturerAdmin)
