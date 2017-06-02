from django.test import TestCase
from .models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the user model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.first_name = "Evan"
        self.last_name = "Model_Test"
        self.phone_number = "+13034959592"
        self.user = User(first_name=self.first_name, last_name=self.last_name, phone_number=self.phone_number)

    def test_model_can_create_a_user(self):
        """Test the user model can create a user."""
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)
        #Assert first_name=="Evan", last_name=="C-Teser", ...

# This needs to be adapted to user  api/v1/sms
# class ViewTestCase(TestCase):
#     """Test suite for the api views."""

#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.client = APIClient()
#         self.user_data = {'first_name': 'Evan', 'last_name' : 'View_Test', 'phone_number' : '+13034959592'}
#         self.response = self.client.post(
#             reverse('create'),
#             self.user_data,
#             format="json")

#     def test_api_can_create_a_user(self):
#         """Test the api has bucket creation capability."""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)