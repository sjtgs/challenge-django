from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone

from django.db import models


#Create user profile 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday =  models.DateField(null=True, blank=True)
    telephone = models.IntegerField(max_length=100, unique=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    


    