
from teacher.models import Teacher
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from teacher.serializers.teachers import TeacherSerializer, TeacherDetailSerializer
from rest_framework.response import Response

class NewTeacher(ListCreateAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': TeacherSerializer,
            'POST': TeacherDetailSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset

class ListofTeachers(ListAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': TeacherSerializer
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset

class TeacherDetails(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': TeacherSerializer, 
            'PUT': TeacherDetailSerializer ,
            'PATCH': TeacherDetailSerializer,
            'DELETE': TeacherDetailsSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset



