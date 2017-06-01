from rest_framework.views import APIView # For SMS
from rest_framework.response import Response # For SMS
from .serializers import UserSerializer 
from .models import User

class SMSView(APIView):
	def post(self, request, *args, **kwargs):
	    print(" ***** SMS Got a POST")
	    return Response('This is a POST request')

	def get(self, request, *args, **kwargs):
	    print(" ***** SMS Got a GET")
	    return Response('This is GET request')