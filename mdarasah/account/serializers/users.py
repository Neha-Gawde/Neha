from rest_framework import serializers
from account.models import User
from rest_framework.exceptions import ValidationError
import re
# to show all users info
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username','is_teacher', 'is_student', 'is_parent', 'is_staff', 'is_superuser']

class CreateuserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name' ,'last_name','password1', 'password2', 'is_admin', 'is_subadmin']
    
    def check_if_exists(self,email):
        email_status = User.objects.filter(email=email).exists()
        if email_status == True:
            return True
        return False
    
    def validate_email(self,email):
     # Check if user already exist
        if self.check_if_exists(email) == True:
            raise ValidationError(
                {'Email': ["User with this details already exists"]}
                )
        return email 
 
    # Validation to create a strong password
    # Length - 8,1 Upper,1lower,1 num, 1 special
    def IsPasswordStrong(self,password):
       return bool(re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",password))
    
    def create(self, validated_data):
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']

        if validated_data['password1'] == validated_data['password2']:
            password = validated_data['password1']
            if self.IsPasswordStrong(password) == False:
                raise ValidationError({'password':'Password is not complex.'})
        else:
            raise ValidationError(
                {'Password':"Both Passwords dont match"})
        user = User.objects.create_user(email=email,first_name=first_name,last_name=last_name,username=username,password=password)
        return user


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Password must match'})
        user.set_password(password)
        user.save()    
        return user