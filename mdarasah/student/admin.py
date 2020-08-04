from django.contrib import admin

# Register your models here.
from student.models import Student, Class , Section

admin.site.register(Section)
admin.site.register(Class)
admin.site.register(Student)