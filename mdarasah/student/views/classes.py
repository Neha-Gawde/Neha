from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from student.models import Class
from student.serializers.classes import ClassSerializer, NewClassSerializer


class NewClass(ListCreateAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': ClassSerializer,
            'POST': NewClassSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Class.objects.all()
        return queryset

class ClassList(ListAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': ClassSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Class.objects.all()
        return queryset
        
class IndividualClassDetails(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': ClassSerializer,
            'POST': NewClassSerializer,
            'PUT': NewClassSerializer,
            'PATCH': NewClassSerializer,
            'DELETE': NewClassSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Class.objects.all()
        return queryset