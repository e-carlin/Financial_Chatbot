from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    blance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)