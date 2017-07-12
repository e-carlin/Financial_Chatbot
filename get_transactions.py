# import datetime
# import plaid

# PLAID_CLIENT_ID = '5942d7e2bdc6a41b5e16d1be'
# PLAID_SECRET = '0cea2489640aa411ce6dec5ad46d3f'
# PLAID_PUBLIC_KEY = 'fb846942c3ce8e2945b4b1fd408333'
# PLAID_ENV='sandbox'

# client = plaid.Client(client_id = PLAID_CLIENT_ID, secret=PLAID_SECRET,
#                   public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV)

#   # Pull transactions for the last 30 days
# start_date = "{:%Y-%m-%d}".format(datetime.datetime.now() + datetime.timedelta(-1))
# end_date = "{:%Y-%m-%d}".format(datetime.datetime.now())

# try:
#     response = client.Transactions.get(
#     	access_token="access-sandbox-60766603-c671-4c43-bc59-79c1b7ba3fd3", 
#     	start_date=start_date, 
#     	end_date=end_date)

#     print(response)
# except plaid.errors.PlaidError as e:
# 	print({'error': {'error_code': e.code, 'error_message': str(e)}})


from background_task import background

@background(schedule=5)
def do_thing():
    # lookup user by id and send them a message
    print("EXECUTED")

do_thing()