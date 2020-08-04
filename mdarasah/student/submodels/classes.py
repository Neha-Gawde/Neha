from django.db import models
from datetime import datetime

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    class_strength = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "Class"