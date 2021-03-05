from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import *

# Create your views here.

def home(request):
	return render(request, 'appusers/home.html')


def user_register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registered = True
			return redirect('login')
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	context = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}
	return render(request, 'appusers/register.html', context)


def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return redirect('home')
			else:
				return HttpResponse('Account is deactivated')
		else:
			return HttpResponse('Please use valid username and password')


	return render(request, 'appusers/login.html')


@login_required
def user_logout(request):
	if request.user is not None:
		logout(request)
	return redirect('home')


def contact(request):
	return render(request, 'appusers/contact.html')


def about(request):
	return render(request, 'appusers/about.html')


def career(request):
	return render(request, 'appusers/career.html')