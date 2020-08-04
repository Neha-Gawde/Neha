from django.urls import path , include
from teacher.views.teachers import NewTeacher, ListofTeachers, TeacherDetails
from django.conf.urls import url

urlpatterns = [
    path('create/', NewTeacher.as_view(), name='create teachers'),
    path('list/', ListofTeachers.as_view(), name='list all teachers'),
    url(r'^update/(?P<pk>\d+)/$',TeacherDetails.as_view(),name='edit techers details'),
]