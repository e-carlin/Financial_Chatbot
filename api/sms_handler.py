from twilio.twiml.messaging_response import MessagingResponse
from wit import Wit
from web_interface.serializers import UserSerializer
from web_interface.models import User

def handle_message(request):

	request_dict = request.data.dict()

	request_message = get_message(request_dict)
	request_phone = get_request_phone(request_dict)

	response = get_response(request_message, request_phone)
	
	return response


def get_response(request_message, request_phone):

	user = User.objects.get(phone_number=request_phone)
	parsed_request = parse_request(request_message)


	#TODO: Chekc if message is valid
	# if 'entities' not in wit_resp or 'intent' not in wit_resp['entities']:
 #        twilio_resp.message("We can't parse what you asked "+str(wit_resp))

	intent = get_intent(parsed_request)
	print("\n ***************************************")
	print("REQUEST: "+str(request_message))
	print("FROM PHONE: "+str(request_phone))
	print("PARSED REQUEST: "+str(parsed_request))
	print("INTENT: "+intent)
	print("******************************************\n")

	if intent is None:
		return build_response("Intent is NONE! "+str(parsed_request))

	elif intent == 'get_balance':
		return build_response("Hi, {} your balance is: ${:0.2f}".format(user.first_name, user.balance))

	elif intent == 'set_balance':
		user.balance = get_amount(parsed_request)
		user.save()
		return build_response("Hi, {} your balance was updated to: ${:0.2f}".format(user.first_name, user.balance))

	elif intent == 'subtract_from_balance':
		amount = get_amount(parsed_request)
		user.balance -= amount
		user.save()
		return build_response("Hi, {} ${:0.2f} was subtracted from your balance. You have ${:0.2f} remaining".format(user.first_name, amount, user.balance))

	else:
		return build_response("Down at ELSE: "+ str(parsed_request))


def parse_request(message):
	client = Wit(access_token='IND2N4JZSL3GLEX4AIBOJQDYDTYSQALY', actions=actions)
	return client.message(message)


def get_amount(message):
	return message['entities']['amount_of_money'][0]['value']


def get_intent(message):
	return message['entities']['intent'][0]['value']

def build_response(string):
	return str(MessagingResponse().message(string))


def get_message(message):
	return message['Body']


def get_request_phone(message):
	return message['From']

def send(request, response):
    print(response['text'])
    
actions = {
    'send': send,
}
