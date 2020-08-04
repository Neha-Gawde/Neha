from rest_framework import serializers
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user_id', 'class_id', 'section_id', 'parent_id', 'admission_no', 'created_at', 'updated_at']


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'class_id', 'section_id']