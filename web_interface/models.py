from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=False, primary_key=True, on_delete=models.PROTECT)
    phone_number = models.TextField(max_length=15, unique=True, null=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Account(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, primary_key=True)
	access_token = models.TextField(max_length=100, null=False)
	item_id = models.TextField(max_length=100, null=False)


# access token: access-sandbox-60766603-c671-4c43-bc59-79c1b7ba3fd3
# item ID: LvzlemE6qZURGxyW97GafD67w8eMXGSABWe1w
