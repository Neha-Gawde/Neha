from rest_framework import serializers
from student.models import Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'class_teacher_id','section_name', 'class_id', 'created_at', 'updated_at']


class SectionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'class_teacher_id','section_name', 'class_id']