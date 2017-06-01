from rest_framework.views import APIView # For SMS
from django.http import HttpResponse # For SMS
from .serializers import UserSerializer 
from .sms_parser import respond_to_request


class SMSView(APIView):
	def post(self, request, *args, **kwargs):
	    print(" ***** SMS Got a POST ****")
	    return HttpResponse(respond_to_request(request))


	def get(self, request, *args, **kwargs):
	    print(" ***** SMS Got a GET")
	    resp = MessagingResponse()
	    resp.message("WHAT, Why was a GET triggered!!????")
	    return HttpResponse(str(resp))