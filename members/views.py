from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import UserCreateForm # , UserUpdateForm, CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
# from mainapp.models import Article, Comment
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from .models import Customer


def logout(request):
    django_logout(request)
    return redirect('home')

def register(request):
	error = ''
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST.get('username')  
			password = request.POST.get('password1')  
			user = authenticate(request, username = username, password = password)
			if user is not None: 
				login(request, user)
				return redirect('home')
		else:
			error = 'Логин бос емес немесе құпия сөздер сәйкес емес!'
			data = {
				'register_form':form,
				'message':error,
			}
			return render(request, 'members/register.html', data)
	else:
		form = UserCreateForm()
	return render(request, 'members/register.html', {'register_form':form})

def authentication(request):
	error = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None: 
			login(request, user)
			return redirect('home')
		else:
			error = 'Логин и пароль не совпадает, повторите попытку!'
			return render(request, 'members/auth.html', {'error':error})	
	return render(request, 'members/auth.html')

def members_view(request):
	return render(request, 'members/members.html')