from rest_framework import serializers
from student.models import Class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id','class_name', 'class_strength', 'created_at', 'updated_at']

class NewClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'class_strength']