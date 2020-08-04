from django.urls import path
from student.views.classes import NewClass, ClassList, IndividualClassDetails
from django.conf.urls import url

urlpatterns = [
    path('create/', NewClass.as_view(), name='create classes'),
    path('list/', ClassList.as_view(), name='list all classes'),
    url(r'^update/(?P<pk>\d+)/$', IndividualClassDetails.as_view(),name='class-detail'),
]