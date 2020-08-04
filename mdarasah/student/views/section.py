from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from student.models import Section
from student.serializers.section import SectionSerializer, SectionDetailsSerializer


class NewSection(ListCreateAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': SectionSerializer,
            'POST': SectionDetailsSerializer
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Section.objects.all()
        return queryset

class SectionList(ListAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': SectionSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Section.objects.all()
        return queryset

class IndividualSectionDetails(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        switcher = {
            'GET': SectionSerializer,
            'PUT': SectionDetailsSerializer,
            'PATCH': SectionDetailsSerializer,
            'DELETE': SectionDetailsSerializer,
        } 
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = Section.objects.all()
        return queryset