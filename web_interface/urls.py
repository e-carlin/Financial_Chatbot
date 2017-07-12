import plaid
from django.conf.urls import url, include
from .views import show_users, welcome, show_account, get_access_token, get_transactions

urlpatterns = [
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^account/', show_account, name='show_account'),
	url(r'^show/', show_users, name='show_users'),
	url(r'^get_access_token/', get_access_token, name='get_access_token'),
	url(r'^get_transactions/', get_transactions, name='get_transactions'),
	url(r'^$', welcome, name='welcome_view'),
]