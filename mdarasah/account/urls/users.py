from django.urls import path
from account.views.users import registration_view, NewUserAPIView, UserListView, UserDetailsView
from django.conf.urls import url

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('create/', NewUserAPIView.as_view(), name='create new user'),
    path('list/', UserListView.as_view(), name='list all users'),
    url(r'^update/(?P<pk>\d+)/$',UserDetailsView.as_view(),name='edit user info') 
]
