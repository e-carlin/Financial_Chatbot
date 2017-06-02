from django.db import models

class User(models.Model):
    """This class represents the user model."""
    phone_number = models.CharField(max_length=255, blank=False, unique=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    balance = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "ID: {}, Fname: {}, Lname: {}, Phone: {}, Bal: {}, DC: {}, DM: {}".format(self.id, 
            self.first_name, 
            self.last_name, 
            self.phone_number, 
            self.balance, 
            self.date_created,
            self.date_modified)