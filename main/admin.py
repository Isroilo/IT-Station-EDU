from django.contrib import admin
from .models import Payment, User, Reception, Director, Teacher, Student, Group, Course, TeacherSalary

admin.site.register(Payment)
admin.site.register(User)
admin.site.register(Reception)
admin.site.register(Director)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(TeacherSalary)
admin.site.register(Course)