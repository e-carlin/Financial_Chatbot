from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.TextField(max_length=15, unique=True, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

# class Items(models.Model):
# 	user = models.


# access token: access-sandbox-60766603-c671-4c43-bc59-79c1b7ba3fd3
# item ID: LvzlemE6qZURGxyW97GafD67w8eMXGSABWe1w
