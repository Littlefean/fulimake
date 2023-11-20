from django.contrib import admin

# Register your models here.
from .models import (
    Government,
    School, Teacher,
    Student, ClassRoom,
    User, UnionExam,
    Course
)

admin.site.register(Government)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ClassRoom)
admin.site.register(User)
admin.site.register(UnionExam)
admin.site.register(Course)
