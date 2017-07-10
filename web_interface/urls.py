import plaid
from django.conf.urls import url, include
from .views import show_users, welcome, show_account, get_access_token

urlpatterns = [
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^account/', show_account, name='show_account_view'),
	url(r'^show/', show_users, name='show_users_view'),
	url(r'^get_access_token/', get_access_token, name='get_access_token'),
	url(r'^$', welcome, name='welcome_view'),
]