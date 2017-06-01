from rest_framework.views import APIView # For SMS
from django.http import HttpResponse # For SMS
from django.views import View
from .serializers import UserSerializer 
from .sms_parser import respond_to_request
# ------ For IndexView --------
from rest_framework.response import Response # For GET
from django.http import HttpResponse # For index
from django.shortcuts import render
from .models import User
from .forms import UserForm


class SMSView(APIView):
	def post(self, request, *args, **kwargs):
	    print(" ***** SMS Got a POST ****")
	    return HttpResponse(respond_to_request(request))


	def get(self, request, *args, **kwargs):
	    return Response("You got me")


class IndexView(View):

	def get(self, request, *args, **kwargs):
		# users = User.objects.all()
		# return render(request, 'web_interface/index.html', {'users': users})
		form = UserForm()
		return render(request, 'web_interface/add_user.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = UserForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("You have been added to the db")
		else:
			return HttpResponse("Woops something went wrong!")