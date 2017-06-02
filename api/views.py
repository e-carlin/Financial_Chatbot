from rest_framework.views import APIView 
from django.http import HttpResponse
from django.views import View 
from .sms_parser import respond_to_request
# ------ For IndexView --------
from rest_framework.response import Response # For GET
from django.http import HttpResponse # For index
from django.shortcuts import render
from web_interface.models import User


class SMSView(APIView):
	def post(self, request, *args, **kwargs):
	    print(" ***** SMS Got a POST ****")
	    return HttpResponse(respond_to_request(request))


	def get(self, request, *args, **kwargs):
	    return Response("You got me")