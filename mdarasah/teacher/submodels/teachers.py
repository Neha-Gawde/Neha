from django.db import models
from datetime import datetime
from account.submodels.users import User

class Teacher(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user')
    designation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        db_table = "Teacher"