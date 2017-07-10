from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def welcome(request):
	return render(request, 'welcome.html')

@login_required
def show_users(request):
	users = User.objects.all()
	for user in users:
		print(str(user))
	return render(request, 'show_users.html', {'users': users})

@login_required
def show_account(request):
	return render(request, 'show_account.html')