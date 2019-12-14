from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone

from django.db import models


#Create user profile 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.IntegerField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    


    