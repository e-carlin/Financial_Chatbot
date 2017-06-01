from rest_framework.views import APIView # For SMS
from django.http import HttpResponse # For SMS
from .serializers import UserSerializer 
from .models import User

from twilio.twiml.messaging_response import MessagingResponse

class SMSView(APIView):
	def post(self, request, *args, **kwargs):
	    print(" ***** SMS Got a POST ****")
	    twilio_resp = MessagingResponse() #our response


	    print("**** DATA: "+str(request.data.dict()))
	    request_dict = request.data.dict()
	    message = request_dict['Body']
	    from_phone = request_dict['From']

	    print("***** Message: "+message+" Phone: " + from_phone+" *****")
	    twilio_resp.message("Hi from API!")
	    return HttpResponse(str(twilio_resp))



	def get(self, request, *args, **kwargs):
	    print(" ***** SMS Got a GET")
	    resp = MessagingResponse()
	    resp.message("The Robots are coming! Head for the hills!")
	    return HttpResponse(str(resp))