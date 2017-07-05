from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.TextField(max_length=15, unique=True, primary_key=True)
    blance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)