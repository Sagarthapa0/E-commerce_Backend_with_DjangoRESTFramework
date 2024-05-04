from rest_framework import serializers
from .models import User




class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)


class LogoutSerializer(serializers.Serializer):
    token=serializers.CharField(required=True)


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password','email']

    def create(self, validated_data):
        username= validated_data.get('username',None)
        email= validated_data.get('email',None)
        password= validated_data.get('password',None)
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username','email',]
    
