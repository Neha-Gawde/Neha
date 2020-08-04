from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from account.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from account.serializers.users import UserSerializer, RegistrationSerializer, CreateuserSerializer

# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     # authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)


#list all users
class UserListView(ListAPIView):
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAdminUser]
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

#creates new user
class NewUserAPIView(ListCreateAPIView):
    # serializer_class = CreateuserSerializer
    def get_serializer_class(self):
        switcher = {
            'GET': UserSerializer,
            'POST': CreateuserSerializer,
        }
        return switcher[self.request.method]
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

class UserDetailsView(RetrieveUpdateDestroyAPIView):
    # serializer_class = CreateuserSerializer
    def get_serializer_class(self):
        switcher = {
                'GET' : UserSerializer,
                'PUT' : UserSerializer,
                'PATCH' : UserSerializer,
                'DELETE' : UserSerializer,
            }
        return switcher[self.request.method]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset




#need Registration form
@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Sucessfully registered a new user"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)