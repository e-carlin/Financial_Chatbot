import plaid
import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Plaid API keys
PLAID_CLIENT_ID = '5942d7e2bdc6a41b5e16d1be'
PLAID_SECRET = '0cea2489640aa411ce6dec5ad46d3f'
PLAID_PUBLIC_KEY = 'fb846942c3ce8e2945b4b1fd408333'
PLAID_ENV='sandbox'


client = plaid.Client(client_id = PLAID_CLIENT_ID, secret=PLAID_SECRET,
                  public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV)


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
	return render(request, 'show_account.html',
		{'plaid_public_key' : 'fb846942c3ce8e2945b4b1fd408333',
		'plaid_environment' : PLAID_ENV})

#TODO: Django'fy this method and add a url 
# @app.route("/get_access_token", methods=['POST'])
def get_access_token(request):
	print("Getting token")
	print("\n")
	print(request.POST)
	print("\n")
	global access_token
	public_token = request.POST['public_token']
	print("***** PUBLIC "+public_token)
	exchange_response = client.Item.public_token.exchange(public_token)
	print('access token: ' + exchange_response['access_token'])
	print('item ID: ' + exchange_response['item_id'])
	return render(request, 'welcome.html')
