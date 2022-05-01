from django.contrib import admin
from.models import Student

# Register your models here.
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=['id','rollnumber','name','lname','attendance','time_of_attendance']
