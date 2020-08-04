from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from student.models import Student
from student.serializers.student import StudentSerializer, StudentDetailsSerializer


class NewStudent(ListCreateAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': StudentSerializer,
            'POST': StudentDetailsSerializer
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

class StudentList(ListAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': StudentSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Section.objects.all()
        return queryset

class IndividualStudentDetails(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': StudentSerializer,
            'POST': StudentDetailsSerializer,
            'PATCH': StudentDetailsSerializer,
            'DELETE': StudentDetailsSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Section.objects.all()
        return queryset