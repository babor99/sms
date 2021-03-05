from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('register/', user_register, name='register'),
	path('login/', user_login, name='login'),
	path('user_logout/', user_logout, name='user_logout'),

	path('contact/', contact, name='contact'),
	path('about/', about, name='about'),
	path('career/', career, name='career'),
]