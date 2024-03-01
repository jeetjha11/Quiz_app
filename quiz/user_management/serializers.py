from rest_framework import serializers

from .models import UserModel, LoginModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = '__all__'
