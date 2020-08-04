from django.db import models
from datetime import datetime
from teacher.submodels.teachers import Teacher
from student.submodels.classes import Class
class Section(models.Model):
    class_teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    section_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='Class')

    class Meta:
        db_table = "Section"