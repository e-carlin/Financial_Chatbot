from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


admin.site.unregister(User) #TODO: This is some hack because of an error. comment it out runserver to debug


admin.site.register(User)
admin.site.register(Profile)