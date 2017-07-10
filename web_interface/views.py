import plaid
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
	return render(request, 'show_account.html',
		{'plaid_public_key' : 'fb846942c3ce8e2945b4b1fd408333',
		'plaid_environment' : 'sandbox'})

#TODO: Django'fy this method and add a url 
# @app.route("/get_access_token", methods=['POST'])
def get_access_token(request):
	print("Getting token")
	return render(request, 'welcome.html')
  # global access_token
  # public_token = request.form['public_token']
  # exchange_response = client.Item.public_token.exchange(public_token)
  # print 'access token: ' + exchange_response['access_token']
  # print 'item ID: ' + exchange_response['item_id']

  # access_token = exchange_response['access_token']

  # return jsonify(exchange_response)

