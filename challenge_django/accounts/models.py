from django.contrib.auth.models import User
from django.db.models.signal import post_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone

from django.db import models


#Create user profile 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

    