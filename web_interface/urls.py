from django.conf.urls import url, include
from .views import show_users, welcome, show_account

urlpatterns = [
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^account/', show_account, name='show_account_view'),
	url(r'^show/', show_users, name='show_users_view'),
	url(r'^$', welcome, name='welcome_view'),
]