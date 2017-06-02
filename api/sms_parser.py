from twilio.twiml.messaging_response import MessagingResponse
# Wit.ai
from wit import Wit
# Environment configuration
from .env_config import access_token as wit_access_token
from web_interface.serializers import UserSerializer
from web_interface.models import User

# Wit.ai send (who knows if I need this), I don't think I do
def send(request, response):
    print(response['text'])
actions = {
    'send': send,
}

def respond_to_request(request):
    """Send a dynamic reply to an incoming text message"""
    print("**** responding to request")
    twilio_resp = MessagingResponse()

    # Get the contents of the POST request
    request_dict = request.data.dict()
    message = request_dict['Body'] # The actual text from the user
    from_phone = request_dict['From'] # The number the text came from

    #TODO: Add try except to see if user exsists in our db
    user = User.objects.get(phone_number=from_phone)
    client = Wit(access_token=wit_access_token, actions=actions)
    wit_resp = client.message(message)
    print('***** Wit.ai response: ' + str(wit_resp))

    if 'entities' not in wit_resp or 'intent' not in wit_resp['entities']:
        twilio_resp.message("We can't parse what you asked "+str(wit_resp))

    elif wit_resp['entities']['intent'][0]['value'] == 'get_balance':
        twilio_resp.message("Hi, {} your balance is: ${}".format(user.first_name, user.balance))

    elif wit_resp['entities']['intent'][0]['value'] == 'set_balance':
        # Update the User balance
        user.balance = wit_resp['entities']['amount_of_money'][0]['value']
        user.save()
        
        #Get their balance to send back to them
        twilio_resp.message("Hi, {} your balance was updated to: ${}".format(user.first_name, user.balance))
    elif wit_resp['entities']['intent'][0]['value'] == 'subtract_from_balance':
        user.balance -= wit_resp['entities']['amount_of_money'][0]['value']
        user.save()

        #Let them know of the change
        twilio_resp.message("Hi, {} ${} was subtracted from your balance. You have ${} remaining".format(user.first_name, wit_resp['entities']['amount_of_money'][0]['value'], user.balance))
    else:
        twilio_resp.message("Not sure what to do..."+str(wit_resp))

    return str(twilio_resp)