from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import date, datetime, time
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['birthday','telephone']
        

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(required=True)

    class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'userprofile', 'email','password',]



    def create(self,  validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],

        )

        user_profile_data = validated_data.pop('userprofile')
        # create user profile
        profile = UserProfile.objects.create(
            user = user,
            telephone = user_profile_data['telephone'],
            birthday = user_profile_data['birthday'],
        )

        
        user.set_password(validated_data['password'])

        user.save()
        return user