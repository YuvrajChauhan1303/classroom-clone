from django.contrib import admin
from .models import Classroom, StudentClassroom, TeacherClassroom
# Register your models here.


admin.site.register(Classroom)
admin.site.register(StudentClassroom)
admin.site.register(TeacherClassroom)