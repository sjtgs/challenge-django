from django import forms
from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
	
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ( 'username','email', 'password')


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('username','email','birthday', 'password')