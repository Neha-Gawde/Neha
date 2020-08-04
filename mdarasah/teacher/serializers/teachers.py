from rest_framework import serializers
from teacher.models import Teacher

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'designation']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user_id', 'desigation', 'created_at', 'updated_at']