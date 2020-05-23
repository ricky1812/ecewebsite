from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2',)

class ProfileUpdateForm(ModelForm):
	class Meta:
		model=Profile
		fields = [	'year',
					'image',
					'email',
					'fb',
					'phone',
					'linkedIn',
					]