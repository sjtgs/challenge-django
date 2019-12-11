from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, time
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .models import *
from django.contrib.auth import get_user_model
from datetime import date, datetime, time
from rest_framework.permissions import AllowAny
from accounts.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from .models import *


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('accountList')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form' : form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'email','birthday', 'password')
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


class CreateUserProfileView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer