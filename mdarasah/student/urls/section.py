from django.urls import path
from student.views.section import NewSection, SectionList, IndividualSectionDetails
from django.conf.urls import url

urlpatterns = [
    path('create/', NewSection.as_view(), name='create section'),
    path('list/', SectionList.as_view(), name='list all Section'),
    url(r'^update/(?P<pk>\d+)/$', IndividualSectionDetails.as_view(),name='Section-detail'),
]