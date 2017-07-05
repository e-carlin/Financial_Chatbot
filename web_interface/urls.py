from django.conf.urls import url, include
from .views import show_users, welcome

urlpatterns = [
	url(r'^show/', show_users, name='show_users_view'),
	url(r'^$', welcome, name='welcome_view'),
]