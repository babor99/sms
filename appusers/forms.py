from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class UserForm(UserCreationForm):
	email = forms.EmailField()
	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		labels = {'password1':'Password', 'password2':'Confirm Password'}

class UserProfileForm(forms.ModelForm):
	bio = forms.CharField(required=False)
	student = 'student'
	parent = 'parent'
	user_types = [(student,'student'), (parent,'parent')]
	user_type = forms.ChoiceField(required=True, choices=user_types)
	class Meta():
		model = UserProfile
		fields = ('bio', 'profile_pic', 'user_type')