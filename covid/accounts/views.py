from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .forms import SignupForm, LoginForm

from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy

# Create your views here.
def register(request):
	if request.user.is_active:
		return HttpResponse("You're signed in!")
	signup_form 	= SignupForm()
	login_form 		= LoginForm()
	is_user = True

	if request.method == "POST":
		if request.POST.get('email'):
			form = SignupForm(data=request.POST)
			if form.is_valid:
				user = form.save()
				return HttpResponse("You've signed up successfully!")
			else:
				signup_form = form
				is_user 	= False
		else:
			form = LoginForm(data=request.POST)
			if form.is_valid:
				username = request.POST.get("username")
				password = request.POST.get("password")
				user = authenticate(username=username, password=password)

				if user is not None:
					# if user.is_active:
					login(request, user)
					return HttpResponse("You're logged in!")
				else:
					print(user)
			if form.errors:
				login_form = form
	return render(request, 'accounts/register.html', {"signup_form":signup_form, "login_form":login_form, "is_user":is_user})

