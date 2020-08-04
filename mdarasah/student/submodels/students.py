from django.db import models
from datetime import datetime
from account.models import User
from student.models import Class, Section
from parent.models import Parent
class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Studentuser')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='StudentClass')
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, related_name= 'StudentSection')
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name= 'StudentParent')
    admission_no = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Student"