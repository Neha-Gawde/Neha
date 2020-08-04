from django.urls import path
from student.views.student import NewStudent, StudentList, IndividualStudentDetails
from django.conf.urls import url

urlpatterns = [
    path('create/', NewStudent.as_view(), name='create student'),
    path('list/', StudentList.as_view(), name='list all students'),
    url(r'^update/(?P<pk>\d+)/$', IndividualStudentDetails.as_view(),name='edit student details'),    
]